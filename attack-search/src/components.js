import $ from "jquery";

// overlay container
let search_overlay = $("#search-overlay");

// button in header to open search
let search_open_trigger = $("#search-button");

// button to close search
let close_button = $("#close-search-icon");

// text input on search page
let search_input = $("#search-input");

// body of search results
let search_body = $("#search-body");

// button to show more results
let load_more_results = $("#load-more-results");
let load_more_results_button = $("#load-more-results-button");

// search parsing icon
let search_parsing_icon = $("#search-parsing-icon");

export {
    search_overlay,
    search_open_trigger,
    close_button,
    search_input,
    search_body,
    load_more_results,
    load_more_results_button,
    search_parsing_icon
}
