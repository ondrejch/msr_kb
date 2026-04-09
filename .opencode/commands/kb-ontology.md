---
description: Propose ontology additions from unresolved entities and conflicts
agent: kb-maintainer
---

Inspect the current KB and propose ontology additions or regex refinements.

Focus on:
- missing reactor aliases
- missing salt-system names
- missing alloy/material names
- report-series detection gaps
- organization aliases
- overbroad topic keywords causing collisions

Inspect:
- `kb/reports/inconsistencies.md`
- `kb/reports/synthesis_coverage.json`
- `deterministic_compiler_v2.py`
- `pdf/`

Return:
1. proposed additions grouped by category
2. exact regexes or keyword additions
3. risk notes for false positives
4. a minimal patch plan

Only make edits if I explicitly confirm.
