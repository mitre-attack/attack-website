# Themes

This folder is reserved for theme-specific Sass.

## Files

| File | Purpose |
| --- | --- |
| `_colors.scss` | Reserved for theme color overrides or extracted theme color definitions. It is currently empty. |

## Active Theme Switch

The active color set is currently controlled by `config.scss` and the two top-level entrypoints:

| File | Behavior |
| --- | --- |
| `style-attack.scss` | Sets `$use-attack-theme: true` and imports the shared style graph. |
| `style-user.scss` | Sets `$use-attack-theme: false` and imports the shared style graph. |

Most theme-aware styling should continue to use semantic color helpers from `abstracts/_color-functions.scss`.
Add theme-specific Sass here only when the existing semantic color map is not enough.
