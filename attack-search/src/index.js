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
const { baseURL, searchFilePaths } = require('./settings.js');
const Debouncer = require('./debouncer.js');
const SearchService = require('./search-service.js');

// Import required components
const {
  searchBody,
  searchOverlay,
  searchInput,
  searchParsingIcon,
  searchButton,
  searchIcon,
  closeButton,
  loadMoreResultsButton,
} = require('./components.js');

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
  searchOverlay.hide();
  searchOverlay.addClass('hidden');
};

// Variable to check if search service is loaded
let searchServiceIsLoaded = false;

// Initialize the search service
async function initializeSearchService() {
  console.debug('Initializing search service...');
  searchParsingIcon.show();

  const saved_uuid = localStorage.getItem('saved_uuid');
  console.debug(`Retrieved the saved_uuid from localStorage: ${saved_uuid}`);

  // Check if the browser supports IndexedDB. Search service can only work in environments that support IndexedDB.
  if ('indexedDB' in window) {
    // Verify if the buildUUID is already cached in LocalStorage. This check is performed to determine if the search
    // service has been initialized. Each website build instance possesses a unique buildUUID, preventing different
    // website builds from sharing the same search index.
    if (saved_uuid && saved_uuid === build_uuid) {
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
      const jsonFiles = [];

      // Download all JSON files from directory
      // Loop through the searchFilePaths array to construct the URLs
      searchFilePaths.forEach(function(filename) {
        jsonFiles.push(baseUrl + filename);
      });

      // Use Promise.all() to download all files concurrently
      Promise.all(jsonFiles.map(url => $.getJSON(url)))
          .then(data => {
            // Concatenate all file data into a single array
            const combinedData = data.reduce((acc, curr) => acc.concat(curr), []);

            // Initialize search service with combined data
            searchService = new SearchService('search-results', build_uuid);
            return searchService.initializeAsync(combinedData);
          })
          .then(() => {
            localStorage.setItem('saved_uuid', build_uuid);
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

// Declare search service variable
let searchService;

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

// Set up event handlers for closing search
searchOverlay.on('click', function (e) {
  if (e.target != this) return; // don't close for children
  closeSearch();
});
$(document).keyup((e) => {
  e.key === 'Escape' ? closeSearch() : null;
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

// Set up event handler for load more results button
loadMoreResultsButton.on('click', () => {
  if (searchService) searchService.loadMoreResults();
  loadMoreResultsButton.blur(); // onfocus
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

