---
description: Re-run the bounded deterministic KB pipeline
agent: kb-maintainer
---

Refresh the knowledge base using the approved deterministic pipeline only.

Steps:
1. Inspect `git status`.
2. Run `bash scripts/kb_refresh.sh`.
3. Inspect:
   - `kb/reports/lint.json`
   - `kb/reports/synthesis_coverage.json`
   - `kb/reports/inconsistencies.md`
4. Summarize:
   - what changed
   - whether inconsistencies increased or decreased
   - whether any documents lost report numbers, dates, or topics
5. Do not make additional edits unless the user explicitly asks.
