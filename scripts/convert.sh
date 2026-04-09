#!/usr/bin/env bash
set -Eeuo pipefail

SRC_DIR="${1:-.}"
OUT_ROOT="${2:-ocr}"
METHOD="${METHOD:-ocr}"

mkdir -p "$OUT_ROOT"

find "$SRC_DIR" -type f -iname '*.pdf' -print0 |
while IFS= read -r -d '' pdf; do
  rel="${pdf#"$SRC_DIR"/}"
  if [[ "$rel" == "$pdf" ]]; then
    rel="$(basename "$pdf")"
  fi

  rel_no_ext="${rel%.*}"
  out_dir="$OUT_ROOT/$rel_no_ext"

  mkdir -p "$out_dir"

  echo "==> $pdf"
  mineru \
	  --api-url http://127.0.0.1:8000 \
    -p "$pdf" \
    -o "$out_dir" \
    -m "$METHOD" \
    -f true \
    -t true
done

