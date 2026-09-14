(function(globalObject, factory) {
    const theme = factory();

    if (typeof module === 'object' && module.exports) {
        module.exports = theme;
    }

    if (globalObject && globalObject.document) {
        let storage = null;

        try {
            storage = globalObject.localStorage;
        } catch (error) {
            // Accessing localStorage itself can fail in restricted contexts.
        }

        theme.bootstrap({
            document: globalObject.document,
            archived: !!(globalObject.document.currentScript
                && globalObject.document.currentScript.hasAttribute('data-archive-theme')),
            mediaQuery: typeof globalObject.matchMedia === 'function'
                ? globalObject.matchMedia('(prefers-color-scheme: dark)')
                : null,
            storage
        });
    }
}(typeof window !== 'undefined' ? window : null, function() {
    const STORAGE_KEY = 'attack-website-theme';
    const EXPLICIT_PREFERENCES = ['light', 'dark'];

    function isExplicitPreference(preference) {
        return EXPLICIT_PREFERENCES.includes(preference);
    }

    function readStoredPreference(storage) {
        if (!storage) return 'system';

        try {
            const storedPreference = storage.getItem(STORAGE_KEY);
            if (isExplicitPreference(storedPreference)) return storedPreference;
            if (storedPreference !== null) storage.removeItem(STORAGE_KEY);
        } catch (error) {
            // Storage may be unavailable in privacy-restricted browser contexts.
        }

        return 'system';
    }

    function savePreference(storage, preference) {
        if (!storage) return;

        try {
            if (isExplicitPreference(preference)) {
                storage.setItem(STORAGE_KEY, preference);
            } else {
                storage.removeItem(STORAGE_KEY);
            }
        } catch (error) {
            // The in-page choice still works when storage is unavailable.
        }
    }

    function applyPreference(root, preference) {
        if (isExplicitPreference(preference)) {
            root.setAttribute('data-theme', preference);
        } else {
            root.removeAttribute('data-theme');
        }
    }

    function effectiveTheme(preference, mediaQuery) {
        if (isExplicitPreference(preference)) return preference;
        return mediaQuery && mediaQuery.matches ? 'dark' : 'light';
    }

    function createThemeController({ document, storage, mediaQuery, archived = false }) {
        const systemTheme = mediaQuery || { matches: false };
        let preference = readStoredPreference(storage);
        let toggle;

        function updateControl() {
            if (!toggle) return;

            const currentTheme = effectiveTheme(preference, systemTheme);
            const nextTheme = currentTheme === 'dark' ? 'light' : 'dark';
            const label = `Switch to ${nextTheme} mode`;
            toggle.setAttribute('aria-label', archived ? 'Dark mode' : label);
            toggle.setAttribute('title', label);
            toggle.setAttribute('aria-checked', String(currentTheme === 'dark'));
            toggle.setAttribute('data-theme-effective', currentTheme);
        }

        function setPreference(nextPreference) {
            preference = isExplicitPreference(nextPreference) ? nextPreference : 'system';
            applyPreference(document.documentElement, preference);
            savePreference(storage, preference);
            updateControl();
        }

        function handleSystemThemeChange() {
            if (preference === 'system') updateControl();
        }

        function init() {
            applyPreference(document.documentElement, preference);
            toggle = document.querySelector('[data-theme-toggle]');

            if (archived && !toggle) {
                const banner = document.querySelector('.version-banner');
                if (banner) {
                    toggle = document.createElement('button');
                    toggle.className = 'archive-theme-toggle';
                    toggle.type = 'button';
                    toggle.setAttribute('role', 'switch');
                    toggle.setAttribute('data-theme-toggle', '');
                    toggle.textContent = 'Dark mode';
                    banner.appendChild(toggle);
                }
            }

            if (toggle) {
                toggle.addEventListener('click', event => {
                    event.preventDefault();
                    const currentTheme = effectiveTheme(preference, systemTheme);
                    setPreference(currentTheme === 'dark' ? 'light' : 'dark');
                });
            }

            if (typeof systemTheme.addEventListener === 'function') {
                systemTheme.addEventListener('change', handleSystemThemeChange);
            } else if (typeof systemTheme.addListener === 'function') {
                systemTheme.addListener(handleSystemThemeChange);
            }

            updateControl();
        }

        return { init, setPreference };
    }

    function bootstrap({ document, storage, mediaQuery, archived = false }) {
        if (archived) document.documentElement.setAttribute('data-archive-theme', '');
        const preference = readStoredPreference(storage);
        applyPreference(document.documentElement, preference);
        const controller = createThemeController({ document, storage, mediaQuery, archived });

        if (document.readyState === 'loading') {
            document.addEventListener('DOMContentLoaded', controller.init, { once: true });
        } else {
            controller.init();
        }

        return controller;
    }

    return {
        STORAGE_KEY,
        applyPreference,
        bootstrap,
        createThemeController,
        effectiveTheme,
        readStoredPreference
    };
}));
