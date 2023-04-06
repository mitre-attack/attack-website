const $ = require('jquery');

// eslint-disable-next-line import/extensions
const AttackIndex = require('./attack-index.js');

// eslint-disable-next-line import/extensions
const { loadMoreResults, searchBody } = require('./components.js');

// eslint-disable-next-line import/extensions
const { buffer, ATTACK_INDEX_KEY } = require('./settings.js');

module.exports = class SearchService {
  constructor(tag, documents, exported= false) {
    console.debug('Initializing new SearchService instance...');
    this.initialized = false;
    this.attackIndex = new AttackIndex(ATTACK_INDEX_KEY, 'website');
    /**
     * If documents are defined, then load them into the AttackIndex instance.
     * Otherwise, if exported equals 'true', then fetch the documents from the IndexDB and load them into the
     * AttackIndex instance.
     */
    if (documents) {
      this.attackIndex.add(documents).then(r => {});
    } else if (exported) {
      this.attackIndex.importFromIndexedDBtoFlexSearch().then(r => {});
    } else {
      console.error('No documents or exported data provided to SearchService.');
      throw Error('AttackIndex cannot be initialized empty.')
    }
    this.current_query = {
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
    this.render_container = $(`#${tag}`);
    this.initialized = true;
    console.debug('SearchService is initialized.');
  }

  /**
     * update the search (query) string
     * @param {string} query string to search for in the indexes
     */
  query(query) {
    console.debug(`Executing query on: ${query}`);

    // eslint-disable-next-line no-underscore-dangle
    this.#cleanTheQuery(query);

    console.debug(`Setting index query to ${this.current_query.clean}`);

    // this.index.setQuery(this.current_query.clean);
    this.attackIndex.setQuery(this.current_query.clean);

    console.debug('Clearing results.');
    this.clearResults();

    console.debug('Calling this.nextPage()');
    this.nextPage(); // render first page of results
  }

  /**
   * Preps the query string before executing it.
   * @param {string} query
   * @private
   */
  #cleanTheQuery(query) {
    console.debug(`Cleaning query string: ${query}`);

    this.current_query.clean = query.trim();

    // build joined string
    const joined = `(${this.current_query.clean.split(' ').join('|')})`;
    this.current_query.joined = new RegExp(joined, 'gi');

    // Build regex for each word

    // remove double spaces which causes query to match on every 0 length string and flip out
    const escaped = this.current_query.clean.replace(/\s+/, ' ');

    // The following map code is modifying the current_query object by setting its words property to an array of
    // objects. Each object in the array represents a word that was entered as part of a search query, along with a
    // regular expression that can be used to match that word in a larger body of text.

    this.current_query.words = escaped.split(' ').map((searchWord) => {
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
      return { word: searchWord, regex: new RegExp(regexString, 'gi') };
    });
  }

  /**
     * parse the result to the HTML required to render it
     * @param result object of format {title, path, content} which describes a page on the site
     */
  #resultToHTML(result) {
    console.debug('SearchService.result_to_html was executed.');
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

    this.current_query.words.forEach((searchWord) => {
      let currMatches;
      while ((currMatches = searchWord.regex.exec(preview)) !== null) {
        positions.push({
          index: searchWord.regex.lastIndex,
          word: searchWord.word,
        });
      }
    });

    positions.sort((a, b) =>
      // console.debug(`a=${a}`);
      // console.debug(`b=${b}`);
      a.index - b.index);

    // are two sets equal
    function setsEqual(s1, s2) {
      if (s1.size !== s2.size) return false;
      for (const a of s1) if (!s2.has(a)) return false;
      return true;
    }

    const allWords = new Set(this.current_query.words.map((word) => word.word));

    const pos = 0;
    const best = {
      min: 0,
      max: 0,
      totalDist: Infinity, // distance between words
      totalFound: 0, // total number of words found
    };
    for (let i = 0; i < positions.length; i++) {
      const position = positions[i];
      const { word } = position;
      const { index } = position;

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
            if (dist > buffer) { // exceeded buffer
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
            if (dist > buffer) { // exceeded buffer
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
    const left = Math.max(0, best.min - buffer);
    const right = Math.min(preview.length, best.max + buffer);
    preview = preview.slice(left, right); // extract buffer

    // add ellipses to preview so people know that the preview is not the complete page data
    if (right < result.content.length) preview += '&hellip;';
    if (left > 0) preview = `&hellip; ${preview}`;

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
        `; // end template
  }

  /**
     * clear the rendered results from the page
     */
  clearResults() {
    this.render_container.html('');
    this.hasResults = false;
  }

  /**
     * render the next page of results if one exists
     */
  nextPage() {
    console.debug('Executing SearchService.nextPage');
    // const results = this.index.nextPage();
    const results = this.attackIndex.nextPage();
    console.debug(`SearchService.nextPage: processing results: ${results}`);
    if (results.length > 0) this.hasResults = true;
    console.debug(`this.hasResults=${this.hasResults}`);
    if (this.hasResults) {
      searchBody.show();
      console.debug('search_body.show() was executed.');
      const self = this;
      let resultHTML = results.map((result) => self.#resultToHTML(result));
      resultHTML = resultHTML.join('');
      this.render_container.append(resultHTML);
      if (this.index.nextPageRef) loadMoreResults.show();
      else loadMoreResults.hide();
    } else if (this.current_query.clean !== '') { // search with no results
      searchBody.show();
      console.debug('search_body.show() was executed.');
      this.render_container.html(`
                    <div class="search-result">no results</div>
                `);
      loadMoreResults.hide();
    } else { // query for empty string
      searchBody.hide();
    }
  }
};
