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
        global.base_url = '/';
        searchService = new SearchService('search-service', null);
        searchService.render_container = {
            append: jest.fn(),
            html: jest.fn(),
        };
    });

    afterEach(async () => {
        searchService = null;
        delete global.base_url;
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

    test('Waits for FlexSearch indexing before backing up the search index', async () => {
        let resolveAddBulk;
        searchService.attackIndex.addBulk = jest.fn(() => new Promise((resolve) => {
            resolveAddBulk = resolve;
        }));
        searchService.backupSearchIndex = jest.fn(() => Promise.resolve());

        const initialization = searchService.initializeAsync(data);
        await Promise.resolve();

        expect(searchService.backupSearchIndex).not.toHaveBeenCalled();

        resolveAddBulk();
        await initialization;

        expect(searchService.backupSearchIndex).toHaveBeenCalled();
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

    test('Keeps only exact ATT&CK ID matches and references, with the object first', async () => {
        const documents = {
            1: {
                id: 1,
                title: 'TA577, Group G1037',
                path: '/groups/G1037/index.html',
                content: 'A group with no reference to the queried technique.',
                attackId: 'G1037',
            },
            2: {
                id: 2,
                title: 'Ingress Tool Transfer, Technique T1105 - Enterprise',
                path: '/techniques/T1105/index.html',
                content: 'The T1105 technique.',
                attackId: 'T1105',
            },
            3: {
                id: 3,
                title: 'A valid reference',
                path: '/resources/reference/index.html',
                content: 'This page references T1105.',
            },
        };
        searchService.attackIndex.search = jest.fn().mockResolvedValue([{ field: 'title', result: [1, 2, 3] }]);
        searchService.resolveSearchResults = jest.fn(async positions => positions.map(position => documents[position]));

        await searchService.query('t1105');

        expect(searchService.allSearchResults.map(result => result.id)).toEqual([2, 3]);
    });

    test('Treats a four-digit query as an exact ATT&CK ID suffix search', async () => {
        const documents = {
            1: {
                id: 1,
                title: 'TA577, Group G1037',
                path: '/groups/G1037/index.html',
                content: 'A group with no reference to the queried technique.',
                attackId: 'G1037',
            },
            2: {
                id: 2,
                title: 'Data from Local System, Technique T1005 - Enterprise',
                path: '/techniques/T1005/index.html',
                content: 'The T1005 technique.',
                attackId: 'T1005',
            },
            3: {
                id: 3,
                title: 'Matching software, Software S1005',
                path: '/software/S1005/index.html',
                content: 'The S1005 software.',
                attackId: 'S1005',
            },
            4: {
                id: 4,
                title: 'A valid reference',
                path: '/resources/reference/index.html',
                content: 'This page references T1005.',
            },
            5: {
                id: 5,
                title: 'Data from Local System: Archive Collected Data, Sub-technique T1005.001',
                path: '/techniques/T1005/001/index.html',
                content: 'The T1005.001 sub-technique.',
                attackId: 'T1005.001',
            },
        };
        searchService.attackIndex.search = jest.fn().mockResolvedValue([{ field: 'title', result: [1, 3, 4, 2, 5] }]);
        searchService.resolveSearchResults = jest.fn(async positions => positions.map(position => documents[position]));

        await searchService.query('1005');

        expect(searchService.allSearchResults.map(result => result.id)).toEqual([2, 5, 3, 4]);
    });

    test('Preserves result ordering for non-ID queries', async () => {
        const documents = {
            1: { id: 1, title: 'First result', path: '/resources/faq/index.html', content: 'Resources' },
            2: { id: 2, title: 'Second result', path: '/resources/attackcon/index.html', content: 'Resources' },
        };
        searchService.attackIndex.search = jest.fn().mockResolvedValue([{ field: 'title', result: [1, 2] }]);
        searchService.resolveSearchResults = jest.fn(async positions => positions.map(position => documents[position]));

        await searchService.query('Resources');

        expect(searchService.allSearchResults.map(result => result.id)).toEqual([1, 2]);
    });
});
