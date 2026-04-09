#!/usr/bin/env python3
"""
Incremental wrapper for deterministic_compiler_v2.py.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import sys
from pathlib import Path
from typing import Dict, List, Optional, Sequence, Set

import deterministic_compiler_v2 as compiler
import distill_research_primitives as distiller

STATE_VERSION = 1
STATE_FILENAME = "incremental_state.json"
BUILD_MANIFEST_FILENAME = "incremental_build_manifest.json"


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8", errors="replace")).hexdigest()


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def read_json(path: Path) -> object:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, obj: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2, sort_keys=True), encoding="utf-8")


def safe_unlink(path: Path) -> None:
    if path.exists() and path.is_file():
        path.unlink()


def safe_rmtree(path: Path) -> None:
    if path.exists() and path.is_dir():
        shutil.rmtree(path)


def folder_fingerprint(doc_dir: Path) -> str:
    parts: List[str] = []
    for path in sorted(p for p in doc_dir.rglob("*") if p.is_file()):
        stat = path.stat()
        rel = path.relative_to(doc_dir).as_posix()
        parts.append(f"{rel}\t{stat.st_size}\t{stat.st_mtime_ns}")
    return sha256_text("\n".join(parts))


def config_signature(entity_patterns_json: Optional[Path], topic_keywords_json: Optional[Path]) -> str:
    parts: List[str] = []
    parts.append(sha256_bytes(Path(compiler.__file__).read_bytes()))
    if entity_patterns_json:
        parts.append(sha256_bytes(entity_patterns_json.read_bytes()))
    else:
        parts.append(sha256_text(json.dumps(compiler.DEFAULT_ENTITY_PATTERNS, sort_keys=True)))
    if topic_keywords_json:
        parts.append(sha256_bytes(topic_keywords_json.read_bytes()))
    else:
        parts.append(sha256_text(json.dumps(compiler.DEFAULT_TOPIC_KEYWORDS, sort_keys=True)))
    return sha256_text("\n".join(parts))


def state_path(output_root: Path) -> Path:
    return output_root / "manifests" / STATE_FILENAME


def build_manifest_path(output_root: Path) -> Path:
    return output_root / "manifests" / BUILD_MANIFEST_FILENAME


def load_state(output_root: Path) -> Dict[str, object]:
    path = state_path(output_root)
    if not path.exists():
        return {"state_version": STATE_VERSION, "config_signature": None, "documents": {}}
    raw = read_json(path)
    if not isinstance(raw, dict):
        raise ValueError(f"Invalid state file: {path}")
    return raw


def save_state(output_root: Path, state: Dict[str, object]) -> None:
    write_json(state_path(output_root), state)


def load_record(output_root: Path, doc_id: str) -> Optional[compiler.DocumentRecord]:
    path = output_root / "normalized" / "docs" / f"{doc_id}.json"
    if not path.exists():
        return None
    raw = read_json(path)
    if not isinstance(raw, dict):
        return None
    return compiler.DocumentRecord(**raw)


def remove_doc_outputs(output_root: Path, doc_id: str) -> None:
    safe_unlink(output_root / "normalized" / "docs" / f"{doc_id}.json")
    safe_unlink(output_root / "normalized" / "entities" / f"{doc_id}.json")
    safe_unlink(output_root / "normalized" / "claims" / f"{doc_id}.jsonl")
    safe_unlink(output_root / "wiki" / "documents" / f"{doc_id}.md")


def existing_output_doc_ids(output_root: Path) -> Set[str]:
    doc_ids: Set[str] = set()
    roots_and_patterns = (
        (output_root / "normalized" / "docs", "*.json"),
        (output_root / "normalized" / "entities", "*.json"),
        (output_root / "normalized" / "claims", "*.jsonl"),
        (output_root / "wiki" / "documents", "*.md"),
    )
    for root, pattern in roots_and_patterns:
        if not root.exists() or not root.is_dir():
            continue
        for path in root.glob(pattern):
            doc_ids.add(path.stem)
    return doc_ids


def prune_orphan_doc_outputs(output_root: Path, active_doc_ids: Sequence[str]) -> List[str]:
    active = set(active_doc_ids)
    existing = existing_output_doc_ids(output_root)
    orphaned = sorted(existing - active)
    for doc_id in orphaned:
        remove_doc_outputs(output_root, doc_id)
    return orphaned


def clear_aggregate_outputs(output_root: Path) -> None:
    safe_rmtree(output_root / "wiki" / "entities")
    safe_rmtree(output_root / "wiki" / "topics")
    safe_rmtree(output_root / "wiki" / "indices")


def parse_args(argv: Optional[Sequence[str]] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Incremental wrapper for deterministic_compiler_v2.py")
    parser.add_argument("--input-root", type=Path, default=Path("pdf"), help="Root directory containing pdf/<document_name>/ folders.")
    parser.add_argument("--output-root", type=Path, default=Path("kb"), help="Output root directory.")
    parser.add_argument("--entity-patterns-json", type=Path, default=None, help="Optional JSON file overriding entity patterns.")
    parser.add_argument("--topic-keywords-json", type=Path, default=None, help="Optional JSON file overriding topic keywords.")
    parser.add_argument("--force", action="store_true", help="Recompile every document regardless of fingerprints.")
    return parser.parse_args(argv)


def main(argv: Optional[Sequence[str]] = None) -> int:
    args = parse_args(argv)
    if not args.input_root.exists() or not args.input_root.is_dir():
        print(f"Input root does not exist or is not a directory: {args.input_root}", file=sys.stderr)
        return 2

    entity_patterns = compiler.load_override_json(args.entity_patterns_json) or compiler.DEFAULT_ENTITY_PATTERNS
    topic_keywords = compiler.load_override_json(args.topic_keywords_json) or compiler.DEFAULT_TOPIC_KEYWORDS

    old_state = load_state(args.output_root)
    old_documents = old_state.get("documents", {}) if isinstance(old_state.get("documents"), dict) else {}
    current_config_signature = config_signature(args.entity_patterns_json, args.topic_keywords_json)
    config_changed = old_state.get("config_signature") != current_config_signature

    records: List[compiler.DocumentRecord] = []
    current_documents_state: Dict[str, object] = {}
    compiled_count = 0
    reused_count = 0
    removed_count = 0
    pruned_orphan_doc_ids: List[str] = []
    skipped_dirs: List[str] = []
    deleted_doc_ids: List[str] = []
    recompiled_doc_ids: List[str] = []
    reused_doc_ids: List[str] = []
    current_rel_dirs = set()

    for doc_dir in compiler.iter_document_dirs(args.input_root):
        rel_dir = doc_dir.relative_to(args.input_root).as_posix()
        current_rel_dirs.add(rel_dir)
        fingerprint = folder_fingerprint(doc_dir)

        prior = old_documents.get(rel_dir)
        prior_doc_id = prior.get("doc_id") if isinstance(prior, dict) else None
        prior_fingerprint = prior.get("fingerprint") if isinstance(prior, dict) else None
        must_compile = args.force or config_changed or prior_doc_id is None or prior_fingerprint != fingerprint

        if must_compile:
            rec = compiler.compile_document(doc_dir, args.output_root, entity_patterns, topic_keywords)
            if rec is None:
                skipped_dirs.append(str(doc_dir))
                continue
            if prior_doc_id and prior_doc_id != rec.doc_id:
                remove_doc_outputs(args.output_root, prior_doc_id)
                deleted_doc_ids.append(prior_doc_id)
            compiled_count += 1
            recompiled_doc_ids.append(rec.doc_id)
            records.append(rec)
            current_documents_state[rel_dir] = {"doc_id": rec.doc_id, "fingerprint": fingerprint, "source_dir": str(doc_dir)}
            print(f"compiled {rec.doc_id}: {rec.title}")
            continue

        rec = load_record(args.output_root, str(prior_doc_id))
        if rec is None:
            rec = compiler.compile_document(doc_dir, args.output_root, entity_patterns, topic_keywords)
            if rec is None:
                skipped_dirs.append(str(doc_dir))
                continue
            compiled_count += 1
            recompiled_doc_ids.append(rec.doc_id)
            print(f"compiled {rec.doc_id}: {rec.title}")
        else:
            reused_count += 1
            reused_doc_ids.append(rec.doc_id)
            print(f"reused   {rec.doc_id}: {rec.title}")

        records.append(rec)
        current_documents_state[rel_dir] = {"doc_id": rec.doc_id, "fingerprint": fingerprint, "source_dir": str(doc_dir)}

    removed_rel_dirs = sorted(set(old_documents.keys()) - current_rel_dirs)
    for rel_dir in removed_rel_dirs:
        prior = old_documents.get(rel_dir)
        if not isinstance(prior, dict):
            continue
        doc_id = prior.get("doc_id")
        if not isinstance(doc_id, str):
            continue
        remove_doc_outputs(args.output_root, doc_id)
        removed_count += 1
        deleted_doc_ids.append(doc_id)
        print(f"removed  {doc_id}: {rel_dir}")

    pruned_orphan_doc_ids = prune_orphan_doc_outputs(args.output_root, [rec.doc_id for rec in records])
    for doc_id in pruned_orphan_doc_ids:
        print(f"pruned   {doc_id}: orphaned generated outputs")

    clear_aggregate_outputs(args.output_root)
    compiler.build_aggregate_pages(records, args.output_root)
    compiler.build_lint_report(records, args.output_root)
    distilled_summary = distiller.build_distilled_outputs(args.output_root)

    new_state = {
        "state_version": STATE_VERSION,
        "config_signature": current_config_signature,
        "documents": current_documents_state,
    }
    save_state(args.output_root, new_state)

    manifest = {
        "input_root": str(args.input_root),
        "output_root": str(args.output_root),
        "config_changed": config_changed,
        "forced": bool(args.force),
        "compiled_count": compiled_count,
        "reused_count": reused_count,
        "removed_count": removed_count,
        "pruned_orphan_count": len(pruned_orphan_doc_ids),
        "document_count": len(records),
        "distilled_claim_counts": distilled_summary.get("claim_counts", {}),
        "distilled_guide_count": distilled_summary.get("guide_count", 0),
        "distilled_catalog_count": distilled_summary.get("catalog_count", 0),
        "recompiled_doc_ids": sorted(recompiled_doc_ids),
        "reused_doc_ids": sorted(reused_doc_ids),
        "deleted_doc_ids": sorted(set(deleted_doc_ids)),
        "pruned_orphan_doc_ids": pruned_orphan_doc_ids,
        "skipped_dirs": skipped_dirs,
        "state_version": STATE_VERSION,
    }
    write_json(build_manifest_path(args.output_root), manifest)

    print(
        "distilled:"
        f" properties={distilled_summary.get('claim_counts', {}).get('properties', 0)}"
        f" compatibility={distilled_summary.get('claim_counts', {}).get('compatibility', 0)}"
        f" physics={distilled_summary.get('claim_counts', {}).get('physics', 0)}"
        f" dynamics={distilled_summary.get('claim_counts', {}).get('dynamics', 0)}"
        f" guides={distilled_summary.get('guide_count', 0)}"
    )
    print(f"done: compiled={compiled_count} reused={reused_count} removed={removed_count} pruned={len(pruned_orphan_doc_ids)} total={len(records)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
