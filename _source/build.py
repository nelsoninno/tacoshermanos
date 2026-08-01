#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Static page generator for tacoshermanos.com

Why a generator: the site is fully bilingual (Spanish at /, English at /en/) and
every page shares a header, footer, SEO block and JSON-LD graph. Generating from
one source guarantees the two languages never drift apart.

Run from the site root:  python3 _source/build.py
Nothing in _source/ ships. Only the generated HTML does.
"""
import os, json, sys, pathlib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from menu_data import (ALMUERZO, MARGARITAS, FROZENS, CERVEZAS, BEBIDAS_MAIN,
                       DESAYUNOS, DESAYUNO_ESPECIALES, DESAYUNO_BEBIDAS,
                       DESAYUNOS_INCLUYE_ES, DESAYUNOS_INCLUYE_EN, photo)

ROOT = pathlib.Path(__file__).resolve().parent.parent
DOMAIN = "tacoshermanos.com"
BASE = f"https://{DOMAIN}"
TODAY = "2026-07-31"
SKILL = "/root/.claude/skills/website-build/assets/eky-credit.svg"

PAGES = {
    "home":      ("index.html",            "en/index.html"),
    "historia":  ("nuestra-historia.html", "en/our-story.html"),
    "menu":      ("menu.html",             "en/menu.html"),
    "desayunos": ("menu-desayunos.html",   "en/menu-breakfast.html"),
    "almuerzo":  ("menu-almuerzo.html",    "en/menu-lunch.html"),
    "info":      ("sucursales.html",       "en/locations.html"),
    "fundacion": ("fundacion.html",        "en/foundation.html"),
    "regala":    ("regala-tacos.html",     "en/gift-tacos.html"),
    "empleados": ("empleados.html",        "en/team.html"),
}
NAV = ["home", "historia", "menu", "info", "regala", "fundacion"]
NAV_LABEL = {
    "es": {"home":"Inicio","historia":"Nuestra Historia","menu":"Menú",
           "regala":"Regala Tacos","fundacion":"La Fundación","info":"Sucursales","empleados":"Equipo"},
    "en": {"home":"Home","historia":"Our Story","menu":"Menu",
           "regala":"Gift Tacos","fundacion":"The Foundation","info":"Locations","empleados":"Team"},
}

# Hours transcribed from the client's own "Horarios Sucursales" artwork,
# received 31 July 2026. La Gran Vía changes once breakfast launches.
H_STD  = [("Lunes a jueves","12:00 md a 3:00 pm · 6:00 pm a 9:00 pm"),
          ("Viernes","12:00 md a 3:00 pm · 6:00 pm a 10:00 pm"),
          ("Sábado","12:00 md a 10:00 pm"),
          ("Domingo","12:00 md a 9:00 pm")]
H_GV   = [("Lunes a jueves","12:00 md a 3:00 pm · 6:00 pm a 9:30 pm"),
          ("Viernes","12:00 md a 3:00 pm · 6:00 pm a 10:30 pm"),
          ("Sábado","12:00 md a 10:30 pm"),
          ("Domingo","12:00 md a 9:30 pm")]
H_CORR = [("Lunes a jueves","12:00 md a 9:00 pm"),
          ("Viernes y sábado","12:00 md a 10:00 pm"),
          ("Domingo","12:00 md a 9:00 pm")]
H_STD_EN  = [("Monday to Thursday","12:00 pm to 3:00 pm · 6:00 pm to 9:00 pm"),
             ("Friday","12:00 pm to 3:00 pm · 6:00 pm to 10:00 pm"),
             ("Saturday","12:00 pm to 10:00 pm"),
             ("Sunday","12:00 pm to 9:00 pm")]
H_GV_EN   = [("Monday to Thursday","12:00 pm to 3:00 pm · 6:00 pm to 9:30 pm"),
             ("Friday","12:00 pm to 3:00 pm · 6:00 pm to 10:30 pm"),
             ("Saturday","12:00 pm to 10:30 pm"),
             ("Sunday","12:00 pm to 9:30 pm")]
H_CORR_EN = [("Monday to Thursday","12:00 pm to 9:00 pm"),
             ("Friday and Saturday","12:00 pm to 10:00 pm"),
             ("Sunday","12:00 pm to 9:00 pm")]

# name, opened_es, opened_en, city, place, photo slug, video slug or None, hours es, hours en
CASAS = [
    ("San Benito","21 de mayo de 2021","May 21, 2021","San Salvador",
     "Calle Circunvalación #130, Colonia San Benito","casa-san-benito",None,H_STD,H_STD_EN),
    ("La Gran Vía","7 de enero de 2022","January 7, 2022","Antiguo Cuscatlán",
     "Centro Comercial La Gran Vía","fachada-de-noche","sucursal-la-gran-via",H_GV,H_GV_EN),
    ("Paseo Venecia, Soyapango","30 de noviembre de 2022","November 30, 2022","Soyapango",
     "Paseo Venecia","salon-principal",None,H_STD,H_STD_EN),
    ("Las Ramblas, Santa Ana","14 de noviembre de 2023","November 14, 2023","Santa Ana",
     "Centro Comercial Las Ramblas","casa-iluminada-de-noche","apertura-santa-ana",H_STD,H_STD_EN),
    ("San Miguel","7 de octubre de 2024","October 7, 2024","San Miguel",
     "San Miguel","rotulo-interior","apertura-san-miguel",H_CORR,H_CORR_EN),
    ("Plaza Mundo, Usulután","26 de marzo de 2025","March 26, 2025","Usulután",
     "Plaza Mundo, Usulután","salon-lleno","apertura-usulutan",H_CORR,H_CORR_EN),
]

VOUCHERS = [
    ("10","Para una persona","For one person",
     "Un plato completo para alguien que querés que hoy coma rico.",
     "A full plate for someone you want to eat well today.",False),
    ("20","Para una pareja","For two",
     "Dos personas, una mesa y una tarde que no se les olvida.",
     "Two people, one table, and an afternoon they will not forget.",True),
    ("50","Para toda la familia","For the whole family",
     "La mesa llena. Como cuando estabas ahí para sentarte con ellos.",
     "The whole table full. Like when you were there to sit down with them.",False),
]

# --------------------------------------------------------------------------
def load(p):
    s = pathlib.Path(p).read_text(encoding="utf-8").strip()
    if s.startswith("<?xml"): s = s[s.index("?>")+2:].strip()
    return s

EKY = load(SKILL)
ISOTIPO = load(ROOT/"assets/images/logos/isotipo-tacos-hermanos-tacoshermanos.com.svg")
WORDMARK = load(ROOT/"assets/images/logos/wordmark-tacos-hermanos-tacoshermanos.com.svg")
BADGE_TAG = load(ROOT/"assets/images/logos/badge-tagline-tacos-hermanos-tacoshermanos.com.svg")

def cls(svg, c):
    return svg.replace("<svg ", f'<svg class="{c}" ', 1)

def badge_img(lang, c="crema", cls_="badge-mark reveal"):
    """The circular lockup as a plain <img>. Inlining it would add 57 KB per page."""
    p = f"assets/images/logos/badge-tagline-{c}-tacos-hermanos-{DOMAIN}.svg"
    alt = ("Tacos Hermanos, lo bonito se comparte, est. 2021" if lang == "es"
           else "Tacos Hermanos, beautiful things are meant to be shared, est. 2021")
    return f'<img class="{cls_}" src="{rel(lang, p)}" alt="{alt}" loading="lazy" width="703" height="341">' 

def pend(text, block=False):
    """Mark copy that still needs the client's own words or sign-off."""
    return f'<span class="pendiente{" pendiente--block" if block else ""}">{text}</span>'

