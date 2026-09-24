#!/usr/bin/env bash
set -euo pipefail
cd /home/gpuadmin/CST/CORA/aco-smfa-pilot
export PILOT_DATA=/data1/CST/CORA/aco-smfa-pilot
export XDG_CACHE_HOME="$PILOT_DATA/cache"
export TMPDIR="$PILOT_DATA/cache/tmp"
export MUJOCO_GL=egl
export OMP_NUM_THREADS=4
export OPENBLAS_NUM_THREADS=4
export MKL_NUM_THREADS=4
export XLA_PYTHON_CLIENT_PREALLOCATE=false
for task in walker_walk walker_run finger_turn_hard; do
  taskset -c 0-7 "$PILOT_DATA/env/bin/python" -u evaluate_control.py \
    --run "$PILOT_DATA/checkpoints/dmc_${task}/seed0/run" \
    --output "$PILOT_DATA/outputs/smoke_${task}" \
    --platform cpu --episodes 1 --max-steps 5
done
echo SMOKE_COMPLETE
