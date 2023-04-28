const Dexie = require("dexie").default;

class TableWrapper {
    constructor(indexeddb, tableName) {
        this.indexeddb = indexeddb;
        this.tableName = tableName;
    }

    /**
     * Performs a put operation on the IndexedDB.
     * @param {Object} data - The data to store in the IndexedDB.
     * @returns {Promise<void>}
     */
    async put(data) {
        await this.indexeddb[this.tableName].put(data);
    }

    /**
     * Performs bulk put operations on the IndexedDB in chunks to improve performance.
     * @param {Array<Object>} data - An array of objects to store in the IndexedDB.
     * @param {number} [chunkSize=100] - The number of objects to put in the IndexedDB at a time.
     * @returns {Promise<void>}
     */
    async bulkPut(data, chunkSize = 100) {

        return new Promise(async (resolve) => {
            /**
             * Schedules work using requestIdleCallback if supported, or setTimeout as a fallback.
             * @param {Function} callback - The function to be executed when the browser is idle or after the specified delay.
             */
            const scheduleWork = (callback) => {
                // As of April 2023, the `requestIdleCallback` function is still an experimental feature and lacks
                // support in Safari. In Safari, we use setTimeout as an alternative.
                if (typeof requestIdleCallback === 'function') {
                    requestIdleCallback(callback);
                } else {
                    // Use setTimeout with a small delay as a fallback
                    setTimeout(callback, 10);
                }
            };

            /**
             * Inserts a chunk of data into the IndexedDB table, and schedules the next chunk to be inserted.
             * @param {number} start - The index of the first item in the data array to be included in the current chunk.
             */
            const putChunk = async (start) => {
                // If all data has been processed, resolve the promise
                if (start >= data.length) {
                    resolve();
                    return;
                }

                // Determine the end index for the current chunk
                const end = Math.min(start + chunkSize, data.length);

                // Extract the chunk from the data array
                const chunk = data.slice(start, end);

                // Insert the chunk into the IndexedDB table
                await this.indexeddb[this.tableName].bulkPut(chunk);

                // Schedule the next chunk to be processed
                scheduleWork(() => putChunk(end));
            };

            // Start processing the data array by inserting the first chunk
            putChunk(0);
        });
    }

    /**
     * Retrieves data from the IndexedDB using the specified key.
     * @param {string} key - The key to retrieve data from the IndexedDB.
     * @returns {Promise<Object>}
     */
    async get(id) {
        return await this.indexeddb[this.tableName].get(id);
    }

    /**
     * Retrieves all records from the table.
     * @returns {Promise<Array<Object>>} An array of objects representing all records in the table.
     */
    async getAll() {
        return await this.indexeddb[this.tableName].toArray();
    }

    /**
     * Retrieves the total number of entries in the table.
     * @returns {Promise<number>} The total number of entries in the table.
     */
    async count() {
        return await this.indexeddb[this.tableName].count();
    }
}

class IndexedDBWrapper {
    constructor(dbName, schemas, version= 1) {
        this.dbName = dbName;
        this.version = version;

        // Initialize the IndexedDB

        // Check if the code is running in a Node.js environment
        const isNode = typeof process !== 'undefined' && process.release && process.release.name === 'node';

        // If running in a Node.js environment, import fake-indexeddb
        if (isNode) {
            const { indexedDB, IDBKeyRange } = require('fake-indexeddb');

            // Initialize the IndexedDB with fake-indexeddb for Node.js environment
            this.indexeddb = new Dexie(this.dbName, {
                indexedDB,
                IDBKeyRange,
            });
        } else {
            // If running in a browser environment, initialize the IndexedDB with the real IndexedDB provided by the browser
            this.indexeddb = new Dexie(this.dbName);
        }

        // Define the schema for the IndexedDB
        this.indexeddb.version(this.version).stores(schemas);
    }

    /**
     * Returns a TableWrapper instance for the specified table.
     * @param {string} tableName - The name of the table to create a TableWrapper for.
     * @returns {TableWrapper} An instance of TableWrapper for the specified table.
     */
    getTableWrapper(tableName) {
        return new TableWrapper(this.indexeddb, tableName);
    }
}

module.exports = {
    IndexedDBWrapper,
    TableWrapper
}
