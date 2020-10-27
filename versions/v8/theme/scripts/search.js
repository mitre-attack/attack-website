let site_base_url = "";
let page_limit = 5; //number of results per page
let buffer = 200; //2* buffer is roughly the size of the result preview


// overlay container
let search_overlay = $("#search-overlay");
// button in header to open search
let search_open_trigger = $("#search-button"); 
// button to close search
let close_button = $("#close-search-icon")
// text input on search page
let search_input = $("#search-input");
// body of search results
let search_body = $("#search-body");
// button to show more results
let load_more_results = $("#load-more-results");
let load_more_results_button = $("#load-more-results-button");
// search parsing icon
let search_parsing_icon = $("#search-parsing-icon");

// register custom matchers globally
FlexSearch.registerMatcher({
    //attack and ATT&CK are equivalent for the purposes of search
    "ATT&CK": "ATTACK", 
    "ATTACK": "ATT&CK"
})

var isChromium = window.chrome;
var isEdgeChromium = isChromium && navigator.userAgent.indexOf("Edg") != -1;
var isGoogleChrome = isChromium && !isEdgeChromium ? true : false;

class IndexHelper {
    constructor(documents, exported) {
        this.indexes = {
            "title": new FlexSearch({
                encode: "simple",     //phonetic normalizations
                tokenize: "forward",  //match substring beginning of word
                threshold: 2,         //exclude scores below this number
                resolution: 9,        //how many steps in the scoring algorithm
                depth: 4,             //how far around words to search for adjacent matches. Disabled for title
                doc: {
                    id: "id",
                    field: "title"
                }
            }),
            "content": new FlexSearch({
                encode: "simple",     //phonetic normalizations
                tokenize: "strict",  //match substring beginning of word
                threshold: 2,        //exclude scores below this number
                resolution: 9,       //how many steps in the scoring algorithm
                depth: 4,            //how far around words to search for adjacent matches. Disabled for title
                doc: {
                    id: "id",
                    field: "content"
                }
            })
        }

        // console.log("adding pages to index");
        if (documents && !exported) {
            this.indexes.title.add(documents);
            this.indexes.content.add(documents);

            localStorage.setItem("saved_uuid", build_uuid);
            localforage.setItem("index_helper_title", this.indexes.title.export());
            localforage.setItem("index_helper_content", this.indexes.content.export());
        } else if (!documents && exported) {
            this.indexes.title.import(exported.title);
            this.indexes.content.import(exported.content);
        } else {
            console.error("invalid argument: constructor must be called with either documents or exported");
        }

        this.setQuery("");
    }
    setQuery(query) {
        this.query = query;
        this.nextPageRef = true;
        this.titleStage = true;
        this.seenPaths = new Set();
    }
    nextPage() {
        let results = this.nextPageHelper();
        let self = this;
        results = results.filter(function(result) { return !self.seenPaths.has(result.path) });
        results.forEach(function(result) { self.seenPaths.add(result.path) });

        // keep fetching until we have no more results or we have enough results
        while (results.length < page_limit) {
            let newResults = this.nextPageHelper(page_limit - results.length);
            if (newResults.length == 0) break; //ran out of results
            // cull duplicates
            newResults = newResults.filter(function(result) { return !self.seenPaths.has(result.path) });
            newResults.forEach(function(result) { self.seenPaths.add(result.path) });
            // append to master list
            results = results.concat(newResults);
        }

        return results;
    }
    /**
     * Get the next page of results, or null if no more pages
     * @param {int} limit the number of results to get (default is the page_limit)
     */
    nextPageHelper(limit=page_limit) {
        if (!this.nextPageRef) {
            console.warn("no next page")
            return []
        }

        if (this.titleStage) {
            // console.log("fetching next title page")
            let response = this.indexes.title.search(this.query, {
                limit: limit,
                page: this.nextPageRef
            });
            let results = response.result.map(function(result) {
                result.source = "title";
                return result;
            });

            if (response.next) { //next page exists on title stage
                this.nextPageRef = response.next;
                return results;
            } else { //end of title stage
                this.titleStage = false;
                this.nextPageRef = true;
                return results;
            }
        } else { //content stage
            // console.log("fetching next content page")
            let response = this.indexes.content.search(this.query, {
                limit: limit,
                page: this.nextPageRef
            });
            this.nextPageRef = response.next;
            return response.result.map(function(result) {
                result.source = "content";
                return result;
            });
        }
        
    }
}

