const fs = require('fs');
const path = require('path');

const themeModulePath = '../../attack-theme/static/scripts/theme.js';

describe('site theme', () => {
  let theme;

  beforeEach(() => {
    jest.resetModules();
    theme = require(themeModulePath);
  });

  test('uses System when no saved override exists', () => {
    const storage = createStorage();
    const root = createRoot();

    expect(theme.readStoredPreference(storage)).toBe('system');

    theme.applyPreference(root, 'system');

    expect(root.removeAttribute).toHaveBeenCalledWith('data-theme');
    expect(root.style.setProperty).not.toHaveBeenCalled();
  });

  test.each(['light', 'dark'])('applies a saved %s override before controls initialize', preference => {
    const storage = createStorage(preference);
    const root = createRoot();

    const storedPreference = theme.readStoredPreference(storage);
    theme.applyPreference(root, storedPreference);

    expect(storedPreference).toBe(preference);
    expect(root.setAttribute).toHaveBeenCalledWith('data-theme', preference);
    // CSS owns color-scheme so the print stylesheet can force light controls.
    expect(root.style.setProperty).not.toHaveBeenCalled();
  });

  test('discards an invalid saved preference', () => {
    const storage = createStorage('sepia');

    expect(theme.readStoredPreference(storage)).toBe('system');
    expect(storage.removeItem).toHaveBeenCalledWith(theme.STORAGE_KEY);
  });

  test('adds a working archive switch to the existing banner without replacing its content', () => {
    const fixture = createControllerFixture({ storedPreference: 'dark' });
    const banner = { appendChild: jest.fn(), textContent: 'Currently viewing ATT&CK v3.0' };
    fixture.document.querySelector = jest.fn(selector => (
      selector === '.version-banner' ? banner : null
    ));
    fixture.document.createElement = jest.fn(() => fixture.toggle);
    fixture.document.readyState = 'complete';

    theme.bootstrap({ ...fixture, archived: true });

    expect(fixture.document.documentElement.setAttribute).toHaveBeenCalledWith('data-archive-theme', '');
    expect(banner.appendChild).toHaveBeenCalledWith(fixture.toggle);
    expect(banner.textContent).toBe('Currently viewing ATT&CK v3.0');
    expect(fixture.toggle.setAttribute).toHaveBeenCalledWith('aria-label', 'Dark mode');
    expect(fixture.toggle.setAttribute).toHaveBeenCalledWith('aria-checked', 'true');
    fixture.toggle.click();
    expect(fixture.storage.setItem).toHaveBeenCalledWith(theme.STORAGE_KEY, 'light');
    expect(fixture.toggle.setAttribute).toHaveBeenCalledWith('aria-checked', 'false');
  });

  test('toggles from the system light theme to a saved dark override', () => {
    const fixture = createControllerFixture({ systemDark: false });
    const controller = theme.createThemeController(fixture);

    controller.init();
    fixture.toggle.click();

    expect(fixture.document.documentElement.setAttribute).toHaveBeenLastCalledWith('data-theme', 'dark');
    expect(fixture.storage.setItem).toHaveBeenCalledWith(theme.STORAGE_KEY, 'dark');
    expect(fixture.toggle.setAttribute).toHaveBeenCalledWith('aria-label', 'Switch to light mode');
    expect(fixture.toggle.setAttribute).toHaveBeenCalledWith('aria-checked', 'true');
  });

  test('toggles from the system dark theme to a saved light override', () => {
    const fixture = createControllerFixture({ systemDark: true });
    const controller = theme.createThemeController(fixture);

    controller.init();
    fixture.toggle.click();

    expect(fixture.document.documentElement.setAttribute).toHaveBeenLastCalledWith('data-theme', 'light');
    expect(fixture.storage.setItem).toHaveBeenCalledWith(theme.STORAGE_KEY, 'light');
    expect(fixture.toggle.setAttribute).toHaveBeenCalledWith('aria-label', 'Switch to dark mode');
    expect(fixture.toggle.setAttribute).toHaveBeenCalledWith('aria-checked', 'false');
  });

  test.each([
    ['light', 'dark'],
    ['dark', 'light'],
  ])('toggles a saved %s override to %s', (storedPreference, expectedPreference) => {
    const fixture = createControllerFixture({ storedPreference });
    const controller = theme.createThemeController(fixture);

    controller.init();
    fixture.toggle.click();

    expect(fixture.document.documentElement.setAttribute).toHaveBeenLastCalledWith(
      'data-theme',
      expectedPreference,
    );
    expect(fixture.storage.setItem).toHaveBeenCalledWith(theme.STORAGE_KEY, expectedPreference);
  });

  test('continues applying a choice when storage access fails', () => {
    const fixture = createControllerFixture();
    fixture.storage.setItem.mockImplementation(() => {
      throw new Error('Storage disabled');
    });
    const controller = theme.createThemeController(fixture);

    expect(() => {
      controller.init();
      fixture.toggle.click();
    }).not.toThrow();
    expect(fixture.document.documentElement.setAttribute).toHaveBeenLastCalledWith('data-theme', 'dark');
  });

  test('updates the toggle when the system preference changes before an override', () => {
    const fixture = createControllerFixture({ systemDark: false });
    const controller = theme.createThemeController(fixture);

    controller.init();
    expect(fixture.toggle.setAttribute).toHaveBeenCalledWith('aria-label', 'Switch to dark mode');

    fixture.mediaQuery.matches = true;
    fixture.mediaQuery.dispatchChange();

    expect(fixture.toggle.setAttribute).toHaveBeenCalledWith('aria-label', 'Switch to light mode');
  });

  test('ignores OS preference changes while an explicit override is active', () => {
    const fixture = createControllerFixture({ storedPreference: 'light', systemDark: false });
    const controller = theme.createThemeController(fixture);

    controller.init();
    fixture.mediaQuery.matches = true;
    fixture.mediaQuery.dispatchChange();

    expect(fixture.toggle.setAttribute).toHaveBeenCalledWith('aria-label', 'Switch to dark mode');
  });

  test('synchronizes a theme change from another tab without writing it back', () => {
    const fixture = createControllerFixture({ storedPreference: 'light' });
    theme.createThemeController(fixture).init();

    fixture.storage.getItem.mockReturnValue('dark');
    fixture.document.defaultView.dispatchStorage({
      key: theme.STORAGE_KEY,
      storageArea: fixture.storage,
    });

    expect(fixture.document.documentElement.setAttribute).toHaveBeenLastCalledWith('data-theme', 'dark');
    expect(fixture.toggle.setAttribute).toHaveBeenCalledWith('aria-checked', 'true');
    expect(fixture.storage.setItem).not.toHaveBeenCalled();
    fixture.toggle.click();
    expect(fixture.storage.setItem).toHaveBeenCalledWith(theme.STORAGE_KEY, 'light');
  });

  test.each([null, 'attack-website-theme'])('returns to the system theme after storage removal (%s)', key => {
    const fixture = createControllerFixture({ storedPreference: 'dark', systemDark: false });
    theme.createThemeController(fixture).init();

    fixture.storage.getItem.mockReturnValue(null);
    fixture.document.defaultView.dispatchStorage({ key, storageArea: fixture.storage });

    expect(fixture.document.documentElement.removeAttribute).toHaveBeenCalledWith('data-theme');
    expect(fixture.toggle.setAttribute).toHaveBeenCalledWith('aria-checked', 'false');
    fixture.mediaQuery.matches = true;
    fixture.mediaQuery.dispatchChange();
    expect(fixture.toggle.setAttribute).toHaveBeenLastCalledWith('data-theme-effective', 'dark');
  });

  test('ignores unrelated storage keys and storage areas', () => {
    const fixture = createControllerFixture({ storedPreference: 'light' });
    theme.createThemeController(fixture).init();
    fixture.storage.getItem.mockClear();

    fixture.document.defaultView.dispatchStorage({ key: 'other', storageArea: fixture.storage });
    fixture.document.defaultView.dispatchStorage({ key: theme.STORAGE_KEY, storageArea: createStorage('dark') });

    expect(fixture.storage.getItem).not.toHaveBeenCalled();
  });

  test('loads the early theme script before styles and renders one toggle before search', () => {
    const template = fs.readFileSync(
      path.join(__dirname, '../../attack-theme/templates/general/base-template.html'),
      'utf8',
    );
    const navigation = fs.readFileSync(
      path.join(__dirname, '../../attack-theme/templates/macros/navigation_menu.html'),
      'utf8',
    );

    expect(template).toContain('<meta name="color-scheme" content="light dark">');
    expect(template.indexOf('/theme/scripts/theme.js')).toBeLessThan(template.indexOf('bootstrap.min.css'));
    expect(navigation.match(/\bdata-theme-toggle(?=[\s>])/g)).toHaveLength(1);
    expect(navigation.indexOf('id="theme-toggle"')).toBeLessThan(navigation.indexOf('id="search-button"'));
    expect(navigation).toContain('role="switch"');
    expect(navigation).toContain('class="theme-toggle-track"');
    expect(navigation).toContain('class="theme-toggle-thumb"');
    expect(navigation).toContain('aria-checked="false"');
    expect(navigation).not.toContain('aria-pressed');
    expect(navigation).not.toContain('data-theme-option');
    expect(navigation).not.toContain('theme-menu');
    expect(navigation).not.toContain('dropdown-toggle" type="button" data-theme-toggle');
  });

  test('uses theme-aware surfaces for the affected resource pages', () => {
    const council = fs.readFileSync(
      path.join(__dirname, '../../modules/resources/templates/attack-advisory-council-members.html'),
      'utf8',
    );
    const dataTools = fs.readFileSync(
      path.join(__dirname, '../../modules/resources/templates/attack-data-and-tools.html'),
      'utf8',
    );
    const attackcon = fs.readFileSync(
      path.join(__dirname, '../../modules/resources/templates/attackcon-overview.html'),
      'utf8',
    );

    expect(council).toContain('background: var(--attack-color-body-alternate);');
    expect(council).toContain('color: var(--attack-on-color-body);');
    expect(dataTools).toContain('class="tab-content card card-body p-3 attack-excel-files"');
    expect(dataTools).not.toContain('style="background: #f8f9fa;"');
    expect(attackcon).toContain('"ATT&CKcon 4.0", "ATT&CKcon 5.0", "ATT&CKcon 6.0", "ATT&CKcon 7.0"');
    expect(attackcon).toContain('attackcon-banner-image{% if con.title in light_banner_titles %} on-light{% endif %}');
  });

  test('uses theme-aware home controls and announcement banner colors', () => {
    const home = fs.readFileSync(
      path.join(__dirname, '../../attack-theme/templates/general/attack-index.html'),
      'utf8',
    );
    const colors = fs.readFileSync(
      path.join(__dirname, '../../attack-style/themes/_palette.scss'),
      'utf8',
    );

    expect(home).toContain('fa-up-right-from-square external-link-icon');
    expect(home).toContain('dropdown-toggle-split random-page-toggle');
    expect(home).not.toContain('external-site-dark.jpeg');
    expect(home).not.toContain('style="color: #4f7cac; background-color: white;');
    expect(colors).toContain('--attack-color-banner: #e7f0f6;');
    expect(colors).toContain('--attack-color-banner: #263a49;');
  });

  test('renders the matrix Navigator link with a theme-aware icon', () => {
    const matrix = fs.readFileSync(
      path.join(__dirname, '../../modules/matrices/templates/matrix.html'),
      'utf8',
    );

    expect(matrix).toContain('fa-up-right-from-square');
    expect(matrix).not.toContain('external-site-dark.jpeg');
  });

  test('paints the initial toggle state from the root theme and suppresses the Bootstrap focus ring', () => {
    const nav = fs.readFileSync(
      path.join(__dirname, '../../attack-style/layout/_nav.scss'),
      'utf8',
    );

    expect(nav).toContain(':root[data-theme="dark"] &');
    expect(nav).toContain(':root:not([data-theme]) &');
    expect(nav).toMatch(/&:focus\s*\{\s*outline: 0;\s*box-shadow: none;/);
  });

  test('uses a warm metadata label color only in dark mode', () => {
    const colors = fs.readFileSync(
      path.join(__dirname, '../../attack-style/themes/_palette.scss'),
      'utf8',
    );
    const layout = fs.readFileSync(
      path.join(__dirname, '../../attack-style/layout/_layout.scss'),
      'utf8',
    );

    expect(colors).toContain('--attack-color-property-label: #1d2226;');
    expect(colors).toContain('--attack-color-property-label: #f2d2a4;');
    expect(layout).toMatch(/\.card-data \.card-title\s*\{\s*color: color-functions\.color\(property-label\);/);
  });
});

function createStorage(value = null) {
  return {
    getItem: jest.fn(() => value),
    removeItem: jest.fn(),
    setItem: jest.fn(),
  };
}

function createRoot() {
  return {
    removeAttribute: jest.fn(),
    setAttribute: jest.fn(),
    style: {
      removeProperty: jest.fn(),
      setProperty: jest.fn(),
    },
  };
}

function createElement() {
  const listeners = {};
  return {
    classList: { toggle: jest.fn() },
    setAttribute: jest.fn(),
    addEventListener: jest.fn((eventName, listener) => {
      listeners[eventName] = listener;
    }),
    click: () => listeners.click({ preventDefault: jest.fn() }),
  };
}

function createControllerFixture({ storedPreference = null, systemDark = false } = {}) {
  const root = createRoot();
  const toggle = createElement();
  let changeListener;
  let storageListener;
  const mediaQuery = {
    matches: systemDark,
    addEventListener: jest.fn((eventName, listener) => {
      if (eventName === 'change') changeListener = listener;
    }),
    dispatchChange: () => changeListener({ matches: mediaQuery.matches }),
  };
  const document = {
    documentElement: root,
    querySelector: jest.fn(selector => (selector === '[data-theme-toggle]' ? toggle : null)),
    defaultView: {
      addEventListener: jest.fn((eventName, listener) => {
        if (eventName === 'storage') storageListener = listener;
      }),
      dispatchStorage: event => storageListener(event),
    },
  };

  return {
    document,
    mediaQuery,
    storage: createStorage(storedPreference),
    toggle,
  };
}
