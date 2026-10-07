# Restaurace ASIA — NÂM visual recreation

Reference observed in a real Chromium browser, desktop 1440 px and mobile iPhone 13 / 390 px, 7 October 2026. Screenshots: research/nam-top-1440.png, nam-view-1440-1…8.png, nam-mobile-0…6.png. Reference source, scripts, fonts and images are not reused.

## Visual system observed
- Desktop content width approximately 1024 px at 1440; left edge approximately 208 px.
- Tall header: two navigation groups flank the central thin wordmark. Orange, underlined text links; no pill buttons.
- Hero approximately 800 px from page top; centered two-line display heading about 64 px, surrounded by overlapping circular and burst badges. No background photograph or overlay.
- Introduction: dark green; large paragraph approximately 40 px left, photograph approximately 470 × 700 px right; badges overlap the image. Mobile changes order to image then text.
- Menu: one pale surface, centered small section label, four widely spaced plain text rows. Dish name/number and price share a line; descriptions italic. Full-menu underlined link at the bottom.
- Interior: dark green; centered large short paragraph, underlined gallery link, edge-to-edge horizontal photo strip with mixed portrait/landscape widths.
- Social: centered heading/link then two food images offset vertically, with badges.
- Contact: narrow outlined centered box overlaps photographs and badges. Address, map, opening hours, telephone, email and social links are centered.
- Footer: same green, simple social links and copyright; substantial breathing room.
- Reference dominant green approximately #082e2c, pale text/surface #dad7de, coral #ff624d, orange #f39710, muted olive badge. For ASIA the pale surface becomes warmer cream; photos contribute wood and food colours.
- Type has a flared, humanist appearance; approximate sizes 64 hero, 40 introduction/contact title, 22 menu/link, 18 section labels. The first root version used open-licensed Arsenal and a thin ASIA wordmark. The current revision replaces these with Bricolage Grotesque and Manrope; Czech glyph coverage is verified.
- Mobile: hamburger; left-aligned hero; decorative elements simplified; large full-width food image before introduction; single-column menu; gallery swipes horizontally; contact stacks cleanly.

## Current revision: art direction and content mapping
The user rejected the previous result as visually dry and lacking artistry. This revision keeps the green/cream family, clear menu, restaurant photography and overall content order, while replacing the scattered badges and repetitive green surfaces with a more coherent editorial composition. It is a deliberate revision of the earlier reference recreation.

1. Compact green header, bold ASIA wordmark, flanking links and telephone CTA.
2. Large left-aligned Bricolage heading and real fresh-rolls photograph on the right. Its arch refers to the restaurant's vaulted interior. On mobile the photo follows the short introduction and remains visible in the initial viewport.
3. Coral typographic ribbon, then off-white introduction with actual crispy-duck photography in a circular crop. No invented history.
4. Pale-sage menu excerpt with actual #4, #13, #17 and #37, real prices, thin rules and full read-only menu link.
5. Deep-green restaurant statement and large actual interior photos in a horizontal strip; accessible gallery dialog.
6. Off-white food spread with offset photos, large expressive type, supplied restaurant reel and Facebook.
7. Warm accommodation surface, genuine room photo marked 2023 and telephone enquiry. No invented rates or facilities.
8. Off-white contact with facade photo and openly arranged hours, phone, email, route and Facebook.
9. Deep-green footer with oversized ASIA identity and simple links.

The primary palette is forest #163e32, warm paper #f5f1e6, sage #e5eadb, wood #e6d9c4, coral #df7657 and rust #a7432c. Food supplies most of the natural colour. Bricolage Grotesque and Manrope use local files and included OFL licences. Original SVG bowl/herb artwork is written from scratch; reference assets and source code are not copied.

## Source precedence
Word: daily 10:30–21:00, +420 770 646 639, hongminh3882@gmail.com, approximately 55 seats. Current menu JSON retains all extracted dishes and variants; cropped prices stay unknown. Assets are the restaurant's local photographs and previously verified public Facebook assets. Full scan set includes the locally supplied final page #35–38. Existing image and content review files remain valid.

## Delivery
New static source at repository root: index.html, menu.html, styles.css, app.js, assets/, fonts/, data/. All internal resource paths relative, including project-path GitHub Pages. No build step, backend or Site hosting dependency. Original website/ retained as prior version.
