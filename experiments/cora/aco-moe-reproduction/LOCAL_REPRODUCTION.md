# 本机初步复现

目标是验证 walker_walk 的数据、适配器训练、Dreamer 训练和冻结评估链路。
这不是论文主表复现，不应据此声称达到论文的 95.3% 恢复率。

## 来源与环境

- 官方仓库：https://github.com/fangzr/aco-moe-code
- 原始提交：0babf8a3fae864c10024bd4ca0f3a45c55ebc175
- 硬件：RTX 4060 Laptop 8 GB、i7-14650HX、约 16 GB RAM。
- 本次采用 Windows 原生 Python 3.10，虚拟环境为项目内 `.venv`。
- 渲染后端为 GLFW；Linux 无显示器环境应改用 EGL。
- PyTorch 2.5.1 CUDA 12.1。其他依赖见 `requirements-local.txt`。
- 使用 dm-control 1.0.14 + MuJoCo 2.3.7 配对，偏离官方 requirements 中的
  dm-control>=1.0.18。原文件同时要求 MuJoCo<3，存在版本配对问题。

## 分阶段运行

在项目目录的 PowerShell 中依次执行：

```powershell
./scripts/run_local.ps1 probe
./scripts/run_local.ps1 data
./scripts/run_local.ps1 adapter
./.venv/Scripts/python.exe -m scripts.evaluate_local_adapter
./scripts/run_local.ps1 policy
./scripts/run_local.ps1 eval
```

数据生成默认拒绝覆盖已有数据；再次运行前请使用不同的输出目录。
策略训练会从同一日志目录的 latest.pt 续训；做独立实验时须换日志目录。
适配器训练没有自动续训功能，再运行 adapter 会从头训练并覆盖该阶段权重。

## 初步配置和限制

| 项目 | 本次设置 |
|---|---|
| 任务 | walker_walk |
| 图像 | 64×64 |
| 离线数据 | 100 个状态，各生成 7 种扰动，共 700 对 |
| 数据划分 | 前 80 个状态训练，后 20 个状态验证；所有扰动使用一致划分 |
| 适配器 | 7 专家，base_channels=16，batch=4，101 次更新 |
| 损失 | RGB、mask、agent-centric 权重均为 1；无扰动标签监督 |
| 策略 | 官方默认网络宽度，batch=4，序列长度=32，train_ratio=16 |
| 策略预算 | steps=600；官方循环会包含 prefill/评估间隔造成的步数差异，以日志为准 |
| episode | 200 个仿真步上限，action_repeat=2，即 100 个 agent steps |
| 初步评估 | seed=10，每种条件 1 个 episode |

论文使用更大网络/数据/批量、更长策略训练和多种子评估。
本次 600 步级策略不足以学会稳定行走，三组回报只验证接口，不能判断论文结论。
图像验证指标使用 [−1,1] 归一化空间，不能直接与 [0,1] 空间的 L1 比较。

## 修复记录

1. Windows 无 symlink 权限时，数据划分回退为文件复制。
2. 适配器加载优先读取 args.num_experts，不再要求无标签权重不存在的 degradation_types。
3. 策略中的适配器调用显式启用 top-1 路由。
4. 新增 eval_only 和 policy_checkpoint：直接读取策略、跳过预填充/训练/优化器加载，
   不复制 replay，不改写策略 checkpoint；缺少策略权重立即报错。
5. eval/log 间隔换算后最小为 1，避免整数除法产生 0。
6. 冻结评估只允许新增适配器参数缺失，策略本身的参数不匹配仍报错。
7. CUDA 架构名称未精确匹配时用真实 kernel 执行检查，修复 sm_89 被误判后回退 CPU 的问题。
8. DMC 环境补充幂等 close 方法，释放 MuJoCo 资源，修复评估结束时的 AttributeError。
9. 权重加载失败只输出错误首行和有限数量的缺失键，避免新增适配器时打印数千个预期缺失键。

## 输出

- `runs/local_initial/probe.json`：GPU、参数量和显存实测。
- `runs/local_initial/adapter_validation.json`：随机初始化与训练后的验证损失。
- `runs/local_initial/adapter_comparison.png`：七种扰动的可视化。
- `runs/local_initial/*.log`：各阶段控制台日志。
- `checkpoints/local_initial/adapter/`：适配器权重。
- `logdir/local_initial/clean/`：Dreamer checkpoint 和训练日志。
- `logdir/local_initial/eval_*/metrics.jsonl`：三组冻结评估。
- `runs/local_initial/frozen_policy_check.json`：策略文件不变性检查。

## 下一阶段

根据短程实测选择资源可承受的配置，增加离线数据、适配器更新和策略步数。
先让干净策略学会行走，再使用完整 episode、多评估种子比较三组回报。
对齐论文时逐项核对图像尺寸、专家数、网络宽度、掩码生成方式、数据覆盖、
训练预算、扰动协议与回报统计；不能把当前缩小配置直接作为论文配置。
