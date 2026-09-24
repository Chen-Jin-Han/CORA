#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."

bash reproduction/00_preflight.sh --require-idle
bash reproduction/01_generate_vdcs_data.sh
bash reproduction/02_train_adapters.sh
bash reproduction/03_train_policies.sh
bash reproduction/04_eval_core.sh
bash reproduction/07_collect_results.sh

echo "Core reproduction pipeline completed."

