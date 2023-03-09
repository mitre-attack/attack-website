const FlexSearch = require('flexsearch');
const localforage = require('localforage');

const { Document } = FlexSearch;

module.exports = class AttackIndex {
  constructor(cacheKey) {
    this.cacheKey = cacheKey;
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
            depth: 4,
            resolution: 2,
          },
        },
      ],
    });
  }

  /**
   * Adds new search content to a search index.
   * @param {flexsearch.Document} document The search index to which data should be added.
   * @param {object[]|object} data An array of objects or a single object.
   * If an array, each object must have the following properties:
   * - id: number
   * - title: string
   * - content: string
   * If a single object, it must have the same properties as described above.
   * @returns {Promise<void>}
  */
  async addOne(data) {
    await this.index.addAsync(data);
    console.log('Task "Add Bulk" Done');
  }

  /**
   * Queries a given search index.
   * @param {flexsearch.Document} document The instance of FlexSearch.Document to which data should be added.
   * @param {string} query The search query to perform
   * @param {'title'|'content'} [field='title'] Optional. The name of the field to search. Defaults to 'title'.
   * @returns {Promise<*>}
   */
  async search(query) {
    const results = await this.index.searchAsync(query);
    console.log(`results: ${results}`);
    console.log('Task "Search" Done.');
    return results;
  }

  /**
   * Exports indexed search data from the index to IndexDB
   * @param {flexsearch.Document} document The instance of FlexSearch.Document from which data should be exported.
   * @returns {Promise<void>}
   */
  async exportToIndexDB() {
    try {
      const backups = [];

      await new Promise((resolve) => {
        this.index.export((key, d) => {
          const backup = { key, data: d };
          backups.push(backup);
        }).then(resolve);
      });

      await localforage.setItem(this.cacheKey, backups);
    } catch (err) {
      console.error(err);
    }
  }

  /**
   *
   * @returns {Promise<void>}
   */
  async importFromIndexDB() {
    try {
      const dataFromStorage = await localforage.getItem(this.cacheKey);

      if (dataFromStorage) {
        dataFromStorage.forEach((item) => {
          this.index.add(item.key, item.data);
        });
      }
    } catch (err) {
      console.error(err);
    }
  }
};
