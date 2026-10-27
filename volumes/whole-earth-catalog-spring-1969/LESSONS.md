# Spring 1969 · 经验

1. **开卷授权**：2026-10-22 群拍板「可以正式开」= Fall 本机验收过 + 开 Spring 本机；**不等于**全文进公开仓。
2. **条目规模**：本卷 302 条（开篇 4 + 七大板块 + 附录 7），比 Fall 142 更大；按区整段推进，避免跳区。
3. **OCR 串页**：工业区多条出现邻页互串（plastics / surplus / zone-system 等）——中译用评介+关键摘录，并写 `zh_note`，英文 OCR 原文保留待重切。
4. **公开仓边界**：只推 STATUS / LESSONS / INDEX 进度 / `toc.public.json`（entry id）；`body_zh`/`body_en`/reader 包/大图不推。推仓须老大明确授权（2026-10-27「可以推仓」= 进度句，仍无全文）。
5. **用语**：同 Fall——用「页」不用「叶」；中英同条对应。
6. **单品裁切**：共享页先批量 `entry_region_crop`，难页（如 n114 五栏）手写 `MANUAL_PAGE_REGIONS`；验收看相邻框 IoU≈0，勿只看 needs_review 计数。
7. **阅读器**：复用 Fall 壳 + 本卷 `data.js`；整包 ~800MB 仅本机/Downloads，公开仓永不进 tar。

（记录于 2026-10-22…2026-10-27 Asia/Shanghai）
