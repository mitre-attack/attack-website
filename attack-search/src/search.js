import FlexSearch from 'flexsearch';
import localforage from 'localforage';
import $ from 'jquery';

/**
 * It is important that the `.js` file extension be included for local imports, otherwise webpack won't be able to
 * resolve it. i.e., webpack will throw an error like the following:
 *
 * ERROR in ./src/search.js 12:0-20
 * Module not found: Error: Can't resolve './settings' in '/foo/bar/attack-website/attack-search/src'
 */

// eslint-disable-next-line import/extensions
import { baseURL } from './settings.js';

// eslint-disable-next-line import/extensions
import Debouncer from './debouncer.js';

// eslint-disable-next-line import/extensions
import SearchService from './search-service.js';

import {
  searchBody,
  searchOverlay,
  searchInput,
  searchParsingIcon,
  searchOpenTrigger,
  closeButton,
  loadMoreResultsButton,
// eslint-disable-next-line import/extensions
} from './components.js';

// Register custom matchers globally
FlexSearch.registerMatcher({
  // attack and ATT&CK are equivalent for the purposes of search
  'ATT&CK': 'ATTACK',
  ATTACK: 'ATT&CK',
});

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
  console.debug(`Executing search on query: ${query}`);
  if (!searchService) {
    console.debug('searchService is NOT defined!');
    searchParsingIcon.show();
    console.debug('Showed the search_parsing_icon');

    // Initializing search service

    const savedUUID = localStorage.getItem('saved_uuid');
    console.debug(`Retrieved the saved_uuid from localStorage: ${savedUUID}`);

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

    if (!isGoogleChrome && 'indexedDB' in window && savedUUID && savedUUID === buildUUID) {
      console.debug('isGoogleChrome=False; indexedDB=truthy; saved_uuid=Truthy; saved_uuid==build_uuid=truthy');
      // Retrieving cached FlexSearch instances
      localforage.getItem('index_helper_title').then((savedTitle) => {
        localforage.getItem('index_helper_content').then((savedContent) => {
          const exported = { title: savedTitle, content: savedContent };
          searchService = new SearchService('search-results', null, exported);
          console.debug('Initialized new searchService (1)');
          searchService.query(query);
          searchParsingIcon.hide();
        });
      });
    } else {
      console.debug('Something in that last condition was falsy so we need to initialize some instances of FlexSearch');
      // Initializing instances of FlexSearch
      $.ajax({ // if docs have not yet been loaded
        url: `${baseURL}/index.json`,
        dataType: 'json',
        success(data) {
          searchService = new SearchService('search-results', data, null);
          console.debug('Initialized new searchService (2)');
          searchService.query(query);
          searchParsingIcon.hide();
        },
      });
      console.debug('Retrieved and processed index.json');
    }
  } else {
    console.debug(`searchService IS defined! Executing searchService.query(${query})`);
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
