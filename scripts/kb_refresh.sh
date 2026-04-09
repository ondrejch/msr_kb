#!/usr/bin/env bash
set -Eeuo pipefail

INPUT_ROOT="${1:-pdf}"
OUTPUT_ROOT="${2:-kb}"

python compile_incremental.py --input-root "$INPUT_ROOT" --output-root "$OUTPUT_ROOT"
python synthesize_domain_pages.py --kb-root "$OUTPUT_ROOT"
python detect_inconsistencies.py --kb-root "$OUTPUT_ROOT"
