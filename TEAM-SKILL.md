---
name: math-modeling-team
description: 三人数学建模竞赛团队协作扩展：GPT-6 Sol 主线、Luna max 子代理探索、A-F 选题、Q1..QN 依赖、异构执行、证据链与进度管理。
---

# 三人数学建模团队扩展

原 `math-modeling` Skill 继续负责建模/编程/论文与 M1/P1/P2/W1/W2 独立门禁。本扩展管理团队决策、题目依赖、角色协作和交付证据；不改变当届官方 AI 与提交规则。

## 启动

1. 2026 华为杯先读 `references/competitions/huawei-cup-2026.md`，再读项目 `AGENTS.md`、`STATUS.md`、`TASKS.md`、`DECISIONS.md`、`submission/SCHEDULE.md` 和 `ai_usage/AI_POLICY.md`。
2. 选题后读 `problem/problem-map.md`、`problem/dependency.md`；具体流程按 `references/team/workflow.md`。
3. 正式代码执行前读本成员 `config/execution-profile.local.yaml`；禁止提交该文件。
4. 调研读 `references/team/research-protocol.md`。跨成员/机器的异步任务读 `references/team/agent-handoff.md`；Git 协作读 `references/team/git-protocol.md`。

## 模型与子代理路由

- **Sol 主线**：默认使用 Codex GPT-6 Sol 完成研究选择、建模、接口、实现、运行、结果验证、论文证据与跨问整合。人类决定选题与关键模型取舍，并核验 AI 输出。
- **Luna 探索**：有可用子代理且任务边界清晰时，优先派 GPT-6 Luna 处理探索、宽搜、文献候选、附件/资料整理、重复性检查、对照分析等高 token/低决策风险工作；`effort=max`（若环境支持配置）。不为等待子代理阻断 Sol 的关键路径。
- Luna 的探索产物是候选，不是经验证的事实。可在明确隔离的写域写草稿；不得擅自冻结模型/公式/阈值/目标函数/约束/接口，也不得把未经 Sol 和人核验的内容写入最终结论。不可用时由 Sol 完成，不影响 Gate。
- 独立只读质检仍按原 Skill 的门禁调度，由未参与被审产物的 Agent 执行；Luna 可在合适情况下承担该工作。**团队模式**允许额外派发上述 Luna 探索任务，覆盖原 Skill “可选协作默认关闭”的通用缺省；非团队任务仍按通用策略。
- DSH/Flash/Astra 与 AnySearch 不再是未来工作流依赖。历史验收资料不得删改。

默认链路：`EXPAND（可派 Luna） -> SELECT（Sol） -> DECIDE（人） -> SPEC/IMPLEMENT/RUN（Sol） -> VERIFY（Sol + 独立门禁）`。
跨成员/跨机器或异步任务使用 Handoff；同一 Sol 会话不为机械拆工强制交接。

## 状态与责任

顶层状态以项目 `STATUS.md` 为准；每问依次 `RESEARCH -> MODEL -> INTERFACE -> SCAFFOLD -> IMPLEMENT -> RUN -> VERIFY -> PAPER -> PASS`。下游只消费已 PASS 或人工明确批准提前消费的上游 artifact，依赖 DAG 以 `problem/dependency.md` 为准。

三人各负责两题初筛；Sol 以数学、实现、论文风险三视角复筛，Luna 可并行扩展资料；人类会议决定主选题与备选题，写 `DECISIONS.md`。A/B/C 是人的职责分工，不是模型分工。

进度答复必须读取 STATUS/TASKS、依赖图、活跃 Handoff/Gate 与必要结果，给出当前状态、阻塞链、每人下一步和下个门禁。不凭聊天记忆推进状态。

Agent 所在地、代码执行端和 artifact 存储解耦；正式 Python 统一 3.11.x，每台执行机器自行建隔离环境。`main` 只收已验证状态；短任务分支，更新 STATUS/TASKS 和关键 DECISIONS。

## 2026 华为杯硬约束

仓库必须 private，公开时禁止写入真实题目/数据/结果/论文；官方附件 3 Word 模板封面及四个 logo 不得替换；正式提交 PDF。AI 辅助数据分析和代码按附件 4 标注，最终正文人工改写与核验。MD5 提交后锁定 PDF 不得覆盖或重导出。详见 `references/competitions/huawei-cup-2026.md`。
