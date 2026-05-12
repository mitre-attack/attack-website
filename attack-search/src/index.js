// Require necessary libraries
const $ = require('jquery');

/**
 * It is important that the `.js` file extension be included for local imports, otherwise webpack won't be able to
 * resolve it. i.e., webpack will throw an error like the following:
 *
 * ERROR in ./src/search.js 12:0-20
 * Module not found: Error: Can't resolve './settings' in '/foo/bar/attack-website/attack-search/src'
 */

// Import required modules with the correct file extension
const { baseURL, searchCacheSchemaVersion, searchFilePaths } = require('./settings.js');
const Debouncer = require('./debouncer.js');
const SearchService = require('./search-service.js');
const { loadSearchDocuments } = require('./search-loader.js');

// Import required components
const {
  searchBody,
  searchOverlay,
  searchInput,
  searchParsingIcon,
  searchButton,
  searchIcon,
  closeButton,
} = require('./components.js');

const searchCacheKey = `saved_uuid_search_schema_${searchCacheSchemaVersion}`;
let searchService;
let openFilterDropdownKey = null;

const setFilterDropdownOpenState = function (dropdownKey, isOpen) {
  const toggle = $(`[data-search-filter-dropdown-toggle="${dropdownKey}"]`);
  const dropdown = $(`[data-search-filter-dropdown="${dropdownKey}"]`);

  toggle.toggleClass('open', isOpen);
  toggle.attr('aria-expanded', isOpen.toString());
  dropdown.toggle(isOpen);
  dropdown.attr('aria-hidden', (!isOpen).toString());
};

const toggleFilterDropdown = function (dropdownKey) {
  if (searchService) {
    searchService.toggleFilterDropdown(dropdownKey);
    return;
  }

  const previousDropdownKey = openFilterDropdownKey;
  const isOpening = previousDropdownKey !== dropdownKey;

  if (previousDropdownKey) setFilterDropdownOpenState(previousDropdownKey, false);
  openFilterDropdownKey = isOpening ? dropdownKey : null;
  if (openFilterDropdownKey) setFilterDropdownOpenState(openFilterDropdownKey, true);
};

const closeFilterDropdowns = function () {
  if (searchService?.closeFilterDropdowns?.()) return true;
  if (!openFilterDropdownKey) return false;

  setFilterDropdownOpenState(openFilterDropdownKey, false);
  openFilterDropdownKey = null;
  return true;
};

// Open search overlay
const openSearch = function () {
  searchBody.hide();
  searchOverlay.show();
  searchOverlay.removeClass('hidden');
  searchInput.focus();
};

// Close search overlay
const closeSearch = function () {
  searchInput.val('');
  if (searchService) searchService.clearSession();
  closeFilterDropdowns();
  searchOverlay.hide();
  searchOverlay.addClass('hidden');
};

// Variable to check if search service is loaded
let searchServiceIsLoaded = false;

// Initialize the search service
async function initializeSearchService() {
  console.debug('Initializing search service...');
  searchParsingIcon.show();

  const saved_uuid = localStorage.getItem(searchCacheKey);
  const cachedBuildId = `${build_uuid}-search-${searchCacheSchemaVersion}`;
  console.debug(`Retrieved the saved_uuid from localStorage: ${saved_uuid}`);

  // Check if the browser supports IndexedDB. Search service can only work in environments that support IndexedDB.
  if ('indexedDB' in window) {
    // Verify if the buildUUID is already cached in LocalStorage. This check is performed to determine if the search
    // service has been initialized. Each website build instance possesses a unique buildUUID, preventing different
    // website builds from sharing the same search index.
    if (saved_uuid && saved_uuid === cachedBuildId) {
      // Restore search service from IndexedDB
      try {
        console.debug('Initializing SearchService (assume documents already cached)...');
        searchService = new SearchService('search-results', saved_uuid);
        await searchService.initializeAsync(null); // Passing null will instruct the search service to attempt
        // restoring itself from the IndexedDB
        console.debug('SearchService is initialized.');
      } catch (error) {
        console.error('Failed to initialize SearchService:', error);
        searchServiceIsLoaded = false;
      } finally {
        searchParsingIcon.hide();
        searchServiceIsLoaded = true;
      }
    }
    else {
      // Initialize search service from scratch
      console.debug('Documents not cached yet.');

      const baseUrl = `${baseURL}/search/`;
      loadSearchDocuments(baseUrl, searchFilePaths, $.getJSON)
        .then(combinedData => {
          searchService = new SearchService('search-results', cachedBuildId);
          return searchService.initializeAsync(combinedData);
        })
        .then(() => {
          localStorage.setItem(searchCacheKey, cachedBuildId);
          localStorage.removeItem('saved_uuid');
          console.debug('SearchService is initialized.');
          searchParsingIcon.hide();
          searchServiceIsLoaded = true;
        })
        .catch(error => {
          console.error('Failed to initialize SearchService:', error);
          searchParsingIcon.hide();
          searchServiceIsLoaded = false;
        });
    }
  }
  else {
    // Disable the search button and display an error icon with a hover effect that displays a message/explanation
    console.error('Search is only available in browsers that support IndexedDB. Please try using Firefox, Chrome, Safari, or another browser that supports IndexedDB.');
    searchInput.prop('disabled', true);
    searchButton.prop('disabled', true);
    searchIcon.removeClass('search-icon');
    searchIcon.addClass('error-icon');
    searchButton.prop('title', 'To use the search feature, please make sure your browser supports IndexedDB. If not, consider upgrading your browser or switching to a supported browser such as Firefox, Chrome, or Safari.')
  }
}

