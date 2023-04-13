const { IndexedDBWrapper } = require("../src/indexed-db-wrapper");
import 'fake-indexeddb/auto';

// Mock the console.log function to prevent logs during testing
console.log = jest.fn();

describe('IndexedDBWrapper', () => {
    const dbName = 'testDb';
    let testDb;
    let contentDb;
    let flexsearchDb;
    let data;

    beforeAll(() => {
        data = require('./mock-index.json');
    });

    beforeEach(() => {
        // define schemas for the content_table (objects loaded from index.json)
        // and the search_index_table (FlexSearch instance)
        const schemas = {
            test_content_table: '&id, title, path, content',
            test_search_index_table: '++id, title, content'
        };

        testDb = new IndexedDBWrapper(dbName, schemas);
        contentDb = testDb.getTableWrapper('test_content_table');
        flexsearchDb = testDb.getTableWrapper('test_search_index_table');
    });

    afterEach(async () => {
        await testDb.indexeddb.delete();
    });

    test('Put one document in IndexedDB', async () => {
        const data = { id: 1, title: 'Test title', content: 'Test content' };
        await contentDb.put(data);
        const result = await contentDb.get(data.id);
        expect(result).toEqual(data);
    });

    test('Bulk put multiple documents in IndexedDB', async () => {
        await contentDb.bulkPut(data);
        const results = await contentDb.getAll();
        expect(results).toEqual(data);
    });

    test('Retrieve data from IndexedDB', async () => {
        const data = { id: 1, title: 'Test title', content: 'Test content' };
        await contentDb.put(data);
        const result = await contentDb.get(data.id);
        expect(result).toEqual(data);
    });

    test('Count documents in IndexedDB', async() => {
        await contentDb.bulkPut(data);
        const count = await contentDb.count();
        expect(count).toEqual(data.length);
    });
});
