# Base Styles

This folder contains broad styles that apply across pages before layout and component-specific rules.

## Files

| File | Purpose |
| --- | --- |
| `_base.scss` | Defines shared utility classes and base color treatments used by generated pages. |
| `_typography.scss` | Defines small text label helpers. |

## Notes

`_base.scss` depends on `abstracts/color-functions` so base classes stay aligned with the active theme.
The `%bg-alternate` placeholder is extended by `.bg-alternate` and should remain theme-aware.

Keep new rules here only when they are genuinely global.
Rules for a specific page section, navigation area, or interactive feature should live in `layout/` or `components/`.
