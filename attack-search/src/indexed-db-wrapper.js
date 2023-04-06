const Dexie = require("dexie");

module.exports = class IndexedDBWrapper {
    constructor(dbName, tableName, cacheKey, schema) {
        this.dbName = dbName;
        this.tableName = tableName;
        this.cacheKey = cacheKey;

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
        this.indexeddb.version(1).stores({
            [this.tableName]: schema,
        });

        // this.indexeddb.version(1).stores({
        //     [this.tableName]: '++id, title, content',
        // });

        // this.indexeddb.version(1).stores({
        //     [this.tableName]: '&id',
        // });
    }

    /**
     * Performs a put operation on the IndexedDB.
     * @param {Object} data - The data to store in the IndexedDB.
     * @returns {Promise<void>}
     */
    async put(data) {
        await this.indexeddb[this.tableName].put(data, this.cacheKey);
    }

    /**
     * Performs bulk put operations on the IndexedDB.
     * @param {Array<Object>} data - An array of objects to store in the IndexedDB.
     * @returns {Promise<void>}
     */
    async bulkPut(data) {
        const putPromises = data.map((eachItem) => this.indexeddb[this.tableName].put(eachItem));
        await Promise.all(putPromises);
    }

    /**
     * Retrieves data from the IndexedDB using the specified key.
     * @param {string} key - The key to retrieve data from the IndexedDB.
     * @returns {Promise<Object>}
     */
    async get(id) {
        return await this.indexeddb[this.tableName].get(id);
    }

    async getAll() {
        return await this.indexeddb[this.tableName].toArray();
    }
}
