# Menu image review

Reviewed restaurant folder, current menu album, 82 public Facebook photo thumbnails and the restaurant food reel. No stock or generated dish photographs are used.

## Verified mapping
- #4 Čerstvé jarní závitky: still/poster from restaurant reel https://www.facebook.com/reel/1451673733369815/; caption explicitly identifies fresh rolls. Plating may differ from the current 2-piece serving.
- #17 Smažené rýžové nudle, Vepřové maso only: https://www.facebook.com/photo/?fbid=1013354267151494. Caption identifies fried rice noodles with pork and vegetables. Other proteins display fallback, not this pork photograph.

## Editorial photographs that are not mapped
- Crispy duck with rice, sauce and salad: caption identified, but current #22 / #29 lists vegetables and different serving size. Used in hero/gallery only.
- Beef/vegetable/peanut photo: no exact dish caption; not mapped to Bun Nam Bo or chicken salad.

## Need exact dish photos
Each of the following has a neutral numbered image slot in the UI. Add a photo only after confirming the dish and any protein/portion match. Set `image` in `dist/data/menu.json`; set `variants[n].image` for a specific protein. `imageVariant` restricts shared images to their identified variant.

| No. | Czech name | Variants requiring photography |
|---|---|---|
| 1 | Polévka se skleněnými nudlemi a kuřecím masem | Exact dish / serving |
| 2 | Pekingská polévka | Exact dish / serving |
| 3 | Zeleninová polévka | Exact dish / serving |
| 5 | Smažené závitky | Exact dish / serving |
| 6 | Mini veganské závitky | Exact dish / serving |
| 7 | Smažené krevety obalované kokosovou strouhankou | Exact dish / serving |
| 8 | Smažené obalované krevety | Exact dish / serving |
| 9 | Krevetové knedlíčky | Exact dish / serving |
| 10 | Hamburger se smaženým sýrem | Exact dish / serving |
| 11 | Míchaný salát | Exact dish / serving |
| 12 | Kuřecí salát | Exact dish / serving |
| 13 | Nudlová polévka Pho / Bun | Kuřecí maso, Hovězí maso |
| 14 | Bun Nam Bo | Hovězí maso, Tofu, Smažené závitky |
| 15 | Smažené nudle | Kuřecí maso, Vepřové maso, Hovězí maso, Krevety, Kachní maso, Tofu |
| 16 | Smažená rýže | Kuřecí maso, Vepřové maso, Hovězí maso, Krevety, Kachní maso, Tofu |
| 18 | Smažené skleněné nudle | Kuřecí maso, Vepřové maso, Hovězí maso, Krevety, Kachní maso, Tofu |
| 19 | Kung Pao s rýží | Kuřecí maso, Vepřové maso, Hovězí maso, Krevety, Tofu |
| 20 | Restovaná zelenina s masem a rýží | Kuřecí maso, Vepřové maso, Hovězí maso, Krevety |
| 21 | Pikantní se zeleninou a rýží | Kuřecí maso, Vepřové maso, Hovězí maso, Krevety, Kachní maso, Tofu |
| 22 | Křupavá kachna se zeleninou a rýží | Exact dish / serving |
| 23 | Kari se zeleninou a rýží | Kuřecí maso, Vepřové maso, Hovězí maso, Krevety, Kachní maso, Tofu |
| 24 | Kuřecí řízek s hranolkami | Exact dish / serving |
| 25 | Smažený sýr s hranolkami | Exact dish / serving |
| 26 | Voňavé a křehké kuře s rýží | Exact dish / serving |
| 27 | Smažené kuřecí kousky s hranolkami | Exact dish / serving |
| 28 | 3 druhy masa se zeleninou a rýží | Exact dish / serving |
| 29 | Křupavá kachna se zeleninou a rýží | Exact dish / serving |
| 30 | Krevety s tofu, zeleninou a rýží | Exact dish / serving |
| 31 | Restovaná zelenina s rýží | Exact dish / serving |
| 32 | Restovaná zelenina s tofu a rýží | Exact dish / serving |
| 33 | Smažený banán | Exact dish / serving |
| 34 | Krevetové lupínky | Exact dish / serving |
| 35 | Sladkokyselá omáčka se zeleninou a rýží | Kuřecí maso, Vepřové maso, Hovězí maso, Krevety, Tofu, Smažené kuřecí kousky |
| 36 | Houby s rýží | Kuřecí maso, Vepřové maso, Hovězí maso, Krevety, Kachní maso, Tofu |
| 37 | Bún chả – grilované vepřové maso s rýžovými nudlemi | Exact dish / serving |
| 38 | Po thajsku se zeleninou a rýží | Kuřecí maso, Vepřové maso, Hovězí maso, Krevety, Kachní maso, Tofu |
| — | Bílá rýže | Exact dish / serving |
| — | Hranolky | Exact dish / serving |
| — | Krokety | Exact dish / serving |
| — | Nudle | Exact dish / serving |
| — | Kečup / Tatarka | Exact dish / serving |
| — | Chili | Exact dish / serving |
| — | Hoisin omáčka | Exact dish / serving |

#17 also needs: Kuřecí maso, Hovězí maso, Krevety, Kachní maso, Tofu.

Total: 43 of 45 menu entries have no verified exact photograph; #17 has only its pork variant covered. This is an asset limitation, not an invented completed photo catalog.

## Current basic website
The October 7 root version uses a read-only menu instead of individual product-style image cards. Missing exact dish photographs are therefore not filled by repeated square placeholders or unrelated images. The list above remains the inventory for any future photography update. Two verified menu images (#4 and the pork variant of #17) are shown as editorial photographs in the complete menu.
