const $ = require('jquery');

// eslint-disable-next-line import/extensions
const { IndexedDBWrapper } = require("./indexed-db-wrapper.js");

// eslint-disable-next-line import/extensions
const AttackIndex = require('./attack-index.js');

// eslint-disable-next-line import/extensions
const { loadMoreResults, searchBody } = require('./components.js');

// eslint-disable-next-line import/extensions
const { buffer } = require('./settings.js');
const {pageLimit} = require("./settings");

module.exports = class SearchService {
  constructor(tag, buildId) {

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

    this.render_container = $(`#${tag}`);

    /**
     * The following two IndexedDBWrapper instances initialize two IndexedDB tables. Each instance corresponds to one
     * table. The wrapper class obfuscates the CRUD logic for interfacing with IndexedDB.
     *
     * 1. content_table: handles all objects loaded from index.json
     *
     * 2. flexsearch_table: handles the FlexSearch document instance (so we don't have to re-index index.json every time
     *    FlexSearch is cleared from browser memory!).
     */

    const schemas = {
      content_table: '&id, title, path, content',
      searchindex_table: '++id, title, content',
    };

    const dbName = buildId ? `AttackWebsite-${buildId}` : 'AttackWebsite';

    this.db = new IndexedDBWrapper(dbName, schemas);

    this.contentDb = this.db.getTableWrapper('content_table');
    this.searchIndexDb = this.db.getTableWrapper('searchindex_table');

    /**
     * A quick note on the schemas passed in the above 👆 IndexedDBWrapper initializations:
     *
     * The &id syntax means that the id field is the primary key of the table, but it will not be auto-incremented.
     * In this case, you must provide a unique value for the id field when inserting a new record, and the
     * IndexedDB will enforce uniqueness on the id field.
     *
     * The ++id syntax means that the id field is the primary key of the table and it will be auto-incremented. In
     * other words, when you insert a new record without providing a value for the id field, the IndexedDB will
     * automatically assign a unique, incremental value to the id field.
     */

    // Initialize the AttackIndex instance (this is our in-memory FlexSearch instance)
    this.attackIndex = new AttackIndex();
  }

  async initializeAsync(documents) {

    // If documents are defined, then load them into the AttackIndex instance.
    if (documents) {
      console.debug('Indexing documents: ', documents);

      // Add the data to the in-memory FlexSearch instance
      this.attackIndex.addBulk(documents);

      console.debug('Backing up search index...');

      // Backup the in-memory FlexSearch index for later restoration
      await this.backupSearchIndex();
      await this.contentDb.bulkPut(documents, 100);

      console.debug('Backup of search index completed.');
    } else {
      console.debug('Restoring search index from backup...');

      // If no documents were provided, then attempt to load them from the IndexedDB database
      await this.restoreSearchIndexFromBackup();
    }
  }

  /**
   * FORMERLY: exportFromFlexSearchToIndexedDB
   * Exports data from the in-memory FlexSearch instance to the IndexedDB.
   * @returns {Promise<Array<string>>}
   */
  async backupSearchIndex() {

    const keys = [];
    let processedKeys = 0;

    // totalKeys(x) = (3 * #searchFields) + 3
    //                          ^
    //                    title + content --> 2 fields
    const totalKeys = 9;

    return new Promise((resolve) => {
      this.attackIndex.index.export(async (key, data) => {
        await this.searchIndexDb.put({ key, data });
        keys.push(key);
        processedKeys++;

        if (processedKeys === totalKeys) {
          resolve(true);
        }
      });
    });
  }

  /**
   * Imports data from the IndexedDB to the in-memory FlexSearch instance.
   * @returns {Promise<void>}
   */
  async restoreSearchIndexFromBackup() {
    // Retrieve all records from the specified object store
    const documents = await this.searchIndexDb.getAll();

    console.debug(`Located ${documents.length} documents in the searchindex_table`);

    for (const document of documents) {
      await this.attackIndex.import(document.key, document.data);
    }
  }

  /**
   * Given an array of index positions returned by a FlexSearch query, retrieves the original content for each position
   * from the IndexedDB content_table and returns an array of matching documents.
   *
   * @param {number[]} positions - An array of index positions returned by a FlexSearch query.
   * @returns {Promise<Object[]>} - An array of matching documents retrieved from the IndexedDB content_table.
   */
  async resolveSearchResults(positions) {
    const results = [];
    for (const position of positions) {
      const doc = await this.contentDb.get(position);
      if (doc) {
        results.push(doc);
      }
    }
    return results;
  }

  /**
   * update the search (query) string
   * @param {string} query string to search for in the indexes
   */
  async query(query) {
    this.#cleanTheQuery(query);
    // this.#clearResults();
    this.render_container.html('');
    this.offset = 0;
    const results = await this.attackIndex.search(this.currentQuery.clean, ["title", "content"], 100, this.offset);
    console.debug('search index results: ', results);
    /**
     * results:  [
     *       {
     *         field: 'title',
     *         result: [
     *           2, 3, 4,  5, 6, ..., 100
     *
     *         ]
     *       },
     *       {
     *         field: 'content',
     *         result: [
     *           1, 5, 6, 7,
     *           2, 3, 8, 9,
     *         ]
     *       }
     *     ]
     */

    // title [b,x,y,z] , content [a,b,c] --> [b,x,y,z, a,c]

    this.searchResults = await this.#setSearchResults(results);
    const firstPage = this.searchResults.slice(0, 5);
    this.#renderSearchResults(firstPage);
  }

  #renderSearchResults(page) {
    if (page.length > 0) {
      // Render the search results
      searchBody.show();
      const self = this;
      let resultHTML = page.map((result) => self.#resultToHTML(result));
      resultHTML = resultHTML.join('');
      this.render_container.append(resultHTML);

    } else if (this.currentQuery.clean !== '') {
      // search with no results
      searchBody.show();
      this.render_container.html(`<div class="search-result">no results</div>`);
      loadMoreResults.hide();
    } else {
      // query for empty string
      // searchBody.hide();
      loadMoreResults.show();
    }
  }

  async #setSearchResults(results) {
    // Get documents corresponding to index positions
    const titlePositions = results.find(r => r?.field === 'title')?.result ?? [];
    const contentPositions = results.find(r => r?.field === 'content')?.result ?? [];

    /**
     * Dedup the search results retrieved by searching the content index. The new filtered array will contain only those
     * elements from contentPositions that are not present in titlePositions.
     *
     * We do this because (1) we don't want to render duplicate search results, and (2) we want to prioritize search
     * results retrieved from the title index because title matches are weighted higher than content matches
     */
    const filteredContentPositions = contentPositions.filter(pos => !titlePositions.includes(pos));

    // Resolve the FlexSearch results to the original elements stored in index.json
    const titleDocuments = await this.resolveSearchResults(titlePositions);
    const contentDocuments = await this.resolveSearchResults(filteredContentPositions);

    // Concatenate the two arrays, with title results appearing first in the concatenated array.
    return titleDocuments.concat(contentDocuments);
  }

  async loadMoreResults() {
    this.offset += 5;
    const nextPage = this.searchResults.slice(this.offset, this.offset + 5);
    console.debug('search index results: ', nextPage);
    this.#renderSearchResults(nextPage);
  }

  /**
   * Preps the query string before executing it.
   * @param {string} query
   * @private
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

  /**
   * parse the result to the HTML required to render it
   * @param result object of format {title, path, content} which describes a page on the site
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

}
