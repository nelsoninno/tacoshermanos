# CLAUDE.md, operating brief for tacoshermanos.com

Read this first in any future session on this site.

## Client

| | |
|---|---|
| Business | Tacos Hermanos, Salvadoran taco restaurant group, six locations |
| Contacts | Alfonso Díaz-Bazán, CEO and co-founder (goes by "Pocho"). Erika Silva, Head of Marketing, esilva@tacoshermanos.com |
| Domain | tacoshermanos.com, owned by the client since 2018. Registrar credentials still to be handed over. |
| Tier | Business |
| Commercials | $500 deposit, $1,000 on delivery. Invoiced through WeSpark with IVA so the client gets a crédito fiscal. |
| Instagram | https://www.instagram.com/tacoshermanossv |
| Agreed on | 9 July 2026 call |

## Language layout, note the inversion

This site is **Spanish-first**, which is the opposite of the EKY default.

- Spanish lives at `/` (the primary language, `index.html`, `menu.html`, and so on)
- English lives at `/en/`
- `hreflang` `x-default` points at the Spanish root
- The client asked for this explicitly: tacoshermanos.com should land on Spanish.

Do not "fix" this to the usual EN-at-root pattern.

## How the site is built

The HTML is **generated**, not hand-written. Editing an `.html` file directly works but will be
overwritten on the next build. Edit the source and rebuild:

```
python3 _source/pages.py     # regenerates all 18 pages plus the two 404s
```

| File | What it holds |
|---|---|
| `_source/build.py` | head, header, footer, JSON-LD, the map, shared components |
| `_source/pages.py` | the page bodies, the FAQ, the per-page SEO metadata, the writer |
| `_source/menu_data.py` | every dish, price and description, in Spanish and English |
| `_source/map.json` | the projected geography for the animated voucher map |

Both languages come from the same source, which is why they cannot drift apart. To change a
price, edit `menu_data.py` and rebuild: it updates the menu page, the JSON-LD `Menu` node and
`llms-full.txt` at once.

The animated map on the home and Regala Tacos pages is real Mercator geography, projected
offline from the `world-atlas` dataset. To regenerate it, see `_source/map.json`.

## The 31 July review with Erika Silva, applied

Erika walked the whole site page by page on 31 July 2026. Transcript:
"Meeting started 2026/07/31 15:22 CST" in Drive. What changed, and why:

- **Hero** now opens with the brand's own Concepto lockup, verbatim from their artwork:
  "Somos tres… ¡Somos hermanos! / Junto a ti… ¡Somos invencibles! / Y lo mejor de todo es;
  que sin habernos conocido… ¡Ya somos hermanos!" She asked for this to be the first thing
  anyone sees. The H1 sits under it and carries the search intent.
- **Header** uses the real isotipo plus the real vector wordmark. The drawn text is gone.
- **Colour**: far less orange. "Nosotros no ocupamos mucho el naranja, ocupamos más el verde
  y las tonalidades de verde." Orange now appears only on primary CTA buttons and on the
  final "¡Ya somos hermanos!" line, which is orange in their own artwork.
- **The orange marquee under the hero is deleted.** She agreed three times.
- **"Tres cosas que no negociamos" is gone**, replaced with the positive framing she dictated:
  big "Un producto espectacular / Un servicio memorable / El mejor valor por su dinero",
  small supporting line under each.
- **No personal byline.** The golden-rule quote is credited to Tacos Hermanos, not to
  Alfonso. There are three brothers, not one figurehead.
- **The efecto mariposa moved to the Fundación page**, where it belongs.
- **Info is now Sucursales**, with a card per branch: photo, opening video, and that
  branch's own hours.
- **Cultura and Valores** are on Nuestra Historia, verbatim from their brand artwork.
- **/empleados** is the unlisted internal page (noindex, robots-disallowed, out of the
  sitemap, not in the nav) holding cultura, visión and valores.
- **Fundación** is now real: Somos Hermanos, the 1 Juan 4:21 verse, +300 baskets every
  Sunday, +5 years in Sonsonate, the three donation steps and the Escuela Bíblica Dominical
  partnership. That section uses the foundation's own blue, not restaurant green.
- **Brand icons** from the brand book (salsa bottle, taco, arch, tostada) now decorate the
  pillars and section rules, instead of anything invented.
- **Social share image** is brand-book page 1, as requested.

Still open from that call: dish stories stay out; the "Brothers" sister brand is parked
pending Pocho; an Instagram video feed page was discussed but not built.

## The 1 August review, applied

- Hero: "¡Ya somos hermanos!" is cream, not orange. The lead-in is about half its size.
  The H1 is the small white line: "Tacos Hermanos, taquería y restaurante en El Salvador,
  seis sucursales". Hero buttons trimmed to two, since Horarios and Sucursales land in the
  same place and Regala Tacos is already in the nav.
- The full three-part Concepto is now a visible block on Nuestra Historia, on green, with
  "Unidad · Colaboración · Solidaridad" under it.
- All negative framing removed from brand copy. Nothing is phrased as "we were not…".
- The five values are centred cards on brand green.
- Menu: margaritas and frozens sit side by side with portrait photos; beers and drinks stay
  plain lists. Every dish now carries an English `gloss` shown under the Spanish name on
  /en/ only.
- The animated map in the home teaser is 40% wider.
- Somos Hermanos links to somoshermanos.ong and @somoshermanossv, and is declared as an
  NGO funder in the schema graph.
