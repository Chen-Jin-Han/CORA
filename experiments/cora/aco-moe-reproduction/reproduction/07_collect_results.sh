#!/usr/bin/env bash
set -euo pipefail
source "$(dirname "$0")/common.sh"

python reproduction/collect_results.py \
  --log-root "${LOG_ROOT}" \
  --output-dir "${LOG_ROOT}/results"

