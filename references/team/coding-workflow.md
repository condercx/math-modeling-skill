# 代码工作流

主 Agent 读取模型 spec 与 interface，建立可运行骨架、函数签名、schema、测试和配置，随后实现、运行并验证。SCAFFOLD 状态可保留用于可运行最小链路，不绑定某个模型或生成按模型命名的 TODO。

跨成员/跨机器或异步任务才写 Handoff Packet，明确只读输入、允许修改的文件、验收标准和人工升级点。子代理可处理边界清晰的探索性或重复整理任务；若涉及代码改动须分配隔离写域、由主 Agent 复核，不得自行改变模型关键定义。

正式 run 生成/关联 reproducibility manifest：commit、环境、输入哈希、随机种子（适用时）、唯一复现命令、输出 artifact 哈希；优先调用 `references/roles/编程手/scripts/repro_manifest.py`。主 Agent 检查公式-代码一致性、边界、异常、泄漏、稳定性和可解释性；独立 P1/P2 门禁不因单模型而取消。
