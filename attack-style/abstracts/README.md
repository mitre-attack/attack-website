# Abstracts

This folder contains Sass primitives used by the rest of `attack-style`.
Files in this folder should not emit large blocks of CSS on their own unless they explicitly define shared declarations such as fonts.

## Files

| File | Purpose |
| --- | --- |
| `_variables.scss` | Defines brand and user color maps plus the semantic `$colors` map used across the site. |
| `_color-functions.scss` | Provides accessors and derived color helpers for entries in `$colors`. |
| `_utilities.scss` | Provides small reusable mixins and unit helpers. |
| `_font-faces.scss` | Defines shared font-face declarations. |

## Color Model

`_variables.scss` keeps raw brand values separate from semantic color names.
Most styles should use semantic keys from `$colors`, such as `primary`, `secondary`, `footer`, `active`, `body`, `link`, `matrix-header`, `search-highlight`, and `deemphasis`.

Each color entry may contain:

| Key | Meaning |
| --- | --- |
| `color` | The background, foreground, or base color value. |
| `on-color` | The readable text color intended for use on top of `color`. |

Some entries omit `on-color` when they are not meant to contain inner text.

## Helper Functions

Use the functions in `_color-functions.scss` instead of reading `$colors` directly from component or layout files:

| Function | Use |
| --- | --- |
| `color($name)` | Reads the base color for a semantic color name. |
| `on-color($name)` | Reads the readable text color for a semantic color name. |
| `color-alternate($name, $contrast: 1)` | Computes a nearby alternate shade for patterning or subtle contrast. |
| `on-color-emphasis($name)` | Computes a stronger foreground color against a semantic background. |
| `on-color-deemphasis($name)` | Computes a quieter foreground color against a semantic background. |
| `border-color($name)` | Computes a border color for a semantic background. |
| `background-color($name)` | Computes a subtle derived background shade. |
| `escape-color($color)` | Escapes a concrete color for use inside inline SVG data URLs. |

## Utility Mixins And Functions

| Helper | Use |
| --- | --- |
| `font($primary, $secondary: sans-serif)` | Emits a font-family declaration. |
| `to-rem($target-val)` | Converts a pixel-like number against a 16px base to `rem`. |
| `rem($value)` | Applies the site's legacy rem offset helper. |
| `margin($property, $value)` | Emits margin declarations based on the site's 24px spacing unit. |
