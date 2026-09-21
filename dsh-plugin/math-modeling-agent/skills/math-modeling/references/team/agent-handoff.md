# Codex / DSH Handoff

默认通过仓库文件交换任务，避免依赖部署拓扑。

## Request Packet
目录：`handoff/<task-id>/`，必须有 `REQUEST.md`、`STATUS.yaml`。
REQUEST 写：目标、Owner、创建方、只读输入、允许修改、禁止修改、执行环境要求、命令、验收标准、预期产物、上游 ref/commit。

## Result Packet
执行方写 `RESULT.md`：完成项、改动文件、实际命令、退出码、结果路径、失败项、异常、需要 Astra 判断的问题；然后将 STATUS 改为 `READY_FOR_REVIEW`。

## 拓扑
- 同机/共享目录：直接读写 Handoff。
- 异机：Git push/pull 传文本、小结果、manifest。
- 大 artifact：RESULT 中记录位置与哈希，通过团队选定的 rsync/NAS/对象存储传输。
