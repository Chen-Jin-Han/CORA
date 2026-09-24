# ACO-RGB 与 SMFA-RGB：十任务正式实验（一个种子）

本目录是独立实验项目，不覆盖 `aco-smfa-pilot`。代码已编写；交付本身不代表已在服务器训练或验证全部十个策略。

## 1. 已固定的最新协议

| 项目 | 固定配置 |
|---|---|
| 比较模型 | ACO-RGB、SMFA-RGB，不引入其他网络 |
| 输出/损失 | 仅完整 RGB；L1；无掩码分支、标签、损失或前景合成 |
| 任务 | walker_walk/run/stand、hopper_stand、quadruped_run、finger_turn_hard、cartpole_swingup_sparse、cup_catch、reacher_easy/hard |
| 策略 | 每任务已有 seed0，公开 JAX DreamerV3 严格加载、全部冻结 |
| 还原模型训练 | 每模型仅 seed 0；从头训练；15,000 次优化器更新 |
| batch | 有效 128，默认真实 batch 128；两模型相同 micro-batch |
| 优化器 | AdamW，lr=1e-4，weight_decay=1e-4，betas=(0.9,0.999)，eps=1e-8，无调度 |
| 输入 | 64×64 RGB，[-1,1]；同步水平翻转 |
| 数据 | 每任务训练4,500对、验证500对；十任务45,000/5,000 |
| 图像测试 | 每任务另采1,000张干净图×7扰动，共70,000对；另检查10,000张干净输入 |
| 控制测试 | 10任务×4条件×10完整回合=400；clean/raw/aco/smfa |
| 验证 | 每500步完整验证，主结果固定step15000；不使用验证最优模型替换主结果 |
| 禁止自动扩展 | 不追加种子、不延长训练、不做OOD/DMC-GB、不训练Dreamer |

**5,000是每任务七种扰动合计的配对样本数，不是每类5,000，也不是5,000×7。** 独立图像测试集才逐干净帧扩展七种扰动。

ACO-RGB保留共享U-Net编码器、9个RGB专家和路由器；训练软混合、验证/推理实际top-1，仅计算选中专家。SMFA-RGB使用8个FMB、36通道、同分辨率残差RGB输出。两者都没有可训练掩码参数。

## 2. 与论文的关系及边界

- ACO七种VDCS算子：rain .6、fog/haze .6、snow .6、motion_blur .35、gaussian_noise .5、low_light .7、jpeg .7。
- 动态测试：停留概率.8，其余类别均分.2；初始/切换强度为基础值±10%；持续段随机游走标准差.02；每回合重置。
- `corruptions.VDCS`按公式先输出初始状态，再在下一帧更新；像素随机性使用独立的算子实例，不依赖输入内容。与旧预实验逐帧随机实现不逐像素相同；两模型在本轮使用同一实现。算子内容来自固定ACO本地代码快照。
- ACO原论文84×84、batch1024、三项损失；本轮64×64、batch128、仅RGB L1。因此必须称为ACO-RGB改造对照，不能称完整ACO复现。
- 原文每任务5,000与伪代码循环存在计数歧义，本项目固定采用正文总量解释。9:1为训练/验证比例，独立测试集是本轮补充。
- 轨迹先划分；不同split不共享episode seed。同一轨迹每5决策抽帧，每回合最多100帧；策略/随机动作交替回合，因取整不保证精确50%。
- 基于BasicSR的uint8 PSNR-Y/SSIM-Y与RGB指标，BT.601 Y转换、11×11 Gaussian SSIM、crop_border=0。无超分倍率裁边。
- 单模型训练种子的回合置信区间不代表跨训练种子稳定性。固定checkpoint策略不等于ACO原论文训练策略。
- 当前MAC统计只包含实际执行Conv2d/Linear，FLOPs=2×MACs，不冒充包含所有算子的完整FLOPs。

## 3. 文件说明

`config.json` 唯一正式协议与路径；`models.py` RGB-only网络；`data.py` 采集/固定配对/审计；`engine.py` 训练、验证、图像测试、效率；`control.py` 完整回合控制；`report.py` 汇总与曲线；`pipeline.py` 独占锁、GPU等待、子进程及断点；`experiment.py` 分阶段入口；`tests.py` 本地CPU检查；`vendor/` 固定上游代码。

来源与已有快照见 `source_manifest.json`。其哈希描述旧预实验引入时的来源，不是本次改造文件哈希；正式运行另记录 `source_hashes.json`、策略权重/配置SHA256以及数据文件SHA256。依赖锁通过bootstrap输出。

