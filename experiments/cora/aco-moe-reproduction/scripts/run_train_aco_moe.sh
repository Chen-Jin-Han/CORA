#!/usr/bin/env bash
# Train the ACO-MoE adapter on the offline VDCS H5 dataset.
#
# The main paper configuration is LABEL-FREE: the router never sees
# corruption-type labels and there is no teaching signal. That is the
# default for `scripts/train_aco_moe.py` and we deliberately do NOT pass
# any flag that re-enables label supervision here.
#
# `NUM_EXPERTS` is an architectural capacity hyperparameter -- it is NOT
# the number of corruption modes and the experts are never assigned to
# fixed corruption categories.
#
# To reproduce the supervised-router ablation, append on the CLI:
#     bash scripts/run_train_aco_moe.sh --use_label_supervision
set -euo pipefail
cd "$(dirname "$0")/.."

DATA_DIR="${DATA_DIR:-data/h5}"
TASKS="${TASKS:-walker_walk cheetah_run finger_spin cartpole_swingup hopper_stand hopper_hop walker_run}"
OUT_DIR="${OUT_DIR:-checkpoints/aco_moe}"
LOG_DIR="${LOG_DIR:-logs/aco_moe}"
STEPS="${STEPS:-20000}"
BATCH_SIZE="${BATCH_SIZE:-64}"
NUM_EXPERTS="${NUM_EXPERTS:-7}"

ROOTS=""
for t in ${TASKS}; do
    if [[ -z "${ROOTS}" ]]; then
        ROOTS="${DATA_DIR}/${t}_vdcs_seg64_split"
    else
        ROOTS="${ROOTS},${DATA_DIR}/${t}_vdcs_seg64_split"
    fi
done

MUJOCO_GL="${MUJOCO_GL:-egl}" python -m scripts.train_aco_moe \
    --data_roots "${ROOTS}" \
    --output_dir "${OUT_DIR}" \
    --log_dir "${LOG_DIR}" \
    --steps "${STEPS}" \
    --batch_size "${BATCH_SIZE}" \
    --num_experts "${NUM_EXPERTS}" \
    "$@"
