# ACO / SMFA 三种子 ID 马尔可夫控制实验

- seed1：只读加载既有 OOD 实验的最终 checkpoint，仅补测控制。
- seed2、seed3：每模型各训练一次，15000步、batch128、RGB64、L1 + 0.05 FFT；数据、结构和硬路由推理保持一致，保留每500步验证。
- 七种ID由 `corruptions.VDCS` 动态切换，保持概率0.8、强度范围基础值±10%；复用第一轮实际实现，非逐扰动独立回合。
- 每模型每种子每任务10回合：600；共享Raw100、Clean100重新评估：总800。
- 不运行OOD、完整图像测试、DrQ、逐帧指标或自动续训。

## 路径与运行

代码：`/home/gpuadmin/CST/CORA/aco-smfa-markov`。
数据、日志、checkpoint、报告：`/data1/CST/CORA/aco-smfa-markov`。
Python：`/data1/CST/CORA/aco-smfa-pilot/env/bin/python`。

在代码目录运行 `python -u supervisor.py`。已有实例持有文件锁时新实例立即退出。
后台运行将日志重定向到数据目录的 `supervisor.log`。

GPU2运行ACO，GPU3运行SMFA，分别先独立batch128 smoke，再顺序训练seed2和seed3。
每30秒检查显存和子进程；ACO需至少6000MiB空闲，SMFA需至少10000MiB。
两路CPU控制与训练并行；新种子只在训练完成后开始评估。
不干预其他用户进程。出现子任务错误会停止本调度器子进程并记录failed，需诊断后恢复。
checkpoint、完成标记及逐回合JSONL支持恢复；源码hash变化会阻止未经检查的恢复。

## 查看进展与验收

读取数据目录 `status.json`、`supervisor.log`、`logs/` 和 `stages/`，并核验真实PID。
每个种子的输出由 `config_seedN.json` 中的experiment指定。
训练日志为 `logs/train_MODEL_seedN.log`，控制日志为 `logs/control_sN_TASK_CONDITION.log`。

最终 `summarize.py` 验证六个模型checkpoint（seed1来源只读）、800个唯一完整回合、每回合500决策和action_repeat2。
输出根目录 `results.json` 和 `REPORT.md`：主表对三个训练种子均值计算均值±种子间样本标准差，详细表保留各种子10回合均值±回合样本标准差。

已进行本地语法检查、配置校验及500帧配对马尔可夫序列一致性检查。GPU smoke与真实策略加载在服务器执行。
