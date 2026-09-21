# 代码工作流

## Astra Scaffold
读取 model spec 和 interface 后生成可运行骨架：目录、入口、函数签名、schema、核心算法难点、测试入口、日志、配置，以及清晰的 `TODO_FLASH_*`。不必写完机械代码，但骨架必须能 smoke-run 或清楚指出唯一阻塞。

## Flash Implement
仅处理一个细粒度 Handoff 中允许的 TODO。优先负责清洗、IO、循环、常规指标、批量配置、绘图和重复性代码。不得自行改变模型公式、目标函数、约束、阈值或接口。

## Run & Verify
真实运行后写 Result Packet。正式 run 必须生成或关联 reproducibility manifest，至少含 commit、环境、输入哈希、随机种子（适用时）、唯一复现命令和输出 artifact 哈希；优先调用上游 `references/roles/编程手/scripts/repro_manifest.py`。

Astra 检查公式-代码一致性、边界、异常、数据泄漏、数值稳定性和结果可解释性。核心问题由 Astra 修，机械返工再交 Flash。

团队层 VERIFY 不替代上游 `P1/P2`：最小可运行链路通过 P1 后再做全量实验，正式结果冻结并通过 P2 后才允许该子问题进入最终 PAPER/PASS。