import unicodedata
def casa_id(nombre):
    """Stable anchor for a branch, e.g. 'La Gran Vía' -> 'la-gran-via'."""
    txt = unicodedata.normalize("NFKD", nombre).encode("ascii", "ignore").decode()
    out = "".join(ch.lower() if ch.isalnum() else "-" for ch in txt)
    while "--" in out: out = out.replace("--", "-")
    return out.strip("-")

def rel(lang, p):  return p if lang == "es" else "../" + p
def href(lang, k):
    es_f, en_f = PAGES[k]
    return es_f if lang == "es" else en_f.split("/",1)[1]
def url_of(k, lang):
    es_f, en_f = PAGES[k]
    if lang == "es": return BASE + "/" + ("" if es_f == "index.html" else es_f)
    return BASE + "/" + ("en/" if en_f == "en/index.html" else en_f)

def img(lang, path, alt, priority=False, cls_=""):
    c = f' class="{cls_}"' if cls_ else ""
    extra = ' fetchpriority="high"' if priority else ' loading="lazy" decoding="async"'
    return f'<img src="{rel(lang,path)}" alt="{alt}"{c}{extra}>'

# --------------------------------------------------------------------------
def _ohs(spec):
    return [{"@type":"OpeningHoursSpecification","dayOfWeek":d,"opens":o,"closes":c}
            for d,o,c in spec]

