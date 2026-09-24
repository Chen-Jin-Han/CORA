#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
export RGB_DATA=/data1/CST/CORA/aco-smfa-rgb
mkdir -p "$RGB_DATA/cache/tmp" "$RGB_DATA/launcher"
export TMPDIR="$RGB_DATA/cache/tmp"
export PYTHONUNBUFFERED=1
RGB_PYTHON="${RGB_PYTHON:-$RGB_DATA/env/bin/python}"
test -x "$RGB_PYTHON"
# Linux advisory lock inside pipeline.py prevents a second pipeline from executing stages.
nohup setsid "$RGB_PYTHON" -u pipeline.py --config config.json "$@" \
  >> "$RGB_DATA/launcher/pipeline.log" 2>&1 < /dev/null &
echo "Supervisor requested, launcher PID $!. Check status.json AND live process; startup may fail."
echo "Log: $RGB_DATA/launcher/pipeline.log"
