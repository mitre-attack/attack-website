const $ = require('jquery');

// eslint-disable-next-line import/extensions
const { IndexedDBWrapper } = require("./indexed-db-wrapper.js");

// eslint-disable-next-line import/extensions
const AttackIndex = require('./attack-index.js');

// eslint-disable-next-line import/extensions
const {
  searchBody,
  searchResultsFooter,
  searchResultsPagination,
} = require('./components.js');

const PAGE_TYPE_GROUPS = [
  {
    key: 'core',
    label: 'Core ATT&CK Objects',
    pageTypes: ['matrices', 'tactics', 'techniques', 'sub-techniques'],
  },
  {
    key: 'defenses',
    label: 'Defenses',
    pageTypes: ['mitigations', 'assets', 'detectionstrategies', 'analytics', 'datacomponents'],
  },
  {
    key: 'cti',
    label: 'CTI',
    pageTypes: ['groups', 'software', 'campaigns'],
  },
  {
    key: 'reference',
    label: 'Reference',
    pageTypes: ['resources'],
  },
];

const PAGE_TYPE_LABELS = {
  analytics: 'Analytics',
  assets: 'Assets',
  campaigns: 'Campaigns',
  datacomponents: 'Data Components',
  detectionstrategies: 'Detection Strategies',
  groups: 'Groups',
  matrices: 'Matrices',
  mitigations: 'Mitigations',
  resources: 'Resources',
  software: 'Software',
  'sub-techniques': 'Sub-Techniques',
  tactics: 'Tactics',
  techniques: 'Techniques',
};

const DOMAIN_LABELS = {
  enterprise: 'Enterprise',
  mobile: 'Mobile',
  ics: 'ICS',
};

const PAGE_TYPES = PAGE_TYPE_GROUPS.flatMap((group) => group.pageTypes);
const DEFAULT_PAGE_TYPES = PAGE_TYPES.concat('misc');
const DOMAINS = ['enterprise', 'mobile', 'ics'];
const FILTER_DROPDOWNS = PAGE_TYPE_GROUPS.map((group) => group.key).concat('domains');

