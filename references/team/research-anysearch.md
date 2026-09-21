# AnySearch 调研协议

团队 DSH 统一使用 AnySearch 作为网页调研入口；AnySearch 是工具层，本 Skill 决定搜索策略。

每个 qN 默认 3-5 个互补查询：
1. 领域机理/经典数学模型；
2. 近年改进方法；
3. 类似数据、指标、验证方案；
4. 公开代码/工程实现；
5. 局限、失败模式、边界条件。

输出到 `research/qN/`，至少维护 `queries.md`、`sources.md`、`candidates.md`。每条来源记录 URL/题名、核心结论、适用条件、所需数据、限制、可信度备注、是否进入 Astra shortlist。

禁止 Flash 直接拍板最终模型，禁止使用来源不明的公式作为权威依据。