class SearchService {
    constructor(tag, documents, exported) {
        // init indexes
        this.index = new IndexHelper(documents, exported);
        this.current_query = {
            clean: "",
            words: [
                /* 
                 * { 
                 *    word: the raw word
                 *    regex: regular expression to find this word in the document
                 * }
                 */ 
            ],
            joined: "" //alternation
        }
        this.render_container = $("#" + tag);
    }


    /**
     * update the search (query) string
     * @param {str} querystr string to search for in the indexes
     */
    query(querystr) {
        this.current_query.clean = querystr.trim();

        // build joined string
        let joined = "(" + this.current_query.clean.split(" ").join("|") + ")";
        this.current_query.joined = new RegExp(joined, "gi")

        //build regex for each word
        let escaped = this.current_query.clean.replace(/\s+/, " "); //remove double spaces which causes query to match on every 0 length string and flip out
        this.current_query.words = escaped.split(" ").map(function(searchword) {
            let regexstr = searchword.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'); //escape all regex chars so that entering ".." doesn't cause it to flip out
            regexstr = regexstr.replace(/((?:att&ck)|(?:attack))/gi, '((?:att&ck)|(?:attack))') //equivalence of ATT&CK and attack
            return { word: searchword, regex: new RegExp(regexstr, "gi") }
        });

        this.index.setQuery(this.current_query.clean);
        this.clearResults();
        this.nextPage(); //render first page of results
    }

    /**
     * parse the result to the HTML required to render it
     * @param result object of format {title, path, content} which describes a page on the site
     */
    result_to_html(result) {
        //create title and path
        let title = result.title;
        let path = base_url.slice(0, -1) + result.path;
        if (path.endsWith("/index.html")) {
            path = path.slice(0, -11);
        }
        // create preview html
        let preview = result.content;
        
        // Find a position where the search words occur near each other
        let positions = []

        this.current_query.words.forEach(function(searchword) {
            let currMatches;
            while((currMatches = searchword.regex.exec(preview)) !== null) {
                positions.push({
                    index: searchword.regex.lastIndex,
                    word: searchword.word
                });
            }
        })



        
        positions.sort(function(a,b) { return a.index - b.index });
        //are two sets equal
        function setsEqual(s1, s2) {
            if (s1.size !== s2.size) return false;
            for (var a of s1) if (!s2.has(a)) return false;
            return true;
        }
        let allWords = new Set(this.current_query.words.map(function(word) { return word.word }))
        
        let pos = 0;
        let best = {
            min: 0,
            max: 0,
            totalDist: Infinity, //distance between words
            totalFound: 0 //total number of words found
        };
        for (let i = 0; i < positions.length; i++) {
            const position = positions[i];
            let word = position.word;
            let index = position.index;

            // find out how far we have to go from this position to find all words
            let foundWords = new Set();
            foundWords.add(position.word);

            let totalDist = 0; //total distance between words for this combination
            let max = index; //leftmost word find
            let min = index //rightmost word find

            if (setsEqual(allWords, foundWords)) {
                //1 word search
                best.min = index + 10;
                best.max = index - 10
                break;
            } else {
                // search around this word
                for (let j = 0; i + j < positions.length || i - j > 0; j++) {
                    // search j ahead
                    let exceeded = 0;
                    if (i + j < positions.length - 1) {
                        let ahead = positions[i + j];
                        let dist = ahead.index - index;
                        if (dist > buffer) { //exceeded buffer
                            exceeded++;
                        } else if (!foundWords.has(ahead.word)) { // found a word
                            foundWords.add(ahead.word);
                            max = ahead.index;
                            totalDist += ahead.index - index
                        }
                    }
                    //search j behind
                    if (i - j >= 0) {
                        let behind = positions[i - j];
                        let dist = index - behind.index;
                        if (dist > buffer) { //exceeded buffer
                            exceeded++;
                        } else if (!foundWords.has(behind.word)) { // found a word
                            foundWords.add(behind.word);
                            min = behind.index;
                            totalDist += index - behind.index;
                        }
                    }
                    if (setsEqual(allWords, foundWords) || exceeded == 2) { //found all the words in proximity, or both searches exceeded the buffer
                        break;
                    }
                }
            }
            //by now we must have found as many words as we can
            //total found words takes priority over the distance
            if (foundWords.size > best.totalFound || (totalDist < best.totalDist && foundWords.size >= best.totalFound)) {
                // new best
                best.totalDist = totalDist;
                best.max = max;
                best.min = min;
                best.totalFound = foundWords.size;
            }
        }
        
        // buffer around keyword
        let left = Math.max(0, best.min - buffer);
        let right = Math.min(preview.length, best.max + buffer);
        preview = preview.slice(left, right); //extract buffer

        // add elipses to preview so people know that the preview is not the complete page data
        if (right < result.content.length) preview += "&hellip;";
        if (left > 0) preview = "&hellip; " + preview;

        // surround preview keywords with highlight class span tags
        preview = preview.replace(this.current_query.joined, "<span class='search-word-found'>$1</span>");
        // surround title keywords with highlight class span tags
        title = title.replace(this.current_query.joined, "<span class='search-word-found'>$1</span>");

        // result html template
        return `
            <div class="search-result mb-4">
                <div class="title">
                    <a href="${path}">${title}</a>
                </div>
                <div class="preview">
                    ${preview}
                </div>
            </div>
        `; //end template
    }

