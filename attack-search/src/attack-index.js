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
     * @param {string} field - The index field to search: 'title' or 'content'.
     * @param {number} [limit=5] - The maximum number of results to return.
     * @param {number} [offset=0] - The offset to start the search results from.
     * @returns {Promise<Array<Object>>} - An array of search results.
     */
    async search(query, field, limit = 5, offset = 0) {
        const searchOptions = {
            field,
            limit,
            offset,
        };
        return await this.index.searchAsync(query, searchOptions);
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
     * @returns {Promise<void>[]} - An array of Promises that resolve when each data object is added to the FlexSearch index.
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

            // totalKeys(x) = (3 * #searchFields) + 3
            // x = len['title', 'content']
            const totalKeys = 9;

            this.index.export(async (key, data) => {
                this.indexeddb[this.tableName].put({ key, data }).then((key) => {
                    keys.push(key);
                    processedKeys++;

                    if (processedKeys === totalKeys) {
                        resolve(true); // TODO validate this -- changed from `resolve(keys)`
                    }
                });
            });
        });
    }

    /**
     * Imports data from the IndexedDB to the FlexSearch instance.
     * @returns {Promise<void>}
     */
    async importFromIndexedDBtoFlexSearch() {
        console.log(`Executing importBooksFromIndexedDBtoFlexSearch...`);
        // Retrieve all records from the specified object store
        const records = await this.indexeddb[this.tableName].toArray();

        // Import the records into the FlexSearch instance
        for (const record of records) {
            await this.index.import(record.key, record.data);
        }
    }

}
