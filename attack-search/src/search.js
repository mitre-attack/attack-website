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

        // Initializing search service

        let saved_uuid = localStorage.getItem("saved_uuid");

        if (!isGoogleChrome && 'indexedDB' in window && saved_uuid && saved_uuid === build_uuid) {
            // Retrieving cached FlexSearch instances
            localforage.getItem("index_helper_title").then((saved_title) => {
                localforage.getItem("index_helper_content").then((saved_content) => {
                    exported = {title: saved_title, content: saved_content};
                    searchService = new SearchService("search-results", null, exported);
                    searchService.query(query);
                    search_parsing_icon.hide();
                });
            });
        } else {
            // Initializing instances of FlexSearch
            fetch(`${base_url}/index.json`)
                .then(response => response.json())
                .then(data => {
                    let search_service = new SearchService("search-results", data, null);
                    search_service.query(query);
                    search_parsing_icon.style.display = 'none';
                })
                .catch(error => console.error(error));
        }
    } else {
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
    debounce.debounce(function () {
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
