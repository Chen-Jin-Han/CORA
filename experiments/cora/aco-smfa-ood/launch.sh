#!/usr/bin/env bash
set -euo pipefail
cd /home/gpuadmin/CST/CORA/aco-smfa-ood
mkdir -p /data1/CST/CORA/aco-smfa-ood
nohup setsid /data1/CST/CORA/aco-smfa-pilot/env/bin/python -u supervisor.py </dev/null >>/data1/CST/CORA/aco-smfa-ood/supervisor.log 2>&1 &
echo "Supervisor requested PID $!; verify process and status. Lock prevents duplicate runs."
