#!/usr/bin/env bash
set -euo pipefail
source "$(dirname "$0")/common.sh"
disk_guard

for task in "${DATA_TASKS[@]}"; do
  split="${DATA_DIR}/${task}_vdcs_seg${IMAGE_SIZE}_split"
  base="${DATA_DIR}/${task}_vdcs_seg${IMAGE_SIZE}"
  count=0
  [[ -d "${split}" ]] && count="$(find "${split}" -type l -o -type f | wc -l)"
  expected=$((7 * SAMPLES_PER_TASK))
  if [[ "${SKIP_COMPLETED}" == "1" && "${count}" -ge "${expected}" ]]; then
    echo "[SKIP] complete dataset ${task}: ${count}/${expected} split entries"
    continue
  fi
  overwrite=()
  if [[ -e "${base}" || -e "${split}" ]]; then
    if [[ "${OVERWRITE_PARTIAL_DATA}" != "1" ]]; then
      echo "Partial dataset found for ${task}: ${count}/${expected}." >&2
      echo "Inspect it, then set OVERWRITE_PARTIAL_DATA=1 to regenerate this project-owned task." >&2
      exit 3
    fi
    overwrite=(--overwrite)
  fi
  echo "Generating ${IMAGE_SIZE}x${IMAGE_SIZE} VDCS data for ${task}"
  MUJOCO_GL="${MUJOCO_GL:-egl}" python -m scripts.generate_vdcs_dataset \
    --out_h5_dir "${DATA_DIR}" --tasks "${task}" \
    --samples_per_task "${SAMPLES_PER_TASK}" \
    --size "${IMAGE_SIZE}" "${IMAGE_SIZE}" --action_repeat 2 \
    --train_ratio 0.9 "${overwrite[@]}" "$@"
done
