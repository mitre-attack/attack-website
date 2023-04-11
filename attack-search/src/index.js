const localforage = require('localforage');
const $ = require('jquery');

/**
 * It is important that the `.js` file extension be included for local imports, otherwise webpack won't be able to
 * resolve it. i.e., webpack will throw an error like the following:
 *
 * ERROR in ./src/search.js 12:0-20
 * Module not found: Error: Can't resolve './settings' in '/foo/bar/attack-website/attack-search/src'
 */

// eslint-disable-next-line import/extensions
const { baseURL } = require('./settings.js');

// eslint-disable-next-line import/extensions
const Debouncer = require('./debouncer.js');

// eslint-disable-next-line import/extensions
const SearchService = require('./search-service.js');

const {
  searchBody,
  searchOverlay,
  searchInput,
  searchParsingIcon,
  searchOpenTrigger,
  closeButton,
  loadMoreResultsButton,
// eslint-disable-next-line import/extensions
} = require('./components.js');

/**
 * FlexSearch.registerMatcher({REGEX: REPLACE})
 * Enables FlexSearch to globally replace RegEx matches.
 * Here, we use it to augment the "&" in ATT&CK, so searches for "attack" will still match "ATT&CK" and vice versa.
 */
// TODO Figure out how to do this is v0.7.31
// flexsearch.default.registerMatcher({
//   'ATT&CK': 'ATTACK',
//   ATTACK: 'ATT&CK',
// });

const isChromium = window.chrome;
const isEdgeChromium = isChromium && navigator.userAgent.indexOf('Edg') != -1;
const isGoogleChrome = !!(isChromium && !isEdgeChromium);

const openSearch = function () {
  // console.log("open search")
  searchBody.hide();
  searchOverlay.show();
  searchOverlay.removeClass('hidden');
  searchInput.focus();
};

const closeSearch = function () {
  // console.log("close search")
  searchInput.val('');
  searchOverlay.hide();
  searchOverlay.addClass('hidden');
};

// Variable to check if search service is loaded
let searchServiceIsLoaded = false;

  if (show) {
    searchInput.prop('disabled', true);
    searchInput.attr('placeholder', 'Please count to five...');
    overlayInner.append(loadingBar);
    loadingBar.css({ width: '100%', opacity: 1 });
  } else {
    searchInput.prop('disabled', false);
    searchInput.attr('placeholder', 'search');
    loadingBar.remove();
  }
}

// Simulate initialization
// toggleLoadingAnimation(true);
// setTimeout(() => {
//   toggleLoadingAnimation(false);
// }, 5000); // Adjust the timeout value to match the actual initialization time


// function toggleLoadingAnimation(show) {
//   const loadingIcon = $('.loading-icon');
//   const searchInput = $('#search-input');
//   const loadingBar = $('.loading-bar');
//
//   if (show) {
//     loadingIcon.show();
//     searchInput.prop('disabled', true);
//     searchInput.attr('placeholder', 'Please count to five...');
//     searchInput.hide();
//     loadingBar.show();
//     loadingBar.css({ opacity: 1 });
//   } else {
//     loadingIcon.hide();
//     searchInput.prop('disabled', false);
//     searchInput.attr('placeholder', 'search');
//     searchInput.show();
//     loadingBar.hide();
//     loadingBar.css({ opacity: 0 });
//   }
// }

async function initializeSearchService() {
  toggleLoadingAnimation(true);
  console.debug('Initializing search service...');
  searchParsingIcon.show();

  const saved_uuid = localStorage.getItem('saved_uuid');
  console.debug(`Retrieved the saved_uuid from localStorage: ${saved_uuid}`);

  if (!isGoogleChrome && 'indexedDB' in window && saved_uuid && saved_uuid === build_uuid) {
    try {
      console.debug('Initializing SearchService (assume documents already cached)...');
      searchService = new SearchService('search-results', saved_uuid);
      await searchService.initializeAsync(null);
      console.debug('SearchService is initialized.');
    } catch (error) {
      console.error('Failed to initialize SearchService:', error);
      searchServiceIsLoaded = false;
    } finally {
      searchParsingIcon.hide();
      searchServiceIsLoaded = true;
    }
  } else {
    console.debug('Documents not cached yet.');

    $.ajax({
      url: `${baseURL}/index.json`,
      dataType: 'json',
      async success(data) {
        try {
          console.debug('Retrieved and processed index.json.');
          console.debug('Initializing SearchService...');

          searchService = new SearchService('search-results', build_uuid);
          await searchService.initializeAsync(data);

          localStorage.setItem("saved_uuid", build_uuid);

          console.debug('SearchService is initialized.');
          searchParsingIcon.hide();
        } catch (error) {
          console.error('Failed to initialize SearchService:', error);
          searchServiceIsLoaded = false;
        } finally {
          searchParsingIcon.hide();
          searchServiceIsLoaded = true;
        }
      },
    });
  }
}

let searchService;
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

const debounce = new Debouncer(300);

// triggers for closing search
searchOverlay.on('click', function (e) {
  if (e.target != this) return; // don't close for children
  closeSearch();
});
$(document).keyup((e) => {
  e.key === 'Escape' ? closeSearch() : null;
});

closeButton.on('click', closeSearch);

// triggers for opening search
searchOpenTrigger.on('click', openSearch);

// triggers for performing search functions
searchInput.on('input', (e) => {
  console.log(`Executing search on input: ${e.target.value}`);
  debounce.debounce(() => {
    console.log(`debounce callback: ${e.target.value}`);
    search(e.target.value);
  });
});

// trigger to render more results
loadMoreResultsButton.on('click', () => {
  if (searchService) searchService.loadMoreResults();
  loadMoreResultsButton.blur(); // onfocus
});

// Internet Explorer compatability patches
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

console.debug('search module is loaded.');

// Initialize the search service when the module loads
initializeSearchService();
