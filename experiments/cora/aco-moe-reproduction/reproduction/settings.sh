#!/usr/bin/env bash
# Paper-oriented defaults. Override any value in the environment before launch.

REPRO_ROOT="${REPRO_ROOT:-$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)}"
LARGE_ROOT="${LARGE_ROOT:-/data1/CST/CORA/aco-moe-reproduction}"
DATA_DIR="${DATA_DIR:-${LARGE_ROOT}/datasets/h5_paper}"
CHECKPOINT_DIR="${CHECKPOINT_DIR:-${LARGE_ROOT}/checkpoints}"
LOG_ROOT="${LOG_ROOT:-${LARGE_ROOT}/outputs/logdir}"
DAVIS_PATH="${DAVIS_PATH:-}"
export TORCH_HOME="${TORCH_HOME:-${LARGE_ROOT}/cache/torch}"
export XDG_CACHE_HOME="${XDG_CACHE_HOME:-${LARGE_ROOT}/cache/xdg}"
export PIP_CACHE_DIR="${PIP_CACHE_DIR:-${LARGE_ROOT}/cache/pip}"

# Main VDCS tasks from the paper.
DATA_TASKS=(
  cartpole_swingup finger_spin finger_turn_hard hopper_stand
  hopper_hop cheetah_run walker_walk walker_run
)

# Union of the main-table and DMC-GB policy tasks.
POLICY_TASKS=(
  cartpole_swingup finger_spin finger_turn_hard hopper_stand
  hopper_hop cheetah_run walker_stand walker_walk walker_run
)
DMCGB_TASKS=(cartpole_swingup finger_spin walker_stand walker_walk cheetah_run)
if [[ -n "${DATA_TASKS_OVERRIDE:-}" ]]; then read -r -a DATA_TASKS <<<"${DATA_TASKS_OVERRIDE}"; fi
if [[ -n "${POLICY_TASKS_OVERRIDE:-}" ]]; then read -r -a POLICY_TASKS <<<"${POLICY_TASKS_OVERRIDE}"; fi
if [[ -n "${DMCGB_TASKS_OVERRIDE:-}" ]]; then read -r -a DMCGB_TASKS <<<"${DMCGB_TASKS_OVERRIDE}"; fi
SEEDS=(${SEEDS:-0 1 2 3 4})
ADAPTER_SEEDS=(${ADAPTER_SEEDS:-0})
# Use one GPU by default to preserve capacity for other users. Override only
# after coordination, for example GPUS="0 2".
GPUS=(${GPUS:-1})

IMAGE_SIZE="${IMAGE_SIZE:-84}"
SAMPLES_PER_TASK="${SAMPLES_PER_TASK:-5000}"
POLICY_STEPS="${POLICY_STEPS:-1000000}"
EVAL_EPISODES="${EVAL_EPISODES:-10}"

# The paper reports batch 1024 and 15,000 optimizer updates. On a 32 GB GPU,
# use micro-batches plus accumulation to preserve the effective batch size.
ACO_STEPS="${ACO_STEPS:-15000}"
ACO_MICRO_BATCH="${ACO_MICRO_BATCH:-128}"
ACO_GRAD_ACCUM="${ACO_GRAD_ACCUM:-8}"
ACO_VAL_BATCH="${ACO_VAL_BATCH:-128}"
ACO_WORKERS="${ACO_WORKERS:-8}"

# Launch guard. Set ALLOW_BUSY_GPUS=1 only after checking shared workloads.
MAX_GPU_UTIL="${MAX_GPU_UTIL:-15}"
MAX_GPU_MEMORY_MIB="${MAX_GPU_MEMORY_MIB:-1500}"
ALLOW_BUSY_GPUS="${ALLOW_BUSY_GPUS:-0}"
SKIP_COMPLETED="${SKIP_COMPLETED:-1}"
OVERWRITE_PARTIAL_DATA="${OVERWRITE_PARTIAL_DATA:-0}"
MIN_FREE_GB="${MIN_FREE_GB:-50}"
# The server currently has limited free disk. These only remove generated
# replay/episode directories under LOG_ROOT after a stage succeeds.
PRUNE_REPLAY_AFTER_TRAIN="${PRUNE_REPLAY_AFTER_TRAIN:-1}"
PRUNE_EVAL_EPISODES="${PRUNE_EVAL_EPISODES:-1}"
