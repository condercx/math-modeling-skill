# 团队比赛状态机

## 顶层状态
| 状态 | 核心任务 | 完成证据 |
|---|---|---|
| PREP | Skill、AnySearch、Git、个人执行环境 | 三人 profile 可用，最小流程 smoke test |
| PROBLEM_SELECTION | A-F 初筛、三 Astra 复筛、人工选题 | selection/final-selection.md + DECISIONS.md |
| PROBLEM_DECOMPOSITION | 拆 Q1..QN、依赖 DAG、Owner、接口 | problem/problem-map.md + dependency.md |
| QUESTION_PIPELINES | 各 qN 按子状态推进 | STATUS/TASKS + Gate 证据 |
| CROSS_QUESTION_INTEGRATION | 统一符号、接口、结果、论文故事线 | reviews/full-model.md |
| FINAL_REVIEW | 三 Astra 交叉审查、复现、格式、AI 记录 | reviews/final/ 无阻断项 |
| FROZEN | 提交版冻结 | Git tag + 最终 artifact 哈希 |

## 每个 qN
1. RESEARCH：Flash + AnySearch 宽搜。
2. MODEL：Astra 收敛模型；人确认关键假设与取舍。
3. INTERFACE：固定输入/输出/单位/文件格式，尤其是后问会消费时。
4. SCAFFOLD：Astra 写可运行骨架、难点代码、测试入口、TODO。
5. IMPLEMENT：Flash 仅按 TODO 补常规实现。
6. RUN：按 execution profile 真实运行，保存日志/结果/manifest。
7. VERIFY：Astra 审核公式-代码-结果、边界、异常、泄漏、稳定性。
8. PAPER：只把已验证证据写入该问论文段落。
9. PASS：允许作为下游依赖；发生实质修改后 PASS 失效。

## 与上游 math-modeling 门禁的映射
团队状态机不替代上游门禁：
- MODEL / INTERFACE 完成后，进入正式实现前应满足上游 `M1`。
- SCAFFOLD / IMPLEMENT 的最小链路跑通后、全量实验前满足 `P1`。
- RUN / VERIFY 完成并冻结正式结果、图和复现材料后满足 `P2`。
- PAPER 进入长篇正文前满足 `W1`，最终论文冻结前满足 `W2`。
- 团队层 `PASS` 只有在当前子问题所需的上游 Gate 已通过时才成立。

## 并行规则
- 只有 DAG 中上游依赖已 PASS 的节点可进入依赖性实现。
- Research 可提前，但不得把未 PASS 的上游数值当事实。
- 论文随各 qN 同步写，不等全题结束。
- 大实验可并行，但模型、指标、参数范围先冻结。