module.exports = class SearchService {

  /**
   * The SearchService class is responsible for managing the search functionality of the application. It allows for
   * initialization of the search index, processing search queries, and rendering search results.
   *
   * @class SearchService
   * @constructor
   * @param {string} tag - The ID of the DOM element that will be used as the container for rendering search results.
   * @param {string} [buildId] - An optional build ID used as a part of the IndexedDB database name.
   */
  constructor(tag, buildId) {

    // 2* buffer is roughly the size of the result preview
    this.buffer = 200;

    this.pageLimit = 5;
    this.currentPage = 1;

    this.currentQuery = {
      clean: '',
      words: [
        /*
         * {
         *    word: the raw word
         *    regex: regular expression to find this word in the document
         * }
         */
      ],
      joined: '', // alternation
    };

    this.render_container = $(`#${tag}`);

    this.selectedPageTypes = new Set(DEFAULT_PAGE_TYPES);
    this.selectedDomains = new Set(DOMAINS);
    this.allSearchResults = [];
    this.searchResults = [];
    this.openFilterDropdown = null;

    if (this.render_container?.on) {
      this.render_container.on('click', '#clear-search-filters', () => this.resetFilters());
    }

    /**
     * The following two IndexedDBWrapper instances initialize two IndexedDB tables. Each instance corresponds to one
     * table. The wrapper class obfuscates the CRUD logic for interfacing with IndexedDB.
     *
     * 1. content_table: handles all objects loaded from index.json
     *
     * 2. flexsearch_table: handles the FlexSearch document instance (so we don't have to re-index index.json every time
     *    FlexSearch is cleared from browser memory!).
     */

    const schemas = {
      content_table: '&id, title, path, content',
      searchindex_table: '++id, title, content',
    };

    const dbName = buildId ? `AttackWebsite-${buildId}` : 'AttackWebsite';

    this.db = new IndexedDBWrapper(dbName, schemas);

    this.contentDb = this.db.getTableWrapper('content_table');
    this.searchIndexDb = this.db.getTableWrapper('searchindex_table');

    /**
     * A quick note on the schemas passed in the above 👆 IndexedDBWrapper initializations:
     *
     * The &id syntax means that the id field is the primary key of the table, but it will not be auto-incremented.
     * In this case, you must provide a unique value for the id field when inserting a new record, and the
     * IndexedDB will enforce uniqueness on the id field.
     *
     * The ++id syntax means that the id field is the primary key of the table and it will be auto-incremented. In
     * other words, when you insert a new record without providing a value for the id field, the IndexedDB will
     * automatically assign a unique, incremental value to the id field.
     */

    // Initialize the AttackIndex instance (this is our in-memory FlexSearch instance)
    this.attackIndex = new AttackIndex();
  }

  /**
   * Asynchronously initializes the search engine by either indexing the provided documents or restoring the search
   * index from a backup stored in IndexedDB. If documents are provided, the method will add them to the search index,
   * create a backup of the search index, and store the documents in IndexedDB.
   *
   * @async
   * @function
   * @param {Array<Object>} [documents] - An optional array of document objects to be indexed. Each document object
   * should have an `id`, a `title`, a `path`, and a `content` property.
   */
  async initializeAsync(documents) {

    // If documents are defined, then load them into the AttackIndex instance.
    if (documents) {
      console.debug('Indexing documents: ', documents);

      const searchableDocuments = documents.map(document => this.#normalizeDocumentMetadata(document));

      this.maxSearchResults = searchableDocuments.length;

      // Add the data to the in-memory FlexSearch instance
      this.attackIndex.addBulk(searchableDocuments);

      console.debug('Backing up search index...');

      // Backup the in-memory FlexSearch index for later restoration
      await this.backupSearchIndex();
      await this.contentDb.bulkPut(searchableDocuments, 100);

      console.debug('Backup of search index completed.');
    } else {
      console.debug('Restoring search index from backup...');

      this.maxSearchResults = await this.contentDb.count();

      // If no documents were provided, then attempt to load them from the IndexedDB database
      await this.restoreSearchIndexFromBackup();
    }
  }

  /**
   * Exports data from the in-memory FlexSearch instance to the IndexedDB.
   * @returns {Promise<Array<string>>}
   */
  async backupSearchIndex() {

    const keys = [];
    let processedKeys = 0;

    // totalKeys(x) = (3 * #searchFields) + 3
    //                          ^
    //                    title + content --> 2 fields
    const totalKeys = 9;

    return new Promise((resolve) => {
      this.attackIndex.index.export(async (key, data) => {
        await this.searchIndexDb.put({ key, data });
        keys.push(key);
        processedKeys++;

        if (processedKeys === totalKeys) {
          resolve(true);
        }
      });
    });
  }

  /**
   * Imports data from the IndexedDB to the in-memory FlexSearch instance.
   * @returns {Promise<void>}
   */
  async restoreSearchIndexFromBackup() {
    // Retrieve all records from the specified object store
    const documents = await this.searchIndexDb.getAll();

    console.debug(`Located ${documents.length} documents in the searchindex_table`);

    for (const document of documents) {
      await this.attackIndex.import(document.key, document.data);
    }
  }

  /**
   * Given an array of index positions returned by a FlexSearch query, retrieves the original content for each position
   * from the IndexedDB content_table and returns an array of matching documents.
   *
   * @param {number[]} positions - An array of index positions returned by a FlexSearch query.
   * @returns {Promise<Object[]>} - An array of matching documents retrieved from the IndexedDB content_table.
   */
  async resolveSearchResults(positions) {
    // Create an array of promises to get documents from the IndexedDB content_table
    const getPromises = positions.map(position => this.contentDb.get(position));

    // Wait for all promises to resolve
    const docs = await Promise.all(getPromises);

    // Filter out null or undefined documents
    return docs
      .filter(doc => doc !== null && doc !== undefined)
      .map(doc => this.#normalizeDocumentMetadata(doc));
  }

  /**
   * Asynchronously performs a search query on the search index and renders the search results on the web page.
   * The search will be performed on both the title and content fields of the indexed documents.
   * The search results are paginated, showing the first page of results after the search.
   *
   * @async
   * @function
   * @param {string} query - The raw search query string.
   */
  async query(query) {
    this.currentPage = 1;
    this.#cleanTheQuery(query);
    this.render_container.html('');

    if (this.currentQuery.clean === '') {
      this.allSearchResults = [];
      this.searchResults = [];
      this.currentPage = 1;
      this.#renderSearchResults([]);
      this.#updateFilterControls();
      return;
    }

    const results = await this.attackIndex.search(this.currentQuery.clean, ["title", "content"], this.maxSearchResults);
    console.debug('search index results: ', results);

    /**
     * results:  [
     *       {
     *         field: 'title',
     *         result: [
     *           2, 3, 4, 5, 6,
     *           ..., 100
     *         ]
     *       },
     *       {
     *         field: 'content',
     *         result: [
     *           1, 5, 6, 7,
     *           2, 3, 8, 9,
     *         ]
     *       }
     *     ]
     */

    this.allSearchResults = await this.#setSearchResults(results);
    this.#renderFilteredSearchResults();
  }

  /**
   * Renders the search results on the web page based on the given search result page.
   * If the search query is empty, it will show the "Load More Results" button.
   * If the search query has no results, it will display a "no results" message.
   *
   * @private
   * @function
   * @param {Array<{ id: number, title: string, path: string, content: string }>} page - An array of search result
   * objects, where each object has an `id`, a `title`, a `path`, and a `content` property.
   *
   * @example
   * page: [
   *   {
   *     id: 0,
   *     title: "Random title",
   *     path: "/path/to/random/page.html",
   *     content: "Some random content."
   *   },
   *   {
   *     id: 1,
   *     title: "Another random title",
   *     path: "/path/to/another/random/page.html",
   *     content: "Some more random content."
   *   }
   * ]
   */
  #renderSearchResults(page) {
    if (page.length > 0) {
      // Render the search results
      searchBody?.show?.();
      const self = this;
      let resultHTML = page.map((result) => self.#resultToHTML(result));
      resultHTML = resultHTML.join('');
      if (this.render_container?.append) this.render_container.append(resultHTML);

      this.#renderResultsFooter();

    } else if (this.currentQuery.clean !== '') {
      // search with no results
      searchBody?.show?.();
      if (this.render_container?.html) this.render_container.html(this.#emptyResultsHTML());
      this.#renderResultsFooter();
    } else {
      // query for empty string
      searchBody?.hide?.();
      this.#clearResultsFooter();
    }
  }

  /**
   * Asynchronously sets the search results by merging title and content results without duplication, prioritizing
   * title matches over content matches.
   *
   * @async
   * @private
   * @function
   * @param {Array<{ field: string, result: Array<number> }>} results - An array containing search results, each object
   * in the array should have a `field` property ("title" or "content") and a `result` property (an array of indices).
   *
   * @returns {Promise<Array>} A Promise that resolves to an array containing the search results with duplicates removed
   * and title matches prioritized over content matches.
   *
   * @example
   * results: [
   *   {
   *     field: 'title',
   *     result: [2, 3, 4, 5, 6, ..., 100]
   *   },
   *   {
   *     field: 'content',
   *     result: [1, 5, 6, 7, 2, 3, 8, 9]
   *   }
   * ]
   */
  async #setSearchResults(results) {
    // Get documents corresponding to index positions
    const titlePositions = results.find(r => r?.field === 'title')?.result ?? [];
    const contentPositions = results.find(r => r?.field === 'content')?.result ?? [];

    /**
     * Dedup the search results retrieved by searching the content index. The new filtered array will contain only those
     * elements from contentPositions that are not present in titlePositions.
     *
     * We do this because (1) we don't want to render duplicate search results, and (2) we want to prioritize search
     * results retrieved from the title index because title matches are weighted higher than content matches
     */
    const filteredContentPositions = contentPositions.filter(pos => !titlePositions.includes(pos));

    // Resolve the FlexSearch results to the original elements stored in index.json
    const titleDocuments = await this.resolveSearchResults(titlePositions);
    const contentDocuments = await this.resolveSearchResults(filteredContentPositions);

    // Concatenate the two arrays, with title results appearing first in the concatenated array.
    return titleDocuments.concat(contentDocuments);
  }

  /**
   * Filters a result set using the selected page type and domain filters.
   * @param {Array<Object>} documents - Search results to filter.
   * @returns {Array<Object>} Filtered documents.
   */
  applyFilters(documents) {
    return documents
      .map(document => this.#normalizeDocumentMetadata(document))
      .filter(document => this.#matchesSelectedPageTypes(document) && this.#matchesSelectedDomains(document));
  }

  /**
   * Sets selected page type filters.
   * @param {Array<string>} pageTypes - Page type keys to select.
   */
  setSelectedPageTypes(pageTypes) {
    this.selectedPageTypes = new Set(pageTypes.filter(pageType => PAGE_TYPES.includes(pageType)));
    this.#renderFilteredSearchResults();
  }

  /**
   * Sets selected domain filters.
   * @param {Array<string>} domains - Domain keys to select.
   */
  setSelectedDomains(domains) {
    this.selectedDomains = new Set(domains.filter(domain => DOMAINS.includes(domain)));
    this.#renderFilteredSearchResults();
  }

  /**
   * Toggles one page type.
   * @param {string} pageType - Page type key to toggle.
   */
  togglePageType(pageType) {
    if (!PAGE_TYPES.includes(pageType)) return;
    this.selectedPageTypes.delete('misc');
    this.#toggleSetValue(this.selectedPageTypes, pageType);
    this.#renderFilteredSearchResults();
  }

  /**
   * Toggles one domain.
   * @param {string} domain - Domain key to toggle.
   */
  toggleDomain(domain) {
    if (!DOMAINS.includes(domain)) return;
    this.#toggleSetValue(this.selectedDomains, domain);
    this.#renderFilteredSearchResults();
  }

  /**
   * Selects or clears all page types in a group.
   * @param {string} groupKey - Page type group key.
   * @param {boolean} selected - Whether group values should be selected.
   */
  setPageTypeGroupSelected(groupKey, selected) {
    const group = PAGE_TYPE_GROUPS.find(candidate => candidate.key === groupKey);
    if (!group) return;

    group.pageTypes.forEach((pageType) => {
      if (selected) {
        this.selectedPageTypes.add(pageType);
      } else {
        this.selectedPageTypes.delete(pageType);
      }
    });
    this.selectedPageTypes.delete('misc');
    this.#renderFilteredSearchResults();
  }

  /**
   * Selects every page type.
   */
  selectAllPageTypes() {
    this.selectedPageTypes = new Set(DEFAULT_PAGE_TYPES);
    this.#renderFilteredSearchResults();
  }

  /**
   * Clears every page type.
   */
  clearPageTypes() {
    this.selectedPageTypes = new Set();
    this.#renderFilteredSearchResults();
  }

  /**
   * Selects every domain.
   */
  selectAllDomains() {
    this.selectedDomains = new Set(DOMAINS);
    this.#renderFilteredSearchResults();
  }

  /**
   * Clears every domain.
   */
  clearDomains() {
    this.selectedDomains = new Set();
    this.#renderFilteredSearchResults();
  }

  /**
   * Resets all filters to their default all-selected state.
   */
  resetFilters() {
    this.selectedPageTypes = new Set(DEFAULT_PAGE_TYPES);
    this.selectedDomains = new Set(DOMAINS);
    this.#renderFilteredSearchResults();
  }

  /**
   * Clears query-scoped search state and resets filters to the default all-selected state.
   */
  clearSession() {
    this.currentQuery.clean = '';
    this.allSearchResults = [];
    this.searchResults = [];
    this.selectedPageTypes = new Set(DEFAULT_PAGE_TYPES);
    this.selectedDomains = new Set(DOMAINS);
    this.currentPage = 1;
    this.openFilterDropdown = null;
    if (this.render_container?.html) this.render_container.html('');
    this.#updateFilterControls();
    searchBody?.hide?.();
    this.#clearResultsFooter();
  }

  /**
   * Opens or closes one compact filter dropdown.
   * @param {string} dropdownKey - Filter dropdown key to toggle.
   */
  toggleFilterDropdown(dropdownKey) {
    if (!FILTER_DROPDOWNS.includes(dropdownKey)) return;

    this.openFilterDropdown = this.openFilterDropdown === dropdownKey ? null : dropdownKey;
    this.#updateFilterControls();
  }

  /**
   * Closes any compact filter dropdown.
   */
  closeFilterDropdowns() {
    if (!this.openFilterDropdown) return false;

    this.openFilterDropdown = null;
    this.#updateFilterControls();
    return true;
  }

  /**
   * Gets the currently open compact filter dropdown.
   * @returns {?string} Current dropdown key, or null if every compact dropdown is closed.
   */
  getOpenFilterDropdown() {
    return this.openFilterDropdown;
  }

  /**
   * Counts filter matches for the current query result set.
   * @param {Array<Object>} documents - Search results to count.
   * @returns {{pageTypes: Object, domains: Object}} Filter counts.
   */
  getFilterCounts(documents) {
    const normalizedDocuments = documents.map(document => this.#normalizeDocumentMetadata(document));
    const pageTypes = {};
    const domains = {};

    PAGE_TYPES.forEach((pageType) => {
      pageTypes[pageType] = normalizedDocuments.filter(document => (
        document.pageType === pageType && this.#matchesSelectedDomains(document)
      )).length;
    });

    DOMAINS.forEach((domain) => {
      domains[domain] = normalizedDocuments.filter(document => (
        this.#matchesSelectedPageTypes(document) && document.domains.includes(domain)
      )).length;
    });

    return { pageTypes, domains };
  }

  goToPage(pageNumber) {
    const totalPages = Math.max(1, Math.ceil(this.searchResults.length / this.pageLimit));
    const nextPage = Math.min(Math.max(pageNumber, 1), totalPages);
    if (nextPage === this.currentPage) return;

    this.currentPage = nextPage;
    this.#renderCurrentSearchResultPage();
    searchBody?.scrollTop?.(0);
  }

  getPaginationState() {
    const totalResults = this.searchResults.length;
    const totalPages = Math.max(1, Math.ceil(totalResults / this.pageLimit));
    const startResult = totalResults === 0 ? 0 : ((this.currentPage - 1) * this.pageLimit) + 1;
    const endResult = Math.min(this.currentPage * this.pageLimit, totalResults);

    return {
      currentPage: this.currentPage,
      endResult,
      pageSize: this.pageLimit,
      pages: this.#pageWindow(totalPages),
      showPagination: totalPages > 1,
      startResult,
      totalPages,
      totalResults,
    };
  }

  #renderFilteredSearchResults() {
    this.currentPage = 1;
    this.#renderCurrentSearchResultPage();
  }

  #renderCurrentSearchResultPage() {
    if (this.render_container?.html) this.render_container.html('');
    this.searchResults = this.applyFilters(this.allSearchResults);
    this.#updateFilterControls();
    const startIndex = (this.currentPage - 1) * this.pageLimit;
    this.#renderSearchResults(this.searchResults.slice(startIndex, startIndex + this.pageLimit));
  }

  #matchesSelectedPageTypes(document) {
    return this.selectedPageTypes.has(document.pageType);
  }

  #matchesSelectedDomains(document) {
    if (this.selectedDomains.size === DOMAINS.length) return true;
    if (this.selectedDomains.size === 0) return false;
    return document.domains.some(domain => this.selectedDomains.has(domain));
  }

  #toggleSetValue(targetSet, value) {
    if (targetSet.has(value)) {
      targetSet.delete(value);
    } else {
      targetSet.add(value);
    }
  }

  #updateFilterControls() {
    const counts = this.getFilterCounts(this.allSearchResults);

    this.#setElementText(
      $('[data-search-filter-summary="page-types"]'),
      this.#selectedSummary(this.selectedPageTypes, PAGE_TYPES, PAGE_TYPE_LABELS),
    );
    this.#setElementText(
      $('[data-search-filter-summary="domains"]'),
      this.#selectedSummary(this.selectedDomains, DOMAINS, DOMAIN_LABELS),
    );
    PAGE_TYPE_GROUPS.forEach((group) => {
      this.#setElementText(
        $(`[data-search-filter-summary="group-${group.key}"]`),
        this.#selectedSummary(
          new Set(group.pageTypes.filter((pageType) => this.selectedPageTypes.has(pageType))),
          group.pageTypes,
          PAGE_TYPE_LABELS,
        ),
      );
    });

    PAGE_TYPES.forEach((pageType) => {
      const button = $(`[data-search-filter-page-type="${pageType}"]`);
      const selected = this.selectedPageTypes.has(pageType);
      const chip = button?.closest?.('.search-filter-chip');
      this.#toggleElementClass(chip, 'selected', selected);
      this.#setElementProperty(button, 'checked', selected);
      this.#setElementText(chip?.find?.('.search-filter-count'), this.#countLabel(counts.pageTypes[pageType]));
    });

    DOMAINS.forEach((domain) => {
      const button = $(`[data-search-filter-domain="${domain}"]`);
      const selected = this.selectedDomains.has(domain);
      const chip = button?.closest?.('.search-filter-chip');
      this.#toggleElementClass(chip, 'selected', selected);
      this.#setElementProperty(button, 'checked', selected);
      this.#setElementText(chip?.find?.('.search-filter-count'), this.#countLabel(counts.domains[domain]));
    });

    $('[data-search-filter-reset]')?.toggle?.(this.#visibleFiltersAreActive());
    $('#search-filters')?.toggleClass?.('has-query', this.currentQuery.clean !== '');

    FILTER_DROPDOWNS.forEach((dropdownKey) => {
      const isOpen = this.openFilterDropdown === dropdownKey;
      const toggle = $(`[data-search-filter-dropdown-toggle="${dropdownKey}"]`);
      const dropdown = $(`[data-search-filter-dropdown="${dropdownKey}"]`);

      this.#toggleElementClass(toggle, 'open', isOpen);
      this.#setElementAttribute(toggle, 'aria-expanded', isOpen.toString());
      dropdown?.toggle?.(isOpen);
      this.#setElementAttribute(dropdown, 'aria-hidden', (!isOpen).toString());
    });
  }

  #setElementText(element, value) {
    if (element?.text) element.text(value);
  }

  #setElementAttribute(element, name, value) {
    if (element?.attr) element.attr(name, value);
  }

  #setElementProperty(element, name, value) {
    if (element?.prop) element.prop(name, value);
  }

  #toggleElementClass(element, className, value) {
    if (element?.toggleClass) element.toggleClass(className, value);
  }

  #selectedSummary(selectedValues, allValues, labels) {
    const visibleSelectedValues = allValues.filter(value => selectedValues.has(value));
    if (visibleSelectedValues.length === allValues.length) return 'All';
    if (visibleSelectedValues.length === 0) return 'None';
    if (visibleSelectedValues.length <= 2) {
      return visibleSelectedValues.map(value => labels[value]).join(', ');
    }
    return `${visibleSelectedValues.length} selected`;
  }

  #countLabel(count) {
    return this.currentQuery.clean === '' ? '' : count;
  }

  #visibleFiltersAreActive() {
    const selectedVisiblePageTypes = PAGE_TYPES.filter(pageType => this.selectedPageTypes.has(pageType));
    return (
      selectedVisiblePageTypes.length !== PAGE_TYPES.length ||
      this.selectedDomains.size !== DOMAINS.length
    );
  }

  #pageWindow(totalPages) {
    if (totalPages <= 5) return Array.from({ length: totalPages }, (_, index) => index + 1);

    const startPage = Math.min(Math.max(this.currentPage - 2, 1), totalPages - 4);
    return Array.from({ length: 5 }, (_, index) => startPage + index);
  }

  #renderResultsFooter() {
    if (this.currentQuery.clean === '') {
      this.#clearResultsFooter();
      return;
    }

    const pagination = this.getPaginationState();
    if (pagination.totalResults === 0) {
      this.#setElementHTML(searchResultsFooter, '<div class="search-results-count" aria-live="polite">No results</div>');
      this.#clearResultsPagination();
      return;
    }

    const countLabel = pagination.showPagination
      ? `${pagination.startResult}-${pagination.endResult} of ${pagination.totalResults} results`
      : `${pagination.totalResults} ${pagination.totalResults === 1 ? 'result' : 'results'}`;

    const paginationHTML = pagination.showPagination ? `
            <div class="search-pagination" aria-label="Search results pages">
                <button type="button" class="search-pagination-control" data-search-page="${this.currentPage - 1}"
                    ${this.currentPage === 1 ? 'disabled' : ''}>Prev</button>
                <span class="search-pagination-pages">
                    ${pagination.pages.map(page => `
                        <button type="button" class="search-pagination-page${page === this.currentPage ? ' current' : ''}"
                            data-search-page="${page}" ${page === this.currentPage ? 'aria-current="page"' : ''}>
                            ${page}
                        </button>
                    `).join('')}
                </span>
                <span class="search-pagination-mobile">Page ${pagination.currentPage} of ${pagination.totalPages}</span>
                <button type="button" class="search-pagination-control" data-search-page="${this.currentPage + 1}"
                    ${this.currentPage === pagination.totalPages ? 'disabled' : ''}>Next</button>
            </div>
        ` : '';

    this.#setElementHTML(searchResultsFooter, `
            <div class="search-results-count" aria-live="polite">${countLabel}</div>
        `);
    this.#setElementHTML(searchResultsPagination, paginationHTML);
  }

  #clearResultsFooter() {
    this.#setElementHTML(searchResultsFooter, '');
    this.#clearResultsPagination();
  }

  #clearResultsPagination() {
    this.#setElementHTML(searchResultsPagination, '');
  }

  #setElementHTML(element, value) {
    if (element?.html) element.html(value);
  }

  #emptyResultsHTML() {
    if (!this.#visibleFiltersAreActive() || this.allSearchResults.length === 0) {
      return '<div class="search-result">No results</div>';
    }

    return `
            <div class="search-result search-no-results">
                <div class="title">No results match the selected filters</div>
                <div class="preview">
                    <button type="button" class="btn btn-default btn-sm" id="clear-search-filters"
                        data-search-filter-reset>
                        Reset filters
                    </button>
                </div>
            </div>
        `;
  }

  /**
   * Cleans and processes the search query by trimming white spaces, escaping special characters, and creating
   * regular expressions for each word in the query. The processed query is stored in the `this.currentQuery` object.
   *
   * @private
   * @function
   * @param {string} query - The raw search query string.
   */
  #cleanTheQuery(query) {
    console.debug(`Cleaning query string: ${query}`);

    this.currentQuery.clean = query.trim();

    // build joined string
    const joined = `(${this.currentQuery.clean.split(/\s+/).join('|')})`;
    this.currentQuery.joined = new RegExp(joined, 'gi');

    // Build regex for each word

    // remove double spaces which causes query to match on every 0 length string and flip out
    const escaped = this.currentQuery.clean.replace(/\s+/g, ' ');

    // The following map code is modifying the current_query object by setting its words property to an array of
    // objects. Each object in the array represents a word that was entered as part of a search query, along with a
    // regular expression that can be used to match that word in a larger body of text.

    this.currentQuery.words = escaped.split(' ').map((searchWord) => {
      // This line replaces any special characters in the search word with escape characters, so that they can be safely
      // used in a regular expression. The g flag ensures that all occurrences of special characters in the word are
      // replaced, and \\$& inserts the original character as a literal string in the replacement.
      // In other words: escape all regex chars so that entering ".." doesn't cause it to flip out
      let regexString = searchWord.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');

      // This line replaces any occurrence of "att&ck" or "attack" with the regular expression pattern
      // ((?:att&ck)|(?:attack)). This is done to make the search more flexible and include results that may use
      // different forms of the term.
      regexString = regexString.replace(/((?:att&ck)|(?:attack))/gi, '((?:att&ck)|(?:attack))');

      // This line creates a new object that contains the original search word and its corresponding regular expression.
      // The regular expression is created using the RegExp constructor, with the gi flags to make it global and
      // case-insensitive.
      return {
        word: searchWord,
        regex: new RegExp(regexString, 'gi')
      };
    });
  }

  /**
   * Converts a search result object to an HTML string with highlighted search words.
   * The HTML string will include the result's title, a link to the result's path, and a preview of the content
   * with search words highlighted. The preview will be trimmed to a buffer size around the found words.
   *
   * @private
   * @function
   * @param {Object} result - A search result object containing an `id`, a `title`, a `path`, and a `content` property.
   * @returns {string} An HTML string representing the search result with highlighted search words.
   */
  #resultToHTML(result) {
    // create title and path
    let { title } = result;

    let path = base_url.slice(0, -1) + result.path;

    if (path.endsWith('/index.html')) {
      path = path.slice(0, -11);
    }

    // create preview html
    let preview = result.content;

    // Find a position where the search words occur near each other
    const positions = [];

    this.currentQuery.words.forEach((searchWord) => {
      let currMatches;
      while ((currMatches = searchWord.regex.exec(preview)) !== null) {
        positions.push({
          index: searchWord.regex.lastIndex,
          word: searchWord.word,
        });
      }
    });

    positions.sort((a, b) => a.index - b.index);

    // are two sets equal
    function setsEqual(s1, s2) {
      if (s1.size !== s2.size) return false;
      for (const a of s1) if (!s2.has(a)) return false;
      return true;
    }

    const allWords = new Set(this.currentQuery.words.map((word) => word.word));

    const pos = 0;
    const best = {
      min: 0,
      max: 0,
      totalDist: Infinity, // distance between words
      totalFound: 0, // total number of words found
    };
    for (let i = 0; i < positions.length; i++) {
      const position = positions[i];
      const {word} = position;
      const {index} = position;

      // find out how far we have to go from this position to find all words
      const foundWords = new Set();
      foundWords.add(position.word);

      let totalDist = 0; // total distance between words for this combination
      let max = index; // leftmost word find
      let min = index; // rightmost word find

      if (setsEqual(allWords, foundWords)) {
        // 1 word search
        best.min = index + 10;
        best.max = index - 10;
        break;
      } else {
        // search around this word
        for (let j = 0; i + j < positions.length || i - j > 0; j++) {
          // search j ahead
          let exceeded = 0;
          if (i + j < positions.length - 1) {
            const ahead = positions[i + j];
            const dist = ahead.index - index;
            if (dist > this.buffer) { // exceeded buffer
              exceeded++;
            } else if (!foundWords.has(ahead.word)) { // found a word
              foundWords.add(ahead.word);
              max = ahead.index;
              totalDist += ahead.index - index;
            }
          }
          // search j behind
          if (i - j >= 0) {
            const behind = positions[i - j];
            const dist = index - behind.index;
            if (dist > this.buffer) { // exceeded buffer
              exceeded++;
            } else if (!foundWords.has(behind.word)) { // found a word
              foundWords.add(behind.word);
              min = behind.index;
              totalDist += index - behind.index;
            }
          }
          // found all the words in proximity, or both searches
          if (setsEqual(allWords, foundWords) || exceeded == 2) {
            // exceeded the buffer
            break;
          }
        }
      }
      // by now we must have found as many words as we can
      // total found words takes priority over the distance
      if (foundWords.size > best.totalFound || (totalDist < best.totalDist
          && foundWords.size >= best.totalFound)) {
        // new best
        best.totalDist = totalDist;
        best.max = max;
        best.min = min;
        best.totalFound = foundWords.size;
      }
    }

    // buffer around keyword
    const left = Math.max(0, best.min - this.buffer);
    const right = Math.min(preview.length, best.max + this.buffer);
    preview = preview.slice(left, right); // extract buffer

    // add ellipses to preview so people know that the preview is not the complete page data
    if (right < result.content.length) preview += '&hellip;';
    if (left > 0) preview = `&hellip; ${preview}`;

    // surround preview keywords with highlight class span tags
    preview = preview.replace(this.currentQuery.joined, "<span class='search-word-found'>$1</span>");
    // surround title keywords with highlight class span tags
    title = title.replace(this.currentQuery.joined, "<span class='search-word-found'>$1</span>");

    // result html template
    return `
            <div class="search-result mb-4">
                <div class="title">
                    <a href="${path}">${title}</a>
                </div>
                ${this.#resultBadgesHTML(result)}
                <div class="preview">
                    ${preview}
                </div>
            </div>
        `; // end template
  }

  #resultBadgesHTML(result) {
    const badges = [];
    const pageTypeLabel = this.#pageTypeBadgeLabel(result);

    if (pageTypeLabel) badges.push(pageTypeLabel);
    result.domains.forEach((domain) => {
      if (DOMAIN_LABELS[domain]) badges.push(DOMAIN_LABELS[domain]);
    });

    if (badges.length === 0) return '';

    return `
                <div class="search-result-badges">
                    ${badges.map(badge => `<span class="search-result-badge">${badge}</span>`).join('')}
                </div>
        `;
  }

  #normalizeDocumentMetadata(document) {
    return {
      ...document,
      pageType: DEFAULT_PAGE_TYPES.includes(document.pageType) ? document.pageType : this.#inferPageType(document.path),
      domains: Array.isArray(document.domains) ? document.domains.filter(domain => DOMAINS.includes(domain)) : [],
    };
  }

  #inferPageType(path = '') {
    if (/^\/techniques\/[^/]+\/[^/]+\/index\.html$/.test(path)) return 'sub-techniques';
    if (path.startsWith('/analytics/')) return 'analytics';
    if (path.startsWith('/assets/')) return 'assets';
    if (path.startsWith('/campaigns/')) return 'campaigns';
    if (path.startsWith('/datacomponents/')) return 'datacomponents';
    if (path.startsWith('/detectionstrategies/')) return 'detectionstrategies';
    if (path.startsWith('/groups/')) return 'groups';
    if (path.startsWith('/matrices/')) return 'matrices';
    if (path.startsWith('/mitigations/')) return 'mitigations';
    if (path.startsWith('/software/')) return 'software';
    if (path.startsWith('/tactics/')) return 'tactics';
    if (path.startsWith('/techniques/')) return 'techniques';
    if (path.startsWith('/resources/')) return 'resources';
    return 'misc';
  }

  #pageTypeBadgeLabel(result) {
    if (result.pageType === 'misc') return null;
    if (this.#isOverviewPage(result.path)) return PAGE_TYPE_LABELS[result.pageType];

    return {
      analytics: 'Analytic',
      assets: 'Asset',
      campaigns: 'Campaign',
      datacomponents: 'Data Component',
      detectionstrategies: 'Detection Strategy',
      groups: 'Group',
      matrices: 'Matrix',
      mitigations: 'Mitigation',
      resources: 'Resource',
      software: 'Software',
      'sub-techniques': 'Sub-Technique',
      tactics: 'Tactic',
      techniques: 'Technique',
    }[result.pageType];
  }

  #isOverviewPage(path = '') {
    return /^\/[^/]+\/index\.html$/.test(path) || /^\/(matrices|tactics|techniques|mitigations)\/(enterprise|mobile|ics)\/index\.html$/.test(path);
  }

}