# (days, opens, closes) per branch, from the client's Horarios artwork
LD_STD = [(["Monday","Tuesday","Wednesday","Thursday"],"12:00","15:00"),
          (["Monday","Tuesday","Wednesday","Thursday"],"18:00","21:00"),
          (["Friday"],"12:00","15:00"), (["Friday"],"18:00","22:00"),
          (["Saturday"],"12:00","22:00"), (["Sunday"],"12:00","21:00")]
LD_GV  = [(["Monday","Tuesday","Wednesday","Thursday"],"12:00","15:00"),
          (["Monday","Tuesday","Wednesday","Thursday"],"18:00","21:30"),
          (["Friday"],"12:00","15:00"), (["Friday"],"18:00","22:30"),
          (["Saturday"],"12:00","22:30"), (["Sunday"],"12:00","21:30")]
LD_CORR= [(["Monday","Tuesday","Wednesday","Thursday"],"12:00","21:00"),
          (["Friday","Saturday"],"12:00","22:00"), (["Sunday"],"12:00","21:00")]
LD_BY_BRANCH = {"San Benito":LD_STD,"La Gran Vía":LD_GV,"Paseo Venecia, Soyapango":LD_STD,
                "Las Ramblas, Santa Ana":LD_STD,"San Miguel":LD_CORR,"Plaza Mundo, Usulután":LD_CORR}

def graph_jsonld(lang, with_menu=False):
    hours = _ohs(LD_STD)
    org = {
        "@type":["Organization","Restaurant","LocalBusiness"], "@id":f"{BASE}/#org",
        "name":"Tacos Hermanos",
        "alternateName":["Tacos Hnos","Tacos Hermanos SV","Tacos Hermanos El Salvador"],
        "url":BASE+"/",
        "logo":f"{BASE}/assets/images/logos/wordmark-tacos-hermanos-{DOMAIN}.svg",
        "image":f"{BASE}/assets/images/social-share/social-share-tacos-hermanos-{DOMAIN}.jpg",
        "slogan":"Sin habernos conocido, ya somos hermanos",
        "description":("Cadena salvadoreña de tacos con seis casas en El Salvador. Tacos, burros, "
                       "tortas y desayunos para la familia salvadoreña, con un producto espectacular, "
                       "un servicio memorable y el mejor valor por su dinero. Fundada en 2021."
                       if lang=="es" else
                       "Salvadoran taco restaurant group with six houses across El Salvador. Tacos, "
                       "burritos, tortas and breakfast for the Salvadoran family, with a spectacular "
                       "product, memorable service and the best value for money. Founded in 2021."),
        "servesCuisine":["Mexican","Salvadoran","Tacos","Breakfast"],
        "priceRange":"$$", "currenciesAccepted":"USD",
        "areaServed":[{"@type":"Country","name":"El Salvador"}],
        "knowsLanguage":["es","en"],
        "knowsAbout":["tacos","quesabirrias","burros","desayunos","restaurantes en El Salvador",
                      "celebraciones familiares","cumpleaños"],
        "foundingDate":"2021-05-21",
        "numberOfEmployees":{"@type":"QuantitativeValue","minValue":100},
        "address":{"@type":"PostalAddress","addressCountry":"SV","addressRegion":"San Salvador",
                   "addressLocality":"San Salvador",
                   "streetAddress":"Calle Circunvalación #130, Colonia San Benito"},
        "openingHoursSpecification":hours,
        "acceptsReservations":"False",
        "sameAs":["https://www.instagram.com/tacoshermanossv"],
        "funder":{"@type":"NGO","name":"Somos Hermanos","foundingDate":"2021",
                  "url":"https://somoshermanos.ong",
                  "sameAs":["https://www.instagram.com/somoshermanossv"]},
        "hasMenu":{"@id":f"{BASE}/#menu"},
    }
    website = {"@type":"WebSite","@id":f"{BASE}/#website","url":BASE+"/",
               "name":"Tacos Hermanos","inLanguage":["es","en"],
               "publisher":{"@id":f"{BASE}/#org"}}
    menu = {"@type":"Menu","@id":f"{BASE}/#menu","name":"Menú Tacos Hermanos",
            "inLanguage":"es","url":url_of("menu","es"),
            "hasMenuSection":[
              {"@type":"MenuSection","name":sec["es"],
               "hasMenuItem":[{"@type":"MenuItem","name":i["n"],
                               "description":i["es"],
                               **({"offers":{"@type":"Offer","price":i["p"],"priceCurrency":"USD"}} if i["p"] else {})}
                              for blk in sec["blocks"] for i in blk["items"]]}
              for sec in ALMUERZO] +
              [{"@type":"MenuSection","name":"Desayunos",
                "hasMenuItem":[{"@type":"MenuItem","name":d["n"],"description":d["es"],
                                "offers":{"@type":"Offer","price":d["p"],"priceCurrency":"USD"}}
                               for d in DESAYUNOS]}]}
    branches = [{"@type":"Restaurant","@id":f"{BASE}/#casa-{i+1}",
                 "name":f"Tacos Hermanos {c[0]}","parentOrganization":{"@id":f"{BASE}/#org"},
                 "servesCuisine":["Mexican","Salvadoran"],"priceRange":"$$",
                 "acceptsReservations":"False","hasMenu":{"@id":f"{BASE}/#menu"},
                 "address":{"@type":"PostalAddress","addressCountry":"SV","addressLocality":c[3],
                            "streetAddress":c[4]},
                 "openingHoursSpecification":_ohs(LD_BY_BRANCH[c[0]])}
                for i, c in enumerate(CASAS)]
    nodes = [org, website] + ([menu] if with_menu else []) + branches
    g = {"@context":"https://schema.org","@graph":nodes}
    return '  <script type="application/ld+json">\n' + json.dumps(g, ensure_ascii=False, indent=2) + "\n  </script>\n"

