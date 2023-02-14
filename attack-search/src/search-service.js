import {IndexHelper} from "./index-helper.js";
import {load_more_results, search_body} from "./components.js";
import {buffer} from "./settings.js";

export class SearchService {
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
     * @param {str} queryString string to search for in the indexes
     */
    query(queryString) {
        console.debug("Executing query method.");

        console.debug(`SearchService.query: Executing queryString.trim()`);
        this.current_query.clean = queryString.trim();
        console.debug(`this.current_query.clean=${this.current_query.clean}`);

        // build joined string
        let joined = "(" + this.current_query.clean.split(" ").join("|") + ")";
        this.current_query.joined = new RegExp(joined, "gi");

        //build regex for each word
        let escaped = this.current_query.clean.replace(/\s+/, " "); //remove double spaces which causes query to match on every 0 length string and flip out
        this.current_query.words = escaped.split(" ").map(function (searchWord) {
            let regexString = searchWord.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'); //escape all regex chars so that entering ".." doesn't cause it to flip out
            regexString = regexString.replace(/((?:att&ck)|(?:attack))/gi, '((?:att&ck)|(?:attack))') //equivalence of ATT&CK and attack
            return {word: searchWord, regex: new RegExp(regexString, "gi")}
        });
        console.debug(`Setting index query to ${this.current_query.clean}`);
        this.index.setQuery(this.current_query.clean);
        console.debug(`Clearing results.`);
        this.clearResults();
        console.debug(`Calling this.nextPage()`);
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

        this.current_query.words.forEach(function (searchWord) {
            let currMatches;
            while ((currMatches = searchWord.regex.exec(preview)) !== null) {
                positions.push({
                    index: searchWord.regex.lastIndex,
                    word: searchWord.word
                });
            }
        })


        positions.sort(function (a, b) {
            console.debug(`a=${a}`);
            console.debug(`b=${b}`);
            return a.index - b.index
        });

        //are two sets equal
        function setsEqual(s1, s2) {
            if (s1.size !== s2.size) return false;
            for (var a of s1) if (!s2.has(a)) return false;
            return true;
        }

        let allWords = new Set(this.current_query.words.map(function (word) {
            return word.word
        }))

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
        console.debug(`Executing SearchService.nextPage`);
        let results = this.index.nextPage();
        console.debug(`SearchService.nextPage: processing results: ${results}`);
        if (results.length > 0) this.hasResults = true;
        console.debug(`this.hasResults=${this.hasResults}`);
        if (this.hasResults) {
            search_body.show();
            console.debug(`search_body.show() was executed.`);
            let self = this;
            let resultHTML = results.map(function (result) {
                return self.result_to_html(result)
            });
            resultHTML = resultHTML.join("");
            this.render_container.append(resultHTML);
            if (this.index.nextPageRef) load_more_results.show();
            else load_more_results.hide();
        } else {
            if (this.current_query.clean !== "") { //search with no results
                search_body.show();
                console.debug(`search_body.show() was executed.`);
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
