const fs = require('fs');
const FlexSearch = require('flexsearch');
const fakeIndexedDB = require('fake-indexeddb');
const IDBKeyRange = require('fake-indexeddb/lib/FDBKeyRange');
const localforage = require('localforage').createInstance({
  driver: [fakeIndexedDB],
});

// Define the index key
const INDEX_KEY = 'myIndex';

const { Document } = FlexSearch;

class AttackIndex {
  constructor() {
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

  async add(data) {
    await this.index.addAsync(data);
    console.log('Task "Add Bulk" Done');
  }

  async search(query) {
    const results = await this.index.searchAsync(query);
    console.log(`results: ${results}`);
    console.log('Task "Search" Done.');
    return results;
  }

  async exportToIndexDB() {
    try {
      const backups = [];

      await new Promise((resolve) => {
        this.index.export((key, d) => {
          const backup = { key, data: d };
          backups.push(backup);
        }).then(resolve);
      });

      await localforage.setItem(INDEX_KEY, backups);
    } catch (err) {
      console.error(err);
    }
  }

  async importFromIndexDB() {
    try {
      const dataFromStorage = await localforage.getItem(INDEX_KEY);

      if (dataFromStorage) {
        dataFromStorage.forEach((item) => {
          this.index.add(item.key, item.data);
        });
      }
    } catch (err) {
      console.error(err);
    }
  }
}
const initDocument = () => new Document({
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

const fakeData = [
  {
    id: 0,
    title: 'title-0',
    content: 'content-0',
  },
  {
    id: 1,
    title: 'title-1',
    content: 'content-1',
  },
];

async function add(document, data) {
  await document.addAsync(data);
  console.log('Task Done');
}

async function search(document, query) {
  const results = await document.searchAsync(query);
  return results;
}

async function exportToFile(document) {
  document.export((key, data) => new Promise((resolve) => {
    const backup = { key, data };
    const json = JSON.stringify(backup);

    fs.appendFile('backup.json', json, (err) => {
      if (err) throw err;
      resolve();
    });
  }));
}

async function exportToIndexDB(document) {
  try {
    const backups = [];

    await new Promise((resolve) => {
      document.export((key, d) => {
        const backup = { key, data: d };
        backups.push(backup);
      }).then(resolve);
    });

    await localforage.setItem(INDEX_KEY, backups);
  } catch (err) {
    console.error(err);
  }
}

function importFromFile(document) {
  fs.readFile('backup.json', 'utf-8', (err, d) => {
    if (err) throw err;

    const backups = JSON.parse(d);

    backups.forEach((backup) => {
      document.add(backup.key, backup.data);
    });
  });
}

async function importFromIndexDB(document) {
  try {
    const dataFromStorage = await localforage.getItem(INDEX_KEY);

    if (dataFromStorage) {
      dataFromStorage.forEach((item) => {
        document.add(item.key, item.data);
      });
    }
  } catch (err) {
    console.error(err);
  }
}

const testOne = async (dataArray) => {
  console.log('Test 1 Step 1: Initialize the index.');
  const document = new Document({
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

  console.log('Test 1 Step 2: Add data to the index');
  const promises = dataArray.map(async (item) => add(document, item));
  await Promise.all(promises);

  console.log('Test 1 Step 3: Search for data in the index');
  const results = await search(document, 'content');
  console.log(`RESULTS: ${JSON.stringify(results)}`);
};

const testTwo = async () => {
  console.log('Test 2 Step 1: Initialize the index.');
  const index = new AttackIndex();

  console.log('Test 2 Step 2: Add data to the index');
  const promises = fakeData.map(async (item) => index.add(item));
  await Promise.all(promises);

  console.log('Test 2 Step 3: Search the index...');
  const results = await index.search('content');
  console.log(`Test 2 Step 3 Results: ${JSON.stringify(results)}`);
};

// testOne(fakeData).then(() => console.log('Test 1 complete.'));
/**
 * OUTPUT:
 * ❯ node test/document.test.js
 * Task Done
 * Task Done
 * RESULTS: [{"field":"content","result":[0,1]}]
 * done
 */

testTwo().then(() => console.log('Test 2 complete.'));
