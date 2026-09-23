# 跨成员/跨机器异步 Handoff

同一 Sol 会话直接推进 SPEC/IMPLEMENT/RUN/VERIFY；只有跨成员、跨机器或异步任务才使用 `handoff/<task-id>/`，含 `REQUEST.md`、`STATUS.yaml`、`RESULT.md`。一个 Packet 只覆盖一个独立可验收单元。

REQUEST 写目标、Owner、创建方、只读输入、允许/禁止修改、执行环境、命令、验收标准、预期产物、上游 ref。执行方写 RESULT：改动文件、实际命令及退出码、结果路径、失败/异常和需 Sol/人决定的问题，状态转 READY_FOR_REVIEW。正式运行须关联 commit、环境、输入与输出哈希、随机种子（适用时）和复现命令。

异机以私有 Git 传文本与小结果；大 artifact 记录路径/哈希，按团队批准的传输方式同步。Luna 子代理的即时探索可直接在任务回执交付，不必机械创建跨主机 Handoff。
