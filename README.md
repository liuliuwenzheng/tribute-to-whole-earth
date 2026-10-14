# 致敬伟大的全球概览

**Tribute to the Whole Earth Catalog**

把《全球概览》系列做成**可搜索、可关联、可随时查阅**的中英对照数字化百科——像电子版大英百科那样，一本本做完整。

A Chinese–English digital encyclopedia of the Whole Earth publications: searchable, cross-linked, readable anytime—volume by volume, complete.

---

## 目标 / Goal

不只做目录。我们要：

1. **逐本制作**：一期一期 OCR → 结构化 → 中英全文对照  
2. **可搜索**：题名、作者、工具、正文关键词  
3. **可关联**：同一工具/人物/主题在不同刊期之间跳转  
4. **可查阅**：像百科一样打开就读，让更多人接触这批过去有趣的文化  

Not a shelflist. Volume-by-volume full bilingual text, search, and cross-links—so more people can meet this culture.

## 致谢 / Credits

刊物属于开创者与历代贡献者。详见 [CREDITS.md](./CREDITS.md)。

| | |
| --- | --- |
| 创办人 | **Stewart Brand** |
| 出版 | **POINT Foundation** 与 Whole Earth 团队 |
| 内容 | 历代编辑、作者、插画与书评贡献者（约 1968–2002） |
| 扫描托管 | [Internet Archive](https://archive.org/) |
| 索引站 | [wholeearth.info](https://wholeearth.info/)（设计致谢 Jon Gacnik、Mindy Seu 等） |

我们只做数字化整理与中英对照，**不冒充官方**，**不声称拥有版权**。

## 版权门槛 / Rights

全文上公开站或公开仓前，需要权利方许可（或确认可合法使用的范围）。  
在此之前：目录与流程可以公开；**全文译稿默认不进公开仓**，先在本地/`volumes/` 私有工作流里一本本做。

Before publishing full text: get permission (or a clear legal basis). Until then, catalog + tooling can be public; **full translations stay out of the public tree** by default.

说明见 [docs/RIGHTS.md](./docs/RIGHTS.md)。

## 怎么一本本做 / Volume workflow

见 [docs/WORKFLOW.md](./docs/WORKFLOW.md)。摘要：

1. 从 [data/catalog.json](./data/catalog.json) 选一期（现从 **Fall 1968** 起）  
2. 对照 IA 扫描：切页 → OCR → 条目结构化  
3. 英文校对 → 中文翻译 → 中英对照页  
4. 建搜索索引与交叉引用  
5. 验收后记入 `volumes/<slug>/`

模板：[volumes/_template/](./volumes/_template/)  
第一本工位：[volumes/whole-earth-catalog-fall-1968/](./volumes/whole-earth-catalog-fall-1968/)

## 仓库结构 / Layout

```
data/catalog.json          # 147 期总目
volumes/<slug>/            # 每一本的制作目录
locales/en.json | zh-CN.json
docs/WORKFLOW.md | RIGHTS.md | NOTES.md
schema/entry.schema.json   # 单条工具/文章结构
scripts/inspect_homepage.py
```

## 许可 / License

本仓库代码与说明：[MIT](./LICENSE)。  
刊物正文与扫描：原权利方所有。
