# Restaurace ASIA — visual redesign QA

Revision: 7 October 2026. Static website in the workspace root, ready for GitHub Pages. The former website/ implementation and the previous root design are retained.

## Visual review
- Reviewed the homepage vertically and detailed desktop/mobile views of the hero, menu excerpt, social photography, accommodation and contact.
- Screenshots and measured results: research/art-qa/. Results: results.json.
- Composition: large expressive type and arched real-food photograph, off-white introduction with circular dish photography, sage menu rows, deep-green restaurant and horizontal gallery, offset food spread, warm accommodation, open contact layout and oversized footer wordmark.
- A small original bowl seal and herb line drawing replace the earlier collection of unrelated badges. No stock or generated restaurant photographs.
- Bricolage Grotesque display font and Manrope body font are hosted locally. Czech lowercase and uppercase diacritics checked in the source fonts; browser rendering checked.

## Browser checks — passed
Both index.html and menu.html at 375, 390, 430, 768, 1440 and 1920 px:
- HTTP 200; no uncaught JavaScript errors.
- Document scrollWidth equals viewport width; no unintended horizontal overflow.
- All restaurant images, including lazy gallery images, load.
- All 45 menu entries appear at every tested width.
- Prices and category navigation remain legible on mobile.

Interaction checks:
- Mobile navigation opens and closes after selecting an anchor; Escape and keyboard focus handling work.
- Gallery dialog opens; arrow keys, next photo and Escape work.
- Clicking the video inserts the correct restaurant Facebook reel with autoplay=false. Closing removes the iframe; a direct Facebook link remains available.
- Menu categories use unique anchor IDs and sticky horizontally scrollable navigation. The menu is read-only.
- HTML anchor targets and duplicate IDs checked in both pages.

## GitHub Pages
All website paths are relative. A parent-directory server simulates a repository subpath; both pages and their referenced local resources/links load, including the original menu PDF. The ZIP has index.html at its root; no build or backend is required.

## Content checks
- 45 entries: 38 numbered dishes + 7 sides; 68 variant/price rows; 8 source categories; 2 packaging charges.
- Menu PDF includes all 8 supplied pages. Cropped prices for #21/#22 remain unknown rather than invented.
- Word supplies daily 10:30–21:00, +420 770 646 639, email and approximately 55 seats.
- Telephone ordering; no cart, dish selectors, checkout or payment claims.
- Accommodation uses the actual room photo marked 2023, the supplied Facebook post and telephone contact.

## Limits
Facebook may restrict its embedded player; the direct reel link is available. CONTENT_REVIEW.md records owner-confirmation items. The tested static files are prepared for branch-based GitHub Pages deployment from the repository root.
