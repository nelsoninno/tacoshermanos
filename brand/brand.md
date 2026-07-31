# Tacos Hermanos, brand sheet

The human-readable companion to `assets/css/tokens.css`. If you change one, change the other.

Source of truth: `GRAFICA MARZO2022_TACOS HERMANOS` (the client's brand manual, `.ai` and `.pdf`).
The colours below were sampled directly from the palette page of that document, not guessed.

## Colours

| Role | Name | Hex | Where it is used |
|---|---|---|---|
| Primary | Verde hermano | `#2D8769` | Brand green. Logo, accents, CTA bands, headings on cream. |
| Deep | Verde hondo | `#266E54` | Hero overlays, dark bands, footer. |
| Light | Verde claro | `#389975` | Tints and small details. |
| Cream | Crema | `#F6E2B4` | The brand cream. Alternating bands, cards, type on green. |
| Peach | Durazno | `#F7CC91` | Highlight tint, hero emphasis words. |
| Accent | Rojo tatemado | `#F0512A` | Primary buttons, prices, the marquee band. |
| Accent deep | Rojo hondo | `#CC3D26` | Price type, hover states. |

Site-level roles derived from the above: page background `#FFFBF1` (cream lifted almost to white),
body text `#16352C` (a green-black drawn from the brand rather than a neutral grey), muted text
`#6E7B72`, hairlines `#E6DCC6`.

## Typography

**Causten** is the brand typeface. The client owns the full 18-weight family (it sits in their
Drive folder). It is a commercial face, and using it as a **webfont** needs a licence that has
not been confirmed yet.

Until that is confirmed the site ships **Outfit**, a geometric sans chosen because it sits as
close to Causten as a free face gets. It is self-hosted as a variable woff2 in `assets/fonts/`,
so the site never waits on a third-party server.

**To switch to real Causten:** convert the four weights we actually use (Regular, Medium, Bold,
ExtraBold) to `.woff2`, drop them in `assets/fonts/`, and uncomment the four `@font-face` blocks
at the top of `tokens.css`. The font stack already lists Causten first, so nothing else changes.

## Logo

All four lockups were extracted as clean vector from the brand manual and live in
`assets/images/logos/`. Each exists in three versions:

- `isotipo-*` the arch mark on its own. Used in the site header.
- `wordmark-*` the two-line TACOS HERMANOS lockup.
- `badge-*` the circular lockup with EST. 2021.
- `badge-tagline-*` the circular lockup with LO BONITO, SE COMPARTE.

The base file uses `fill="currentColor"`, so inlining it lets CSS colour it. The `-crema-` and
`-verde-` variants are pre-coloured for use as plain `<img>`.

## Voice

The client's own words, taken from the founder interview. Use these, do not invent new ones.

- "Lo bonito se comparte." The tagline. It belongs on the site.
- "¡Ya somos hermanos!" Used in the graphic language.
- "¡Aquí es donde la vida se celebra!" From the concept deck.
- "Una experiencia extraordinaria, una experiencia que cambia vidas." The golden rule.
- "El efecto mariposa." How the founders describe why small kindnesses matter.

Tone in Spanish is warm, direct, Salvadoran, second person singular with *voseo* ("podés",
"vení", "mandales"). Not neutral Latin American Spanish, and definitely not Spain Spanish.
English is a natural translation, never literal. Dish names stay in Spanish in both languages.

## Do not

- Do not use an em-dash anywhere a person or a search engine can see it.
- Do not strip Spanish accents, ñ, or the opening ¡ and ¿.
- Do not translate dish names.
- Do not promise reservations or delivery. The company offers neither, on purpose.
- Do not invent hours, phone numbers or foundation details. They are still pending from the client.
