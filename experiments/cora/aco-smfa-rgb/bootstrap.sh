#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
RGB_DATA=/data1/CST/CORA/aco-smfa-rgb
mkdir -p "$RGB_DATA/cache/pip" "$RGB_DATA/cache/tmp"
export PIP_CACHE_DIR="$RGB_DATA/cache/pip" TMPDIR="$RGB_DATA/cache/tmp"
RGB_BASE_PYTHON="${RGB_BASE_PYTHON:-/home/gpuadmin/anaconda3/bin/python}"
if [ ! -x "$RGB_DATA/env/bin/python" ]; then
  "$RGB_BASE_PYTHON" -m venv "$RGB_DATA/env"
fi
"$RGB_DATA/env/bin/python" -m pip install -r requirements.txt
"$RGB_DATA/env/bin/python" -m pip freeze > "$RGB_DATA/environment-lock.txt"
"$RGB_DATA/env/bin/python" tests.py
echo 'Environment ready. Formal training was NOT started.'
