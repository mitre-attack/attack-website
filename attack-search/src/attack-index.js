// const Dexie = require('dexie');
const FlexSearch = require('flexsearch');
// const {pageLimit} = require("./settings");
// const {indexedDB, IDBKeyRange} = require("fake-indexeddb");
// const IndexedDBWrapper = require("./indexed-db-wrapper");
const { Document } = FlexSearch;

module.exports = class AttackIndex {
    /**
     * Creates a new AttackIndex instance.
     */
    constructor() {
        // Initialize the FlexSearch instance with two indexes: 'title' and 'content'
        this.index = new Document({
            id: 'id',
            index: [
                {
                    field: 'title',
                    tokenize: 'forward',
                    optimize: true,
                },
                {
                    field: 'content',
                    tokenize: 'forward',
                    optimize: true,
                    // minlength: 3,   <--- THESE TWO PROPS ARE COMMENTED OUT BECAUSE THEY APPEAR TO BREAK
                    // context: {      <---  SEARCHING ON THE CONTENT INDEX!
                    //     depth: 3,
                    //     resolution: 2,
                    // },
                },
            ],
            page: 0, // Default starting page,
            limit: Number.MAX_SAFE_INTEGER // Default limit for results per page
        });
    }


    /**
     * Searches the FlexSearch instance.
     * @param {string} query - The search query.
     * @param {Array<string>} fields - The index fields to search: ['title'], ['content'], or ['title', 'content'].
     * @param {number} [limit=5] - The maximum number of results to return.
     * @param {number} [offset=0] - The offset to start the search results from.
     * @returns {Promise<Array<Object>>} - An array of search results.
     */
    async search(query, fields, limit = 5, offset = 0) {

        // Validate input fields
        const allowedFields = [
            ['title'],
            ['content'],
            ['title', 'content']
        ];

        if (!allowedFields.some(allowed => fields.join(',') === allowed.join(','))) {
            throw new Error(`Invalid fields specified. Allowed values are: ${allowedFields.join(', ')}`);
        }

        const searchOptions = {
            index: fields,
            bool: 'or', // the bool option specifies that the search should match documents that container either the
                        // title or the content field
            limit,
            offset,
        };
        const results = await this.index.searchAsync(query, searchOptions);

        /**
         * Here is a typical FlexSearch response -- it only provides the index positions of the matching documents, not
         * the documents themselves!
         *
         * results:  [
         *       {
         *         field: 'title',
         *         result: [
         *           2, 3, 4,  5, 6,
         *           7, 8, 9, 10
         *         ]
         *       },
         *       {
         *         field: 'content',
         *         result: [
         *           1, 5, 6, 7,
         *           2, 3, 8, 9
         *         ]
         *       }
         *     ]
         */

        // If both indexes (title and content) were searched, then we need to combine their results and remove any
        // duplicate IDs.
        const uniqueIds = new Set([...results[0].result, ...results[1].result]);

        // TODO make this 👆 conditional - only execute when both indexes are searched, then return the result
    }

    /**
     * Adds a single data object to the FlexSearch index.
     *
     * @param {Object} data - The data object to be added to the FlexSearch index.
     * @returns {Promise<void>} - A Promise that resolves when the data object is added to the FlexSearch index.
     */
    async add(data) {
        await this.index.addAsync(data);
    }

    /**
     * Adds an array of data objects to the FlexSearch index in bulk.
     *
     * @param {Object[]} data - An array of data objects to be added to the FlexSearch index.
     * @returns {Promise<void>[]} - A promise that resolves when all data objects have been added to the FlexSearch index.
     */
    async addBulk(data) {
        // data.map(async (item) => await this.index.addAsync(item));

        const promises = data.map(async (item) => await this.index.addAsync(item));
        await Promise.all(promises);
    }

    /**
     * Exports data from the FlexSearch instance to the IndexedDB.
     * @returns {Promise<Array<string>>}
     */
    async exportFromFlexSearchToIndexedDB() {
        return new Promise(async (resolve) => {
            const keys = [];
            let processedKeys = 0;

    /*** LEGACY INDEX-HELPER.JS CODE BELOW ***/


    // setQuery(query) {
    //     this.queryString = query;
    //     this.nextPageRef = true;
    //     this.titleStage = true;
    //     this.seenPaths = new Set();
    // }

    /**
     * This method is used to fetch the search results, filter out any duplicates, and return the results up to a
     * specified limit, while continuing to fetch more results until the limit has been reached or there are no more
     * results available.
     * @returns {T[]}
     */
    // nextPage() {
    //     console.debug('IndexHelper.nextPage is executing...');
    //     let results = this.nextPageHelper();
    //     const self = this;
    //     results = results.filter((result) => !self.seenPaths.has(result.path));
    //     results.forEach((result) => {
    //         self.seenPaths.add(result.path);
    //     });
    //
    //     // continue fetching new results from nextPageHelper until the pageLimit number of results has been reached or
    //     // there are no more results available.
    //
    //     while (results.length < pageLimit) {
    //
    //         // For each new result set obtained from nextPageHelper, filter out duplicates, add new results to the
    //         // seenPaths set, and append the new results to the existing results array.
    //
    //         let newResults = this.nextPageHelper(pageLimit - results.length);
    //         if (newResults.length == 0) break; // ran out of results
    //         // cull duplicates
    //         newResults = newResults.filter((result) => !self.seenPaths.has(result.path));
    //         newResults.forEach((result) => {
    //             self.seenPaths.add(result.path);
    //         });
    //         // append to master list
    //         results = results.concat(newResults);
    //     }
    //
    //     return results;
    // }

    /**
     * Get the next page of results, or null if no more pages
     * @param {int} limit the number of results to get (default is the page_limit)
     */
    // nextPageHelper(limit = pageLimit) {
    //     if (!this.nextPageRef) {
    //         console.warn('no next page');
    //         return [];
    //     }
    //
    //     if (this.titleStage) {
    //         const response = this.search(this.query, 'title', limit)
    //
    //         const results = response.result.map((result) => {
    //             result.source = 'title';
    //             return result;
    //         });
    //         if (response.next) { // next page exists on title stage
    //             this.nextPageRef = response.next;
    //             return results;
    //         } // end of title stage
    //         this.titleStage = false;
    //         this.nextPageRef = true;
    //         return results;
    //     } // content stage
    //     const response = this.search(this.query, 'content', limit);
    //     this.nextPageRef = response.next;
    //     return response.result.map((result) => {
    //         result.source = 'content';
    //         return result;
    //     });
    // }
}
