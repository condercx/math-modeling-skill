# 人类团队进度与下一步建议

用户问“做到哪一步”“下一步是什么”“现在谁该干什么”时，必须证据驱动。

读取：
- `STATUS.md`
- `TASKS.md`
- `problem/dependency.md`
- 活动中的 `handoff/*/STATUS.yaml`
- 必要时查看 `results/`、`reviews/`

输出：
1. 当前顶层阶段及原因；
2. q1..qN 状态和 Owner；
3. 真正阻塞项及依赖链；
4. A/B/C 下一步，每人最多 2 项；
5. 当前可并行任务；
6. 下一个 Gate 与所需证据。

只有真实文件、运行日志、review 或 Gate 能推进状态。口头讨论、Agent 自述、未运行代码、未合并分支都不算完成。
