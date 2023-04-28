import {
    searchBody,
    searchOverlay,
    searchInput,
    searchParsingIcon,
    searchButton,
    searchIcon,
    closeButton,
    loadMoreResults,
    loadMoreResultsButton,
} from './components.mjs';

import $ from "jquery";

import { Debouncer } from './debouncer.mjs';

import { MessageType } from "./settings.mjs";

export class SearchRenderer {

    constructor(workbox) {

        this.workbox = workbox;

        // this.render_container = $(`#${tag}`);
        this.render_container = $('#search-results');

        // Sets the maximum number of search results displayed on a single page.
        // Clicking "Load more results" will add ${pageLimit} additional results to the current page.
        this.pageLimit = 5;

        // 2* buffer is roughly the size of the result preview
        this.buffer = 200;

        this.offset = 0;

        this.debouncer = new Debouncer(300);

        this.currentQuery = {
            clean: '',
            words: [
                /*
                 * {
                 *    word: the raw word
                 *    regex: regular expression to find this word in the document
                 * }
                 */
            ],
            joined: '', // alternation
        };

        this.searchResults = [];
    }

    initializeEventHandlers() {
        console.log('Initializing event handlers for SearchRenderer.');

        const self = this; // Save a reference to the instance

        // Set up event handlers for closing search
        searchOverlay.on('click', function (e) {
            if (e.target != this) return; // don't close for children
            self.#closeSearch();
        });

        $(document).keyup((e) => {
            e.key === 'Escape' ? self.#closeSearch() : null;
        });

        // Set up event handler for close button
        closeButton.on('click', self.#closeSearch);

        // Set up event handlers for opening search
        searchButton.on('click', self.#openSearch);

        // Set up event handler for load more results button
        loadMoreResultsButton.on('click', () => {
            self.loadMoreResults();
            loadMoreResultsButton.blur(); // onfocus
        });

        // Set up event handler for search input
        searchInput.on('input', async (e) => {
            console.debug(`Executing search on input: ${e.target.value}`);
            self.debouncer.debounce(async () => {

                console.debug('Cleaning query string before send.');
                self.#cleanTheQuery(e.target.value);

                console.debug(`Posting search request (${e.target.value}) to service worker.`);
                let response;
                try {
                    response = await self.workbox.messageSW({
                        type: MessageType.SEARCH,
                        data: this.currentQuery.clean
                    });
                } catch (e) {
                    console.error('An error occurred while waiting for a response from the service worker: ', e);
                }
                console.debug('Received response from service worker.');

                if (response.type === MessageType.ERROR) {
                    console.error(response.error);
                    throw new Error('Service Worker was unable process search request.');
                }

                if (response.type === MessageType.SEARCH_RESULTS) {
                    console.debug('Service Worker successfully processed search request.');
                    self.setSearchResults(response.data);
                }
            });
        });

    }

    /**
     * Renders the search results on the web page based on the given search result page.
     * If the search query is empty, it will show the "Load More Results" button.
     * If the search query has no results, it will display a "no results" message.
     *
     * @private
     * @function
     * @param {Array<{ id: number, title: string, path: string, content: string }>} page - An array of search result
     * objects, where each object has an `id`, a `title`, a `path`, and a `content` property.
     *
     * @example
     * page: [
     *   {
     *     id: 0,
     *     title: "Random title",
     *     path: "/path/to/random/page.html",
     *     content: "Some random content."
     *   },
     *   {
     *     id: 1,
     *     title: "Another random title",
     *     path: "/path/to/another/random/page.html",
     *     content: "Some more random content."
     *   }
     * ]
     */
    #renderSearchResults(page) {
        console.debug('Rendering search results: ', page);
        if (page.length > 0) {
            // Render the search results
            searchBody.show();
            const self = this;
            let resultHTML = page.map((result) => self.#resultToHTML(result));
            resultHTML = resultHTML.join('');
            this.render_container.append(resultHTML);

            // if there are more pages to show
            if (this.offset + this.pageLimit < this.searchResults.length) {
                loadMoreResults.show();
            } else {
                loadMoreResults.hide();
            }

        } else if (this.currentQuery.clean !== '') {
            // search with no results
            searchBody.show();
            this.render_container.html(`<div class="search-result">no results</div>`);
            loadMoreResults.hide();
        } else {
            // query for empty string
            searchBody.hide();
        }
    }

    /**
     * Converts a search result object to an HTML string with highlighted search words.
     * The HTML string will include the result's title, a link to the result's path, and a preview of the content
     * with search words highlighted. The preview will be trimmed to a buffer size around the found words.
     *
     * @private
     * @function
     * @param {Object} result - A search result object containing an `id`, a `title`, a `path`, and a `content` property.
     * @returns {string} An HTML string representing the search result with highlighted search words.
     */
    #resultToHTML(result) {
        // create title and path
        let { title } = result;

        let path = base_url.slice(0, -1) + result.path;

        if (path.endsWith('/index.html')) {
            path = path.slice(0, -11);
        }

        // create preview html
        let preview = result.content;

        // Find a position where the search words occur near each other
        const positions = [];

        this.currentQuery.words.forEach((searchWord) => {
            let currMatches;
            while ((currMatches = searchWord.regex.exec(preview)) !== null) {
                positions.push({
                    index: searchWord.regex.lastIndex,
                    word: searchWord.word,
                });
            }
        });

        positions.sort((a, b) => a.index - b.index);

        // are two sets equal
        function setsEqual(s1, s2) {
            if (s1.size !== s2.size) return false;
            for (const a of s1) if (!s2.has(a)) return false;
            return true;
        }

        const allWords = new Set(this.currentQuery.words.map((word) => word.word));

        const pos = 0;
        const best = {
            min: 0,
            max: 0,
            totalDist: Infinity, // distance between words
            totalFound: 0, // total number of words found
        };
        for (let i = 0; i < positions.length; i++) {
            const position = positions[i];
            const {word} = position;
            const {index} = position;

            // find out how far we have to go from this position to find all words
            const foundWords = new Set();
            foundWords.add(position.word);

            let totalDist = 0; // total distance between words for this combination
            let max = index; // leftmost word find
            let min = index; // rightmost word find

            if (setsEqual(allWords, foundWords)) {
                // 1 word search
                best.min = index + 10;
                best.max = index - 10;
                break;
            } else {
                // search around this word
                for (let j = 0; i + j < positions.length || i - j > 0; j++) {
                    // search j ahead
                    let exceeded = 0;
                    if (i + j < positions.length - 1) {
                        const ahead = positions[i + j];
                        const dist = ahead.index - index;
                        if (dist > this.buffer) { // exceeded buffer
                            exceeded++;
                        } else if (!foundWords.has(ahead.word)) { // found a word
                            foundWords.add(ahead.word);
                            max = ahead.index;
                            totalDist += ahead.index - index;
                        }
                    }
                    // search j behind
                    if (i - j >= 0) {
                        const behind = positions[i - j];
                        const dist = index - behind.index;
                        if (dist > this.buffer) { // exceeded buffer
                            exceeded++;
                        } else if (!foundWords.has(behind.word)) { // found a word
                            foundWords.add(behind.word);
                            min = behind.index;
                            totalDist += index - behind.index;
                        }
                    }
                    // found all the words in proximity, or both searches
                    if (setsEqual(allWords, foundWords) || exceeded == 2) {
                        // exceeded the buffer
                        break;
                    }
                }
            }
            // by now we must have found as many words as we can
            // total found words takes priority over the distance
            if (foundWords.size > best.totalFound || (totalDist < best.totalDist
                && foundWords.size >= best.totalFound)) {
                // new best
                best.totalDist = totalDist;
                best.max = max;
                best.min = min;
                best.totalFound = foundWords.size;
            }
        }

        // buffer around keyword
        const left = Math.max(0, best.min - this.buffer);
        const right = Math.min(preview.length, best.max + this.buffer);
        preview = preview.slice(left, right); // extract buffer

        // add ellipses to preview so people know that the preview is not the complete page data
        if (right < result.content.length) preview += '&hellip;';
        if (left > 0) preview = `&hellip; ${preview}`;

        // surround preview keywords with highlight class span tags
        preview = preview.replace(this.currentQuery.joined, "<span class='search-word-found'>$1</span>");
        // surround title keywords with highlight class span tags
        title = title.replace(this.currentQuery.joined, "<span class='search-word-found'>$1</span>");

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
        `; // end template
    }

    /**
     * Cleans and processes the search query by trimming white spaces, escaping special characters, and creating
     * regular expressions for each word in the query. The processed query is stored in the `this.currentQuery` object.
     *
     * @private
     * @function
     * @param {string} query - The raw search query string.
     */
    #cleanTheQuery(query) {
        console.debug(`Cleaning query string: ${query}`);

        this.currentQuery.clean = query.trim();

        // build joined string
        const joined = `(${this.currentQuery.clean.split(' ').join('|')})`;
        this.currentQuery.joined = new RegExp(joined, 'gi');

        // Build regex for each word

        // remove double spaces which causes query to match on every 0 length string and flip out
        const escaped = this.currentQuery.clean.replace(/\s+/, ' ');

        // The following map code is modifying the current_query object by setting its words property to an array of
        // objects. Each object in the array represents a word that was entered as part of a search query, along with a
        // regular expression that can be used to match that word in a larger body of text.

        this.currentQuery.words = escaped.split(' ').map((searchWord) => {
            // This line replaces any special characters in the search word with escape characters, so that they can be safely
            // used in a regular expression. The g flag ensures that all occurrences of special characters in the word are
            // replaced, and \\$& inserts the original character as a literal string in the replacement.
            // In other words: escape all regex chars so that entering ".." doesn't cause it to flip out
            let regexString = searchWord.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');

            // This line replaces any occurrence of "att&ck" or "attack" with the regular expression pattern
            // ((?:att&ck)|(?:attack)). This is done to make the search more flexible and include results that may use
            // different forms of the term.
            regexString = regexString.replace(/((?:att&ck)|(?:attack))/gi, '((?:att&ck)|(?:attack))');

            // This line creates a new object that contains the original search word and its corresponding regular expression.
            // The regular expression is created using the RegExp constructor, with the gi flags to make it global and
            // case-insensitive.
            return {
                word: searchWord,
                regex: new RegExp(regexString, 'gi')
            };
        });
    }

    #openSearch() {
        searchBody.hide();
        searchOverlay.show();
        searchOverlay.removeClass('hidden');
        searchInput.focus();
    }

    #closeSearch() {
        searchInput.val('');
        searchOverlay.hide();
        searchOverlay.addClass('hidden');
    };

    /**
     * Asynchronously loads and renders more search results by increasing the current offset.
     * This method is used for paginating the search results.
     *
     * @async
     * @function
     */
    loadMoreResults() {
        this.offset += this.pageLimit;
        const nextPage = this.searchResults.slice(this.offset, this.offset + this.pageLimit);
        console.debug('search index results: ', nextPage);
        this.#renderSearchResults(nextPage);
    }

    setSearchResults(results) {
        console.debug('Setting search results: ', results);
        this.offset = 0;
        this.render_container.html('');
        this.searchResults = results;
        const firstPage = this.searchResults.slice(0, this.pageLimit);
        this.#renderSearchResults(firstPage);
    }

}
