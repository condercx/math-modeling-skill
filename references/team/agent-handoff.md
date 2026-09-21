# Codex / DSH Handoff

默认通过仓库文件交换任务，避免依赖部署拓扑。

## 粒度规则
一个 Handoff 只覆盖一个可独立验收的工作单元，例如 `q2-baseline`、`q2-sensitivity`、`q4-route`。不要用一个 Handoff 同时实现多个子问题或多个 Gate；如需串联，拆成多个 packet 并显式写依赖。

## Request Packet
目录：`handoff/<task-id>/`，必须有 `REQUEST.md`、`STATUS.yaml`。
REQUEST 写：目标、Owner、创建方、只读输入、允许修改、禁止修改、执行环境要求、命令、验收标准、预期产物、上游 ref/commit。

## Result Packet
执行方写 `RESULT.md`：完成项、改动文件、实际命令、退出码、结果路径、失败项、异常、需要 Astra 判断的问题；然后将 STATUS 改为 `READY_FOR_REVIEW`。

正式运行还必须关联复现 manifest，至少记录 commit、执行环境、输入哈希、随机种子（适用时）、唯一命令和输出 artifact 哈希。优先复用上游 `repro_manifest.py`。

## 拓扑
- 同机/共享目录：直接读写 Handoff。
- 异机：Git push/pull 传文本、小结果、manifest。
- 大 artifact：RESULT 中记录位置与哈希，通过团队选定的 rsync/NAS/对象存储传输。