def faq_jsonld(pairs):
    d = {"@context":"https://schema.org","@type":"FAQPage","@id":f"{BASE}/#faq",
         "mainEntity":[{"@type":"Question","name":q,
                        "acceptedAnswer":{"@type":"Answer","text":a}} for q,a in pairs]}
    return '  <script type="application/ld+json">\n' + json.dumps(d, ensure_ascii=False, indent=2) + "\n  </script>\n"

# --------------------------------------------------------------------------
def head(lang, key, title, desc, keywords, hero=None, extra="", with_menu=False, noindex=False):
    es_url, en_url = url_of(key,"es"), url_of(key,"en")
    canon = es_url if lang=="es" else en_url
    a = lambda p: rel(lang, p)
    share = f"{BASE}/assets/images/social-share/social-share-tacos-hermanos-{DOMAIN}.jpg"
    pre = f'\n  <link rel="preload" as="image" href="{a("assets/images/hero/"+hero)}" type="image/webp">' if hero else ""
    loc, alt = ("es_SV","en_US") if lang=="es" else ("en_US","es_SV")
    F = a("assets/fonts/outfit-latin-variable.woff2")
    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <meta name="keywords" content="{keywords}">

  <link rel="canonical" href="{canon}">
  <link rel="alternate" hreflang="es" href="{es_url}">
  <link rel="alternate" hreflang="es-SV" href="{es_url}">
  <link rel="alternate" hreflang="en" href="{en_url}">
  <link rel="alternate" hreflang="x-default" href="{es_url}">

  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:type" content="website">
  <meta property="og:url" content="{canon}">
  <meta property="og:image" content="{share}">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:image:alt" content="Tacos Hermanos, El Salvador">
  <meta property="og:site_name" content="Tacos Hermanos">
  <meta property="og:locale" content="{loc}">
  <meta property="og:locale:alternate" content="{alt}">

  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{title}">
  <meta name="twitter:description" content="{desc}">
  <meta name="twitter:image" content="{share}">

  <meta name="robots" content="{'noindex, nofollow' if noindex else 'index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1'}">
  <meta name="author" content="Tacos Hermanos">
  <meta name="theme-color" content="#2D8769">
  <meta name="geo.region" content="SV">
  <meta name="geo.placename" content="San Salvador">

  <link rel="icon" href="{a('favicon.ico')}" sizes="any">
  <link rel="icon" type="image/png" sizes="32x32" href="{a('favicon-32x32.png')}">
  <link rel="icon" type="image/png" sizes="16x16" href="{a('favicon-16x16.png')}">
  <link rel="apple-touch-icon" sizes="180x180" href="{a('apple-touch-icon.png')}">
  <link rel="manifest" href="{a('site.webmanifest')}">
  <link rel="alternate" type="text/plain" title="llms.txt" href="{BASE}/llms.txt">{pre}

  <link rel="preload" as="font" type="font/woff2" href="{F}" crossorigin>

  <link rel="stylesheet" href="{a('assets/css/tokens.css')}">
  <link rel="stylesheet" href="{a('assets/css/styles.css')}">
{graph_jsonld(lang, with_menu)}{extra}</head>
<body>
"""

def header(lang, current):
    items = []
    for k in NAV:
        cur = ' aria-current="page"' if k == current else ''
        items.append(f'<a href="{href(lang,k)}"{cur}>{NAV_LABEL[lang][k]}</a>')
    if lang == "es":
        other = PAGES[current][1].split("/",1)[1]
        sw = f'<span class="active">ES</span><span class="sep">/</span><a href="en/{other}" hreflang="en">EN</a>'
    else:
        sw = f'<a href="../{PAGES[current][0]}" hreflang="es">ES</a><span class="sep">/</span><span class="active">EN</span>'
    skip = "Ir al contenido" if lang=="es" else "Skip to content"
    navlbl = "Menú de navegación" if lang=="es" else "Navigation menu"
    return f"""<a class="sr-only" href="#main">{skip}</a>
