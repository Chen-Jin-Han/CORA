#!/usr/bin/env bash
# Evaluate the clean DreamerV3 policy on DMC-GB video_hard with ACO-MoE.
# Requires a DAVIS dataset root (videos used as background distractors).
set -euo pipefail
cd "$(dirname "$0")/.."

TASK_DMC="${TASK_DMC:-walker_walk}"
TASK="dmcgb_${TASK_DMC}"
CLEAN_LOGDIR="${CLEAN_LOGDIR:-logdir/clean/dmc_${TASK_DMC}}"
EVAL_LOGDIR="${EVAL_LOGDIR:-logdir/eval_dmcgb_video_hard/${TASK_DMC}}"
ADAPTER_CKPT="${ADAPTER_CKPT:-checkpoints/aco_moe/moe_unet_best.pth}"
DAVIS_PATH="${DAVIS_PATH:?Set DAVIS_PATH=/path/to/DAVIS}"
EVAL_EPISODES="${EVAL_EPISODES:-10}"

# Read the source policy directly; evaluation never trains or copies replay.
MUJOCO_GL="${MUJOCO_GL:-egl}" python dreamer.py \
    --configs dmc_vision adapt_dmcgb_video_hard \
    --task "${TASK}" \
    --logdir "${EVAL_LOGDIR}" \
    --dual_stream_unet_checkpoint "${ADAPTER_CKPT}" \
    --dmcgb_background_path "${DAVIS_PATH}" \
    --eval_only True \
    --policy_checkpoint "${CLEAN_LOGDIR}/latest.pt" \
    --eval_episode_num "${EVAL_EPISODES}" \
    "$@"
