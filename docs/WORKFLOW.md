# 逐本制作流程 · Volume workflow

目标：像电子百科一样，**一本做完再下一本**。

## 顺序

1. 在 `data/catalog.json` 选定 `slug`（建议系列内按时间：先 Fall 1968）。  
2. 复制 `volumes/_template/` → `volumes/<slug>/`，填 `meta.json`。  
3. **源页**：用 IA `archive_id` 对照扫描（不把大图提交进 git）。  
4. **OCR**：每页文本进 `pages/`（本地）；人工校对英文。  
5. **切片**：按「工具条目 / 文章 / 广告栏」拆成 `entries/*.json`（见 schema）。  
6. **翻译**：每条 `body_en` → `body_zh`；题名、作者、交叉引用一并译。  
7. **关联**：填写 `see_also`（同工具其它期、相关人物/主题）。  
8. **搜索**：该卷验收后生成/更新卷内索引；全集索引等收集一批后再合并。  
9. 更新 `volumes/<slug>/STATUS.md`：`ocr | proof | translate | link | done`。

## 验收（一卷算完成）

- [ ] 全部主要条目有中英正文  
- [ ] 目录可浏览  
- [ ] 卷内搜索可用  
- [ ] 至少一条跨条目/跨期关联可点  
- [ ] 当期署名写入卷内 CREDITS  
