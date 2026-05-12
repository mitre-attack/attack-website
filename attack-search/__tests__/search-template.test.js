const fs = require('fs');
const path = require('path');

describe('search template', () => {
  test('places result counts and pagination above the result list', () => {
    const template = fs.readFileSync(
      path.join(__dirname, '../../attack-theme/templates/macros/search.html'),
      'utf8',
    );

    const searchBodyStart = template.indexOf('<div id="search-body" class="search-body">');
    const footerStart = template.indexOf('<div id="search-results-footer"', searchBodyStart);
    const resultsStart = template.indexOf('<div class="results" id="search-results">', searchBodyStart);

    expect(searchBodyStart).toBeGreaterThan(-1);
    expect(footerStart).toBeGreaterThan(-1);
    expect(resultsStart).toBeGreaterThan(-1);
    expect(footerStart).toBeLessThan(resultsStart);
  });

  test('places pagination controls after the result list for sticky bottom positioning', () => {
    const template = fs.readFileSync(
      path.join(__dirname, '../../attack-theme/templates/macros/search.html'),
      'utf8',
    );

    const searchBodyStart = template.indexOf('<div id="search-body" class="search-body">');
    const resultsStart = template.indexOf('<div class="results" id="search-results">', searchBodyStart);
    const paginationStart = template.indexOf('<div id="search-results-pagination"', searchBodyStart);

    expect(searchBodyStart).toBeGreaterThan(-1);
    expect(resultsStart).toBeGreaterThan(-1);
    expect(paginationStart).toBeGreaterThan(-1);
    expect(resultsStart).toBeLessThan(paginationStart);
  });
});
