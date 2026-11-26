# demo.thonly.org/book — the design of book.thonly.org

Phases 2 and 3 of the four-phase build (spec → drawings → clickable prototype → implementation). Live, unlisted, at
<https://demo.thonly.org/book/>; everything on one surface at `wall.html`.

⭐ **Moved here from `book.thonly.org/demo/` on 2026-11-26** (founder: *"Move book.thonly.org/demo/ to demo.thonly.org ?"*;
`/build` Default 7: a root domain's drawings live on its own `demo.<root>`). Each old page there now redirects to its twin
here. The files were copied as they were, the history stays in `thonly/book.thonly.org`, and only the addresses changed:
the page links, the share URLs and the icons now name this host or `book.thonly.org` in full. ⛔ **These drawings are
dated records** (founder 2026-11-11: no live site is generated from or checked against a drawing). The live landing's
source is `scripts/build-site.py` in `thonly/book.thonly.org`, in English and Khmer; it no longer imports anything here.

⛔ **Nothing here is the site.** No page is live, no note is sent, nobody is charged. **Every quote is sample text**: no
AI model wrote those words, and no model is named (the seats appear by role; the model slot is left blank). The
author's reply is sample text, the cover is placeholder art, and the printed-copy prices are sample figures.

⚠️ **When a screen and the private memory disagree, the memory is canonical** (see the header of `SPEC.md` in [`thonly/book.thonly.org`](https://github.com/thonly/book.thonly.org/blob/main/SPEC.md)).

## Three layers (founder, 2026-09-16)

**The record** (the rules and every conversation, at `github.com/thonly/two-singularities`) → **the full debate** (for
serious readers) → **the story** (for everyone). The story may choose, order and describe; it may not invent. Words in
quotation marks are always a seat's exact words — `build-boards.py` refuses to build if a story quote is not found word
for word in the debate — and the story says what a seat said and did, never what it felt.

## Files

| | |
|---|---|
| `build-boards.py` | ⭐ **the source**: the shared style, the page chrome, and every board's content. Writes `*.dc.html` and `canvas.json` |
| `*.dc.html` | one artboard each — **generated**; edit `build-boards.py`, never these |
| `measure.mjs` | loads every board in headless Chrome at its design width, writes the real height into `canvas.json`, and **fails** on sideways overflow or a nested scroll container |
| `build-index.py` · `build-wall.py` | generate `index.html` (the front door) and `wall.html` (pan and zoom) from `canvas.json` |
| `build-og.py` | renders `og.png` and `og-walkthrough.png`, the 1200×630 link-preview cards, with headless Chrome |
| `build-prototype.py` | ⭐ writes `walkthrough.html`, **the clickable prototype** (phase 3) — it IMPORTS the style, quotes, titles and cover from `build-boards.py`, so the two cannot disagree |
| `test-walkthrough.mjs` | serves the prototype over HTTP and drives it in headless Chrome at 390 and 1280px: every screen, the note, the printed-copy total, the jump from a quote to the debate, Back, overflow, nested scrollers, exceptions |
| `build-library.py` | writes `library.html`, **the library page as drafted** (2026-10-15). It IMPORTS the five pairs (`LIBRARY`), the lede and the style from `build-boards.py`, which also renders them as the *1 · The library* board and the prototype's library screen. ⛔ `--landing` is retired and refuses (2026-11-26): here it would overwrite this host's front door |
| `test-library.mjs` | loads the draft, served from this folder, at a TRUE 390px (device emulation — a window-size screenshot is a crop of a ~500px layout and looks like overflow) and at 1280px: sideways overflow, nested scrollers, five pairs, the one link out says what it opens, **no status words** (named, never pending), no console errors; and what a machine reads (the JSON-LD against the cards, then robots, sitemap and `llms.txt`; the draft must carry no markup). `SCHEME=light` · `SHOTS=<dir>` · `LIB_URL=` for a live host |
| ~~`build-icons.py`~~ | stayed with the site: the live icons and the landing's card are drawn by `scripts/build-icons.py` and `scripts/build-og.py` in `thonly/book.thonly.org` (register M-0009) |

## The loop

```sh
python3 build-boards.py && node measure.mjs && python3 build-prototype.py && node test-walkthrough.mjs \
  && python3 build-library.py && node test-library.mjs \
  && python3 build-index.py && python3 build-wall.py && python3 build-og.py
```

Then the structural checks (div balance, quote integrity, tag nesting, and `node --check` on the wall's script), a
look at the screens, commit, push. GitHub Pages publishes in under a minute.

## Search, link previews and machine readers

These pages are kept out of search engines **by name** (`googlebot`, `bingbot`, `slurp`, `yandex`); there is no blanket
robots meta. The AI companies' crawlers are kept out of `/book/` **by name** too, in this host's `robots.txt` (founder
2026-10-15, carried here with the move): its quotes are sample text attributed to the seats, words no model said, and
those crawlers feed the models and build the search the seats use. Everyone else falls in the `*` group, which **blocks
nothing**. ⛔ Never a `Disallow` in the `*` group: it would also stop the link-preview crawlers, and Facebook caches a
robots file for about a day. ⚠️ robots.txt is a request, and the same sample text is in two public repositories; the move
took it off the BOOK's host, not off the web (the carry list, below). `og:image` is an absolute URL.

What a machine reads about the library is written by `scripts/build-site.py` in `thonly/book.thonly.org`. ⛔ **Nothing on
thonly.org points here for machines:** the Two Singularities seats enter the corpus through thonly.org's `llms.txt`, and a pointer
there would put the book one hop from the readers it is about (SPEC §8).

## What the screens are arguing

- Free to read, whole: no locks, no meters, **no reading progress bars**.
- The thanks line comes **after** reading; the thanks on a printed copy comes **after** the purchase, separately.
- A note in plain words is always checked by the seat it explains, and the answer is printed.
- The opening's "Not yet." is set by the arrival test, never by the author.
- An objection's page is ordered by edition only.
- The note form states its character limit once, with no running tally.

## True only in the prototype — the phase 4 carry list

A prototype is allowed to stub what a build is not. Each of these must be real, or absent, on the day the site is public:

- **Thanks by money** — the button opens nothing. Needs the Stripe Payment Link (reader chooses the amount), held by the
  entity the private legal review names.
- **Thanks by note** — nothing is stored. Needs a create-only Firestore collection (the note and its time, nothing else;
  never read by any client), **and abuse protection** (a rate limit and a bot check), or the author's inbox fills with spam.
- **A printed copy** — the prices are sample figures and nothing is ordered. Needs an approved printed proof, the
  print-on-demand provider's cost API behind a small server, Stripe Checkout at that exact amount, and the order placed on
  payment. Until then the page does not exist.
- **Every quote, title, question, reply and figure is sample text** — the real ones come from the pilot run and the first
  edition. ARC-AGI figures are updated to what is published on 7 January.
- **The quote check** runs here against sample quotes; in the build it must run against the real transcripts, and a second
  check is still to be designed: manner words (*slowly*, *gently*) attached to a seat.
- **Links out** — the record opens `github.com/thonly/two-singularities`, the Machine Door opens `thonly.org/mcp`.
- **Addresses** — the prototype routes by `#/…`; the site uses real paths (`/two-singularities/2027/…`).
- **Not built yet:** the privacy page, analytics, EPUB and PDF generation, the objection pages beyond one, Khmer.
- **`/demo/` comes off the public host** (founder 2026-10-15). ◐ **Half done 2026-11-26:** moved off the book's host to
  `demo.thonly.org/book/`, so `book.thonly.org` no longer serves a word no model said. It is still public here, and its
  sample quotes are kept from the AI crawlers only by a request in this host's `robots.txt`. ⭐ **Kept public until launch**
  (founder 2026-11-26: *"Keep public until launch"*): it comes off the web on the day the site is public, not before.
