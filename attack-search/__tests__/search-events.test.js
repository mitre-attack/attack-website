const mockJqueryCalls = [];
const mockJqueryApis = {};

const mockJquery = jest.fn((selector) => {
  if (typeof selector === 'object' && selector.dataset) {
    return {
      data: jest.fn((key) => selector.dataset?.[toCamelCase(key)]),
    };
  }

  const api = {
    addClass: jest.fn(() => api),
    attr: jest.fn(() => api),
    data: jest.fn(),
    focus: jest.fn(() => api),
    hide: jest.fn(() => api),
    on: jest.fn((events, delegatedSelector, handler) => {
      mockJqueryCalls.push({
        delegatedSelector: typeof delegatedSelector === 'string' ? delegatedSelector : null,
        events,
        handler: typeof delegatedSelector === 'function' ? delegatedSelector : handler,
        selector,
      });
      return api;
    }),
    prop: jest.fn(() => api),
    removeClass: jest.fn(() => api),
    show: jest.fn(() => api),
    toggle: jest.fn(() => api),
    toggleClass: jest.fn(() => api),
    val: jest.fn(() => ''),
    keyup: jest.fn((handler) => {
      mockJqueryCalls.push({
        delegatedSelector: null,
        events: 'keyup',
        handler,
        selector,
      });
      return api;
    }),
  };
  mockJqueryApis[selector] = api;
  return api;
});

mockJquery.getJSON = jest.fn();

jest.mock('jquery', () => mockJquery);

console.debug = jest.fn();
console.error = jest.fn();

describe('search event bindings', () => {
  beforeEach(() => {
    jest.resetModules();
    mockJqueryCalls.length = 0;
    Object.keys(mockJqueryApis).forEach(key => delete mockJqueryApis[key]);
    global.build_uuid = 'test-build';
    global.document = {};
    global.localStorage = {
      getItem: jest.fn(),
      removeItem: jest.fn(),
      setItem: jest.fn(),
    };
    global.window = {};
  });

  afterEach(() => {
    delete global.build_uuid;
    delete global.document;
    delete global.localStorage;
    delete global.window;
  });

  test('filter controls listen for touch activation events', () => {
    require('../src/index');

    expect(eventsForSelector('[data-search-filter-dropdown-toggle]')).toContain('touchend');
    expect(eventsForSelector('[data-search-filter-page-type]')).toContain('touchend');
    expect(eventsForSelector('[data-search-filter-domain]')).toContain('touchend');
    expect(eventsForSelector('[data-search-filter-domain-action]')).toContain('touchend');
    expect(eventsForSelector('[data-search-filter-group-action]')).toContain('touchend');
    expect(eventsForSelector('[data-search-filter-reset]')).toContain('touchend');
  });

  test('search cache key includes the serialized index compatibility version', () => {
    const { searchCacheCompatibilityVersion, searchCacheSchemaVersion } = require('../src/settings');

    require('../src/index');

    expect(global.localStorage.getItem).toHaveBeenCalledWith(
      `saved_uuid_search_schema_${searchCacheSchemaVersion}-${searchCacheCompatibilityVersion}`,
    );
  });

  test('dropdown toggles open before the search service is initialized', () => {
    require('../src/index');

    const handler = handlerForSelector('[data-search-filter-dropdown-toggle]');
    handler({
      currentTarget: { dataset: { searchFilterDropdownToggle: 'core' } },
      stopPropagation: jest.fn(),
      type: 'click',
    });

    expect(mockJqueryApis['[data-search-filter-dropdown-toggle="core"]'].toggleClass)
      .toHaveBeenCalledWith('open', true);
    expect(mockJqueryApis['[data-search-filter-dropdown-toggle="core"]'].attr)
      .toHaveBeenCalledWith('aria-expanded', 'true');
    expect(mockJqueryApis['[data-search-filter-dropdown="core"]'].toggle)
      .toHaveBeenCalledWith(true);
    expect(mockJqueryApis['[data-search-filter-dropdown="core"]'].attr)
      .toHaveBeenCalledWith('aria-hidden', 'false');
  });
});

function eventsForSelector(selector) {
  return mockJqueryCalls
    .filter(call => call.selector === selector || call.delegatedSelector === selector)
    .flatMap(call => call.events.split(/\s+/));
}

function handlerForSelector(selector) {
  return mockJqueryCalls.find(call => call.selector === selector || call.delegatedSelector === selector).handler;
}

function toCamelCase(key) {
  return key.replace(/-([a-z])/g, (_, char) => char.toUpperCase());
}
