#!/usr/bin/env bash
# Generate the VDCS H5 segmentation dataset used to pretrain ACO-MoE.
# Output goes under data/h5/<task>_vdcs_seg64_split/{train,val}/<degradation>/*.h5
set -euo pipefail
cd "$(dirname "$0")/.."

OUT_DIR="${OUT_DIR:-data/h5}"
TASKS="${TASKS:-walker_walk,cheetah_run,finger_spin,cartpole_swingup,hopper_stand,hopper_hop,walker_run}"
SAMPLES="${SAMPLES:-500}"

MUJOCO_GL="${MUJOCO_GL:-egl}" python -m scripts.generate_vdcs_dataset \
    --out_h5_dir "${OUT_DIR}" \
    --tasks "${TASKS}" \
    --samples_per_task "${SAMPLES}" \
    --size 64 64 \
    --action_repeat 2 \
    --train_ratio 0.9 \
    --overwrite "$@"
