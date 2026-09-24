# 初步复现结果

2026-09-07，在本机 Windows / RTX 4060 Laptop 8 GB 上完成。

**结论：已跑通数据生成、ACO-MoE 训练、Dreamer 短程训练和三组冻结评估。**
这是缩小规模的链路验证，尚未复现论文的控制性能或主表。

## 实际完成的工作

| 阶段 | 结果 |
|---|---|
| 环境 | Python 3.10、PyTorch 2.5.1+cu121、MuJoCo 2.3.7、dm-control 1.0.14；pip check 通过 |
| GPU | CUDA 前向、反向和 AdamW 更新均通过 |
| 仿真 | walker_walk / 64×64 / GLFW 正常渲染 |
| 数据 | 700 对：560 训练、140 验证，覆盖 7 种物理扰动 |
| 数据校验 | 所有样本尺寸正确，掩码为二值，gt_agent_only = gt × mask |
| 适配器 | 101 次更新，batch=4，7 专家，base_channels=16，三项损失权重 1:1:1 |
| Dreamer | 成功进行 GPU 更新；含预填充实际记录 800 环境步，最后一次日志记录 update_count=33 |
| 冻结评估 | 干净、扰动、扰动+ACO-MoE 均正常结束 |
| 不变性 | 策略文件 SHA-256 前后一致；评估目录没有生成训练 episode、latest.pt 或 best.pt |

适配器保留了共享编码器、专家路由、RGB 恢复和前景掩码两条输出分支，
训练未使用扰动类型标签。此次适配器参数量为 12,228,426；官方默认网络为
194,640,042，缩小网络是本次与正式实验的重要差异。

## 图像验证结果

140 个验证样本；损失均基于 RGB 的 [−1,1] 归一化空间。

| 指标 | 结果 |
|---|---:|
| 随机初始化，总损失，soft mixture | 1.15820 |
| 训练后，总损失，soft mixture | 0.40328 |
| 训练后，总损失，top-1 推理 | 0.51437 |
| 原始扰动 RGB 与 clean RGB 的 L1 | 0.17636 |
| top-1 恢复 RGB 与 clean RGB 的 L1 | 0.15100 |
| top-1 前景掩码全局 IoU | 0.68847 |

训练后的 soft mixture 总损失相比随机初始化下降约 65.2%。
Top-1 效果弱于 soft mixture，图像仍存在偏色、残余噪声和细肢缺失，短程训练尚不充分。
这些结果只说明该小模型在小验证集上学到了部分恢复和分割能力。

![七种扰动的验证样例](<E:/Agent-Centric IP/aco-moe-code/runs/local_initial/adapter_comparison.png>)

原始机器可读数据：`runs/local_initial/adapter_validation.json`。

## 控制评估结果

同一个策略、相同评估种子 10，每种条件只有 1 个 episode；每个 episode 上限为
100 个决策步（action_repeat=2，即 200 个仿真步），使用未归一化的累计回报。

| 输入条件 | 累计回报 |
|---|---:|
| 干净 RGB | 5.10258 |
| Markov 时变扰动 RGB | 5.06995 |
| Markov 时变扰动 RGB + ACO-MoE | 5.00708 |

**本次没有观察到控制收益。** 策略只进行了约 800 个环境步的短程运行，
回报很低，单种子单 episode 也不足以判断差异。这些数字不支持任何
“恢复了论文性能”或“方法无效”的结论，更不能与论文完整 episode 的回报直接比较。

策略文件 SHA-256：
`D9514A8D522FF92F4072A375975CB0264277E33E22FE07C778F4748D262FD625`

原始数据：`runs/local_initial/control_results.json` 和各 `eval_*/metrics.jsonl`。
干净评估目录保留了修复 close 方法之前的一次相同种子运行，汇总采用最后一次完成运行；
不能把重复记录当作独立评估种子。

## 本机资源和耗时

| 项目 | 实测 |
|---|---:|
| 适配器 probe：3 次更新，batch=4 | 0.77 秒 |
| 同一 probe 的 PyTorch peak allocated | 413.3 MiB |
| 同一 probe 的 PyTorch peak reserved | 448 MiB |
| 101 次适配器训练完整进程（含加载、验证、保存） | 16.11 秒 |
| Dreamer 短程训练完整进程 | 22.26 秒 |
| 三组评估完整进程 | 各约 6.8–7.7 秒 |

上述显存是缩小适配器的 PyTorch 分配量，不包含桌面、其他程序或全部驱动开销，
也不是完整 Dreamer/论文配置的显存峰值。策略运行期间的一次 nvidia-smi 采样为
整卡 3303 MiB；这只是采样值，不是峰值。
这些短程耗时不能线性推算论文全部实验预算：训练比例、批量、序列长度、图像尺寸
和网络规模均会影响吞吐。

## 后续复现的顺序

1. 先增加干净策略训练量，让 walker_walk 具备稳定行走能力，再判断恢复模块的控制收益。
2. 增加离线状态和适配器更新次数，检查恢复图像、top-1 掩码、路由利用率。
3. 使用完整 episode 和多个评估种子重复三组对照。
4. 对齐本地论文的网络/图像/数据/训练设置，再逐步扩大到多个任务。

此次没有启动长期后台训练。可运行步骤、与论文的差异和修复说明见
`LOCAL_REPRODUCTION.md`；精确依赖快照见 `requirements-local-lock.txt`。
原始官方提交：`0babf8a3fae864c10024bd4ca0f3a45c55ebc175`。
