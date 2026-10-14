# Prompt: inspect wholeearth.info and extend i18n

Copy into your coding agent:

> Inspect https://wholeearth.info/ like a reverse-engineering task. Recover how collections and publication pages are structured (`/p/<slug>`, Internet Archive ids). Update `data/catalog.json` if the public index changed. Then add or improve a locale file under `locales/` (start from `en.json` / `zh-CN.json`). Keep page scans as outbound links only — do not commit binaries from archive.org. Show a short plan first, then implement.

## Follow-ups

- Translate all `title` fields in the catalog for one language (e.g. `zh-CN`) into `data/translations/zh-CN.titles.json`.
- Scaffold a static site that renders collections with language switcher.
- Diff catalog against https://searchwhole.earth / lucasgelfond/search-whole-earth for missing metadata ideas (search is separate; we focus on multilingual browsing).
