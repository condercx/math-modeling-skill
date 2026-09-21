# Git 协作协议

- 使用短任务分支：`q1/research-*`、`q2/model-spec`、`q2/implementation`、`q3/experiment-*`、`paper/q2-results`。
- 不建立长期 `member-a/member-b/member-c` 分支。
- `main` 只保留已验证、可被其他问题依赖的版本。下游只读 main 中已通过 Gate 的 interface/result。
- 建议 commit：`model(q2): freeze prediction interface`、`feat(q2): implement baseline solver`、`result(q2): add sensitivity sweep`。
- 不进 Git：个人 execution profile、API key、SSH key、大 checkpoint、超大原始数据、临时缓存。
- 状态推进时同步更新 STATUS/TASKS；关键决定写 DECISIONS。
