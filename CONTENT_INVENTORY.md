# Restaurace ASIA — content inventory / design decisions
Reviewed 2026-10-06, before interface implementation.

## Entire initial folder
- `Tài liệu không có tiêu đề.docx`: read all paragraphs and all three hyperlinks; no embedded images. Restaurant name, Czech UI, Česká 76, Volary, +420 770 646 639, hongminh3882@gmail.com, approximately 55 seats, daily 10:30–21:00. White/green direction. Accommodation service.
- `6f757eb6c26e69bc8378a68edc13a996308f7571.jpg`: exterior landscape, teal green sign, pale ochre facade, historical opening hours.
- `dc587478fd51df1d8681820c356affd6fbe3e7ac.jpg`: alternate exterior composition.
- `da935abf34db1cc5c919e10f26255faba29fd629.jpg`: warm wood tables/chairs, white vaulted ceiling, red napkins, restaurant event setup.
- `c8c81d31e9187942fb8cdd5455567489d8d910b0.jpg`: missing final menu page, numbered dishes 35–38 and exact variants/prices.

## Source discovery
All three supplied URLs opened. Web reader throttled; public Chromium access succeeded without authentication. Menu share resolves to post 1548818203605095, dated July 15, 2026. Captured all 9 album photographs (two covers and seven menu pages), plus local supplemental page. Menu: 38 numbered dishes, 7 sides, 68 protein variants, 2 packaging prices, 8 actual categories. No current drink menu supplied. Facebook gallery inspected as three contact sheets (82 thumbnails). Only relevant food, empty interiors, and accommodation images selected; guest portraits, birthday cakes, unrelated personal material excluded.

Verified restaurant food photos:
- photo 1013354267151494: caption identifies fried rice noodles with pork and vegetables, July 29, 2024. Maps to #17 pork only. Current price from 2026 menu: 175 CZK; historical caption price 145 excluded.
- photo 1013302247156696: crispy duck with rice, sauce and salad, July 28, 2024. General food photography only; current #22 describes vegetables, price cropped. Historical 200 CZK excluded.
- photo 817500800070176: beef/vegetable/peanut food photo, no identifying caption; editorial gallery only, no menu mapping.
- reel 1451673733369815: caption explicitly names fresh spring rolls. Poster maps to #4, but pictured plating/quantity may differ from the current 2-piece serving.

Accommodation source post 1458449992641917: clean, comfortable pension, rest/work travel. Its photographed notice states a room for up to 4 people; per person 750 CZK first night, 650 second night, 550 from third night; morning soup included; phone 720 368 150 and 770 646 639. Old room images (June 2023) are genuine photos on restaurant account, retained with date disclosed. Availability and current furnishing should be confirmed. No invented rooms, rating, parking, breakfast, or booking backend.

## References (specific contributions only)
- https://www.tamarindtree.cz/ — short approachable Czech content and direct contacts.
- https://www.siarestaurant.cz/ — direct Menu navigation; store interface deliberately not copied.
Other reference domains could not be read; no design/content derived from them.

## Visual system
Thesis: a bright local Vietnamese/Asian table in Volary, refreshed with confident shop-sign typography, real food, wood warmth and vaulted photo crops.
Palette: warm white #f7f7f0; deep blue-green #174a3d (sign inspired); pale natural green #e4eacb; warm wood #e9dfce; terracotta #af492f (napkins/menu). No gradients, stock imagery, synthetic food, heavy wood textures, shadow cards or luxury type.
Typography: Barlow Condensed 600/700 display + Manrope 400/500/600/700 body. All Czech glyphs tested from downloaded font cmap; local font hosting.
Rhythm: asymmetric identity/food hero → warm white welcome → pale green food discovery → light menu preview → full-bleed real interior → deep green story → warm accommodation with real room photo → light editorial gallery → green/white contacts → deep green footer.
Compositions: oversized identity with offset photography; two unequal food panels; separator-based image/text menu rows; full-width photo; typographic dark story; warm hospitality split; horizontal/editorial gallery; address beside facade.
Mobile: separate expandable navigation and bottom phone CTA, swipe category tabs, visible prices, compact image/meal rows. QA widths 375/390/430/768/1440/1920.

## Current root implementation — October 7
The user superseded the original independent design direction with a close visual recreation of https://www.namviet.cz/, while requesting a basic website with no detailed dish selection and root index.html for GitHub Pages. See DESIGN_REFERENCE.md for the observed desktop/mobile reference and mapping. New code is in the workspace root; the old website/ directory is retained. Read-only menu: 45 entries, 8 categories, 68 variant price entries. Original eight-page menu PDF includes the supplied final page. Fresh drawn ASIA wordmark; open-licensed Arsenal fonts, locally hosted and Czech glyph coverage checked.