// Perform a search using the search service
const search = async function (query) {
  console.debug(`search -> Received search query: ${query}`);

  // Wait until the search service is loaded
  while (!searchServiceIsLoaded) {
    console.debug('search -> search index is not loaded...');
    searchParsingIcon.show();
    await new Promise(resolve => setTimeout(resolve, 100));
  }

  console.debug(`Executing search: ${query}`);
  await searchService.query(query);
  searchParsingIcon.hide();
};

// Instantiate a debouncer
const debounce = new Debouncer(300);
let lastTouchActivation = 0;

const shouldHandleActivation = function (e) {
  if (e.type === 'touchend') {
    lastTouchActivation = Date.now();
    e.preventDefault();
    e.stopPropagation();
    return true;
  }

  if (Date.now() - lastTouchActivation < 700) return false;

  e.stopPropagation();
  return true;
};

// Set up event handlers for closing search
searchOverlay.on('click', function (e) {
  if (e.target != this) return; // don't close for children
  closeSearch();
});
$(document).keyup((e) => {
  if (e.key !== 'Escape') return;
  if (closeFilterDropdowns()) return;
  closeSearch();
});

// Set up event handler for close button
closeButton.on('click', closeSearch);

// Set up event handlers for opening search
searchButton.on('click', openSearch);

// Set up event handler for search input
searchInput.on('input', (e) => {
  console.log(`Executing search on input: ${e.target.value}`);
  debounce.debounce(() => {
    console.log(`debounce callback: ${e.target.value}`);
    search(e.target.value);
  });
});

$('[data-search-filter-dropdown-toggle]').on('touchend click', (e) => {
  if (!shouldHandleActivation(e)) return;
  toggleFilterDropdown($(e.currentTarget).data('search-filter-dropdown-toggle'));
});

$('[data-search-filter-dropdown]').on('touchend click', (e) => {
  e.stopPropagation();
});

$(document).on('touchend click', () => {
  closeFilterDropdowns();
});

$('[data-search-filter-page-type]').on('touchend change', (e) => {
  if (!shouldHandleActivation(e)) return;
  if (searchService) searchService.togglePageType($(e.currentTarget).data('search-filter-page-type'));
});

$('[data-search-filter-domain]').on('touchend change', (e) => {
  if (!shouldHandleActivation(e)) return;
  if (searchService) searchService.toggleDomain($(e.currentTarget).data('search-filter-domain'));
});

$('[data-search-filter-domain-action]').on('touchend click', (e) => {
  if (!shouldHandleActivation(e)) return;
  if (!searchService) return;
  const action = $(e.currentTarget).data('search-filter-domain-action');

  if (action === 'all') searchService.selectAllDomains();
  if (action === 'none') searchService.clearDomains();
});

$('[data-search-filter-group-action]').on('touchend click', (e) => {
  if (!shouldHandleActivation(e)) return;
  if (!searchService) return;
  const button = $(e.currentTarget);
  searchService.setPageTypeGroupSelected(
    button.data('search-filter-group'),
    button.data('search-filter-group-action') === 'all',
  );
});

$('[data-search-filter-reset]').on('touchend click', (e) => {
  if (!shouldHandleActivation(e)) return;
  if (searchService) searchService.resetFilters();
});

$(document).on('click', '[data-search-page]', (e) => {
  if (searchService) searchService.goToPage(Number($(e.currentTarget).data('search-page')));
});

// Add compatibility patches for Internet Explorer
if (!String.prototype.includes) {
  String.prototype.includes = function (search, start) {
    if (typeof start !== 'number') {
      start = 0;
    }
    if (start + search.length > this.length) {
      return false;
    }
    return this.indexOf(search, start) !== -1;
  };
}
if (typeof String.prototype.endsWith !== 'function') {
  String.prototype.endsWith = function (suffix) {
    return this.indexOf(suffix, this.length - suffix.length) !== -1;
  };
}

// Log that search module is loaded
console.debug('search module is loaded.');

// Initialize the search service when the module loads
initializeSearchService();
