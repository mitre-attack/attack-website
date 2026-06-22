const SearchService = require("../src/search-service");
import 'fake-indexeddb/auto';

// The following line is necessary to mock the jQuery library and
// provide a default implementation for the '$' function in the test
// environment, since it is not defined by default. The mock
// implementation is necessary to allow the 'SearchService' class 
// to select the "#tag" and "#search-overlay" elements 
// without throwing errors during testing.
jest.mock('jquery');

// Mock the console functions to prevent logs during testing
console.log = jest.fn();
console.debug = jest.fn();

describe('SearchService', () => {
    let data;
    let searchService;

    beforeAll(() => {
        data = require('./mock-index.json');
    });

    beforeEach(() => {
        searchService = new SearchService('search-service', null);
    });

    afterEach(async () => {
        searchService = null;
    });

    it('Access data from mock-index.json', () => {
        expect(Array.isArray(data)).toBe(true);
        expect(data.length).toBe(10);
        expect(data[0].id).toBe(1);
        expect(data[0].title).toBe('Introduction to Machine Learning');
        expect(data[0].content).toContain('Machine learning is a subfield');
    });

    test('Initialize SearchService instance', () => {
        expect(searchService.db).toBeDefined();
        expect(searchService.contentDb).toBeDefined();
        expect(searchService.searchIndexDb).toBeDefined();
        expect(searchService.attackIndex).toBeDefined();
    });

    test('Add new documents to the search engine', async () => {
        await searchService.initializeAsync(data);
        expect(searchService.maxSearchResults).toEqual(data.length);
        
        const tableResults = await searchService.contentDb.getAll();
        expect(tableResults).toEqual(data);
    });

    test('Backup search index completes when FlexSearch exports fewer than nine persisted chunks', async () => {
        const exportedChunks = [
            ['title.1.map', 'title map data'],
            ['content.1.map', 'content map data'],
            ['content.1.ctx', 'content context data'],
            ['1.reg', 'register data'],
        ];

        searchService.attackIndex = {
            index: {
                export: jest.fn((handler) => {
                    exportedChunks.forEach(([key, value], index) => {
                        setTimeout(() => handler(key, value), index);
                    });
                }),
            },
        };
        searchService.searchIndexDb = {
            put: jest.fn(() => Promise.resolve()),
        };

        const result = await Promise.race([
            searchService.backupSearchIndex().then(() => 'completed'),
            new Promise((resolve) => setTimeout(() => resolve('timed out'), 250)),
        ]);

        expect(result).toBe('completed');
        expect(searchService.searchIndexDb.put).toHaveBeenCalledTimes(exportedChunks.length);
    });

    test('Resolve search results', async () => {
        await searchService.initializeAsync(data);
        
        const positions = [1, 2, 5];
        const results = await searchService.resolveSearchResults(positions);
        
        results.forEach((doc, index) => {
            expect(doc.id).toEqual(positions[index]);
        });

    });
});
