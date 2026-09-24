#!/usr/bin/env bash
set -euo pipefail
source "$(dirname "$0")/common.sh"

echo "Repository: ${REPRO_ROOT}"
echo "Data:       ${DATA_DIR}"
echo "Checkpoints:${CHECKPOINT_DIR}"
echo "Logs:       ${LOG_ROOT}"
echo "GPUs:       ${GPUS[*]}"
disk_guard
nvidia-smi --query-gpu=index,name,driver_version,memory.total,memory.used,utilization.gpu \
  --format=csv
python reproduction/validate_setup.py

if [[ "${1:-}" == "--require-idle" ]]; then
  gpu_guard
fi
