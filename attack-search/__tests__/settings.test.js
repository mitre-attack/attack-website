const {
  searchCacheCompatibilityVersion,
  searchFilePaths,
} = require('../src/settings');
const packageJson = require('../package.json');

describe('search settings', () => {
  test('includes the FlexSearch version in the cache compatibility token', () => {
    const expectedFlexSearchVersion = packageJson.dependencies.flexsearch.replace(/^[^\d]*/, '');

    expect(searchCacheCompatibilityVersion).toBe(`flexsearch-${expectedFlexSearchVersion}`);
  });

  test('loads the generated sub-technique search index', () => {
    expect(searchFilePaths).toContain('sub-techniques.json');
  });

  test('keeps the generated misc search index for unknown pages', () => {
    expect(searchFilePaths).toContain('misc.json');
  });
});
