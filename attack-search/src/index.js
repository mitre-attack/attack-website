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
const { baseURL, TITLE_INDEX_KEY } = require('./settings.js');

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

// eslint-disable-next-line import/extensions
const { CONTENT_INDEX_KEY } = require('./settings.js');

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

let searchService;
const search = function (query) {
  console.debug(`search -> Received search query: ${query}`);
  if (!searchService) {
    console.debug('search -> search index is not loaded...');
    searchParsingIcon.show();

    // Initializing search service

    // eslint-disable-next-line camelcase
    const saved_uuid = localStorage.getItem('saved_uuid');

    // eslint-disable-next-line camelcase
    console.debug(`Retrieved the saved_uuid from localStorage: ${saved_uuid}`);

    /**
     * IndexedDB is a web-based database that allows you to store and retrieve data in the client-side (in the
     * browser). It is designed for web applications that need to store large amounts of data, such as audio and
     * video files, images, and structured data, on the client side. IndexedDB provides a transactional, NoSQL-style
     * database that can be used to store and retrieve data even when the user is offline.
     *
     * IndexedDB is a part of the Web Storage API and is supported by modern browsers, including Google Chrome,
     * Mozilla Firefox, Microsoft Edge, and Apple Safari.
     *
     * The main benefits of using IndexedDB over other client-side storage options, such as local storage or
     * cookies, are its ability to store large amounts of structured data, its transactional nature, and its ability
     * to search and retrieve data using indexes.
     *
     * To use IndexedDB in your web application, you need to create a database, define object stores to store your
     * data, and use transactions to interact with the data. The database is created using the indexedDB.open
     * method, and transactions are used to read and write data using the IDBTransaction object.
     *
     * Overall, IndexedDB is a powerful and flexible client-side database that can be used to store and retrieve
     * large amounts of structured data in web applications. It is particularly useful for web applications that
     * need to work offline or that need to store large amounts of data on the client side.
     */

    // eslint-disable-next-line camelcase
    if (!isGoogleChrome && 'indexedDB' in window && saved_uuid && saved_uuid === build_uuid) {

      /**
       * Basically, if we're running in a non Chrome-based browser (such as Firefox) that has access to an IndexDB (most
       * modern web browsers should...) AND we already have the build UUID stored in localStorage, then we can assume
       * that the search indexes (there are two: one for title queries and one for content queries) are cached in the
       * IndexDB, in which case we should retrieve them (using localforage) and load them into memory; THEN we can
       * execute the user's search query.
       */

      console.debug('search -> Attempting to retrieve cached search index...');
      searchService = new SearchService('search-results', null);
      console.debug('search -> Initialized new search index!');
      console.debug(`search -> Executing search query: ${query}`);
      searchService.query(query);
      searchParsingIcon.hide();

      // TODO remove this block after all IndexedDB logic has been migrated to the new AttackIndex class
      // Retrieving cached FlexSearch instances
      // localforage.getItem(TITLE_INDEX_KEY).then((savedTitle) => {
      //   localforage.getItem(CONTENT_INDEX_KEY).then((savedContent) => {
      //     const exported = {
      //       title: savedTitle,
      //       content: savedContent
      //     };
      //     searchService = new SearchService('search-results', null, exported);
      //     console.debug('search -> Initialized new search index!');
      //     console.debug(`search -> Executing search query: ${query}`);
      //     searchService.query(query);
      //     searchParsingIcon.hide();
      //   });
      // });

    } else {
      console.debug('search -> Generating new search index...');
      // Initializing instances of FlexSearch
      $.ajax({ // if docs have not yet been loaded
        url: `${baseURL}/index.json`,
        dataType: 'json',
        success(data) {
          console.debug('Retrieved and processed index.json');
          searchService = new SearchService('search-results', data);
          console.debug('search -> Initialized new search index!');
          console.debug(`search -> Executing search query: ${query}`);
          searchService.query(query);
          searchParsingIcon.hide();
        },
      });
    }
  } else {
    console.debug(`search -> Executing search query: ${query}`);
    searchService.query(query);
  }
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
  if (searchService) searchService.nextPage();
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
