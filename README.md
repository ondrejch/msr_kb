# MSR KB Bundle

## Purpose

This repository preserves a deterministic, provenance-backed knowledge base for historical molten-salt reactor research.

It has two complementary uses:

- **historical knowledge base** under `kb/` for document-grounded entities, topics, timelines, reports, and normalized claims
- **distilled research layer** under `kb/distilled/` and `kb/wiki/research-guides/` for reusable salts, materials, compatibility, reactor-physics, and system-dynamics knowledge

The pipeline is intentionally deterministic: all generated outputs are derived from OCRed source documents and should remain traceable back to specific documents, sections, and line ranges.

<<<<<<< HEAD
=======
The repository now tracks the OCR-side source artifacts under `pdf/**/hybrid_ocr/`, including:

- fulltext Markdown (`*.md`)
- OCR sidecar JSON (`*.json`)
- extracted image assets under `images/`

Raw PDF assets remain excluded from git.

>>>>>>> 69f00500a (Initial commit: MSR Knowledge Base pipeline)
This bundle contains:

- `deterministic_compiler_v2.py`
- `compile_incremental.py`
- `synthesize_domain_pages.py`
- `detect_inconsistencies.py`
- `.opencode/agents/*`
- `.opencode/commands/*`
- `scripts/kb_refresh.sh`

## Usage

### 1. Refresh the knowledge base

Incremental refresh:

```bash
python compile_incremental.py --input-root pdf --output-root kb
python synthesize_domain_pages.py --kb-root kb
python detect_inconsistencies.py --kb-root kb
```

Or use the wrapper:

```bash
bash scripts/kb_refresh.sh pdf kb
```

The incremental pipeline now also regenerates the distilled research layer automatically.

### 2. Use the historical KB

Primary historical outputs live under:

- `kb/wiki/entities/`
- `kb/wiki/topics/`
- `kb/wiki/timelines/`
- `kb/wiki/report-series/`
- `kb/reports/`

These are best for tracing what the original corpus says and where it says it.

### 3. Use the distilled research layer

Primary distilled outputs live under:

- `kb/distilled/catalogs/`
- `kb/distilled/claims/`
- `kb/distilled/reports/`
- `kb/wiki/research-guides/`

The most useful entry points are:

- `kb/wiki/research-guides/index.md`
- `kb/wiki/research-guides/reactor-physics.md`
- `kb/wiki/research-guides/system-dynamics.md`
- `kb/wiki/research-guides/salt-systems.md`
- `kb/wiki/research-guides/materials-and-compatibility.md`

These guides are intended for downstream research use, but they remain evidence-backed and corpus-derived.

### 4. Extend the corpus

To add more source material deterministically:

1. add a new document directory under `pdf/<document_name>/`
2. place the OCR markdown and related extracted assets in that directory using the existing input layout
3. run the incremental refresh commands
4. inspect:
   - `kb/reports/lint.json`
   - `kb/reports/synthesis_coverage.json`
   - `kb/reports/inconsistencies.md`
   - `kb/distilled/reports/distilled_coverage.json`
5. review the regenerated research guides under `kb/wiki/research-guides/`

The historical KB remains the source-truth layer. The distilled layer should only be regenerated from deterministic normalized outputs, not hand-written claims.

## Expected input layout

```text
pdf/
  <document_name>/
<<<<<<< HEAD
    document.md
    figures/
    tables/
=======
    <document_name>/
      hybrid_ocr/
        <document_name>.md
        *.json
        images/
>>>>>>> 69f00500a (Initial commit: MSR Knowledge Base pipeline)
```

## Basic workflow

```bash
python compile_incremental.py --input-root pdf --output-root kb
python synthesize_domain_pages.py --kb-root kb
python detect_inconsistencies.py --kb-root kb
```

Or:

```bash
bash scripts/kb_refresh.sh pdf kb
```

## OpenCode commands

```text
/kb-review
/kb-ontology
/kb-refresh
/kb-fix-doc ornl-3872
```
