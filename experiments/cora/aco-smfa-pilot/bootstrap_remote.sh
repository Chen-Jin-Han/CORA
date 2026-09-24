#!/usr/bin/env bash
set -euo pipefail
cd /home/gpuadmin/CST/CORA/aco-smfa-pilot
export PILOT_DATA=/data1/CST/CORA/aco-smfa-pilot
export PIP_CACHE_DIR="$PILOT_DATA/cache/pip"
export TMPDIR="$PILOT_DATA/cache/tmp"
mkdir -p "$TMPDIR" "$PILOT_DATA/outputs"
/home/gpuadmin/anaconda3/bin/python -m venv "$PILOT_DATA/env"
"$PILOT_DATA/env/bin/python" -m pip install -r requirements.txt
"$PILOT_DATA/env/bin/python" -m pip freeze > "$PILOT_DATA/outputs/requirements-lock.txt"
echo BOOTSTRAP_COMPLETE
