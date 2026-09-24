#!/usr/bin/env bash
# Train DreamerV3 on clean DMC (no degradations, no adapter). The resulting
# logdir/latest.pt is reused unchanged for VDCS / DMC-GB evaluation.
set -euo pipefail
cd "$(dirname "$0")/.."

TASK="${TASK:-dmc_walker_walk}"
LOGDIR="${LOGDIR:-logdir/clean/${TASK}}"
STEPS="${STEPS:-1000000}"

MUJOCO_GL="${MUJOCO_GL:-egl}" python dreamer.py \
    --configs dmc_vision \
    --task "${TASK}" \
    --logdir "${LOGDIR}" \
    --steps "${STEPS}" \
    "$@"
