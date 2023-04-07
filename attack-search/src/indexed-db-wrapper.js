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

    /**
     * Retrieves all records from the table.
     * @returns {Promise<Array<Object>>} An array of objects representing all records in the table.
     */
    async getAll() {
        return await this.indexeddb[this.tableName].toArray();
    }
}

class IndexedDBWrapper {
    constructor(dbName, schemas, version= 1) {
        this.dbName = dbName;
        // this.tableName = tableName;
        // this.cacheKey = cacheKey;
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
