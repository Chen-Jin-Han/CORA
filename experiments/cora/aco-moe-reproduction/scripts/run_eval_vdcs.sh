#!/usr/bin/env bash
# Evaluate the clean DreamerV3 policy on VDCS Markov-temporal corruptions
# with the frozen ACO-MoE adapter inserted before the world-model encoder.
#
# Load the clean policy through the dedicated frozen evaluation entry point.
set -euo pipefail
cd "$(dirname "$0")/.."

TASK="${TASK:-dmc_walker_walk}"
CLEAN_LOGDIR="${CLEAN_LOGDIR:-logdir/clean/${TASK}}"
EVAL_LOGDIR="${EVAL_LOGDIR:-logdir/eval_vdcs/${TASK}}"
ADAPTER_CKPT="${ADAPTER_CKPT:-checkpoints/aco_moe/moe_unet_best.pth}"
EVAL_EPISODES="${EVAL_EPISODES:-10}"

# Read the source policy directly; evaluation never trains or copies replay.
MUJOCO_GL="${MUJOCO_GL:-egl}" python dreamer.py \
    --configs dmc_vision adapt_vdcs_markov_temporal \
    --task "${TASK}" \
    --logdir "${EVAL_LOGDIR}" \
    --dual_stream_unet_checkpoint "${ADAPTER_CKPT}" \
    --eval_only True \
    --policy_checkpoint "${CLEAN_LOGDIR}/latest.pt" \
    --eval_episode_num "${EVAL_EPISODES}" \
    "$@"
