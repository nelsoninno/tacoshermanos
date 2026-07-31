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
python3 _source/pages.py     # regenerates all 16 pages plus the two 404s
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

## What is real and what is pending

Everything on the site marked with the amber `.pendiente` style is **not final copy**. It is
visible on purpose so the client can see the gaps during review. Search for `pendiente` before
launch, that class must be gone (or every instance filled) before the site goes live.

Still needed from the client:

1. Exact opening hours per location, and whether breakfast has its own hours
2. Exact addresses or Google Maps links per location
3. Contact phone numbers, and the business-inquiries email
4. The foundation: name, what it does, who it has helped, how to support it
5. The founding story: the first weeks, the early challenges, what has not changed since day one
6. Confirmation of the webfont licence for Causten
7. The two reference websites they liked
8. Registrar access for tacoshermanos.com

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

Not deployed yet. Next stage is the **cloudflare-pages-deploy** skill: GitHub repo, Cloudflare
Pages project, custom domain, HTTPS. `CNAME` and `.nojekyll` are already in place.
`_source/` and `brand/` should be excluded from the deployed output.

## Release gate

Re-run the section 15 checklist in the website-build skill's `seo-ai-findability.md` against the
final copy, in both languages, before publishing. In particular: no `pendiente` markers left, no
em-dashes, one clean H1 per page, and the JSON-LD matching what the pages actually say.