    /**
     * clear the rendered results from the page
     */
    clearResults() {
        this.render_container.html("");
        this.hasResults = false;
    }

    /**
     * render the next page of results if one exists
     */
    nextPage() {
        let results = this.index.nextPage();
        if (results.length > 0) this.hasResults = true;
        if (this.hasResults) {
            search_body.show();
            let self = this;
            let resultHTML = results.map(function(result) { return self.result_to_html(result) });
            resultHTML = resultHTML.join("");
            this.render_container.append(resultHTML);
            if (this.index.nextPageRef) load_more_results.show();
            else                        load_more_results.hide();
        } else {
            if (this.current_query.clean !== "") { //search with no results
                search_body.show();
                this.render_container.html(`
                    <div class="search-result">no results</div>
                `)
                load_more_results.hide();
            } else { // query for empty string
                search_body.hide();
            }
        }
    }
}





let openSearch = function() {
    // console.log("open search")
    search_body.hide();
    search_overlay.show();
    search_overlay.removeClass("hidden");
    search_input.focus();
}

let closeSearch = function() {
    // console.log("close search")
    search_input.val('');
    search_overlay.hide();
    search_overlay.addClass("hidden");
}

let search_service = null;
let search = function(query) {
    if (search_service == null) {
        search_parsing_icon.show()
        // console.log("initializing search service")

        let saved_uuid = localStorage.getItem("saved_uuid");

        if (!isGoogleChrome && 'indexedDB' in window && saved_uuid && saved_uuid == build_uuid) {
            // console.log("getting cached flexsearch objects");
            localforage.getItem("index_helper_title").then((saved_title) => {
                localforage.getItem("index_helper_content").then((saved_content) => {
                    exported = {title: saved_title, content: saved_content};
                    search_service = new SearchService("search-results", null, exported);
                    search_service.query(query);
                    search_parsing_icon.hide();
                });
            });
        } else {
            // console.log("making new flexsearch objects");
            $.ajax({ //if docs have not yet been loaded
                url: base_url + "/index.json",
                dataType: "json",
                success: function (data) {
                    search_service = new SearchService("search-results", data, null);
                    search_service.query(query);
                    search_parsing_icon.hide();     
                }
            });
        }
    } else {
        search_service.query(query);
    }
}

//utility class for debouncing function calls.
//used to debounce keyboard input so that rapid keypresses doesn't overwhelm the computer.
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
        setTimeout(function() {
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
search_overlay.on("click", function(e) {
    if (e.target != this) return; //don't close for children
    else closeSearch();
})
$(document).keyup(function(e) { e.key === 'Escape'? closeSearch():null });
close_button.on("click", closeSearch);
// triggers for opening search
search_open_trigger.on("click", openSearch);
// triggers for performing search functions
search_input.on("input", function(e) { 
    debounce.debounce(function() { search(e.target.value) });
})
// trigger to render more results
load_more_results_button.on("click", function() {
    if (search_service) search_service.nextPage();
    load_more_results_button.blur(); //onfocus
});

//internet explorer compatability patches
if (!String.prototype.includes) {
    String.prototype.includes = function(search, start) {
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
    String.prototype.endsWith = function(suffix) {
        return this.indexOf(suffix, this.length - suffix.length) !== -1;
    };
}