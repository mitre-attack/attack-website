const AttackIndex = require('../src/attack-index');
const { IndexedDBWrapper } = require("../src/indexed-db-wrapper");
import 'fake-indexeddb/auto';

// Mock the console.log function to prevent logs during testing
console.log = jest.fn();

describe('AttackIndex', () => {
    const dbName = 'TestDatabase';

    let attackIndex;
    let testDb;
    let contentDb;
    let data;

    beforeAll(async () => {
        data = require('./mock-index.json');

        // define schemas for the content_table (objects loaded from index.json)
        // and the search_index_table (FlexSearch instance)
        const schemas = {
            test_content_table: '&id, title, path, content',
            test_search_index_table: '++id, title, content'
        };

        testDb = new IndexedDBWrapper(dbName, schemas);
        contentDb = testDb.getTableWrapper('test_content_table');
        await contentDb.bulkPut(data);
    })

    beforeEach(() => {
        attackIndex = new AttackIndex();
    });

    afterEach(async () => {
        attackIndex = null;
    });

    afterAll(async () => {
        await testDb.indexeddb.delete();
    });

    it('Access data from mock-index.json', () => {
        expect(Array.isArray(data)).toBe(true);
        expect(data.length).toBe(10);
        expect(data[0].id).toBe(1);
        expect(data[0].title).toBe('Introduction to Machine Learning');
        expect(data[0].content).toContain('Machine learning is a subfield');
    });

    test('Initialize AttackIndex instance', () => {
        expect(attackIndex.index).toBeDefined();
    });

    test('Add one document to FlexSearch', async () => {
        const data = { id: 1, title: 'Test title', content: 'Test content' };

        await attackIndex.add(data);

        const results = await attackIndex.search('Test', ['title'], 5, 0);

        const expectedResult = [{"field":"title","result":[1]}]

        expect(results).toEqual(expectedResult);
    });

    test('Bulk add documents to FlexSearch', async () => {
        attackIndex.addBulk(data);

        // Search the title index for "The"
        const results = await attackIndex.search('The', ['title']);

        // Index 2 through 6 (inclusive) should have "The" in the title
        const expectedResult = [{"field":"title","result":[2,3,4,5,6]}]

        expect(results).toEqual(expectedResult);
    });

    test('Paginate FlexSearch responses', async () => {
        attackIndex.addBulk(data);

        /**
         * limit, offset --> [ paginatedSearchResults ]
         *
         * 10, 1 --> [ 2, 3, 4, 5, 6, 7, 8, 9, 10 ]
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

    test('Resolve search results', async () => {
        // Index the data
        attackIndex.addBulk(data);

        const results = await attackIndex.search('of', ['title','content'], 10, 0);

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

        async function resolveSearchResults(positions) {
            const results = [];
            for (const position of positions) {
                const doc = await contentDb.get(position);
                if (doc) {
                    results.push(doc);
                }
            }
            return results;
        }

        const titleDocuments = await resolveSearchResults(titlePositions);
        const contentDocuments = await resolveSearchResults(contentPositions);

        titleDocuments.forEach((doc, index) => {
            expect(doc.id).toEqual(titlePositions[index]);
        });

        contentDocuments.forEach((doc, index) => {
            expect(doc.id).toEqual(contentPositions[index]);
        });

    });
})
