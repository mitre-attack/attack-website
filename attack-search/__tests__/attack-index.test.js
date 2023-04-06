const AttackIndex = require('../src/attack-index');

// Mock the console.log function to prevent logs during testing
console.log = jest.fn();

describe('AttackIndex', () => {
    const cacheKey = 'test-cache-key';
    const tableName = 'test-table-name';
    const dbName = 'TestDatabase';

    let attackIndex;
    let data;

    beforeAll(() => {
        data = require('./mock-index.json');
    })

    beforeEach(() => {
        attackIndex = new AttackIndex(cacheKey, tableName, dbName);
    });

    afterEach(async () => {
        await attackIndex.indexeddb.delete();
    });

    it('should access data from mock-index.json', () => {
        expect(Array.isArray(data)).toBe(true);
        expect(data.length).toBe(10);
        expect(data[0].id).toBe(1);
        expect(data[0].title).toBe('Introduction to Machine Learning');
        expect(data[0].content).toContain('Machine learning is a subfield');
    });

    test('constructor initializes instance with correct properties', () => {
        // expect(attackIndex.cacheKey).toBe(cacheKey);
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
        attackIndex.addBulk(data);

        // Search the title index for "The"
        const results = await attackIndex.search('The', 'title');

        console.debug(JSON.stringify(results));
        // Index 2 through 6 (inclusive) should have "The" in the title
        const expectedResult = [{"field":"title","result":[2,3,4,5,6]}]

        expect(results).toEqual(expectedResult);
    });

    test('can export documents from FlexSearch to IndexedDB', async () => {
        attackIndex.addBulk(data);
        const exportResult = await attackIndex.exportFromFlexSearchToIndexedDB();

        // Verify that the IndexedDB received the exported data
        await attackIndex.indexeddb[attackIndex.tableName].toArray().then((items) => {
            console.debug('IndexedDB contents:', items);
        });

        expect(exportResult).toBeTruthy();
    });

    test('can import documents from IndexedDB to FlexSearch', async () => {
        attackIndex.addBulk(data);
        const exportResult = await attackIndex.exportFromFlexSearchToIndexedDB();

        // Create a new AttackIndex but hook it up to the same instance of IndexedDB that the first
        // attackIndex exported to.
        const newAttackIndex = new AttackIndex(cacheKey, tableName, dbName);

        // Now perform an import. The newAttackIndex should populate itself with content from the IndexedDB.
        await newAttackIndex.importFromIndexedDBtoFlexSearch();

        // If the import succeed, we should be able to search on newAttachIndex.
        const results = await newAttackIndex.search('data', 'content');

        console.debug('results:', JSON.stringify(results));
        const expectedResult = [{"field":"content","result":[1]}]

        expect(results).toEqual(expectedResult);
    });

    test('can isolate two instances of IndexedDB', async () => {
        attackIndex.addBulk(data);
        const exportResult = await attackIndex.exportFromFlexSearchToIndexedDB();

        // Create a new AttackIndex but hook it up to the same instance of IndexedDB that the first
        // attackIndex exported to.
        const newAttackIndex = new AttackIndex('test-cache-key-2', 'test-table-name-2', 'NewTestDatabase');

        // Now perform an import. The newAttackIndex should populate itself with content from the IndexedDB.
        await newAttackIndex.importFromIndexedDBtoFlexSearch();

        // If the import succeed, we should be able to search on newAttachIndex.
        const results = await newAttackIndex.search('data', ['content']);

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

    test('can paginate FlexSearch responses', async () => {
        attackIndex.addBulk(data);

        /**
         * limit, offset --> [ paginatedSearchResults ]
         *
         * 10, 0 --> [ 2, 3, 4, 5, 6, 7, 8, 9, 10 ]
         * 1, 0 --> [ 2 ]       1, 5 --> [ 7 ]
         * 1, 1 --> [ 3 ]       1, 6 --> [ 8 ]
         * 1, 2 --> [ 4 ]       1, 7 --> [ 9 ]
         * 1, 3 --> [ 5 ]       1, 8 --> [ 10 ]
         * 1, 4 --> [ 6 ]       1, 9 --> [ ]
         */

        let results;
        let expectedResult;

        // Get all documents - there should be 9 results with string 'The' in the title
        results = await attackIndex.search('The', ['title'], 10, 0);
        expectedResult = [{"field":"title","result":[2, 3, 4, 5, 6, 7, 8, 9, 10]}]
        expect(results).toEqual(expectedResult);

        // Get the first matching object by setting the limit parameter to 1
        results = await attackIndex.search('The', ['title'], 1);
        expectedResult = [{"field":"title","result":[2]}]
        expect(results).toEqual(expectedResult);

        // Get the second matching object by setting limit to 1 and offset to 1
        results = await attackIndex.search('The', ['title'], 1, 1);
        expectedResult = [{"field":"title","result":[3]}]
        expect(results).toEqual(expectedResult);

        // Get the last matching object by setting limit to 1 and offset to 8
        results = await attackIndex.search('The', ['title'], 1, 8);
        expectedResult = [{"field":"title","result":[10]}]
        expect(results).toEqual(expectedResult);

        // Request a page that does not exist - should return an empty array
        results = await attackIndex.search('The', ['title'], 1, 9);
        expectedResult = []
        expect(results).toEqual(expectedResult);
    });

    test('can exclusively search the title index', async () => {
        attackIndex.addBulk(data);
        await attackIndex.exportFromFlexSearchToIndexedDB();

        let results;
        let expectedResult;

        // Search title index: "The" -- expect 9 results
        results = await attackIndex.search('The', ['title'], 10, 0);
        expectedResult = [{"field":"title","result":[2, 3, 4, 5, 6, 7, 8, 9, 10]}]
        expect(results).toEqual(expectedResult);

        // Search content index: "of"
        results = await attackIndex.search('of', ['title','content'], 10, 0);
        console.debug('results: ', results);
        /**
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
        // Get documents corresponding to index positions
        const titlePositions = results.find(r => r.field === 'title').result;
        const contentPositions = results.find(r => r.field === 'content').result;

        const titleDocuments = await attackIndex.getDocumentsByPositions(titlePositions);
        const contentDocuments = await attackIndex.getDocumentsByPositions(contentPositions);

        console.debug('titleDocuments: ', titleDocuments);
        console.debug('contentDocuments: ', contentDocuments);
    });
})
