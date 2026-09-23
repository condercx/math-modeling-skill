# 团队比赛状态机

| 状态 | 核心任务 | 完成证据 |
|---|---|---|
| PREP | Codex Skill、Git、个人执行环境、官方材料 | 三人 profile/附件核验、最小流程 smoke test；不要求 DSH/AnySearch |
| PROBLEM_SELECTION | A-F 三人初筛、Sol 三视角复筛、人工选题 | selection/final-selection.md + DECISIONS.md |
| PROBLEM_DECOMPOSITION | 拆 Q1..QN、依赖 DAG、Owner、接口 | problem/problem-map.md + dependency.md |
| QUESTION_PIPELINES | 各 qN 按子状态推进 | STATUS/TASKS + Gate 证据 |
| CROSS_QUESTION_INTEGRATION | 统一符号、接口、结果、论文故事线 | reviews/full-model.md |
| FINAL_REVIEW | 独立审查、复现、格式、AI 记录 | reviews/final/ 无阻断项 |
| PAPER_CHECKPOINT → CONTENT_FROZEN → MD5_READY → MD5_LOCKED → PDF_UPLOADED → ATTACHMENT_DONE → ARCHIVED | 按当届提交规则冻结/上传 | submission/ 与官方系统证据 |

每个 qN：`RESEARCH（Sol 可派 Luna max 探索） -> MODEL（Sol + 人） -> INTERFACE -> SCAFFOLD -> IMPLEMENT -> RUN -> VERIFY -> PAPER -> PASS`。

M1 在正式实现前；P1 在全量实验前；P2 在正式结果冻结后；W1 在长篇正文前；W2 在最终论文冻结前。独立质检仍须未参与被审产物的写入者执行；发生实质变更后 PASS 失效。下游依赖只消费已 PASS 或人工批准提前消费的 artifact。研究可先行，但未 PASS 的上游数值不能当事实。论文随每问推进，模型/参数冻结后方可并行大实验。
