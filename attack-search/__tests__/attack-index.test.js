const AttackIndex = require('../src/attack-index');

// Mock the console.log function to prevent logs during testing
console.log = jest.fn();

describe('AttackIndex', () => {
    const cacheKey = 'test-cache-key';
    const tableName = 'test-table-name';
    const dbName = 'TestDatabase';

    let attackIndex;

    beforeEach(() => {
        attackIndex = new AttackIndex(cacheKey, tableName, dbName);
    });

    afterEach(async () => {
        await attackIndex.indexeddb.delete();
    });

    test('constructor initializes instance with correct properties', () => {
        expect(attackIndex.cacheKey).toBe(cacheKey);
        expect(attackIndex.tableName).toBe(tableName);
        expect(attackIndex.indexeddb.name).toBe(dbName);
    });

    test('putInIndexedDB stores data in IndexedDB', async () => {
        const data = { id: 1, title: 'Test title', content: 'Test content' };

        await attackIndex.putInIndexedDB(data);
        const result = await attackIndex.getFromIndexedDB(data.id);

        expect(result).toEqual(data);
    });

    test('can bulk put multiple documents in IndexedDB', async () => {
        const data = [
            { id: 1, title: 'Test title 1', content: 'Test content 1' },
            { id: 2, title: 'Test title 2', content: 'Test content 2' },
        ];

        await attackIndex.bulkPutInIndexedDB(data);
        const results = await Promise.all(data.map((item) => attackIndex.getFromIndexedDB(item.id)));

        expect(results).toEqual(data);
    });

    test('can retrieve data from IndexedDB', async () => {
        const data = { id: 1, title: 'Test title', content: 'Test content' };

        await attackIndex.putInIndexedDB(data);
        const result = await attackIndex.getFromIndexedDB(data.id);

        expect(result).toEqual(data);
    });

    test('can add one document to FlexSearch', async () => {
        const data = { id: 1, title: 'Test title', content: 'Test content' };

        await attackIndex.add(data);

        const results = await attackIndex.search('Test', 'title', 5, 0);

        console.debug(JSON.stringify(results));
        const expectedResult = [{"field":"title","result":[1]}]

        expect(results).toEqual(expectedResult);
    });

    test('can bulk add documents to FlexSearch', async () => {
        const data = [
            { id: 1, title: 'Test title 1', content: 'Test content 1' },
            { id: 2, title: 'Test title 2', content: 'Test content 2' },
            { id: 3, title: 'Test title 3', content: 'Test content 3' },
            { id: 4, title: 'Test title 4', content: 'Test content 4' },
        ];

        await attackIndex.addBulk(data);

        const results = await attackIndex.search('Test', 'title');

        console.debug(JSON.stringify(results));
        const expectedResult = [{"field":"title","result":[1,2,3,4]}]

        // write expect statement here
        expect(results).toEqual(expectedResult);
    });

    test('can search for matching documents', async () => {
        const data = [
            { id: 1, title: 'Dog', content: 'The dog said woof.' },
            { id: 2, title: 'Cat', content: 'The cat said meow.' },
            { id: 2, title: 'Cow', content: 'The cow said moo.' },
        ];

        await attackIndex.addBulk(data);

        const results = await attackIndex.search('Dog', 'title');

        console.debug('results:', JSON.stringify(results));
        const expectedResult = [{"field":"title","result":[1]}]

        expect(results).toEqual(expectedResult);
    });

    test('can export documents from FlexSearch to IndexedDB', async () => {
        const data = [
            { id: 1, title: 'Dog', content: 'The dog said woof.' },
            { id: 2, title: 'Cat', content: 'The cat said meow.' },
            { id: 2, title: 'Cow', content: 'The cow said moo.' },
        ];

        await attackIndex.addBulk(data);
        const exportResult = await attackIndex.exportFromFlexSearchToIndexedDB();

        // Verify that the IndexedDB received the exported data
        await attackIndex.indexeddb[attackIndex.tableName].toArray().then((items) => {
            console.debug('IndexedDB contents:', items);
        });

        expect(exportResult).toBeTruthy();
    });

    test('can import documents from IndexedDB to FlexSearch', async () => {
        const data = [
            { id: 1, title: 'Dog', content: 'The dog said woof.' },
            { id: 2, title: 'Cat', content: 'The cat said meow.' },
            { id: 2, title: 'Cow', content: 'The cow said moo.' },
        ];

        await attackIndex.addBulk(data);
        const exportResult = await attackIndex.exportFromFlexSearchToIndexedDB();

        // Create a new AttackIndex but hook it up to the same instance of IndexedDB that the first
        // attackIndex exported to.
        const newAttackIndex = new AttackIndex(cacheKey, tableName, dbName);

        // Now perform an import. The newAttackIndex should populate itself with content from the IndexedDB.
        await newAttackIndex.importFromIndexedDBtoFlexSearch();

        // If the import succeed, we should be able to search on newAttachIndex.
        const results = await newAttackIndex.search('Dog', 'title');

        console.debug('results:', JSON.stringify(results));
        const expectedResult = [{"field":"title","result":[1]}]

        expect(results).toEqual(expectedResult);
    });

    test('can isolate two instances of IndexedDB', async () => {
        const data = [
            { id: 1, title: 'Dog', content: 'The dog said woof.' },
            { id: 2, title: 'Cat', content: 'The cat said meow.' },
            { id: 2, title: 'Cow', content: 'The cow said moo.' },
        ];

        await attackIndex.addBulk(data);
        const exportResult = await attackIndex.exportFromFlexSearchToIndexedDB();

        // Create a new AttackIndex but hook it up to the same instance of IndexedDB that the first
        // attackIndex exported to.
        const newAttackIndex = new AttackIndex('test-cache-key-2', 'test-table-name-2', 'NewTestDatabase');

        // Now perform an import. The newAttackIndex should populate itself with content from the IndexedDB.
        await newAttackIndex.importFromIndexedDBtoFlexSearch();

        // If the import succeed, we should be able to search on newAttachIndex.
        const results = await newAttackIndex.search('Dog', 'title');

        console.debug('results:', JSON.stringify(results));

        /**
         * We expect an empty response back because we wired up a new IndexedDB instance.
         *
         * Explanation:
         *
         * `attackIndex` exports its documents to an IndexedDB instance with a dbName of 'TestDatabase'. TestDatabase
         * contains importable data. But we don't import it. We spin up a *new* instance of AttackIndex (called
         * `newAttackIndex`) and wire it up to an IndexedDB instance with a dbName of 'NewTestDatabase'. We want to
         * demonstrate that the two IndexedDB instances (TestDatabase and NewTestDatabase) are not interconnected. We
         * can validate this by trying performing an import on `newAttackIndex`. Because we wired it up to an allegedly
         * empty IndexedDB instance, it should import nothing. We can validate this by performing a search on
         * `newAttackIndex` and validating that no results are returned.
         */
        expect(results).toEqual([]);
    });
})
