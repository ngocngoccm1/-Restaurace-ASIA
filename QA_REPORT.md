# Restaurace ASIA — root website QA

Revision: 7 October 2026. Delivery: static GitHub Pages files in workspace root. The former website/ implementation is retained as a prior version.

## Reference and visual review
- NÂM homepage observed in Chromium at desktop 1440 px and a real mobile browser configuration (iPhone 13, 390 px).
- Fresh code, drawn ASIA identity and ASIA restaurant photographs. No NÂM source, photographs, logo, menu or business data reused.
- Full homepage screenshots reviewed vertically, plus close views of the hero, introduction, cream menu and warm accommodation block.
- Final screenshots: research/root-qa/index-{width}.png and menu-{width}.png.
- Compositions: typographic badge hero, text/tall food photo, plain restaurant menu rows, full-width horizontal photography, offset food collage, warm accommodation feature, outlined contact panel overlapping photographs.

## Browser checks — passed
Both index.html and menu.html at **375, 390, 430, 768, 1440 and 1920 px**:
- HTTP 200, no uncaught JavaScript errors.
- Document scrollWidth equals viewport width; no unintended overflow.
- Visible images load; horizontal-gallery images also verified. Mobile-hidden secondary contact photograph does not load unnecessarily.
- Locally hosted Arsenal renders Czech characters. All four source font files checked for ě š č ř ž ý á í é ů ú ď ť ň and uppercase equivalents before WOFF2 conversion.
- All 45 menu entries displayed in every menu viewport.

Interaction checks:
- Mobile menu opens, closes after choosing an anchor, supports Escape and keyboard focus cycling.
- Horizontal gallery opens an accessible native dialog; next photo, arrow keys and Escape work.
- Video activation inserts the supplied restaurant Facebook reel iframe, with autoplay=false. Closing removes the iframe. A direct Facebook link is always available.
- Menu category links tested on 1440 and 390 px: soups, main dishes and desserts jump below the sticky navigation. Menu category anchors use unique IDs.
- Desktop navigation spacing refined against the reference; mobile video button overlap removed; contact badge kept inside the viewport.

## GitHub Pages checks — passed
Served from /Restaurace%20ASIA/ under a parent-directory server to simulate a project URL. Both pages and all referenced local resources/links returned HTTP 200, including the menu PDF. CSS, JavaScript, SVG, images, fonts and document links use relative paths.

## Content checks
- 45 entries: 38 numbered dishes + 7 sides; 68 protein/option price rows; 8 actual categories; 2 packaging charges.
- Original menu PDF contains all 8 pages, including the separately supplied final page.
- Names, portions, prices and declared allergens come from data/menu.json. No invented prices for cropped items #21/#22.
- Word remains authoritative for daily 10:30–21:00, phone +420 770 646 639, email and approximately 55 seats.
- Read-only menu, telephone ordering; no cart, detailed dish selection, checkout or invented payment backend.
- Accommodation: factual short introduction, actual room photograph marked 2023, phone and supplied Facebook post.

## Practical limits
Facebook can restrict its embedded player or require login; the direct reel link remains available. Owner-confirmation items remain in CONTENT_REVIEW.md. The website is ready for GitHub Pages; no GitHub repository/remote was supplied, so no GitHub publication was performed.
