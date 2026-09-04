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

  test('a failed index build stops search from waiting for an index that never arrives', async () => {
    await loadIndexWithAFailingColdStart();

    const parsingIcon = mockJqueryApis['#search-parsing-icon'];
    parsingIcon.show.mockClear();
    parsingIcon.hide.mockClear();

    handlerForSelector('#search-input')({ target: { value: 'mimikatz' } });

    // Before the fix `search` looped on the loaded flag, so it showed the parsing icon on
    // its first pass and kept doing so every 100ms for as long as the page stayed open.
    expect(parsingIcon.show).not.toHaveBeenCalled();
    expect(parsingIcon.hide).toHaveBeenCalled();
  });

  test('a failed restore from the cache is not reported as a successful load', async () => {
    await loadIndexWithAFailingWarmRestore();

    // The catch used to set the loaded flag false and the finally set it straight back to
    // true, so `search` went on to query an index that was never populated.
    expect(mockJqueryApis['#search-input'].prop).toHaveBeenCalledWith('disabled', true);
    expect(mockJqueryApis['#search-icon'].addClass).toHaveBeenCalledWith('error-icon');
  });

  test('a failed index build puts the search controls into their unavailable state', async () => {
    await loadIndexWithAFailingColdStart();

    expect(mockJqueryApis['#search-input'].prop).toHaveBeenCalledWith('disabled', true);
    expect(mockJqueryApis['#search-button'].prop).toHaveBeenCalledWith('disabled', true);
    expect(mockJqueryApis['#search-icon'].removeClass).toHaveBeenCalledWith('search-icon');
    expect(mockJqueryApis['#search-icon'].addClass).toHaveBeenCalledWith('error-icon');
    expect(mockJqueryApis['#search-button'].prop)
      .toHaveBeenCalledWith('title', expect.stringContaining('search index could not be built'));
  });
});

// Load the module on the cold-start path with the document fetch failing, and run the
// debouncer straight through so the input handler reaches `search` without a timer.
async function loadIndexWithAFailingColdStart() {
  global.window = { indexedDB: {} };
  global.localStorage.getItem.mockReturnValue(null);

  jest.doMock('../src/search-loader.js', () => ({
    loadSearchDocuments: () => Promise.reject(new Error('documents unavailable')),
  }));
  jest.doMock('../src/debouncer.js', () => class {
    debounce(callback) {
      callback();
    }
  });

  require('../src/index');
  await new Promise(resolve => setImmediate(resolve));
}

// Load the module on the cached path, with restoring the index from IndexedDB failing.
async function loadIndexWithAFailingWarmRestore() {
  const { searchCacheCompatibilityVersion, searchCacheSchemaVersion } = require('../src/settings');
  const version = `${searchCacheSchemaVersion}-${searchCacheCompatibilityVersion}`;

  global.window = { indexedDB: {} };
  global.localStorage.getItem.mockReturnValue(`${global.build_uuid}-search-${version}`);

  jest.doMock('../src/search-service.js', () => class {
    initializeAsync() {
      return Promise.reject(new Error('cached index is unreadable'));
    }
  });

  require('../src/index');
  await new Promise(resolve => setImmediate(resolve));
}

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
