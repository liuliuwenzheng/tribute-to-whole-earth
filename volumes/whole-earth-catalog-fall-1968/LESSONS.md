# Fall 1968 · 经验

1. IA `imagecount=70`，叶号 `n0`–`n69`；`cover_w1000` 与 `n0` 同图。OCR 后：`n0` 有封面标题字（WHOLE EARTH CATALOG / access to tools）；**PURPOSE/FUNCTION 在 `n1`**；目录在 `n2`；CATALOG procedure 在 `n3`。勿把 `n1` 当成只有图的封面。
2. 公开仓只提交 `media/manifest.json`（URL）与 `toc.public.json`（板块+叶号+entry id）；OCR/`body_en` 留本机 `tribute-work`，避免未授权全文进公开树。
3. 末叶 `n68`/`n69` OCR 常为空（封底/色卡），验收时按图检查，不要当成漏页。
4. **多栏版面**：同一叶常并排 2–3 条书目（如 `n6` Full Earth∥Earth Photographs，`n9` Cage∥General Systems，`n13` Ghost∥Year 2000∥Futurist）。OCR 会把栏文交叉串行；边界不可靠时宁可整叶全文挂到相关条目并写 `ocr_note`，也不要删节。人工校对必须对照 IA 页图按栏重切。
5. **大板块边界**：用「该板块第一条书目」所在叶作 `leaf_start`（Understanding=`n4` Buckminster Fuller；Shelter=`n14` Dymaxion World；Industry=`n23` Way Things Work；Communications=`n33` Human Biocomputer；Community=`n42` Modern Utopian；Nomadics=`n46` Innovator；Learning=`n53` Toward a Theory of Instruction），再用印刷目录（`n2`/`n65`）交叉核对，比只搜标题行更稳。
6. **艺术/满版图页**（如 `n11` Tantra Art）OCR 几乎不可读（镜像乱码）；条目仍保留 raw OCR + IA 图 URL，证明与翻译以图为准。