## 4. 上传代码（在本地PowerShell执行）

先确认SSH alias `gpu-238`可用。所有认证交给SSH，不在代码中保存密码。

```powershell
cd 'E:\Agent-Centric IP'
ssh gpu-238 'ls -ld /home/gpuadmin/CST/CORA/aco-smfa-rgb /data1/CST/CORA/aco-smfa-rgb 2>/dev/null; df -h /data1'
```

若同名项目已存在，先检查内容，不要直接覆盖正在运行的版本。新部署可上传交付的源码包：

```powershell
scp '.\aco-smfa-rgb-source.tar.gz' gpu-238:/home/gpuadmin/CST/CORA/
ssh gpu-238 'test ! -e /home/gpuadmin/CST/CORA/aco-smfa-rgb && tar -xzf /home/gpuadmin/CST/CORA/aco-smfa-rgb-source.tar.gz -C /home/gpuadmin/CST/CORA'
```

源码包不包含策略权重、数据或环境。服务器目录：

```text
/home/gpuadmin/CST/CORA/aco-smfa-rgb                 # 代码
/data1/CST/CORA/aco-smfa-rgb/env                    # 可选独立环境
/data1/CST/CORA/aco-smfa-rgb/cache                  # 缓存
/data1/CST/CORA/aco-smfa-rgb/<experiment>/          # 全部实验输出
```

## 5. 准备十个策略checkpoint

当前config.policy_root为 `/data1/CST/CORA/aco-smfa-rgb/policies`。部署时在此放置补传的七任务，并为已存在的三个策略建立只读使用的目录链接，不修改旧权重。
预实验只验证过三个任务，不保证这个目录已含全部十个。正式运行前逐一确认：

```text
<policy_root>/dmc_walker_walk/seed0/run/config.yaml
<policy_root>/dmc_walker_walk/seed0/run/ckpt/latest
<policy_root>/dmc_walker_walk/seed0/run/ckpt/<latest内容>/agent.pkl
```

其余任务相同结构。若需要独立上传本地全部已有策略，先在服务器检查目的目录，然后：

```powershell
ssh gpu-238 'mkdir -p /data1/CST/CORA/aco-smfa-rgb/policies'
scp -r '.\dmc_vision_local_v1' gpu-238:/data1/CST/CORA/aco-smfa-rgb/policies/
```

这会传输较大的模型文件（含walker_run其他种子，但程序只读seed0）。然后把config.policy_root改为
`/data1/CST/CORA/aco-smfa-rgb/policies/dmc_vision_local_v1`。
首次运行前允许调整路径；启动绑定协议之后不要原地修改路径/参数。

## 6. 安装与启动（在服务器执行）

```bash
cd /home/gpuadmin/CST/CORA/aco-smfa-rgb
bash bootstrap.sh
RGB_PYTHON=/data1/CST/CORA/aco-smfa-rgb/env/bin/python
"$RGB_PYTHON" experiment.py preflight --config config.json
nvidia-smi
```

`preflight`检查十任务权重文件、config、尺寸、任务和哈希；真实294叶等严格结构与数值加载在每任务采集/控制进程中执行，任一不匹配立即停止，绝不使用随机初始化策略代替。

也可以复用旧环境，避免重新安装：先运行旧环境的tests并检查`pip check`，需要安装缺少的matplotlib等依赖，再设置：

```bash
export RGB_PYTHON=/data1/CST/CORA/aco-smfa-pilot/env/bin/python
"$RGB_PYTHON" -m pip check
"$RGB_PYTHON" tests.py
```

复用旧环境不等于代码已验证全部依赖；优先推荐独立bootstrap环境。`requirements.txt`提供版本约束，安装时可能因驱动/包索引而失败，应先处理安装错误，不要直接启动。

正式启动（默认顺序CPU控制）：

```bash
bash launch.sh --gpu auto --control-workers 1
```

若CPU和内存资源允许，可从一开始选择最多4个独立控制进程，例如：

```bash
bash launch.sh --gpu auto --control-workers 2
```

选择固定GPU也仍需等待空闲：`--gpu 3`。每10秒检查显存<2000MiB且利用率<15%；不抢占、不终止其他人的任务。空闲检查不是调度器预留，其他用户仍可能在之后启动任务；共享负载下效率数据需要择时重测。

`nohup setsid`使服务器任务独立于SSH和Codex额度存活，但不保证跨服务器重启。无需依赖聊天轮询。

