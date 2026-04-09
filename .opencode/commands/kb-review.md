---
description: Review the KB reports and recommend the smallest next fix
agent: kb-readonly-auditor
---

Review the current knowledge base reports.

Inspect:
- `kb/reports/lint.json`
- `kb/reports/synthesis_coverage.json`
- `kb/reports/inconsistencies.md`
- `kb/manifests/build_manifest.json`
- `kb/manifests/incremental_build_manifest.json`

Return:
1. top 10 actionable issues
2. root-cause grouping:
   - ontology
   - report regex
   - title/date extraction
   - entity normalization
   - timeline synthesis
   - duplicate detection noise
3. the single highest-value next deterministic patch

Do not edit files.
