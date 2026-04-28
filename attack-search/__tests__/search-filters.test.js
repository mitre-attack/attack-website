const SearchService = require('../src/search-service');
import 'fake-indexeddb/auto';

jest.mock('jquery');

console.log = jest.fn();
console.debug = jest.fn();

describe('SearchService filters', () => {
  let searchService;
  let documents;

  beforeEach(() => {
    global.base_url = '/';
    searchService = new SearchService('search-service', null);
    documents = [
      {
        id: 1,
        title: 'Credential Access',
        content: 'Credential access technique',
        pageType: 'techniques',
        domains: ['enterprise'],
      },
      {
        id: 2,
        title: 'Credential Access: Credentials from Password Stores',
        content: 'Credential access sub-technique',
        pageType: 'sub-techniques',
        domains: ['enterprise'],
      },
      {
        id: 3,
        title: 'Account Use Policies',
        content: 'Credential mitigation',
        pageType: 'mitigations',
        domains: ['mobile'],
      },
      {
        id: 4,
        title: 'APT29',
        content: 'Credential campaign reporting',
        pageType: 'groups',
        domains: [],
      },
      {
        id: 5,
        title: 'Training',
        content: 'Credential reference material',
        pageType: 'resources',
        domains: [],
      },
    ];
  });

  afterEach(async () => {
    await searchService.db.indexeddb.delete();
    searchService = null;
  });

  test('default filters include every document', () => {
    expect(searchService.applyFilters(documents)).toEqual(documents);
  });

  test('page type filters treat techniques and sub-techniques independently', () => {
    searchService.setSelectedPageTypes(['techniques']);

    expect(searchService.applyFilters(documents).map(result => result.id)).toEqual([1]);
  });

  test('domain filters only match documents with explicit selected domains', () => {
    searchService.setSelectedDomains(['enterprise']);

    expect(searchService.applyFilters(documents).map(result => result.id)).toEqual([1, 2]);
  });

  test('empty page type selection returns no results', () => {
    searchService.setSelectedPageTypes([]);

    expect(searchService.applyFilters(documents)).toEqual([]);
  });

  test('counts reflect current query results before applying the changed facet', () => {
    searchService.setSelectedPageTypes(['techniques', 'sub-techniques', 'mitigations']);
    searchService.setSelectedDomains(['enterprise']);

    const counts = searchService.getFilterCounts(documents);

    expect(counts.pageTypes).toEqual({
      analytics: 0,
      assets: 0,
      campaigns: 0,
      datacomponents: 0,
      detectionstrategies: 0,
      groups: 0,
      matrices: 0,
      mitigations: 0,
      resources: 0,
      software: 0,
      'sub-techniques': 1,
      tactics: 0,
      techniques: 1,
    });
    expect(counts.domains).toEqual({
      enterprise: 2,
      ics: 0,
      mobile: 1,
    });
  });

  test('clear session resets filters and query-scoped results', () => {
    searchService.allSearchResults = documents;
    searchService.setSelectedPageTypes(['techniques']);
    searchService.setSelectedDomains(['enterprise']);
    searchService.toggleFilterDropdown('core');

    searchService.clearSession();

    expect(searchService.applyFilters(documents)).toEqual(documents);
    expect(searchService.allSearchResults).toEqual([]);
    expect(searchService.searchResults).toEqual([]);
    expect(searchService.getOpenFilterDropdown()).toBeNull();
  });

  test('only one subgroup dropdown can be open at a time', () => {
    searchService.toggleFilterDropdown('core');

    expect(searchService.getOpenFilterDropdown()).toBe('core');

    searchService.toggleFilterDropdown('defenses');

    expect(searchService.getOpenFilterDropdown()).toBe('defenses');
  });

  test('clicking away closes subgroup dropdowns without changing selections', () => {
    searchService.toggleFilterDropdown('domains');
    searchService.setSelectedDomains(['enterprise']);

    searchService.closeFilterDropdowns();

    expect(searchService.getOpenFilterDropdown()).toBeNull();
    expect(searchService.applyFilters(documents).map(result => result.id)).toEqual([1, 2]);
  });

  test('full filters panel closes subgroup dropdowns', () => {
    searchService.toggleFilterDropdown('cti');

    searchService.toggleFiltersPanel();

    expect(searchService.getOpenFilterDropdown()).toBeNull();
    expect(searchService.filtersExpanded).toBe(true);
  });
});