<header class="site-header">
  <div class="wrap site-header__inner">
    <a class="brand" href="index.html" aria-label="Tacos Hermanos">
      {cls(ISOTIPO,"brand__mark")}
      {cls(WORDMARK,"brand__word")}
    </a>
    <button class="nav-toggle" aria-label="{navlbl}" aria-expanded="false"><span></span></button>
    <nav class="nav" aria-label="{'Principal' if lang=='es' else 'Main'}">
      {''.join(items)}
      <span class="lang">{sw}</span>
    </nav>
  </div>
</header>
<main id="main">
"""

def footer(lang, current):
    es = lang == "es"
    a = lambda p: rel(lang, p)
    nav_li = "".join(f'<li><a href="{href(lang,k)}">{NAV_LABEL[lang][k]}</a></li>' for k in NAV)
    casas_li = "".join(f"<li>{c[0]}</li>" for c in CASAS)
    if es:
        other = PAGES[current][1].split("/",1)[1]
        sw = f'<span class="active">ES</span><span class="sep">/</span><a href="en/{other}" hreflang="en">EN</a>'
    else:
        sw = f'<a href="../{PAGES[current][0]}" hreflang="es">ES</a><span class="sep">/</span><span class="active">EN</span>'
    credit = "Sitio web hecho con amor, por" if es else "Website made with love, by"
    aria = ("Sitio web hecho con amor por everybodyknowsyou.com" if es
            else "Website made with love by everybodyknowsyou.com")
    return f"""</main>
<footer class="site-footer">
  <div class="wrap">
    <div class="footer-grid">
      <div class="footer-col">
        <h4>{'Navegación' if es else 'Navigation'}</h4>
        <ul>{nav_li}</ul>
      </div>
      <div class="footer-col">
        <h4>{'Menú' if es else 'Menu'}</h4>
        <ul>
          <li><a href="{href(lang,'desayunos')}">{'Desayunos' if es else 'Breakfast'}</a></li>
          <li><a href="{href(lang,'almuerzo')}">{'Almuerzo y cena' if es else 'Lunch and dinner'}</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4>{'Nuestras casas' if es else 'Our houses'}</h4>
        <ul>{casas_li}</ul>
      </div>
      <div class="footer-col">
        <h4>{'Contacto' if es else 'Contact'}</h4>
        <ul>
          <li><a href="https://www.instagram.com/tacoshermanossv" rel="noopener" target="_blank">@tacoshermanossv</a></li>
          <li>{pend('Teléfono' if es else 'Phone')}</li>
          <li>{pend('Correo de business inquiries' if es else 'Business inquiries email')}</li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span>&copy; 2026 Tacos Hermanos. {'Todos los derechos reservados.' if es else 'All rights reserved.'}</span>
      <span class="lang">{sw}</span>
      <a class="eky-credit" href="https://everybodyknowsyou.com" target="_blank" rel="noopener" aria-label="{aria}">
        <span class="eky-credit__text">{credit}</span>
        {EKY}
      </a>
    </div>
  </div>
