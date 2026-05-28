# Layout Styles

This folder contains page structure, navigation, and footer styles.

## Files

| File | Purpose |
| --- | --- |
| `_layout.scss` | Defines document-level layout, common page utilities, button treatments, image sizing, and responsive page structure. |
| `_nav.scss` | Defines top navigation, dropdowns, side navigation, mobile navigation behavior, and navigation icon styling. |
| `_footer.scss` | Defines footer layout, footer links, responsive footer behavior, and print hiding. |

## Notes

Layout files may depend on `base/` placeholders and `abstracts/` helpers.
Keep layout rules focused on structural page behavior and shared chrome.

When adding styles for a specific feature such as search, matrix tables, tours, or version controls, prefer `components/`.
