const FlexSearch = require('flexsearch');
const { Document } = FlexSearch;

module.exports = class AttackIndex {
    /**
     * Creates a new AttackIndex instance.
     */
    constructor() {
        // Initialize the FlexSearch instance with two indexes: 'title' and 'content'
        this.index = new Document({
            id: 'id',
            index: [
                {
                    field: 'title',
                    tokenize: 'forward',
                    optimize: true,
                    resolution: 9,
                },
                {
                    field: 'content',
                    tokenize: 'strict',
                    optimize: true,
                    resolution: 9,
                    minlength: 3,
                    context: {
                        depth: 3,
                        resolution: 2,
                    },
                },
            ],
            page: 0, // Default starting page,
            limit: Number.MAX_SAFE_INTEGER, // Default limit for results per page
            // worker: true <--- Cannot call import when this is passed:
            //                   TypeError: this.index[c].import is not a function
        });
    }


    /**
     * Searches the FlexSearch instance.
     * @param {string} query - The search query.
     * @param {Array<string>} fields - The index fields to search: ['title'], ['content'], or ['title', 'content'].
     * @param {number} [limit=5] - The maximum number of results to return.
     * @param {number} [offset=0] - The offset to start the search results from.
     * @returns {Promise<Array<Object>>} - An array of search results.
     */
    async search(query, fields, limit = 5, offset = 0) {

        // Validate input fields
        const allowedFields = [
            ['title'],
            ['content'],
            ['title', 'content']
        ];

        if (!allowedFields.some(allowed => fields.join(',') === allowed.join(','))) {
            throw new Error(`Invalid fields specified. Allowed values are: ${allowedFields.join(', ')}`);
        }

        const searchOptions = {
            index: fields,
            bool: 'or', // the bool option specifies that the search should match documents that container either the
                        // title or the content field
            limit,
            offset,
        };

        console.debug('query: ', query);
        console.debug('searchOptions: ', searchOptions);

        const results = await this.index.searchAsync(query, searchOptions);

        console.debug('results: ', results);

        /**
         * Here is a typical FlexSearch response -- it only provides the index positions of the matching documents, not
         * the documents themselves!
         *
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

        return results;
    }

    /**
     * Adds a single data object to the FlexSearch index.
     *
     * @param {Object} data - The data object to be added to the FlexSearch index.
     * @returns {Promise<void>} - A Promise that resolves when the data object is added to the FlexSearch index.
     */
    async add(data) {
        await this.index.addAsync(data);
    }

    /**
     * Adds an array of data objects to the FlexSearch index in bulk.
     *
     * @param {Object[]} data - An array of data objects to be added to the FlexSearch index.
     * @returns {Promise<void>[]} - A promise that resolves when all data objects have been added to the FlexSearch index.
     */
    async addBulk(data) {
        const promises = data.map(async (item) => await this.index.addAsync(item));
        await Promise.all(promises);
    }

    async import(key, data) {
        return await this.index.import(key, data);
    }
}
