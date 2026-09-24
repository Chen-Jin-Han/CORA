#!/usr/bin/env bash
set -euo pipefail
cd /home/gpuadmin/CST/CORA/drqv2-walker
DATA=/data1/CST/CORA/drqv2-walker
mkdir -p "$DATA"
PY=/data1/CST/CORA/aco-smfa-pilot/env/bin/python
nohup setsid "$PY" -u wait_gpu.py </dev/null >>"$DATA/queue.log" 2>&1 &
echo "Queue PID: $! (lock prevents duplicate launch)"
