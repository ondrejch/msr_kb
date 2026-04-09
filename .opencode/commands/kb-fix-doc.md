---
description: Investigate and fix one problematic document by doc id
agent: kb-maintainer
---

Investigate and fix the document `$ARGUMENTS`.

Workflow:
1. Find the matching normalized record in `kb/normalized/docs/`.
2. Inspect the generated document page and any inconsistency findings.
3. Inspect the source markdown under `pdf/<document_name>/`.
4. Determine whether the problem is caused by:
   - title extraction
   - report number extraction
   - date extraction
   - topic classification
   - entity normalization
   - timeline/report-series synthesis
5. Prepare the smallest deterministic patch.
6. Re-run only the necessary pipeline steps.
7. Show the before/after result.

Do not rewrite raw OCR text.
Do not make broad repo-wide changes for a single-document issue.