</footer>
<script src="{a('assets/js/main.js')}" defer></script>
</body>
</html>
"""

# --------------------------------------------------------------------------
# reusable sections
# --------------------------------------------------------------------------
def hero(lang, image, alt, eyebrow, h1, sub, ctas, aria=None, variant=""):
    lbl = f' aria-label="{aria}"' if aria else ""
    return f"""<section class="hero {variant}">
  <div class="hero__media">{img(lang,'assets/images/hero/'+image, alt, priority=True)}</div>
  <div class="wrap hero__inner">
    <span class="eyebrow">{eyebrow}</span>
    <h1{lbl}>{h1}</h1>
    <p class="hero__sub">{sub}</p>
    <div class="hero__cta">{''.join(ctas)}</div>
  </div>
</section>"""

def marquee(words):
    """Two identical groups, each repeated enough times to overflow any viewport,
    so the -50% slide loops seamlessly with no dead gap."""
    run = "".join(f"<span>{w}</span>" for w in words) * 3
    group = f'<div class="marquee__group">{run}</div>'
    return f'<div class="marquee" aria-hidden="true"><div class="marquee__track">{group}{group}</div></div>'

def faq_block(title, pairs):
    items = "".join(f'<div class="faq-item reveal"><h3>{q}</h3><p>{a}</p></div>' for q,a in pairs)
    return f"""<section class="section band-cream" aria-labelledby="faq-title">
  <div class="wrap narrow">
    <h2 id="faq-title" class="reveal mb-3">{title}</h2>
    {items}
  </div>
</section>"""

def cta_band(title, text, buttons):
    return f"""<section class="section section--tight cta-band">
  <div class="wrap narrow reveal">
    <h2>{title}</h2>
    <p class="mt-1">{text}</p>
    <div class="hero__cta mt-3" style="justify-content:center">{''.join(buttons)}</div>
  </div>
