# 系统结构 · System map

简单三层，包容全系列：

1. **总索引** `INDEX.md` + `data/reading-order.json`  
   - 全局序号 1…N，创刊起按序制作  
   - 状态：排队 / 进行中 / 完成  

2. **系列总目** `data/catalog.json`  
   - 6 个系列、147 本、IA id、原站链接  

3. **单卷工位** `volumes/<slug>/`  
   - meta / STATUS / CREDITS / LESSONS  
   - `media/manifest.json`：全页配图（不丢图）  
   - `entries/*.json`：完整中英条目 + figures  

阅读与搜索（后续）：先卷内，再全集；配图始终跟条目走。
