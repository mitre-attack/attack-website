const { searchFilePaths } = require('../src/settings');

describe('search settings', () => {
  test('loads the generated sub-technique search index', () => {
    expect(searchFilePaths).toContain('sub-techniques.json');
  });

  test('keeps the generated misc search index for unknown pages', () => {
    expect(searchFilePaths).toContain('misc.json');
  });
});
