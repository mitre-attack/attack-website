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

    function initNavigationToggle(document, toggle) {
        const view = document.defaultView;
        const home = document.querySelector('[data-theme-toggle-home]');
        const mobile = document.querySelector('[data-theme-toggle-mobile]');
        if (!view || !home || !mobile || !toggle) return;

        const navbar = mobile.closest('.navbar');
        const brand = navbar.querySelector('.navbar-brand');
        const hamburger = mobile.querySelector('.navbar-toggler');
        let pending = false;

        function outerWidth(element) {
            const style = view.getComputedStyle(element);
            return element.getBoundingClientRect().width
                + parseFloat(style.marginLeft) + parseFloat(style.marginRight);
        }

        function updatePlacement() {
            pending = false;
            const focused = document.activeElement === toggle;
            let destination = home;

            // Bootstrap controls the breakpoint; measure only when the hamburger is shown.
            if (view.getComputedStyle(hamburger).display !== 'none') {
                if (toggle.parentNode !== mobile) mobile.insertBefore(toggle, hamburger);
                const style = view.getComputedStyle(navbar);
                const availableWidth = navbar.clientWidth
                    - parseFloat(style.paddingLeft) - parseFloat(style.paddingRight);
                if (outerWidth(brand) + mobile.getBoundingClientRect().width <= availableWidth) {
                    destination = mobile;
                }
            }

            if (toggle.parentNode !== destination) destination.appendChild(toggle);
            home.hidden = destination === mobile;

            // Moving a focused node can blur it. If it now lives in the closed menu,
            // leave focus on the button that opens that menu instead.
            if (focused) {
                const focusTarget = toggle.getClientRects().length ? toggle : hamburger;
                focusTarget.focus({ preventScroll: true });
            }
        }

        function schedulePlacement() {
            if (pending) return;
            pending = true;
            view.requestAnimationFrame(updatePlacement);
        }

        updatePlacement();
        view.addEventListener('resize', schedulePlacement);
        if (typeof view.ResizeObserver === 'function') {
            const observer = new view.ResizeObserver(schedulePlacement);
            [navbar, brand, hamburger, toggle].forEach(element => observer.observe(element));
        }
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

        function handleToggleClick(event) {
            if (!event.target || typeof event.target.closest !== 'function') return;

            const clickedToggle = event.target.closest('[data-theme-toggle]');
            if (!clickedToggle) return;

            event.preventDefault();
            toggle = clickedToggle;
            const currentTheme = effectiveTheme(preference, systemTheme);
            setPreference(currentTheme === 'dark' ? 'light' : 'dark');
        }

        // The head script runs before the toggle markup is parsed. Delegation makes
        // the visible control interactive without waiting for DOMContentLoaded.
        document.addEventListener('click', handleToggleClick);

        function handleSystemThemeChange() {
            if (preference === 'system') updateControl();
        }

        function handleStorageChange(event) {
            if (!storage || event.storageArea !== storage
                || (event.key !== STORAGE_KEY && event.key !== null)) return;

            preference = readStoredPreference(storage);
            applyPreference(document.documentElement, preference);
            updateControl();
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

            if (typeof systemTheme.addEventListener === 'function') {
                systemTheme.addEventListener('change', handleSystemThemeChange);
            } else if (typeof systemTheme.addListener === 'function') {
                systemTheme.addListener(handleSystemThemeChange);
            }

            if (document.defaultView) {
                document.defaultView.addEventListener('storage', handleStorageChange);
            }
            if (!archived) initNavigationToggle(document, toggle);
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