- The golden rule moved out of "La esencia" and now closes the "Lo que siempre vas a
  encontrar aquí" section, as a green band under the three pillars, titled "La regla de oro
  en Tacos Hermanos". Without a personal byline the quote had nothing to anchor it where it
  was. "La esencia" keeps the essay and the photo.
- Each of the six rows in the home page's "Nuestras casas" list links straight to that
  branch's card on Sucursales, using a slug from `casa_id()` in `build.py`. The jump is
  deliberately instant, not smooth: `html{scroll-behavior:smooth}` was animating the
  cross-page landing for over a second and leaving the last cards below the fold.

## Videos

Four are live, all self-hosted, all well under the 20 MB ceiling Nelson set on the call:
apertura San Miguel, apertura Santa Ana, apertura Usulután and sucursal La Gran Vía.
Nothing autoloads. Each card shows a poster and only fetches the MP4 on click, which is
the behaviour Erika saw demonstrated. San Benito and Paseo Venecia have no video yet.
Re-encode new ones with: `ffmpeg -i in.mov -vf scale=720:-2 -c:v libx264 -crf 27 -maxrate
2200k -movflags +faststart -c:a aac -b:a 96k out.mp4`.

## What is real and what is pending

Everything on the site marked with the amber `.pendiente` style is **not final copy**. It is
visible on purpose so the client can see the gaps during review. Search for `pendiente` before
launch, that class must be gone (or every instance filled) before the site goes live.

Still needed from the client:

1. Exact addresses or Google Maps links per location, and phone numbers per branch
2. The business-inquiries email
3. The founding story: the first weeks, the early challenges, what has not changed since day one
4. The service protocol and welcome protocol, for /empleados (Erika is updating them)
5. The price and contents of a Somos Hermanos aid basket
6. Videos for San Benito and Paseo Venecia
7. Erika's note saying which of the "famous" videos goes where on the site
8. The menu Illustrator files (on her external drive)
9. Foundation photos from her old phone, the foundation video, and the two story threads
10. Confirmation of the webfont licence for Causten
11. Registrar access for tacoshermanos.com
12. La Gran Vía hours change once breakfast launches

Already received and applied: per-branch hours, cultura y valores, the concept line, the
foundation stand artwork, the brand icons, the text logo, and the first batch of videos.

## Decisions already made, do not relitigate

- **No dish stories.** Alfonso asked to keep it simple on the 9 July call: "no quisiera poner
  historias de platos ahorita." A Behind the Scenes section can be added later.
- **No reservations, no delivery.** Both are deliberate business policy and the site explains
  the reasoning rather than hiding it. This is a positioning asset, not a gap.
- **Business inquiries** were requested as a later addition. Currently handled by a CTA band on
  the Info page pointing at Instagram, pending a real email address.
- **Menu as HTML, never a PDF.** Explicitly agreed. The whole point is that people and AI models
  can read it.

## Phase two, the voucher programme

`regala-tacos.html` and `en/gift-tacos.html` are built and live in the nav, with the animated
map Alfonso asked for ("como las remesas") and the three tiers he specified: $10 one person,
$20 a couple, $50 the whole family. **The buy buttons are deliberately disabled.** Phase two is
building the actual purchase flow after launch. Still undefined: the payment gateway, the code
format, how it is redeemed at the till, and the accounting treatment.

Note for whoever picks this up: the voucher idea does not appear in any recorded call or Drive
document. It came from a conversation outside the transcripts, most likely WhatsApp. The
wording currently on the page is EKY's, not the client's, so it needs their sign-off.

## Assets, where they came from

There were no client-supplied photos. Everything on the site was extracted from files the
client did provide:

- **Dish photography**: pulled out of `Main MENU.pdf`, where each page's photo is stored as a
  clean raster underneath the vector type. So the site shows the real professional shots with
  no menu text baked in.
- **Location, team and guest photography**: extracted from `Concepto Tacos Hermanos Ablir2026.pdf`.
- **Logos**: extracted as true vector from the brand manual PDF, then cleaned to `currentColor`.
- **Colours**: sampled from the brand manual's palette page.

Originals are archived in `_source/photos-original/` and `_source/logos-original/`.

There are also seven location videos in the client's folder (30 MB to 120 MB each). None are
used yet. If any is wanted as a hero, it must go on YouTube or Cloudflare Stream: Cloudflare
Pages rejects any single file over 25 MB.

## Deploy

**GitHub repo: https://github.com/nelsoninno/tacoshermanos** (branch `main`), pushed 31 July 2026.

Not yet on Cloudflare. Next stage is the **cloudflare-pages-deploy** skill, step 2 onward:
create the Pages project connected to this repo (framework preset None, no build command,
output directory `/`), then connect tacoshermanos.com. After that every `git push` auto-deploys.
`CNAME` and `.nojekyll` are already in place and are harmless on Cloudflare.

`_source/` (the build scripts) and `brand/` ARE committed on purpose: the HTML is generated,
so without them nobody can rebuild the site. They are small and contain no secrets.
`_source/photos-original/` is gitignored, it is 19 MB of raw extractions recoverable from the
client's own PDFs.

## Release gate

Re-run the section 15 checklist in the website-build skill's `seo-ai-findability.md` against the
final copy, in both languages, before publishing. In particular: no `pendiente` markers left, no
em-dashes, one clean H1 per page, and the JSON-LD matching what the pages actually say.
