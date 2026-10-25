# Website update QA — 25 October 2026

## Completed update
- Six supplied apartment photographs and original 10.77-second portrait MP4 are local assets. Photo viewer navigates only within the six apartment photos when opened from accommodation.
- Apartment: 40 m², one bedroom with four beds, combined living room/kitchen, shared bathroom and WC, stove, microwave, breakfast included. Room rates: 750 / 650 / 550 Kč per person/night, with telephone reservations.
- All 45 menu entries and four homepage excerpts have adjacent dish images. Two restaurant images are retained; 43 individually generated AI illustrations are clearly labeled. Pictured protein variants are captioned.
- Source menu prices, portions, allergens and all variant prices are unchanged. Unreadable prices remain “Cena na dotaz”.
- Supplied allergen scan is linked and transcribed in an expandable list.

## Passed browser checks
Both homepage and menu at 320, 375, 390, 430, 768, 1024, 1440 and 1920 px:
- HTTP 200, no uncaught JS errors or local resource failures.
- No document horizontal overflow; all local images load.
- All 45 menu items have images. Pho image appears beside its title at every width.
- Menu category navigation and allergen disclosure work.

Interactions at 390 px: mobile navigation, accommodation anchor, six-photo viewer, next photograph, Escape close and native MP4 playback passed. Actual video dimensions: 720 × 1280. The final portrait video layout was additionally checked at 320, 390, 768 and 1440 px, including playback and no horizontal overflow.

Screenshots and measurements: research/update-qa/. Food image subjects reviewed via contact sheet; room, menu and final video layout visually inspected on desktop and phone.

## GitHub Pages checks
- index.html remains in repository root; .nojekyll retained.
- All local resources, internal anchors and duplicate IDs validated.
- Parent-directory server simulated /Restaurace%20ASIA/ repository subpath: homepage, menu navigation and MP4 request passed.
- ZIP refreshed with index.html at ZIP root and all current website assets. No build/backend required.

This is a local project update, prepared for the user's GitHub Pages deployment.