## 7. 实际执行顺序

1. 十任务策略文件/config预检。
2. 逐任务严格加载策略并生成train/val/test；完成的数据split跳过。
3. 检查数据数量、文件哈希、轨迹互斥、帧ID唯一、类别均衡；报告跨split像素完全重复数量（自然相同初始渲染可能出现，不默默删除）。
4. 先完成clean/raw共200回合。
5. 等GPU，训练ACO-RGB一次、图像测试、效率测试；完成ACO的100回合。
6. 同样运行SMFA-RGB一次及其100回合。
7. 严格确认总400回合、每模型15,000步、每模型70,000图像对、30个验证点，生成报告并退出。

全过程只训练两个模型，不训练策略，不自动续训。数据集从头新建；不混用旧预实验图像或模型。

## 8. 监控、失败与恢复

```bash
RGB_RUN=/data1/CST/CORA/aco-smfa-rgb/rgb10_seed0_b128_s15000_ep10_v1
cat "$RGB_RUN/status.json"
tail -n 30 /data1/CST/CORA/aco-smfa-rgb/launcher/pipeline.log
tail -n 5 "$RGB_RUN/logs/train_aco.log"
ps -ef | grep '[p]ipeline.py\|[e]xperiment.py'
```

状态文件需结合真实进程判断；不要仅因为日志暂时未输出就重复启动。独占锁会阻止第二个pipeline执行。

- 训练每500步原子保存模型、优化器、GradScaler、随机状态和历史；失败后最多重做不足500步。
- 每一步的数据索引/翻转由独立step seed决定，两模型一致、恢复顺序一致，不受模型初始化消耗随机数影响。
- 控制每完成一个回合就保存；恢复跳过已完成回合。中断的回合从头再跑，不把部分回合当正式结果。
- 图像评测中断会重做该模型的图像评测；不会重复训练。
- 再次运行同一 `launch.sh` 恢复。源码/配置/策略哈希发生变化则拒绝混用结果。
- batch128若OOM：进程会报错停止，不悄悄缩batch。先确认没有相关任务仍运行，再在配置中将micro_batch设32或16（有效batch仍128），并换一个experiment名称；两模型均采用同一micro-batch。BatchNorm使梯度累积不等价于真实batch128，报告中必须披露。
- 非有限损失或梯度会停止，不把GradScaler跳过的更新计为有效训练。

不要在pipeline运行时额外执行同一阶段的手工命令。手工分阶段入口不提供跨pipeline互斥调度。

## 9. 输出与解读

```text
protocol.json / source_hashes.json / policy_manifest.json
datasets/<task>/<train|val|test>/{clean.npy,input.npy,metadata.npz,complete.json}
audit/<task>/checkpoint_load.json
data_audit.json
checkpoints/<aco|smfa>/{last.pt,step_00500.pt,...,step_15000.pt,best_validation.pt,history.json}
images/<aco|smfa>/{summary.json,per_image.csv,panel_*.png}
control/<task>/<clean|raw|aco|smfa>/{episodes.jsonl,summary.json}
efficiency/{aco,smfa}.json
curves.png / comparison.json / REPORT.md
```

主结果仅加载`last.pt`且强制step15000。`best_validation.pt`只保存供参考，不用于正式测试。
报告晚期验证PSNR均值变化（13000–15000与10000–12000窗口比较），不自动判断已经收敛，也不触发追加训练。
ACO训练损失为软路由/AMP、验证为top-1/FP32，两条曲线不能直接将差距全部解释为过拟合；判断以验证趋势为主。
单种子、每条件10回合用于第一轮全任务实验；尤其高方差任务不能据此宣称稳定显著优势。

## 10. 时间、磁盘及本地验证边界

预算：两模型训练12–20 GPU小时；图像/效率1–4 GPU小时；400回合按历史速度顺序约6–12小时（任务差异、负载会改变）；数据采集另计。50–100GB空间预算足够保留检查点及数据（无全回合视频）。这是预估，不是正式RGB-only测量。

本地`tests.py`验证：两网络RGB形状和梯度、无mask参数、ACO每图仅执行一个专家、固定配对与同步翻转、七扰动与Markov复现性、Y/RGB指标与SMFANet仓库BasicSR纯函数逐值对照。
不在交付时声称已通过服务器CUDA batch128测试或十任务完整仿真；服务器preflight/首次采集会实际验证依赖与策略。

本地重建源码包：`python package.py`；只打包源码和必要文本，不打包checkpoint、PDF、数据或大模型资源。
