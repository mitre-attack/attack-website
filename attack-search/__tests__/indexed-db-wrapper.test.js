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

    // A failed write must settle the promise. Racing against a sentinel tells a
    // rejection apart from a promise that never settles at all, which a plain
    // rejects assertion cannot do: it would time out and look like a slow test.
    const settle = (promise) => Promise.race([
        promise.then(() => 'resolved', (error) => `rejected:${error.message}`),
        new Promise((resolve) => setTimeout(() => resolve('HUNG'), 1000)),
    ]);

    test('Bulk put rejects when the underlying write fails', async () => {
        jest.spyOn(contentDb.indexeddb[contentDb.tableName], 'bulkPut')
            .mockRejectedValue(new Error('QuotaExceededError'));

        await expect(settle(contentDb.bulkPut(data))).resolves.toBe('rejected:QuotaExceededError');
    });

    test('Bulk put rejects when a later chunk fails', async () => {
        let calls = 0;
        jest.spyOn(contentDb.indexeddb[contentDb.tableName], 'bulkPut')
            .mockImplementation(() => (++calls === 2
                ? Promise.reject(new Error('DatabaseClosedError'))
                : Promise.resolve()));

        await expect(settle(contentDb.bulkPut(data, 1))).resolves.toBe('rejected:DatabaseClosedError');
    });
});
