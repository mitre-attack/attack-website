const IndexedDBWrapper = require("../src/indexed-db-wrapper");
import 'fake-indexeddb/auto';

// Mock the console.log function to prevent logs during testing
console.log = jest.fn();

describe('IndexedDBWrapper', () => {

    const cacheKey = 'test-cache-key';
    const contentTableName = 'test_content_table_name';
    const searchIndexTableName = 'test_search_index_table_name';
    const dbName = 'TestDatabase';

    let dbVersion = 1;
    let contentDb;
    let flexsearchDb;
    let data;

    beforeAll(() => {
        data = require('./mock-index.json');
    });

    beforeEach(() => {
        contentDb = new IndexedDBWrapper(dbName, contentTableName, cacheKey, '&id, title, path, content', dbVersion);
        flexsearchDb = new IndexedDBWrapper(dbName, searchIndexTableName, cacheKey, '++id, title, content', dbVersion);
    });

    afterEach(async () => {
        // contentDb.clearTable();
        // flexsearchDb.clearTable();

        // contentDb.deleteObjectStore();
        // flexsearchDb.deleteObjectStore();

        // delete contentDb;
        // delete flexsearchDb;

        // Close the database connections
        // contentDb.indexeddb.close();
        // flexsearchDb.indexeddb.close();

        // Delete the databases
        // await indexedDB.deleteDatabase(contentDb.dbName);
        // await indexedDB.deleteDatabase(flexsearchDb.dbName);

        await contentDb.indexeddb.delete();
        await flexsearchDb.indexeddb.delete();

        // clearTable throws error: Exceeded timeout of 5000 ms for a hook.
        // await contentDb.clearTable();
        // await flexsearchDb.clearTable();

        // contentDb = null;
        // flexsearchDb = null;
    });

    test('can put one document in IndexedDB', async () => {
        const data = { id: 1, title: 'Test title', content: 'Test content' };
        await contentDb.put(data);
        const result = await contentDb.get(data.id);
        expect(result).toEqual(data);
    });

    test('can bulk put multiple documents in IndexedDB', async () => {
        await contentDb.bulkPut(data);
        const results = await contentDb.getAll();
        expect(results).toEqual(data);
    });

    test('can retrieve data from IndexedDB', async () => {
        const data = { id: 1, title: 'Test title', content: 'Test content' };
        await contentDb.put(data);
        const result = await contentDb.get(data.id);
        expect(result).toEqual(data);
    });
});
