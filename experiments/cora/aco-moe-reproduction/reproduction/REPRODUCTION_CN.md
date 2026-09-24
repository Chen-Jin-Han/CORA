# ACO-MoE 核心实验复现说明

这套文件基于作者公开仓库的 Dreamer、ACO-MoE、VDCS 和 DMCGB 源码，目标是验证四个核心结论：

1. 冻结控制策略后，ACO 能提高动态 VDCS 下的控制回报；
2. RGB 修复、前景掩码和 MoE 路由各自有贡献；
3. ACO 不会明显破坏干净环境性能，并接近真实前景输入的上限；
4. ACO 对静态退化和 DMCGB 背景变化具有泛化能力。

## 文件作用

| 文件 | 作用 |
|---|---|
| `settings.sh` | 统一设置任务、种子、GPU、步数和输出目录 |
| `00_create_env.sh` | 创建独立 Conda 环境并安装锁定依赖 |
| `00_preflight.sh` | 检查 CUDA、依赖、EGL 渲染、模型参数和 84×84 前向 |
| `01_generate_vdcs_data.sh` | 为论文 8 个任务生成 84×84 配对数据 |
| `02_train_adapters.sh` | 并行训练 Full、Single、Mask-only、RGB-only |
| `03_train_policies.sh` | 在干净 DMC 上训练五种子 Dreamer 策略 |
| `04_eval_core.sh` | 评估 clean、raw、oracle、ACO 和所有核心消融 |
| `05_eval_static.sh` | 评估七种固定退化 |
| `06_eval_dmcgb.sh` | 评估 color-hard 和可选 video-hard |
| `07_collect_results.sh` | 生成 CSV 和 Markdown 汇总表 |
| `gpu_status.sh` | 查看 GPU 和计算进程 |
| `remote_phase1.sh` | 服务器首阶段：smoke、完整 ACO 数据/消融、一个正式控制任务 |

远程排队默认在首阶段通过后继续运行其余策略种子、核心评估、静态退化和
DMCGB color-hard；整个队列仍只使用设置中的一张 GPU。设置
`CONTINUE_FULL=0` 可以让任务在首阶段完成后停止。

## 上传

在 Windows PowerShell 中运行：

```powershell
cd "E:\Agent-Centric IP\aco-moe-code"
.\upload_to_gpu238.ps1
```

默认目标为：

```text
/home/gpuadmin/CST/CORA/aco-moe-reproduction
```

脚本会先检查远端目录。如果目录已经存在，会停止并显示其内容；确认它属于本项目后，使用：

```powershell
.\upload_to_gpu238.ps1 -UpdateExisting
```

上传包排除 `.git`、本地数据、检查点和日志，不会上传密码或私钥。

## 服务器首次运行

```bash
cd /home/gpuadmin/CST/CORA/aco-moe-reproduction
bash reproduction/00_create_env.sh
conda activate /data1/CST/CORA/aco-moe-reproduction/envs/aco_moe_repro
bash reproduction/00_preflight.sh --require-idle
```

只有四张指定 GPU 都低于默认占用阈值时，训练脚本才会启动。查看状态：

```bash
bash reproduction/gpu_status.sh
```

## 先做小规模贯通测试

```bash
SEEDS="0" ADAPTER_SEEDS="0" GPUS="0" \
DATA_TASKS_OVERRIDE="cartpole_swingup" \
POLICY_TASKS_OVERRIDE="cartpole_swingup" \
SAMPLES_PER_TASK=20 ACO_STEPS=2 \
ACO_MICRO_BATCH=2 ACO_GRAD_ACCUM=1 \
POLICY_STEPS=200 EVAL_EPISODES=1 \
bash reproduction/run_core_pipeline.sh
```

小规模测试输出不能用于论文结论，只用于确认服务器依赖、渲染、训练、检查点加载和评估链路正常。

## 正式核心实验

建议在 `tmux` 中分阶段执行：

```bash
tmux new -s aco-repro
conda activate /data1/CST/CORA/aco-moe-reproduction/envs/aco_moe_repro
cd /home/gpuadmin/CST/CORA/aco-moe-reproduction

bash reproduction/01_generate_vdcs_data.sh
bash reproduction/02_train_adapters.sh
bash reproduction/03_train_policies.sh
bash reproduction/04_eval_core.sh
bash reproduction/05_eval_static.sh
bash reproduction/07_collect_results.sh
```

如果已经准备 DAVIS 2017：

```bash
DAVIS_PATH=/path/to/DAVIS/JPEGImages/480p \
bash reproduction/06_eval_dmcgb.sh
```

未设置 `DAVIS_PATH` 时，DMCGB 脚本只运行 `color_hard`，不会错误启动 `video_hard`。

## 断点和输出

- ACO 保存 `moe_unet_latest.pth` 和 `moe_unet_best.pth`，中断后自动从 latest 继续；
- Dreamer 使用原仓库的 `latest.pt` 自动继续；
- 已产生 `eval_return` 的评估默认跳过；
- 已完整生成的数据集默认跳过；
- 检测到部分数据时停止，检查后通过 `OVERWRITE_PARTIAL_DATA=1` 明确重建；
- 所有标准输出保存在 `/data1/CST/CORA/aco-moe-reproduction/outputs/logdir/stdout/`；
- 汇总结果位于 `/data1/CST/CORA/aco-moe-reproduction/outputs/logdir/results/`。

汇总器还会生成 `core_comparisons.csv`，逐任务、逐种子计算相对 clean
性能、相对 foreground oracle 性能以及从 raw 到 clean 的性能缺口恢复率。

服务器系统盘当前只剩约 84 GiB，因此默认在策略成功完成并写入
`latest.pt`、`TRAINING_COMPLETE` 后删除该策略的 replay，在评估指标写入后
删除评估 episode。删除范围经过路径检查，只能位于本项目的
`/data1/CST/CORA/aco-moe-reproduction/outputs/logdir/` 下。若以后挂载了更大的独立数据盘，可设置
`PRUNE_REPLAY_AFTER_TRAIN=0 PRUNE_EVAL_EPISODES=0` 保留这些轨迹。

## 开源内容造成的限制

作者没有公开论文训练权重、原始五种子日志、完整基线代码和统一 VDCS+DMCGB 数据。公开数据生成器使用随机动作并只生成 VDCS 物理退化。因此：

- 本实验能够检验 ACO 的核心趋势和组件作用；
- 不能保证逐项得到论文表格中的相同数值；
- DMCGB 在这里是 VDCS 训练后进行的零样本迁移测试；
- DrQ-v2、SVEA、SODA、SGQN、SimGRL、Q2、FTR、RoboSuite 和 TD-MPC2 不包含在本复现包中。
