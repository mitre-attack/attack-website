# Themes

This folder contains the runtime color palettes used by the generated stylesheets.

## Files

| File | Purpose |
| --- | --- |
| `_palette.scss` | Shared light/dark token mixins, including the charcoal surfaces. |
| `_archive.scss` | Scoped color compatibility rules and a banner switch for preserved sites. |
| `_colors.scss` | Emits the light and dark semantic color tokens, system preference behavior, explicit theme overrides, and shared Bootstrap surface adjustments. |

## Active Theme Switch

The site has two independent theme layers. The brand layer is selected at build time by `config.scss` and the two top-level entrypoints:

| File | Behavior |
| --- | --- |
| `style-attack.scss` | Sets `$use-attack-theme: true` and imports the shared style graph. |
| `style-user.scss` | Sets `$use-attack-theme: false` and imports the shared style graph. |

The light/dark appearance is selected at runtime. With no `data-theme` attribute on the root element, the stylesheet follows `prefers-color-scheme`. The single navigation toggle stores an explicit `data-theme="light"` or `data-theme="dark"` override after the user first switches themes.

Most styling should use semantic color helpers from `abstracts/_color-functions.scss`. Add a token to `_palette.scss` when a component needs a distinct theme-aware surface or foreground instead of embedding a light-only color in that component.

## Preserved Sites

`style-archive.scss` builds `style-archive.css` alongside the two current-site stylesheets. The versions deployment module adds this stylesheet and the shared theme script to extracted HTML pages with an archive banner. It skips sidebar fragments, redirects, and pages with native theme controls. The stored tarballs are unchanged; every extraction source receives the same idempotent enhancement.

The script adds a keyboard-accessible “Dark mode” switch to the existing `.version-banner`. It shares the current site's stored appearance preference. The archive stylesheet supplies color overrides only in dark screen mode; light mode and print retain the archive's original presentation. The archive's original styles, content, URLs, logos, and external widgets remain in place.

Theme scripts set `data-theme` only. CSS owns `color-scheme`, allowing print to use light native controls even when a dark preference is saved.
