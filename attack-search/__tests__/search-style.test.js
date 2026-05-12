const fs = require('fs');
const path = require('path');

describe('search styles', () => {
  test('marks page type and domain result badges with distinct classes', () => {
    const searchService = fs.readFileSync(
      path.join(__dirname, '../src/search-service.js'),
      'utf8',
    );

    expect(searchService).toContain('search-result-badge-page-type');
    expect(searchService).toContain('search-result-badge-domain');
  });

  test('renders result badges as subtle prominent chips', () => {
    const styles = fs.readFileSync(
      path.join(__dirname, '../../attack-style/components/_search.scss'),
      'utf8',
    );

    const badgeStyle = styles.match(/\.search-result-badge\s*\{(?<body>[^}]+)\}/)?.groups?.body ?? '';

    expect(badgeStyle).toContain('color: white;');
    expect(badgeStyle).toContain('font-size: 0.8rem;');

    expect(styles).toContain('.search-result-badge-page-type');
    expect(styles).toContain('border-color: color-functions.color(active);');
    expect(styles).toContain('background: color-functions.color-alternate(active, 1.5);');
    expect(styles).toContain('.search-result-badge-domain');
    expect(styles).toContain('border-color: color-functions.color(deemphasis);');
    expect(styles).toContain('background: color-functions.color(deemphasis);');
  });

  test('renders search pagination controls as accessible icon buttons', () => {
    const searchService = fs.readFileSync(
      path.join(__dirname, '../src/search-service.js'),
      'utf8',
    );
    const styles = fs.readFileSync(
      path.join(__dirname, '../../attack-style/components/_search.scss'),
      'utf8',
    );

    expect(searchService).toContain('aria-label="Previous page"');
    expect(searchService).toContain('aria-label="Next page"');
    expect(searchService).not.toContain('>Prev</button>');
    expect(searchService).not.toContain('>Next</button>');
    expect(styles).toContain('.search-pagination-icon');
  });
});
