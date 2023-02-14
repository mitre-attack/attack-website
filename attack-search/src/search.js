import FlexSearch from "flexsearch";
import localforage from "localforage";
import $ from "jquery";

/**
 * It is important that the `.js` file extension be included on the following import, otherwise webpack won't be able to
 * resolve it. Otherwise, webpack will throw an error like the following:
 *
 * ERROR in ./src/search.js 12:0-20
 * Module not found: Error: Can't resolve './settings' in '/foo/bar/attack-website/attack-search/src'
 */

import { base_url } from "./settings.js";
import { Debouncer } from "./debouncer.js";
import { SearchService } from "./search-service.js";
import {search_body, search_overlay, search_input, search_parsing_icon, search_open_trigger, close_button,
    load_more_results_button} from "./components.js";

// Register custom matchers globally
FlexSearch.registerMatcher({
    //attack and ATT&CK are equivalent for the purposes of search
    "ATT&CK": "ATTACK",
    "ATTACK": "ATT&CK"
});

let isChromium = window.chrome;
let isEdgeChromium = isChromium && navigator.userAgent.indexOf("Edg") != -1;
let isGoogleChrome = isChromium && !isEdgeChromium ? true : false;

let openSearch = function () {
    // console.log("open search")
    search_body.hide();
    search_overlay.show();
    search_overlay.removeClass("hidden");
    search_input.focus();
}

let closeSearch = function () {
    // console.log("close search")
    search_input.val('');
    search_overlay.hide();
    search_overlay.addClass("hidden");
}

let searchService;
let search = function (query) {
    console.debug(`Executing search on query: ${query}`);
    if (!searchService) {
        console.debug(`searchService is NOT defined!`);
        search_parsing_icon.show()
        console.debug(`Showed the search_parsing_icon`);

        // Initializing search service

        let saved_uuid = localStorage.getItem("saved_uuid");
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

        if (!isGoogleChrome && 'indexedDB' in window && saved_uuid && saved_uuid === build_uuid) {
            console.debug(`isGoogleChrome=False; indexedDB=truthy; saved_uuid=Truthy; saved_uuid==build_uuid=truthy`);
            // Retrieving cached FlexSearch instances
            localforage.getItem("index_helper_title").then((saved_title) => {
                localforage.getItem("index_helper_content").then((saved_content) => {
                    const exported = {title: saved_title, content: saved_content};
                    searchService = new SearchService("search-results", null, exported);
                    console.debug(`Initialized new searchService (1)`);
                    searchService.query(query);
                    search_parsing_icon.hide();
                });
            });
        } else {
            console.debug(`Something in that last condition was falsy so we need to initialize some instances of FlexSearch`);
            // Initializing instances of FlexSearch
            $.ajax({ //if docs have not yet been loaded
                url: base_url + "/index.json",
                dataType: "json",
                success: function (data) {
                    searchService = new SearchService("search-results", data, null);
                    console.debug(`Initialized new searchService (2)`);
                    searchService.query(query);
                    search_parsing_icon.hide();
                }
            });
            console.debug(`Retrieved and processed index.json`);
        }
    } else {
        console.debug(`searchService IS defined! Executing searchService.query(${query})`);
        searchService.query(query);
    }
}


/**
 * Debouncer is a utility class for debouncing function calls. It is used to debounce keyboard input so that rapid
 * keypresses doesn't overwhelm the computer.
 */
class Debouncer {
    // new debouncer, param is the amount of debounce delay time in ms
    constructor(delay) {
        this.callback = null;
        this.i = 0;
        this.delay = delay;
    }

    //callback with debounce
    debounce(callback) {
        this.callback = callback;
        this.i++;
        let i = this.i;
        let self = this;
        setTimeout(function () {
            self.resolve(i)
        }, this.delay)
    }

    //resolve the debounced callback
    resolve(i) {
        // only do the callback if a new debounced input hasn't been added.
        if (this.i == i) this.callback();
    }
}

let debounce = new Debouncer(300);

// triggers for closing search
search_overlay.on("click", function (e) {
    if (e.target != this) return; //don't close for children
    else closeSearch();
})
$(document).keyup(function (e) {
    e.key === 'Escape' ? closeSearch() : null
});
close_button.on("click", closeSearch);
// triggers for opening search
search_open_trigger.on("click", openSearch);
// triggers for performing search functions
search_input.on("input", function (e) {
    console.log(`Executing search on input: ${e.target.value}`);
    debounce.debounce(function () {
        console.log(`debounce callback: ${e.target.value}`);
        search(e.target.value)
    });
})
// trigger to render more results
load_more_results_button.on("click", function () {
    if (searchService) searchService.nextPage();
    load_more_results_button.blur(); //onfocus
});

//internet explorer compatability patches
if (!String.prototype.includes) {
    String.prototype.includes = function (search, start) {
        if (typeof start !== 'number') {
            start = 0;
        }
        if (start + search.length > this.length) {
            return false;
        } else {
            return this.indexOf(search, start) !== -1;
        }
    };
}

if (typeof String.prototype.endsWith !== 'function') {
    String.prototype.endsWith = function (suffix) {
        return this.indexOf(suffix, this.length - suffix.length) !== -1;
    };
}

console.debug("search.js is loaded.");
