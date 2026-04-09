# MSR Knowledge Base Agent Instructions

## Project Overview

This is a deterministic knowledge-base pipeline for Molten Salt Reactor (MSR) documents. Source PDFs are converted to markdown via MinerU OCR, then compiled into a structured KB with entities, topics, timelines, and report series.

**Key constraint**: All KB outputs must be derived deterministically from source documents. Do not invent citations or use LLM-based extraction.

---

## Input/Output Layout

```
pdf/                          # Source documents (read-only)
  <document_name>/
    hybrid_cr/
      *.md                    # MinerU OCR output
kb/                           # Generated outputs
  normalized/                 # Intermediate JSON records
  wiki/                       # Synthesized markdown pages
  reports/                    # Lint, coverage, inconsistency reports
  manifests/                  # Build state tracking
```

**Do not edit**: `pdf/`, `kb/normalized/`, `kb/wiki/documents/`

**May edit**: `kb/wiki/entities/`, `kb/wiki/topics/`, `kb/wiki/timelines/`, `kb/wiki/report-series/`, `deterministic_compiler_v2.py` (for ontology/regex fixes only)

---

## Essential Commands

### Full refresh (all docs rebuild)
```bash
bash scripts/kb_refresh.sh pdf kb
```

### Incremental refresh (only changed docs)
```bash
python compile_incremental.py --input-root pdf --output-root kb
python synthesize_domain_pages.py --kb-root kb
python detect_inconsistencies.py --kb-root kb
```

### Single report check
```bash
python detect_inconsistencies.py --kb-root kb
```

---

## OpenCode Commands

- `/kb-review` - Audit KB reports, identify issues
- `/kb-ontology` - Inspect ontology patterns
- `/kb-refresh` - Run full pipeline
- `/kb-fix-doc <doc_id>` - Fix specific document extraction

---

## Before Making Changes

Always inspect reports first:
1. `kb/reports/lint.json` - Document-level issues
2. `kb/reports/synthesis_coverage.json` - Series/timeline coverage
3. `kb/reports/inconsistencies.md` - Cross-document contradictions

If you see high false positives, stop and ask for confirmation.

---

## Common Issues and Fixes

### High duplicate reports
- **Cause**: Directory names like `ORNL-0528` vs `ORNL-528` create duplicate doc_ids
- **Fix**: Add leading-zero normalization in `extract_doc_id()` in `deterministic_compiler_v2.py`

### Entity variant fragmentation
- **Example**: "Hastelloy N" has 10 surface variants (Hastelloy N, Hastelloy-N, HASTELLOY N, HASTELLOYN, etc.)
- **Fix**: Add regex variants in `DEFAULT_ENTITY_PATTERNS["alloy-material"]`

### Report series not detected
- **Example**: 227+ docs lack series attribution (EIR, NAS-NS, NAT, etc.)
- **Fix**: Add patterns to `REPORT_SERIES_HINTS` in `deterministic_compiler_v2.py`

### Title extraction fallback
- **Cause**: OCR picks up headers like "AEC RESEARCH AND DEVELOPMENT REPORT" instead of real titles
- **Fix**: Narrow title detection or add title skip patterns

---

## Ontology Patterns

Entity types live in `DEFAULT_ENTITY_PATTERNS`:
- `reactor`: Reactor acronyms (ARE, MSRE, MSBR, MOSEL, etc.)
- `salt-system`: Salt names (FLiBe, FLiNaK, LiF-BeF2-UF4, etc.)
- `alloy-material`: Structural alloys (INOR-8, Hastelloy N, Inconel 600, etc.)
- `component`: Physical components (freeze valve, drain tank, heat exchanger, etc.)
- `organization`: Institutions (ORNL, ANL, Union Carbide, etc.)
- `report-series`: Report collection names

**Pattern rules**:
- Use `\b` word boundaries
- Prefer `[- ]?` for optional hyphen/space (Hastelloy[- ]?N)
- Case-insensitive by default in extraction
- Don't use overly generic terms (avoid "system", "analysis", "operation")

---

## Report Series Detection

Series are detected via `REPORT_SERIES_HINTS` (regex patterns) and report number prefix fallback.

**Current series**: ornl-technical-memorandum, ornl-central-files, fluid-fuel-reactors, msr-program-quarterly-progress-report, msr-program-semiannual-progress-report, anp-quarterly-progress-report, nuclear-science-and-engineering, nuclear-applications-and-technology, eir-series, nas-ns-series, natural-language-summaries, ornl-review-series

**To add series**:
1. Add pattern to `REPORT_SERIES_HINTS`
2. Optional: Add report number prefix check in `detect_report_series()`
3. Re-run pipeline

---

## Known Quirks

### OCR unicode handling
German "für" may appear as "fuer" or with umlauts. Patterns like `f[üue]r` help but are imperfect.

### Directory name vs extracted report number conflict
Directory names (e.g., `ORNL-TM-0728`) are the authoritative source for doc_ids. Extracted report numbers from text often cite OTHER documents (bibliographies), so directory name takes priority.

### 705 documents total
637 from `pdf/` + 68 synthesized documents from `kb/wiki/` entities/topics

---

## Patch History

Recent fixes documented in:
- `kb/reports/patch_record_v1.0_duplicate_fix.json` - Directory name deduplication
- `kb/reports/patch_record_v2.0_ontology_refinements.json` - Alloy & org additions
- `kb/reports/patch_record_v3.0_phase2_series_detection.json` - Series pattern expansions

Review these before proposing similar fixes.

---

## When to Ask

Ask the maintainer before:
- Changing entity page content without citing source docs
- Adding generic terms to ontology (risk of false positives)
- Proposing non-deterministic solutions
- Making large-scale refactors
- Editing `pdf/` source markdown

**Success criteria**: Fewer inconsistencies, more stable entity names, cleaner report-series grouping, better timeline coverage, no loss of provenance.

---

## Quick Reference

| Goal | File/Command |
|------|--------------|
| Inspect inconsistencies | `kb/reports/inconsistencies.md` |
| Check series coverage | `kb/reports/synthesis_coverage.json` |
| Add alloy pattern | `deterministic_compiler_v2.py` line 71-98 |
| Add report series | `deterministic_compiler_v2.py` line 208-226 |
| Normalize doc IDs | `deterministic_compiler_v2.py` `extract_doc_id()` |
| Refresh KB | `bash scripts/kb_refresh.sh pdf kb` |
