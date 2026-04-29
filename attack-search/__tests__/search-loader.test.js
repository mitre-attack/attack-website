const { loadSearchDocuments } = require('../src/search-loader');

describe('search loader', () => {
  test('skips missing optional search files and returns loaded documents', async () => {
    const getJSON = jest.fn((url) => {
      if (url.endsWith('misc.json')) return Promise.reject({ status: 404 });
      return Promise.resolve([{ id: url, title: 'Loaded' }]);
    });

    const documents = await loadSearchDocuments('/search/', ['techniques.json', 'misc.json'], getJSON);

    expect(documents).toEqual([{ id: '/search/techniques.json', title: 'Loaded' }]);
  });

  test('fails when every optional search file is missing', async () => {
    const getJSON = jest.fn(() => Promise.reject({ status: 404 }));

    await expect(loadSearchDocuments('/search/', ['misc.json'], getJSON)).rejects.toThrow('No search index files');
  });

  test('fails malformed existing search files', async () => {
    const getJSON = jest.fn(() => Promise.reject(new SyntaxError('Unexpected token')));

    await expect(loadSearchDocuments('/search/', ['techniques.json'], getJSON)).rejects.toThrow('Unexpected token');
  });
});
