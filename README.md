# 致敬伟大的全球概览

**Tribute to the Whole Earth Catalog**

中英对照索引 · 便于随时查阅  
EN/中文 bilingual index · ready to browse anytime

---

## 这是什么 / What this is

我们对 Stewart Brand 创办的 **《全球概览》（Whole Earth Catalog）** 及其系列刊物（约 1968–2002）做**数字化索引整理**，做成**中英对照**，方便随时打开查看。

We digitize and index the **Whole Earth Catalog** family of publications as a **Chinese–English** browsing aid.

本仓库**不是**官方项目，也**不声称**拥有刊物版权。我们只做整理与对照；正文与扫描页仍归原权利方，页面影像请走 [Internet Archive](https://archive.org/) / [wholeearth.info](https://wholeearth.info/)。

This repo is **unofficial**. We only organize and bilingualize the index; we do **not** claim the publications. Scans stay on IA / the original index site.

当前范围：**只做中英**。目录与译文收集齐全后，再考虑下一步。  
Scope for now: **Chinese + English only**. More work after the catalog is complete.

## 致谢 / Credits

刊物与事业属于开创者与历代贡献者；我们在此致敬并声明清楚：

| 角色 | 致谢 |
| --- | --- |
| 创办人 Founder | **Stewart Brand** |
| 出版机构 Publisher | **POINT Foundation** 及 Whole Earth 相关团队 |
| 历代编辑与作者 Editors & writers | CoEvolution Quarterly、Whole Earth Review、Whole Earth Magazine 等各期编辑、作者、插画与工具书评贡献者（1968–2002） |
| 数字化托管 Digitization host | [Internet Archive](https://archive.org/) 及其志愿者与支持者 |
| 公开索引站 Index site | [wholeearth.info](https://wholeearth.info/)（设计致谢 **Jon Gacnik**、**Mindy Seu** 等） |
| 可检索伴侣项目 Search companion | [searchwhole.earth](https://searchwhole.earth/)（Lucas Gelfond 等，可参考，非本仓范围） |

若名单有疏漏，欢迎开 Issue 补全。Omissions welcome via Issues.

## 仓库里有什么 / What’s in the repo

```
data/catalog.json     # 147 份刊物目录（系列 → 刊号 → IA id）
locales/en.json       # English UI
locales/zh-CN.json    # 简体中文 UI
scripts/inspect_homepage.py  # 从 wholeearth.info 首页刷新目录
```

```bash
python3 scripts/inspect_homepage.py
```

## 许可 / License

本仓库代码与语言包：[MIT](./LICENSE)。  
刊物内容版权：见上表原权利方；本仓不镜像全文扫描。
