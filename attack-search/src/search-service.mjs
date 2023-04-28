/** service worker - runs on separate thread **/

import AttackIndex from './attack-index.cjs';
import databaseManager from "./db/database-manager.mjs";

export class SearchService {

  /**
   * The SearchService class is responsible for managing the search functionality of the application. It allows for
   * initialization of the search index, processing search queries, and rendering search results.
   *
   * @class SearchService
   * @constructor
   */
  constructor() {

    // Sets the maximum number of search results displayed on a single page.
    // Clicking "Load more results" will add ${pageLimit} additional results to the current page.
    this.pageLimit = 5;

    this.contentDb = databaseManager.contentDb;
    this.searchIndexDb = databaseManager.searchIndexDb;

    // Initialize the AttackIndex instance (this is our in-memory FlexSearch instance)
    this.attackIndex = new AttackIndex();

    this.searchResults = [];
  }

  /**
   * Asynchronously initializes the search engine by either indexing the provided documents or restoring the search
   * index from a backup stored in IndexedDB. If documents are provided, the method will add them to the search index,
   * create a backup of the search index, and store the documents in IndexedDB.
   *
   * @async
   * @function
   * @param {Array<Object>} [documents] - An optional array of document objects to be indexed. Each document object
   * should have an `id`, a `title`, a `path`, and a `content` property.
   */
  async initializeAsync(documents) {

    // If documents are defined, then load them into the AttackIndex instance.
    if (documents) {
      console.debug('Indexing documents: ', documents);

      this.maxSearchResults = documents.length;

      // Add the data to the in-memory FlexSearch instance
      this.attackIndex.addBulk(documents);

      console.debug('Backing up search index...');

      // Backup the in-memory FlexSearch index for later restoration
      await this.backupSearchIndex();
      await this.contentDb.bulkPut(documents, 100);

      console.debug('Backup of search index completed.');
    } else {
      console.debug('Restoring search index from backup...');

      this.maxSearchResults = await this.contentDb.count();

      // If no documents were provided, then attempt to load them from the IndexedDB database
      await this.restoreSearchIndexFromBackup();
    }
  }

  /**
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
    // Create an array of promises to get documents from the IndexedDB content_table
    const getPromises = positions.map(position => this.contentDb.get(position));

    // Wait for all promises to resolve
    const docs = await Promise.all(getPromises);

    // Filter out null or undefined documents
    return docs.filter(doc => doc !== null && doc !== undefined);
  }

  /**
   * Asynchronously performs a search query on the search index and renders the search results on the web page.
   * The search will be performed on both the title and content fields of the indexed documents.
   * The search results are paginated, showing the first page of results after the search.
   *
   * @async
   * @function
   * @param {string} query - The raw search query string.
   */
  async query(query) {
    this.offset = 0;
    const results = await this.attackIndex.search(query, ["title", "content"], this.maxSearchResults);
    console.debug('search index results: ', results);
    return await this.#processSearchResults(results);
  }

  /**
   * Asynchronously sets the search results by merging title and content results without duplication, prioritizing
   * title matches over content matches.
   *
   * @async
   * @private
   * @function
   * @param {Array<{ field: string, result: Array<number> }>} results - An array containing search results, each object
   * in the array should have a `field` property ("title" or "content") and a `result` property (an array of indices).
   *
   * @returns {Promise<Array>} A Promise that resolves to an array containing the search results with duplicates removed
   * and title matches prioritized over content matches.
   *
   * @example
   * results: [
   *   {
   *     field: 'title',
   *     result: [2, 3, 4, 5, 6, ..., 100]
   *   },
   *   {
   *     field: 'content',
   *     result: [1, 5, 6, 7, 2, 3, 8, 9]
   *   }
   * ]
   */
  async #processSearchResults(results) {
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

}
