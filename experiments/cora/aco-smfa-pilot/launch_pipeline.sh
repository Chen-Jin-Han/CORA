#!/usr/bin/env bash
set -euo pipefail
cd /home/gpuadmin/CST/CORA/aco-smfa-pilot
export PILOT_DATA=/data1/CST/CORA/aco-smfa-pilot
export XDG_CACHE_HOME="$PILOT_DATA/cache"
export PIP_CACHE_DIR="$PILOT_DATA/cache/pip"
export TMPDIR="$PILOT_DATA/cache/tmp"
export MUJOCO_GL=egl
export OMP_NUM_THREADS=4
export OPENBLAS_NUM_THREADS=4
export MKL_NUM_THREADS=4
taskset -c 0-7 "$PILOT_DATA/env/bin/python" -u run_pipeline.py
