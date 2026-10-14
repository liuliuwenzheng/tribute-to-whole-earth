# wholeearth-i18n · 全球地球索引多语言

**EN:** Community project to reverse-engineer the public structure of [wholeearth.info](https://wholeearth.info/) and rebuild a **multilingual** Whole Earth Index shell (UI + metadata first). Method inspired by agent-oriented reverse engineering ([rea.tools](https://rea.tools/)): inspect → recover structure → rebuild what you can change.

**中文：** 社区项目：摸清 [wholeearth.info](https://wholeearth.info/) 公开结构，重建**多语言** Whole Earth 索引壳（先做界面与元数据）。做法借鉴面向编程代理的逆向思路（[rea.tools](https://rea.tools/)）：先检查、再恢复结构、再重建可改的部分。

> Unofficial. Not affiliated with Stewart Brand, POINT Foundation, or wholeearth.info.  
> 非官方。与上述权利方及原站无关。详见 [NOTICE.md](./NOTICE.md)。

## Why / 为什么做

[wholeearth.info](https://wholeearth.info/) is a beautiful English-only archive of Whole Earth publications (1968–2002). This repo aims to make **navigation and issue metadata** readable in many languages, while page scans stay on the [Internet Archive](https://archive.org/).

原站是英文索引。本仓目标是让**导航与刊号元数据**多语言可读，扫描页仍外链 Internet Archive。

## Current snapshot / 当前快照

| Item | Value |
| --- | --- |
| Source | https://wholeearth.info/ |
| Collections | 6 |
| Publications mapped | **147** (`data/catalog.json`) |
| Locales started | `en`, `zh-CN` |
| Page images in git | **None** (link-out only) |

## Layout / 目录

```
data/catalog.json          # extracted collection → publication → archive_id map
locales/en.json            # UI strings (English)
locales/zh-CN.json         # UI strings (简体中文)
docs/reverse-engineering.md
prompts/inspect-and-extend.md
scripts/inspect_homepage.py
NOTICE.md                  # copyright boundaries
```

## Quick start / 快速开始

```bash
# refresh catalog from the live homepage
python3 scripts/inspect_homepage.py
```

Give your coding agent the prompt in [`prompts/inspect-and-extend.md`](./prompts/inspect-and-extend.md).

## Roadmap / 路线图

1. ~~Create repo + catalog extract + EN/zh-CN UI locales~~ (done)
2. Static multilingual browser for collections / publications
3. Per-locale title translations (`data/translations/`)
4. More languages (ja, es, fr, …) via locale PRs
5. Optional: align metadata ideas with [search-whole-earth](https://github.com/lucasgelfond/search-whole-earth) (search is out of scope here)

## Related / 相关

- Original index: [wholeearth.info](https://wholeearth.info/)
- Searchable companion (upstream community): [searchwhole.earth](https://searchwhole.earth/) · [lucasgelfond/search-whole-earth](https://github.com/lucasgelfond/search-whole-earth)
- Reverse-engineering for agents (inspiration): [rea.tools](https://rea.tools/)

## License / 许可

Code and locale packs: [MIT](./LICENSE). Historical publication content: see [NOTICE.md](./NOTICE.md).
