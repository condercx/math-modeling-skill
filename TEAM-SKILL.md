---
name: math-modeling-team
description: 三人数学建模竞赛团队协作扩展：项目级模型路由、A-F 选题、Q1..QN 依赖、异构执行、证据链与进度管理。
---

# 三人数学建模团队扩展

原 `math-modeling` Skill 继续负责建模/编程/论文与 M1/P1/P2/W1/W2 独立门禁。本扩展管理团队决策、题目依赖、角色协作和交付证据；不改变当届官方 AI 与提交规则。

## 启动

1. 2026 华为杯先读 `references/competitions/huawei-cup-2026.md`，再读项目 `AGENTS.md`、`STATUS.md`、`TASKS.md`、`DECISIONS.md`、`submission/SCHEDULE.md` 和 `ai_usage/AI_POLICY.md`。
2. 选题后读 `problem/problem-map.md`、`problem/dependency.md`；具体流程按 `references/team/workflow.md`。
3. 正式代码执行前读本成员 `config/execution-profile.local.yaml`；禁止提交该文件。
4. 调研读 `references/team/research-protocol.md`。跨成员/机器的异步任务读 `references/team/agent-handoff.md`；Git 协作读 `references/team/git-protocol.md`。

## 模型与子代理路由

- 开工先读项目 `AGENTS.md`；若项目存在模型路由文件，以它作为当前型号、effort 和批准池的唯一准据。本 Skill 不另设 Sol/Luna/Astra 等固定主从关系。
- 主 Agent 按任务复杂度、风险、时效、上下文和当前环境能力选型；用户明确指定的受支持路由优先。项目偏好不等于当前会话的实际型号，实际型号未知时不得猜填。
- 独立只读质检仍按原 Skill 的门禁调度，由未参与被审产物编写或修正的 Agent 执行。模型名称不同不自动证明独立；回执须固定输入、范围、实际 model/effort 和证据。
- 探索产物始终是候选，不是经验证事实；不得由子代理擅自冻结模型、公式、阈值、目标函数、约束或接口。是否允许固定质检之外的额外协作，服从用户授权和项目规则。
- 历史回执、AI 账本和旧任务中的实际模型保持原样；不得为了符合现行路由而批量改签。

默认链路：`EXPAND（可按项目规则并行探索） -> SELECT（主 Agent） -> DECIDE（人） -> SPEC/IMPLEMENT/RUN（主 Agent） -> VERIFY（主 Agent + 独立门禁）`。
跨成员/跨机器或异步任务使用 Handoff；同一会话不为机械拆工强制交接。

## 状态与责任

顶层状态以项目 `STATUS.md` 为准；每问依次 `RESEARCH -> MODEL -> INTERFACE -> SCAFFOLD -> IMPLEMENT -> RUN -> VERIFY -> PAPER -> PASS`。下游只消费已 PASS 或人工明确批准提前消费的上游 artifact，依赖 DAG 以 `problem/dependency.md` 为准。

三人各负责两题初筛；主 Agent 以数学、实现、论文风险三视角复筛，可按项目规则并行扩展资料；人类会议决定主选题与备选题，写 `DECISIONS.md`。A/B/C 是人的职责分工，不是模型分工。

进度答复必须读取 STATUS/TASKS、依赖图、活跃 Handoff/Gate 与必要结果，给出当前状态、阻塞链、每人下一步和下个门禁。不凭聊天记忆推进状态。

Agent 所在地、代码执行端和 artifact 存储解耦；正式 Python 统一 3.11.x，每台执行机器自行建隔离环境。`main` 只收已验证状态；短任务分支，更新 STATUS/TASKS 和关键 DECISIONS。

## 2026 华为杯硬约束

仓库必须 private，公开时禁止写入真实题目/数据/结果/论文；官方附件 3 Word 模板封面及四个 logo 不得替换；正式提交 PDF。AI 辅助数据分析和代码按附件 4 标注，最终正文人工改写与核验。MD5 提交后锁定 PDF 不得覆盖或重导出。详见 `references/competitions/huawei-cup-2026.md`。
