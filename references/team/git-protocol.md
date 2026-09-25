# Git 协作协议

- 可使用短任务分支或独立 worktree；不强制分支命名、PR、审核或交接。
- 不删除、覆盖其他人的未提交工作；不执行 `reset --hard` 或 force-push。
- `main` 的候选代码或中途合入不等于已验证；下游按实际使用的 commit、路径和结果定位输入。
- 建议 commit：`model(q2): freeze prediction interface`、`feat(q2): implement baseline solver`、`result(q2): add sensitivity sweep`。
- 不进 Git：个人 execution profile、API key、SSH key、大 checkpoint、超大原始数据、临时缓存。
- 需要协作时直接记录实际任务、输入、命令、结果和限制；不要求维护 `STATUS/TASKS/DECISIONS` 状态机。