</section>"""

def dish_photos(lang, pairs):
    figs = "".join(
        f'<figure class="dish-photo reveal">{img(lang, photo(slug), cap + ", Tacos Hermanos")}'
        f'<figcaption>{cap}</figcaption></figure>' for slug, cap in pairs)
    return f'<div class="dish-photos">{figs}</div>'

def menu_block(lang, blk):
    """One photograph followed immediately by the dishes it actually shows.
    This is the layout agreed with Erika: no cutting dishes out of shared photos."""
    cap = blk.get(f"cap_{lang}") or ""
    names = ", ".join(i["n"] for i in blk.get("items", []))
    alt = (f"{names} de Tacos Hermanos" if lang == "es" else f"{names} at Tacos Hermanos")
    pic = img(lang, photo(blk["photo"]), alt, cls_="menu-block__img")
    if "drinks" in blk:
        body = drink_list(lang, blk["drinks"])
    else:
        body = dish_rows(lang, blk["items"])
    return f"""<div class="menu-block reveal">
      <figure class="menu-block__figure">{pic}<figcaption>{cap}</figcaption></figure>
      <div class="menu-block__items">{body}</div>
    </div>"""

def menu_blocks_pair(lang, blocks):
    """Two photo blocks side by side, kept side by side on desktop."""
    return f'<div class="menu-blocks menu-blocks--pair">{"".join(menu_block(lang, b) for b in blocks)}</div>'

def menu_blocks(lang, blocks):
    return f'<div class="menu-blocks">{"".join(menu_block(lang, b) for b in blocks)}</div>' 

def dish_rows(lang, items):
    out = []
    for i in items:
        price = f'<span class="dish__price">${i["p"]}</span>' if i.get("p") else '<span></span>'
        desc = i.get(lang, "")
        hint = i.get(f"hint_{lang}", "")
        h = f'<span class="dish__hint">{hint}</span>' if hint else ""
        d = f'<p class="dish__desc">{desc}{h}</p>' if (desc or hint) else ""
        gloss = i.get("gloss")
        name = i["n"]
        if lang == "en" and gloss:
            name += f'<span class="dish__gloss">{gloss}</span>'
        out.append(f'<div class="dish reveal"><span class="dish__name">{name}</span>{price}{d}</div>')
    return "".join(out)

def drink_list(lang, rows):
    out = []
    for es_n, en_n, p in rows:
        n = es_n if lang == "es" else en_n
        out.append(f'<div class="drink"><span class="drink__name">{n}</span>'
                   f'<span class="drink__dots"></span><span class="drink__price">${p}</span></div>')
    return f'<div class="drinks">{"".join(out)}</div>'

def menu_nav(lang, current):
    es = lang == "es"
    links = [("menu", "Todo el menú" if es else "Full menu"),
             ("desayunos", "Desayunos" if es else "Breakfast"),
             ("almuerzo", "Almuerzo y cena" if es else "Lunch and dinner")]
    out = []
    for k, lbl in links:
        cur = ' aria-current="page"' if k == current else ''
        out.append(f'<a href="{href(lang,k)}"{cur}>{lbl}</a>')
    return f'<nav class="menu-nav" aria-label="{"Menú" if es else "Menu"}">{"".join(out)}</nav>'

# --------------------------------------------------------------------------
# the animated remittance map (Alfonso's request: "como las remesas")
# --------------------------------------------------------------------------
MAP = json.loads((ROOT/"_source/map.json").read_text(encoding="utf-8"))
ARC = MAP["arc"]
AX, AY = MAP["a"]
BX, BY = MAP["b"]

def taco(extra=""):
    return f"""<g class="mapa__taco {extra}" style="offset-path:path('{ARC}');offset-rotate:0deg">
        <circle r="15" class="mapa__taco-halo"/>
        <path d="M-10,4 A10,10 0 0 1 10,4 Z" class="mapa__taco-shell"/>
        <path d="M-10,4 h20 a2,2 0 0 1 -2,2 h-16 a2,2 0 0 1 -2,-2 z" class="mapa__taco-tortilla"/>
        <circle cx="-4" cy="0" r="2.1" class="mapa__taco-fill"/>
        <circle cx="1" cy="-2" r="2.1" class="mapa__taco-fill2"/>
        <circle cx="5" cy="0" r="2.1" class="mapa__taco-fill"/>
      </g>"""

def mapa(lang, xl=False):
    """Real Mercator geography of North and Central America, projected offline from
    the world-atlas dataset. El Salvador is highlighted; a voucher flies the arc."""
    es = lang == "es"
    aria = ("Mapa animado: un voucher de Tacos Hermanos viaja desde Estados Unidos hasta El Salvador"
            if es else "Animated map: a Tacos Hermanos voucher travels from the United States to El Salvador")
    lands = "\n    ".join(MAP["paths"])
    return f"""<div class="mapa reveal{' mapa--xl' if xl else ''}">
  <svg viewBox="0 0 {MAP['w']} {MAP['h']}" role="img" aria-label="{aria}">
    {lands}
    <path d="{ARC}" class="mapa__arc"/>
    <circle cx="{AX}" cy="{AY}" r="5.5" class="mapa__pin"/>
    <circle cx="{AX}" cy="{AY}" class="mapa__pulse"/>
    <circle cx="{BX}" cy="{BY}" r="5.5" class="mapa__pin"/>
    <circle cx="{BX}" cy="{BY}" class="mapa__pulse mapa__pulse--b"/>
    {taco()}
    {taco("mapa__taco--2")}
    {taco("mapa__taco--3")}
    <text x="{AX}" y="{AY - 34}" text-anchor="middle" class="mapa__label">{'Estados Unidos' if es else 'United States'}</text>
    <text x="{AX}" y="{AY - 17}" text-anchor="middle" class="mapa__label mapa__label--sm">{'Vos, desde donde estés' if es else 'You, wherever you are'}</text>
    <text x="{BX + 16}" y="{BY + 4}" class="mapa__label">El Salvador</text>
    <text x="{BX + 16}" y="{BY + 21}" class="mapa__label mapa__label--sm">{'Tu familia, en la mesa' if es else 'Your family, at the table'}</text>
  </svg>
  <div class="mapa__legend">
    <span><i class="mapa__dot" style="background:var(--crema)"></i>{'Vos comprás el voucher' if es else 'You buy the voucher'}</span>
    <span><i class="mapa__dot" style="background:var(--durazno)"></i>{'Llega al celular de tu familia' if es else 'It reaches your family phone'}</span>
    <span><i class="mapa__dot" style="background:var(--rojo)"></i>{'Ellos comen en Tacos Hermanos' if es else 'They eat at Tacos Hermanos'}</span>
  </div>
