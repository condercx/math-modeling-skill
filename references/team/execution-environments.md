# 异构执行环境

## 三层解耦
1. Agent location：Codex 主 Agent/可选子代理在哪里。
2. Execution backend：代码在哪里运行。
3. Artifact storage：数据/模型/结果在哪里保存。

三者不得绑死。

每人复制 `config/execution-profile.example.yaml` 为 `execution-profile.local.yaml` 并自行填写；该文件 gitignore。允许 local/shared/ssh，语言允许 python/matlab/mixed，计算资源允许 cpu/cuda/other。不得把密钥写进 profile；SSH 用 host alias。

正式实验记录：成员、机器标签、commit、语言/版本、环境名、CPU/GPU、随机种子、输入哈希、命令、输出路径、artifact 哈希。

大计算分配给最合适的机器；其他成员无需完整复制大训练，但必须能核对配置、smoke test、日志和产物哈希。
