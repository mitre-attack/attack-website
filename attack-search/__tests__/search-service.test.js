const SearchService = require("../src/search-service");

// Mock the console.log function to prevent logs during testing
console.log = jest.fn();

describe('SearchService', () => {

    let searchService;
    let documents;

    beforeAll(() => {
        documents = require('./mock-index.json');
    });

    beforeEach(() => {
       searchService = new SearchService('search-service', null);
    });

    test('can export documents from FlexSearch to IndexedDB', async () => {
        searchService
        // attackIndex.addBulk(data);
        // const exportResult = await attackIndex.exportFromFlexSearchToIndexedDB();
        //
        // // Verify that the IndexedDB received the exported data
        // await attackIndex.indexeddb[attackIndex.tableName].toArray().then((items) => {
        //     console.debug('IndexedDB contents:', items);
        // });
        //
        // expect(exportResult).toBeTruthy();
    });

    test('can import documents from IndexedDB to FlexSearch', async () => {
        // attackIndex.addBulk(data);
        // const exportResult = await attackIndex.exportFromFlexSearchToIndexedDB();
        //
        // // Create a new AttackIndex but hook it up to the same instance of IndexedDB that the first
        // // attackIndex exported to.
        // const newAttackIndex = new AttackIndex(cacheKey, contentTableName, dbName);
        //
        // // Now perform an import. The newAttackIndex should populate itself with content from the IndexedDB.
        // await newAttackIndex.importFromIndexedDBtoFlexSearch();
        //
        // // If the import succeed, we should be able to search on newAttachIndex.
        // const results = await newAttackIndex.search('data', 'content');
        //
        // console.debug('results:', JSON.stringify(results));
        // const expectedResult = [{"field":"content","result":[1]}]
        //
        // expect(results).toEqual(expectedResult);
    });
});