</div>"""


# --------------------------------------------------------------------------
# components added after the 31 July review with Erika Silva
# --------------------------------------------------------------------------
def icono(lang, name, cls_="icono", alt=""):
    p = f"assets/images/iconos/icono-{name}-tacos-hermanos-{DOMAIN}.webp"
    a = f' alt="{alt}"' if alt else ' alt="" aria-hidden="true"'
    return f'<img class="{cls_}" src="{rel(lang,p)}"{a} loading="lazy" width="160" height="160">'

def icon_rule(lang, name="arco"):
    return f'<div class="icon-rule">{icono(lang,name)}</div>'

def concepto(lang):
    """The one phrase Erika asked to be the first thing anyone sees:
    "sin habernos conocido... ya somos hermanos". It is their Instagram and
    Facebook bio line, and the closing line of their own Concepto artwork.
    The full three-part Concepto lives on Nuestra Historia, not here."""
    es = lang == "es"
    l1 = "Sin habernos conocido…" if es else "Without ever having met…"
    return f"""<div class="concepto">
      <span class="concepto__line">{l1}</span>
      <span class="concepto__shout">¡Ya somos hermanos!</span>
    </div>"""

PLAY_SVG = ('<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M8 5v14l11-7z"/></svg>')

def video_card(lang, slug, label, alt):
    """Poster only until clicked. Nothing preloads, so the page stays fast."""
    v = f"assets/video/{slug}-tacos-hermanos-{DOMAIN}.mp4"
    poster = f"assets/images/video-posters/{slug}-poster-tacos-hermanos-{DOMAIN}.webp"
    play = "Reproducir el video" if lang == "es" else "Play the video"
    return f"""<figure class="video-card reveal" data-video="{rel(lang,v)}">
        <img class="video-card__poster" src="{rel(lang,poster)}" alt="{alt}" loading="lazy" decoding="async" width="900" height="1600">
        <button class="video-card__play" type="button" aria-label="{play}: {label}"><span>{PLAY_SVG}</span></button>
        <figcaption class="video-card__label">{label}</figcaption>
      </figure>"""

def horario_block(lang, rows):
    out = "".join(f'<div class="horario__row"><span class="horario__day">{d}</span>'
                  f'<span class="horario__time">{t}</span></div>' for d, t in rows)
    return f'<div class="horario">{out}</div>'

def sucursal_cards(lang):
    out = []
    for c in CASAS:
        nombre, f_es, f_en, ciudad, lugar, foto, video, h_es, h_en = c
        media = (video_card(lang, video, nombre,
                            (f"Video de apertura de Tacos Hermanos {nombre}" if lang == "es"
                             else f"Opening video for Tacos Hermanos {nombre}"))
                 if video else
                 f'<figure class="video-card reveal">'
                 + img(lang, f"assets/images/gallery/{foto}-tacos-hermanos-{DOMAIN}.webp",
                       (f"Tacos Hermanos {nombre}" if lang == "es" else f"Tacos Hermanos {nombre}"),
                       cls_="video-card__poster")
                 + f'<figcaption class="video-card__label">{nombre}</figcaption></figure>')
        desde = ("Desde el " + f_es) if lang == "es" else ("Since " + f_en)
        out.append(f"""<article class="sucursal reveal" id="{casa_id(nombre)}">
        {media}
        <div class="sucursal__body">
          <h3>{nombre}</h3>
          <span class="sucursal__place">{lugar}</span>
          <span class="loc__since">{desde}</span>
          {horario_block(lang, h_es if lang == "es" else h_en)}
        </div>
      </article>""")
    return f'<div class="sucursales">{"".join(out)}</div>'
