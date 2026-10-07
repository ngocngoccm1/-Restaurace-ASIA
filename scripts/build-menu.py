"""Regenerate static menu HTML from data/menu.json. No build is needed to host."""
import json
from pathlib import Path
from html import escape as e
root=Path(__file__).resolve().parent.parent
data=json.loads((root/'data/menu.json').read_text(encoding='utf-8'))
items={i['id']:i for i in data['items']}
def price(value):return 'Cena na dotaz' if value is None else f'{value} Kč'
def allergies(values):return f' · Alergeny: {", ".join(map(str,values))}' if values else ''
def heading(i):return f'{i["number"]}. {i["nameCs"]}' if i['number'] else i['nameCs']
preview=[]
for id in ['4','13','17','37']:
 i=items[id];p=i['price'];title=heading(i);note=f'{i["nameVi"]} · {i["portion"]}{allergies(i["allergens"])}'
 if id=='13':p=i['variants'][0]['price'];note=f'Kuřecí nebo hovězí maso · {i["portion"]}'
 if id=='17':p=next(v['price'] for v in i['variants'] if v['nameCs']=='Vepřové maso');note=f'S vepřovým masem · {i["portion"]}{allergies(i["allergens"])}'
 if id=='37':title='37. Bún chả';note=f'Grilované vepřové maso s rýžovými nudlemi · {i["portion"]}'
 badge='<span class="dish-portion">2 ks</span>' if id=='4' else ''
 preview.append(f'<article class="featured-dish"><div class="dish-heading"><h3>{e(title)}{badge}</h3><span class="dish-price">{price(p)}</span></div><p class="dish-note">{e(note)}</p></article>')
path=root/'index.html';s=path.read_text(encoding='utf-8');a='<!-- MENU_PREVIEW_START -->';b='<!-- MENU_PREVIEW_END -->';s=s.split(a)[0]+a+'\n<div class="featured-menu">'+''.join(preview)+'</div>\n'+b+s.split(b)[1];path.write_text(s,encoding='utf-8')
header=s[s.index('  <header'):s.index('  <main')].replace('href="#','href="./index.html#').replace('href="./menu.html"','href="./menu.html" aria-current="page"')
footer=s[s.index('  <footer'):s.index('  <dialog')].replace('href="#','href="./index.html#')
nav=''.join(f'<a href="#menu-{c["id"]}">{e(c["nameCs"])}</a>' for c in data['categories'])
sections=[]
for c in data['categories']:
 rows=[]
 for i in data['items']:
  if i['category']!=c['id']:continue
  variants=''
  if i['variants']:
   variants='<ul class="variant-list">'+''.join(f'<li><span>{e(v["nameCs"])}{e(allergies(v["allergens"]))}</span><span class="variant-price">{price(v["price"])}</span></li>' for v in i['variants'])+'</ul>'
  value='' if variants else f'<span class="dish-price">{price(i["price"])}</span>'
  rows.append(f'<article class="document-dish" data-menu-id="{i["id"]}"><div class="dish-heading"><h3>{e(heading(i))}</h3>{value}</div><p class="dish-meta">{e(i["portion"]+allergies(i["allergens"]))}</p>{variants}</article>')
 photo=''
 if c['id']=='starters':photo='<figure class="document-photo"><img src="./assets/fresh-rolls.webp" alt="Čerstvé jarní závitky z videa restaurace" width="720" height="1280" loading="lazy"><figcaption>Čerstvé závitky u nás v ASIA.<small>Fotografie z videa restaurace; způsob servírování se může lišit.</small></figcaption></figure>'
 if c['id']=='main':photo='<figure class="document-photo"><img src="./assets/rice-noodles.webp" alt="Smažené rýžové nudle s vepřovým masem a zeleninou" width="1800" height="1800" loading="lazy"><figcaption>17. Smažené rýžové nudle<small>Na fotografii varianta s vepřovým masem.</small></figcaption></figure>'
 sections.append(f'<section class="menu-category" id="menu-{c["id"]}" aria-labelledby="heading-{c["id"]}"><h2 id="heading-{c["id"]}">{e(c["nameCs"])}</h2>'+''.join(rows)+photo+'</section>')
pack=' · '.join(f'{e(x["nameCs"])} {price(x["price"])}' for x in data['packaging'])
html=f'''<!doctype html>
<html lang="cs" class="menu-route"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="theme-color" content="#082e2c"><title>Menu · Restaurace ASIA, Volary</title><meta name="description" content="Kompletní jídelní lístek Restaurace ASIA: polévky, závitky, vietnamská a asijská jídla, přílohy a dezerty. Česká 76, Volary."><link rel="icon" href="./assets/favicon.svg" type="image/svg+xml"><link rel="preload" href="./fonts/Arsenal-Regular.woff2" as="font" type="font/woff2" crossorigin><link rel="stylesheet" href="./styles.css"><script src="./app.js" defer></script></head>
<body class="menu-page"><a class="skip-link" href="#main">Přejít k obsahu</a>{header}<main id="main" class="menu-document"><div class="menu-document-header frame"><p class="eyebrow">Restaurace ASIA · Volary</p><h1>Jídelní lístek</h1><p>Asijská a vietnamská kuchyně. Všechny ceny v Kč.</p><div class="document-links"><a class="text-link" href="./assets/menu-restaurace-asia.pdf" target="_blank" rel="noopener">Původní jídelní lístek (PDF) ↗</a><a class="text-link" href="tel:+420770646639">Objednat telefonicky ↗</a></div></div><nav class="menu-category-nav" aria-label="Kategorie jídelního lístku">{nav}</nav><div class="menu-paper"><div class="frame">{''.join(sections)}<div class="menu-footnotes"><p>{pack}</p><p>Alergeny jsou uvedeny podle jídelního lístku restaurace. S dotazy na alergeny se prosím obraťte na obsluhu.</p><p>Ceny jídel č. 21 a 22 ověřte telefonicky.</p><p><a href="./assets/menu-restaurace-asia.pdf" target="_blank" rel="noopener">Prohlédnout původní menu včetně poslední stránky ↗</a></p></div></div></div><div class="menu-callout frame"><h2>Máte chuť? Zavolejte nám.</h2><p>Otevřeno každý den 10:30–21:00 · Česká 76, Volary</p><a class="text-link" href="tel:+420770646639">+420 770 646 639 ↗</a></div></main>{footer}</body></html>'''
(root/'menu.html').write_text(html,encoding='utf-8')
print(f'Generated menu: {len(data["items"])} dishes, {len(data["categories"])} categories; 4 homepage excerpts.')
