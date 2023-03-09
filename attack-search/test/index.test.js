const FlexSearch = require('flexsearch');

const { Document, Index } = FlexSearch;

const index = new Index();

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

const data = [
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

async function add(data) {
  await index.addAsync(data.id, data.content);
  console.log('Task Done');
}

async function search(query) {
  const results = await index.searchAsync(query);
  return results;
}

const doIt = async (dataArray) => {
  const promises = dataArray.map(async (item) => add(item));
  await Promise.all(promises);

  const results = await search('content');
  console.log(`RESULTS: ${results}`);
};

doIt(data).then(() => console.log('done'));

/**
 * OUTPUT:
 * ❯ node test/index.test.js
 * Task Done
 * Task Done
 * RESULTS: 0,1
 * done
 */
