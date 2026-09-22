---
name: math-modeling-team
description: 面向三人数学建模竞赛团队的协作扩展。覆盖 A-F 选题、Q1..QN 子问题依赖、AnySearch 调研、Codex/Astra 高价值推理、DSH/Flash 低成本执行、代码脚手架与交接、异构本地/远程 Python/MATLAB/GPU 执行、Git 协作、论文证据链、阶段门禁，以及回答“现在做到哪一步/下一步做什么”。团队同时使用 Codex 与 DeepSeek Harness 或需要跨成员/跨机器协作时加载。
---

# 三人数学建模团队扩展

这是原 `math-modeling` Skill 的团队编排层。原 Skill 继续负责算法、建模、绘图、论文和质量门禁；本扩展负责比赛状态、成员协作、Astra/Flash 路由、AnySearch、Agent Handoff 和异构执行环境。

## 启动

进入团队竞赛项目后依次：
1. 读取 `references/team/workflow.md`。
2. 读取项目的 `STATUS.md`、`TASKS.md`、`DECISIONS.md`。
3. 读取 `problem/dependency.md`，拿到正式题目后维护 Q1..QN 依赖 DAG。
4. 执行代码前读取本成员 `config/execution-profile.local.yaml`；此文件不得提交 Git。
5. 调研读取 `references/team/research-anysearch.md`。
6. Codex/DSH 交接读取 `references/team/agent-handoff.md`。
7. Git 操作读取 `references/team/git-protocol.md`。

## 模型路由

- Astra/Codex：A-F 复筛、问题依赖、模型收敛、数学推导、代码架构、核心算法、复杂 Debug、结果判断、跨问整合、最终 Review。
- Flash/DSH：AnySearch 广搜、附件/资料整理、EDA、数据清洗、常规代码、批量实验、绘图与格式整理、Astra 明确定义的 TODO。
- 默认研究链：`EXPAND -> SELECT -> DECIDE -> EXECUTE -> VERIFY`。
- 默认编码链：`SPEC -> SCAFFOLD -> HANDOFF -> IMPLEMENT -> RUN -> VERIFY`。
- Flash 遇到模型歧义、会改变结论的实现选择、异常结果无法解释、阈值/约束需改变、核心算法需重写时必须停止并升级给 Astra。

## 比赛状态机

顶层：
`PREP -> PROBLEM_SELECTION -> PROBLEM_DECOMPOSITION -> QUESTION_PIPELINES -> CROSS_QUESTION_INTEGRATION -> FINAL_REVIEW -> FROZEN`

每个 qN：
`RESEARCH -> MODEL -> INTERFACE -> SCAFFOLD -> IMPLEMENT -> RUN -> VERIFY -> PAPER -> PASS`

下游只消费已经 PASS 或经人明确批准提前消费的上游 artifact。依赖以 `problem/dependency.md` 为准。

## 选题与子问题

- A-F 初筛：三人各负责两题，Flash + AnySearch 统一模板宽搜。
- 二次筛选：三次 Astra 深审，分别从数学模型、数据/实现、论文/风险角度看全部题目。
- 人类会议决定主选题和备选题，并写入 `DECISIONS.md`。
- 选题后先拆 Q1..QN，记录输入、输出、约束、指标、上游依赖、下游消费者、Human Owner 和状态，再决定可并行与必须串行的节点。

## 人类进度助理

用户问“现在做到哪一步”“下一步是什么”“谁该做什么”时，不得凭聊天印象回答。必须读取：
- `STATUS.md`
- `TASKS.md`
- `problem/dependency.md`
- 活跃的 `handoff/*/STATUS.yaml`
- 必要时查看 `results/`、`reviews/`

输出：当前顶层阶段、q1..qN 状态、真正阻塞链、A/B/C 各自下一步（每人最多 2 项）、可并行任务、下一个 Gate。

## 异构环境

Agent 位置、代码执行位置、artifact 存储位置三者解耦。每人维护本地 execution profile；允许本地/远程、Python/MATLAB、CPU/GPU 和不同工作路径。Skill 不得写死解释器、SSH 主机或 Conda 环境。

## Git

- `main` 只放已经验证、可供后续问题依赖的状态。
- 使用短任务分支：`q2/model-spec`、`q2/implementation`、`paper/q2-results`。
- 不建立 A/B/C 长期角色分支。
- 状态推进时同步更新 `STATUS.md` 和 `TASKS.md`；关键决策写 `DECISIONS.md`。

完整细则见 `references/team/`。


## 2026 华为杯官方合规模式

当目标竞赛为“华为杯”第二十三届中国研究生数学建模竞赛（2026）时，在启动步骤最前面额外读取 `references/competitions/huawei-cup-2026.md`，并把其中要求视为硬约束。

必须额外执行：
1. 确认比赛工作仓库为 private；public 时将 `PREP` 标记为 BLOCKED，禁止写入真实赛题、数据、结果和论文。
2. 项目内预留并维护 `official/2026/`、`paper/template/`、`paper/working/`、`paper/checkpoints/`、`paper/export/`、`submission/`、`attachments/`、`ai_usage/`。
3. 使用官方附件 3 模板作为 Word 主工作稿起点；首页封皮不可删除，4 个 logo 不得替换；正式提交物是 PDF。
4. 任何 AI 辅助数据分析、程序代码和无法确认来源的模型/公式按 2026 附件 4 执行标注；正式写作必须经过 Human Rewrite/Review gate。
5. MD5 提交后把对应 PDF 视为不可变 artifact；Agent 不得覆盖、重新导出或“顺手修正”。
6. 所有 2026 时间、文件命名和附件规则以 `references/competitions/huawei-cup-2026.md` 为准。
