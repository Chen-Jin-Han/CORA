# Core paper reproduction package

This directory turns the released repository into a reproducible experiment
pipeline for the paper's central claims. It deliberately keeps all generated
data, checkpoints, logs, and results outside the source files.

## Scope

The core matrix covers:

- eight paper VDCS tasks and five policy seeds;
- clean, Markov VDCS without preprocessing, foreground oracle, and full ACO;
- capacity-matched single expert, mask-only, RGB-only, and w/o-repair ablations;
- seven fixed single-degradation evaluations;
- DMC-GB color-hard and optional DAVIS video-hard evaluation;
- CSV and Markdown aggregation from `metrics.jsonl`.

It does not manufacture unavailable author checkpoints or baseline results.
DrQ-v2, SVEA, SODA, SGQN, SimGRL, Q2, FTR, RoboSuite, and TD-MPC2 are outside
the released repository and therefore outside this source-based package.

## Paper-oriented choices

- observations: 84 x 84;
- VDCS Markov stay probability: 0.8;
- severity jitter: 0.1;
- ACO: 9 experts, base channels 9, 4,884,961 parameters;
- capacity-matched single expert: 1 expert, base channels 21, 4,819,409 parameters;
- ACO optimizer: AdamW, learning rate 1e-4, weight decay 1e-4;
- ACO: 15,000 optimizer steps, effective batch 1024;
- Dreamer RSSM deterministic state: 1024;
- Dreamer: batch 16 x sequence length 64 and 1,000,000 environment steps;
- evaluation: 10 episodes for each of five training seeds;
- policy and adapter remain frozen during every evaluation.

The paper and appendix contain conflicting ACO architecture descriptions. The
9-channel/9-expert setting is selected because its 4.884961M parameter count
matches the paper's 4.90M latency table. This decision is recorded rather than
silently treating the repository's 64-channel default as the paper model.

The released data generator samples random actions and creates VDCS physical
corruptions only. The paper does not release its policy-collected unified
VDCS+DMCGB dataset. Consequently, the DMC-GB stage here is explicitly a
zero-shot transfer test for the released VDCS-trained adapter; it should not be
reported as an exact reconstruction of the paper's unified-data protocol.

## Server setup

Upload into its own directory under `/home/gpuadmin/CST/CORA`, then run:

```bash
cd /home/gpuadmin/CST/CORA/aco-moe-reproduction
bash reproduction/00_create_env.sh
conda activate /data1/CST/CORA/aco-moe-reproduction/envs/aco_moe_repro
bash reproduction/00_preflight.sh
```

The preflight checks imports, all config profiles, 84 x 84 hard-routing forward
passes, EGL/MuJoCo rendering, model parameter counts, and visible GPUs. The
server environment is pinned to the dependency versions already exercised by
the local reproduction, with PyTorch 2.5.1/cu121 supported by the server's
575-series driver. To refuse launch while a GPU is occupied:

```bash
bash reproduction/00_preflight.sh --require-idle
```

## Run stages

Run long stages inside `tmux` or another server-side session:

```bash
tmux new -s aco-repro
conda activate /data1/CST/CORA/aco-moe-reproduction/envs/aco_moe_repro
cd /home/gpuadmin/CST/CORA/aco-moe-reproduction

bash reproduction/01_generate_vdcs_data.sh
bash reproduction/02_train_adapters.sh
bash reproduction/03_train_policies.sh
bash reproduction/04_eval_core.sh
bash reproduction/05_eval_static.sh
DAVIS_PATH=/path/to/DAVIS/JPEGImages/480p bash reproduction/06_eval_dmcgb.sh
bash reproduction/07_collect_results.sh
```

`run_core_pipeline.sh` runs the first four core stages and collection in order.
The scripts launch at most one training/evaluation process on each selected GPU.
They refuse to start if utilization exceeds 15% or memory use exceeds 1500 MiB.
They also require at least 50 GiB free space by default.

## Small validation run

Before a full launch, override the defaults without editing source files:

```bash
SEEDS="0" ADAPTER_SEEDS="0" GPUS="0" \
SAMPLES_PER_TASK=20 ACO_STEPS=2 ACO_MICRO_BATCH=2 ACO_GRAD_ACCUM=1 \
POLICY_STEPS=200 EVAL_EPISODES=1 \
DATA_TASKS_OVERRIDE="cartpole_swingup" \
POLICY_TASKS_OVERRIDE="cartpole_swingup" \
bash reproduction/run_core_pipeline.sh
```

For a full run, use the defaults from `settings.sh`. Set `GPUS="1 3"` to use a
subset. Set `ALLOW_BUSY_GPUS=1` only when GPU sharing has been explicitly
approved. `SKIP_COMPLETED=1` is the default; adapter training resumes from its
latest checkpoint and Dreamer resumes from its existing log directory.
Task lists can be reduced with `DATA_TASKS_OVERRIDE`, `POLICY_TASKS_OVERRIDE`,
and `DMCGB_TASKS_OVERRIDE`. A partial dataset is never deleted automatically;
after inspection, set `OVERWRITE_PARTIAL_DATA=1` to regenerate that task.
Because the inspected server has only about 84 GiB free, completed policy replay
and evaluation episode files are pruned after the checkpoint/metrics are safely
written. `TRAINING_COMPLETE` prevents a pruned run from restarting. Set
`PRUNE_REPLAY_AFTER_TRAIN=0` only when a larger project-owned volume is mounted.

## Outputs

```text
/data1/CST/CORA/aco-moe-reproduction/datasets/       paired ACO training data
/data1/CST/CORA/aco-moe-reproduction/checkpoints/    ACO variants
/data1/CST/CORA/aco-moe-reproduction/outputs/        policies, metrics and logs
/data1/CST/CORA/aco-moe-reproduction/cache/          package and model caches
/data1/CST/CORA/aco-moe-reproduction/envs/           Conda environment
```

`core_comparisons.csv` additionally reports return as a percentage of clean,
return as a percentage of the foreground oracle, and the recovered clean-to-raw
performance gap for every task and seed.

The local repository remains the source of truth. Make changes locally, run the
checks, and upload again before restarting a remote workload.
