const { Index, Document } = require('flexsearch');
const localforage = require('localforage');

// eslint-disable-next-line import/extensions
const { pageLimit, TITLE_INDEX_KEY, CONTENT_INDEX_KEY } = require('./settings.js');
const { ATTACK_INDEX_KEY } = require('./settings');

// export default class IndexHelper {
module.exports = class IndexHelper {
  constructor(documents, exported) {
    console.debug('Initializing new IndexHelper instance...');

    this.index = new Document({
      id: 'id',
      index: [
        {
          field: 'title',
          tokenize: 'forward',
          optimize: true,
          resolution: 9,
        },
        {
          field: 'content',
          tokenize: 'strict',
          optimize: true,
          resolution: 9,
          minlength: 3,
          context: {
            depth: 4,
            resolution: 2,
          },
        },
      ],
    });

    // this.titleIndex = new Document({
    //   preset: 'performance',
    //   // encode: 'simple', // phonetic normalizations <-- TODO @seansica: v0.7.30: "Uncaught TypeError: this.encode is not a function"
    //   // tokenize: 'forward', // match substring beginning of word
    //   // threshold: 2, // exclude scores below this number <-- TODO @seansica: not specified in v0.7.30 documentation
    //   // resolution: 9, // how many steps in the scoring algorithm <-- TODO @seansica: 9 is the default
    //   // depth: 4, // how far around words to search for adjacent matches. Disabled for title
    //   // doc: {
    //   //   id: 'id',
    //   //   field: 'title',
    //   // },
    //   document: {
    //     id: 'id',
    //     index: 'title',
    //   },
    // });
    //
    // this.contentIndex = new Document({
    //   preset: 'performance',
    //   // encode: 'simple', // phonetic normalizations
    //   // tokenize: 'strict', // match substring beginning of word
    //   // threshold: 2, // exclude scores below this number
    //   // resolution: 9, // how many steps in the scoring algorithm
    //   depth: 4,
    //   doc: {
    //     id: 'id',
    //     field: 'content',
    //   },
    // });

    // console.debug('IndexHelper.constructor -> Initialized FlexSearch index.');
    console.debug(`IndexHelper.titleIndex: ${JSON.stringify(this.index)}`);

    // Adding pages to index
    if (documents && !exported) {
      console.debug('IndexHelper.constructor -> documents have not been exported yet. Commence export...');
      this.export(documents);
    } else if (!documents && exported) {
      console.debug('Commence importation of search indexes retrieved via localforage...');
      console.debug(`Loading index into memory: ${JSON.stringify(exported)}`);
      // console.debug(`Loading title index into memory: ${JSON.stringify(exported.title)}`);
      // console.debug(`Loading content index into memory: ${JSON.stringify(exported.content)}`);
      this.index.import(exported);
      // this.titleIndex.import(exported.title);
      // this.contentIndex.import(exported.content);
    } else {
      console.error('invalid argument: constructor must be called with either documents or exported');
    }

    this.setQuery('');
    console.debug('IndexHelper constructor is initialized.');
  }

  export(documents) {
    console.debug('Executing IndexHelper.export(documents)...');
    console.debug(`documents: ${JSON.stringify(documents)}`);

    this.index.add(documents);
    console.debug('IndexHelper.cacheDocuments -> added documents to index.');

    // this.titleIndex.add(documents);
    // console.debug('IndexHelper.cacheDocuments -> added documents to title index.');

    // this.contentIndex.add(documents);
    // console.debug('IndexHelper.cacheDocuments -> added documents to content index.');

    localStorage.setItem('saved_uuid', build_uuid);
    console.debug(`IndexHelper.cacheDocuments -> set { saved_uuid: ${build_uuid} } in localStorage.`);

    console.debug(`IndexHelper -> Commence export to cache: ${JSON.stringify(documents)}`);
    localforage.setItem(ATTACK_INDEX_KEY, this.index.export());
    // localforage.setItem(TITLE_INDEX_KEY, this.titleIndex.export());
    // localforage.setItem(CONTENT_INDEX_KEY, this.contentIndex.export());
  }

  setQuery(query) {
    this.query = query;
    this.nextPageRef = true;
    this.titleStage = true;
    this.seenPaths = new Set();
  }

  /**
   * This method is used to fetch the search results, filter out any duplicates, and return the results up to a
   * specified limit, while continuing to fetch more results until the limit has been reached or there are no more
   * results available.
   * @returns {T[]}
   */
  nextPage() {
    console.debug('IndexHelper.nextPage is executing...');
    let results = this.nextPageHelper();
    const self = this;
    results = results.filter((result) => !self.seenPaths.has(result.path));
    results.forEach((result) => {
      self.seenPaths.add(result.path);
    });

    // continue fetching new results from nextPageHelper until the pageLimit number of results has been reached or
    // there are no more results available.

    while (results.length < pageLimit) {

      // For each new result set obtained from nextPageHelper, filter out duplicates, add new results to the
      // seenPaths set, and append the new results to the existing results array.

      let newResults = this.nextPageHelper(pageLimit - results.length);
      if (newResults.length == 0) break; // ran out of results
      // cull duplicates
      newResults = newResults.filter((result) => !self.seenPaths.has(result.path));
      newResults.forEach((result) => {
        self.seenPaths.add(result.path);
      });
      // append to master list
      results = results.concat(newResults);
    }

    return results;
  }

  /**
     * Get the next page of results, or null if no more pages
     * @param {int} limit the number of results to get (default is the page_limit)
     */
  nextPageHelper(limit = pageLimit) {
    if (!this.nextPageRef) {
      console.warn('no next page');
      return [];
    }

    if (this.titleStage) {
      // console.log("fetching next title page")
      // const response = this.titleIndex.search(this.query, {
      //   limit,
      //   page: this.nextPageRef,
      // });
      const response = this.index.search(this.query, {
        limit,
        page: this.nextPageRef,
        field: 'title',
      });

      console.debug(`Received response from index query: ${JSON.stringify(response)}`);

      const results = response.result.map((result) => {
        result.source = 'title';
        return result;
      });
      if (response.next) { // next page exists on title stage
        this.nextPageRef = response.next;
        return results;
      } // end of title stage
      this.titleStage = false;
      this.nextPageRef = true;
      return results;
    } // content stage
    // console.log("fetching next content page")
    // const response = this.contentIndex.search(this.query, {
    //   limit,
    //   page: this.nextPageRef,
    // });
    const response = this.index.search(this.query, {
      limit,
      page: this.nextPageRef,
      field: 'content',
    });
    console.debug(`Received response from index query: ${JSON.stringify(response)}`);
    this.nextPageRef = response.next;
    return response.result.map((result) => {
      result.source = 'content';
      return result;
    });
  }
};
