# Components

This folder contains styles for discrete ATT&CK website features.

## Files

| File | Purpose |
| --- | --- |
| `_search.scss` | Styles the full-screen search overlay, search input, filters, result list, result cards, warnings, loading states, and search highlights. |
| `_matrix.scss` | Styles matrix containers, tactic columns, technique rows, scroll indicators, side matrix behavior, and matrix responsiveness. |
| `_tour.scss` | Styles guided-tour popovers and disables backdrop/highlight animation artifacts. |
| `_versioning.scss` | Styles version switch controls and version table break rows. |

## Notes

Component files should use semantic colors through `abstracts/color-functions` and shared unit helpers through `abstracts/utilities`.

Keep component selectors scoped to the feature they support.
If a selector is reused across unrelated parts of the site, move the shared piece to `base/` or `layout/` instead of coupling components together.
