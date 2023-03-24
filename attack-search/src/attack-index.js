const Dexie = require('dexie');
const FlexSearch = require('flexsearch');
const { indexedDB, IDBKeyRange } = require('fake-indexeddb');

const { Document } = FlexSearch;

module.exports = class AttackIndex {
    /**
     * Creates a new AttackIndex instance.
     * @param {string} cacheKey - The key used to access the IndexedDB.
     * @param {string} tableName - The name of the IndexedDB table.
     * @param {string} [dbName='AttackDatabase'] - The name of the IndexedDB.
     */
    constructor(cacheKey, tableName, dbName = 'AttackDatabase') {
        this.cacheKey = cacheKey;
        this.tableName = tableName;

        this.indexeddb = new Dexie(dbName, {
            indexedDB,
            IDBKeyRange,
        });

        this.indexeddb.version(1).stores({
            [this.tableName]: '++id, title, content',
        });

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
                    minlength: 3,
                    context: {
                        depth: 3,
                        resolution: 2,
                    },
                },
            ],
            page: 0, // Default starting page,
            limit: Number.MAX_SAFE_INTEGER // Default limit for results per page
        });
    }

    /**
     * Performs a put operation on the IndexedDB.
     * @param {Object} data - The data to store in the IndexedDB.
     * @returns {Promise<void>}
     */
    async putInIndexedDB(data) {
        await this.indexeddb[this.tableName].put(data, this.cacheKey);
    }

    /**
     * Performs bulk put operations on the IndexedDB.
     * @param {Array<Object>} data - An array of objects to store in the IndexedDB.
     * @returns {Promise<void>}
     */
    async bulkPutInIndexedDB(data) {
        const putPromises = data.map((eachItem) => this.indexeddb[this.tableName].put(eachItem));
        await Promise.all(putPromises);
    }

    /**
     * Retrieves data from the IndexedDB using the specified key.
     * @param {string} key - The key to retrieve data from the IndexedDB.
     * @returns {Promise<Object>}
     */
    async getFromIndexedDB(id) {
        const result = await this.indexeddb[this.tableName].get(id);
        return result;
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
        data.map(async (item) => await this.index.addAsync(item));
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
