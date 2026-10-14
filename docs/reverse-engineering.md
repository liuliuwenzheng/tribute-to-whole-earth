# Reverse-engineering approach / 逆向做法

Inspired by the spirit of [rea.tools](https://rea.tools/): **inspect the running public artifact → recover the rule/structure → rebuild something you can change** (here: a multilingual index), without pretending to own the original content.

## What we inspected (2026-10-14)

| Layer | Finding |
| --- | --- |
| Stack | Next.js (Pages Router) static/SSR HTML at [wholeearth.info](https://wholeearth.info/) |
| Collections | 6 series anchors: `#whole-earth-catalogs` … `#special-publications` |
| Publications | Routes `/p/<slug>` (147 issues on the homepage) |
| Media | Cover + page images via `archive.org/download/<id>/page/...`; PDF at `archive.org/download/<id>/<id>.pdf` |
| Details | `archive.org/details/<id>` |

## Rebuild target (this repo)

1. **Catalog JSON** (`data/catalog.json`) — machine-readable map of collections → publications → IA ids.
2. **Locale packs** (`locales/*.json`) — UI + collection names first; issue title translations next.
3. **Thin multilingual viewer** (later) — same information architecture, `?lang=` or path prefix, always link out for scans.
4. **Agent prompts** (`prompts/`) — copy-paste instructions so coding agents can re-inspect and extend languages.

## Explicit non-goals

- Do not bulk-mirror IA scans into git.
- Do not scrape behind logins or bypass site terms.
- Do not claim official status.

## Agent one-liner (REA-style)

> Inspect https://wholeearth.info/. Recover the collection and `/p/` slug map, refresh `data/catalog.json`, and propose locale keys for any new UI strings. Do not download page images into the repo.
