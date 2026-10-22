# Fall 1968 · 经验

1. IA `imagecount=70`，页号 `n0`–`n69`；`cover_w1000` 与 `n0` 同图。OCR 后：`n0` 有封面标题字（WHOLE EARTH CATALOG / access to tools）；**PURPOSE/FUNCTION 在 `n1`**；目录在 `n2`；CATALOG procedure 在 `n3`。勿把 `n1` 当成只有图的封面。
2. 公开仓只提交 `media/manifest.json`（URL）与 `toc.public.json`（板块+页号+entry id）；OCR/`body_en`/`body_zh` 留本机 `tribute-work`，避免未授权全文进公开树。
3. 末页 `n68`/`n69` OCR 常为空（封底/色卡），验收时按图检查，不要当成漏页。
4. **多栏版面**：同一页常并排 2–3 条书目（如 `n6` Full Earth∥Earth Photographs，`n9` Cage∥General Systems，`n13` Ghost∥Year 2000∥Futurist）。OCR 会把栏文交叉串行；边界不可靠时宁可整页全文挂到相关条目并写 `ocr_note`，也不要删节。人工校对必须对照 IA 页图按栏重切。
5. **大板块边界**：用「该板块第一条书目」所在页作 `leaf_start`（Understanding=`n4` Buckminster Fuller；Shelter=`n14` Dymaxion World；Industry=`n23` Way Things Work；Communications=`n33` Human Biocomputer；Community=`n42` Modern Utopian；Nomadics=`n46` Innovator；Learning=`n53` Toward a Theory of Instruction），再用印刷目录（`n2`/`n65`）交叉核对，比只搜标题行更稳。
6. **艺术/满版图页**（如 `n11` Tantra Art）OCR 几乎不可读（镜像乱码）；条目仍保留 raw OCR + IA 图 URL，证明与翻译以图为准。
7. **批量起草后半卷**：以印刷目录（`n2`）列书目清单，再用 OCR 标题命中定 `page_start`/`page_end`；共享页一律挂整页 OCR + `ocr_note`。工具目录类短评（Bean、工具商目录等）可按供应商簇合并页范围，但仍各留独立 entry id，便于日后检索关联。
8. **中译顺序**：先开篇宣言/程序（读者入口），再 Understanding Whole Systems；多栏页的中译先保证布兰德评介与可辨引文完整，图注与串行栏待 IA 重切后再补，避免为「干净」而删英文 OCR。
9. **I Ching 等目录有、OCR 边界糊的条目**：先给较宽页范围并注明 pending proof，不要从总目里删掉——完整性优先于页码精确。
10. **全卷中译（142）**：按板块顺序 Shelter→…→Back matter 整段完成，优先整板块质量而非薄概要。共享页先抽出布兰德评介句核再译；工具商/广告栏 OCR 差时仍译完可读订购与短评，细部价目表可保留数字并 `zh_note`。I Ching 印刷在 Learning 区但 OCR 落在与《创造行为》同页（约 n62）——以内容所在页为准，目录页码作交叉索引。


11. **用语**：阅读器与文档统一用「页」，不用「叶」；中英必须同一条目严格对应，禁止错配。
12. **本机阅读器（2026-10-22）**：借鉴 Claude 系 IA（侧栏导航 / 正文区清晰层级）+ 克制古希腊纹样；配图接本机 `pages`/`media`。全文与大图包仍不进公开仓。
13. **验收边界**：本机质量验收 ≠ 全文推公开仓。2026-10-22 拍板后 Fall 本机验收过，立即开 Spring 本机；公开仓只更新 STATUS/INDEX 进度句。
