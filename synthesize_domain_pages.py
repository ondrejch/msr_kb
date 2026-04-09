#!/usr/bin/env python3
"""
Synthesize richer entity pages and chronology pages from deterministic compiler output.
"""

from __future__ import annotations

import argparse
import collections
import dataclasses
import datetime as dt
import json
import re
import shutil
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence, Tuple

import deterministic_compiler_v2 as compiler

TIMELINE_BUCKET_RULES: Dict[str, Dict[str, Sequence[str]]] = {
    "program": {
        "topics": ["program-history"],
        "reactors": [],
        "entity_types": ["report-series"],
    },
    "reactors": {
        "topics": ["reactor-operations", "reactor-physics-neutronics", "breeder-and-converter-design"],
        "reactors": ["MSRE", "MSBR", "MSCR", "DMSR", "ARE", "ART", "HRE", "AHR", "LMFR"],
        "entity_types": ["reactor", "reactor-concept"],
    },
    "materials": {
        "topics": ["materials-and-corrosion", "irradiation-and-damage", "graphite-and-moderator-behavior"],
        "reactors": [],
        "entity_types": ["alloy-material"],
    },
    "salts": {
        "topics": ["salt-systems-and-thermophysics", "salt-chemistry-and-redox"],
        "reactors": [],
        "entity_types": ["salt-system"],
    },
    "chemistry": {
        "topics": ["salt-chemistry-and-redox", "off-gas-fission-products-and-tritium"],
        "reactors": [],
        "entity_types": ["salt-system", "component"],
    },
    "processing": {
        "topics": ["fuel-processing-and-reprocessing"],
        "reactors": [],
        "entity_types": ["component"],
    },
    "operations": {
        "topics": ["reactor-operations", "instrumentation-and-controls", "pumps-loops-and-heat-exchangers"],
        "reactors": ["MSRE", "ARE", "ART", "HRE"],
        "entity_types": ["component"],
    },
    "anp": {
        "topics": ["aircraft-nuclear-propulsion"],
        "reactors": ["ARE", "ART"],
        "entity_types": ["reactor"],
    },
    "aqueous": {
        "topics": ["aqueous-homogeneous-reactors"],
        "reactors": ["HRE", "AHR"],
        "entity_types": ["reactor"],
    },
}

TIMELINE_TITLES = {
    "chronology": "Corpus Chronology",
    "program": "Program Timeline",
    "reactors": "Reactor Timeline",
    "materials": "Materials Timeline",
    "salts": "Salt Systems Timeline",
    "chemistry": "Chemistry Timeline",
    "processing": "Fuel Processing Timeline",
    "operations": "Operations and Instrumentation Timeline",
    "anp": "Aircraft Nuclear Propulsion Timeline",
    "aqueous": "Aqueous Homogeneous Reactor Timeline",
}

MONTHS = {
    "january": 1,
    "february": 2,
    "march": 3,
    "april": 4,
    "may": 5,
    "june": 6,
    "july": 7,
    "august": 8,
    "september": 9,
    "october": 10,
    "november": 11,
    "december": 12,
}


@dataclasses.dataclass
class ParsedDate:
    original: Optional[str]
    sort_date: dt.date
    precision: str
    display: str


@dataclasses.dataclass
class RecordBundle:
    record: compiler.DocumentRecord
    parsed_date: ParsedDate
    claims: List[Dict[str, object]]


def read_json(path: Path) -> object:
    return json.loads(path.read_text(encoding="utf-8"))


def read_jsonl(path: Path) -> List[Dict[str, object]]:
    if not path.exists():
        return []
    rows: List[Dict[str, object]] = []
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            obj = json.loads(line)
            if isinstance(obj, dict):
                rows.append(obj)
    return rows


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def write_json(path: Path, obj: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2, sort_keys=True), encoding="utf-8")


def safe_rmtree(path: Path) -> None:
    if path.exists() and path.is_dir():
        shutil.rmtree(path)


def parse_date_text(date_text: Optional[str]) -> ParsedDate:
    if not date_text:
        return ParsedDate(original=None, sort_date=dt.date(9999, 12, 31), precision="unknown", display="unknown")
    text = date_text.strip()
    m = re.fullmatch(r"(\d{4})-(\d{2})-(\d{2})", text)
    if m:
        year, month, day = map(int, m.groups())
        return ParsedDate(original=text, sort_date=dt.date(year, month, day), precision="day", display=text)
    m = re.fullmatch(r"([A-Za-z]+)\s+(\d{1,2}),\s+(\d{4})", text)
    if m:
        month_name, day, year = m.groups()
        month = MONTHS.get(month_name.lower())
        if month:
            return ParsedDate(original=text, sort_date=dt.date(int(year), month, int(day)), precision="day", display=text)
    m = re.fullmatch(r"([A-Za-z]+)\s+(\d{4})", text)
    if m:
        month_name, year = m.groups()
        month = MONTHS.get(month_name.lower())
        if month:
            return ParsedDate(original=text, sort_date=dt.date(int(year), month, 1), precision="month", display=text)
    m = re.fullmatch(r"(\d{4})", text)
    if m:
        year = int(m.group(1))
        return ParsedDate(original=text, sort_date=dt.date(year, 1, 1), precision="year", display=text)
    return ParsedDate(original=text, sort_date=dt.date(9999, 12, 31), precision="unknown", display=text)


def iter_doc_json_paths(kb_root: Path) -> Iterable[Path]:
    docs_root = kb_root / "normalized" / "docs"
    if not docs_root.exists():
        return []
    return sorted(docs_root.glob("*.json"))


def load_bundles(kb_root: Path) -> List[RecordBundle]:
    bundles: List[RecordBundle] = []
    for path in iter_doc_json_paths(kb_root):
        raw = read_json(path)
        if not isinstance(raw, dict):
            continue
        record = compiler.DocumentRecord(**raw)
        claims = read_jsonl(Path(record.claims_path))
        bundles.append(RecordBundle(record=record, parsed_date=parse_date_text(record.date_text), claims=claims))
    bundles.sort(key=lambda b: (b.parsed_date.sort_date, b.record.title.lower(), b.record.doc_id))
    return bundles


def build_entity_matchers(entity_patterns: Dict[str, Dict[str, Sequence[str]]]) -> Dict[Tuple[str, str], List[re.Pattern[str]]]:
    matchers: Dict[Tuple[str, str], List[re.Pattern[str]]] = {}
    for entity_type, entities in entity_patterns.items():
        for entity_name, patterns in entities.items():
            matchers[(entity_type, entity_name)] = [re.compile(pattern, re.IGNORECASE) for pattern in patterns]
    return matchers


def normalize_entity_refs(bundles: Sequence[RecordBundle]) -> Dict[str, Dict[str, List[Dict[str, object]]]]:
    entity_index: Dict[str, Dict[str, List[Dict[str, object]]]] = collections.defaultdict(lambda: collections.defaultdict(list))
    for bundle in bundles:
        rec = bundle.record
        base = {
            "doc_id": rec.doc_id,
            "title": rec.title,
            "date_text": rec.date_text,
            "sort_date": bundle.parsed_date.sort_date.isoformat(),
            "report_number": rec.report_number,
            "report_series": rec.report_series,
            "topics": list(rec.topics),
        }
        for entity_type, entries in rec.entities.items():
            for item in entries:
                entity_index[entity_type][str(item["name"])] .append({**base, "count": int(item["count"]), "line_hits": list(item["line_hits"])})
    return entity_index


def top_topics(refs: Sequence[Dict[str, object]], limit: int = 8) -> List[Tuple[str, int]]:
    counter: Dict[str, int] = collections.Counter()
    for ref in refs:
        for topic in ref.get("topics", []):
            counter[str(topic)] += 1
    return sorted(counter.items(), key=lambda kv: (-kv[1], kv[0]))[:limit]


def cooccurring_entities(entity_type: str, entity_name: str, refs: Sequence[Dict[str, object]], bundles_by_id: Dict[str, RecordBundle], limit: int = 12) -> List[Tuple[str, int]]:
    counts: Dict[str, int] = collections.Counter()
    doc_ids = {str(ref["doc_id"]) for ref in refs}
    for doc_id in doc_ids:
        bundle = bundles_by_id.get(doc_id)
        if not bundle:
            continue
        for other_type, entries in bundle.record.entities.items():
            for item in entries:
                other_name = str(item["name"])
                if other_type == entity_type and other_name == entity_name:
                    continue
                counts[f"{other_type}:{other_name}"] += 1
    return sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))[:limit]


def find_representative_claims(entity_type: str, entity_name: str, refs: Sequence[Dict[str, object]], bundles_by_id: Dict[str, RecordBundle], matchers: Dict[Tuple[str, str], List[re.Pattern[str]]], limit: int = 10) -> List[Tuple[str, str, Optional[str], Optional[int], str]]:
    patterns = matchers.get((entity_type, entity_name), [])
    candidates: List[Tuple[dt.date, str, str, Optional[str], Optional[int], str]] = []
    for ref in refs:
        bundle = bundles_by_id.get(str(ref["doc_id"]))
        if not bundle:
            continue
        for claim in bundle.claims:
            text = str(claim.get("text", "")).strip()
            if not text:
                continue
            matched = any(p.search(text) for p in patterns)
            if not matched and entity_name.lower() not in text.lower():
                continue
            candidates.append((bundle.parsed_date.sort_date, bundle.record.title, text, bundle.record.date_text, claim.get("page_hint") if isinstance(claim.get("page_hint"), int) else None, bundle.record.doc_id))
    candidates.sort(key=lambda row: (row[0], row[1].lower(), row[2].lower()))
    out: List[Tuple[str, str, Optional[str], Optional[int], str]] = []
    seen = set()
    for _, title, text, date_text, page_hint, doc_id in candidates:
        key = text.lower()
        if key in seen:
            continue
        seen.add(key)
        out.append((title, text, date_text, page_hint, doc_id))
        if len(out) >= limit:
            break
    return out


def unique_preserve_order(values: Iterable[str]) -> List[str]:
    out: List[str] = []
    seen = set()
    for value in values:
        if value in seen:
            continue
        seen.add(value)
        out.append(value)
    return out


def determine_timeline_buckets(bundle: RecordBundle) -> List[str]:
    rec = bundle.record
    buckets = ["chronology"]
    topic_set = set(rec.topics)
    reactor_names = {str(item["name"]) for item in rec.entities.get("reactor", [])}
    entity_types_present = set(rec.entities.keys())
    for bucket, rules in TIMELINE_BUCKET_RULES.items():
        if topic_set.intersection(rules["topics"]):
            buckets.append(bucket)
            continue
        if reactor_names.intersection(rules["reactors"]):
            buckets.append(bucket)
            continue
        if entity_types_present.intersection(rules["entity_types"]):
            if bucket in {"materials", "salts", "program"}:
                buckets.append(bucket)
    return unique_preserve_order(buckets)


def render_entity_page(entity_type: str, entity_name: str, refs: Sequence[Dict[str, object]], bundles_by_id: Dict[str, RecordBundle], matchers: Dict[Tuple[str, str], List[re.Pattern[str]]]) -> str:
    refs = sorted(refs, key=lambda ref: (ref.get("sort_date", "9999-12-31"), str(ref["title"]).lower(), str(ref["doc_id"])))
    topic_profile = top_topics(refs)
    related = cooccurring_entities(entity_type, entity_name, refs, bundles_by_id)
    claims = find_representative_claims(entity_type, entity_name, refs, bundles_by_id, matchers)
    first_date = refs[0].get("date_text") if refs else None
    last_date = refs[-1].get("date_text") if refs else None

    chronology_lines = []
    for ref in refs:
        line = f"- [[../documents/{ref['doc_id']}.md|{ref['title']}]]"
        if ref.get("date_text"):
            line += f" - {ref['date_text']}"
        if ref.get("report_number"):
            line += f" - {ref['report_number']}"
        line += f" - mentions: {ref['count']}"
        chronology_lines.append(line)

    topic_lines = [f"- {topic} ({count})" for topic, count in topic_profile] or ["- none"]
    related_lines = [f"- {label.split(':', 1)[1]} [{label.split(':', 1)[0]}] ({count})" for label, count in related] or ["- none"]

    claim_lines: List[str] = []
    for title, text, date_text, page_hint, doc_id in claims:
        prefix = f"- [[../documents/{doc_id}.md|{title}]]"
        if date_text:
            prefix += f" - {date_text}"
        if page_hint is not None:
            prefix += f" - page {page_hint}"
        claim_lines.append(prefix)
        claim_lines.append(f"  - {text}")
    if not claim_lines:
        claim_lines = ["- none"]

    return "\n".join([
        f"# {entity_name}",
        "",
        "## Overview",
        "",
        f"- Type: {entity_type}",
        f"- Documents: {len(refs)}",
        f"- First seen: {first_date or 'unknown'}",
        f"- Last seen: {last_date or 'unknown'}",
        "",
        "## Topic Profile",
        "",
        *topic_lines,
        "",
        "## Related Entities",
        "",
        *related_lines,
        "",
        "## Representative Claims",
        "",
        *claim_lines,
        "",
        "## Chronology",
        "",
        *chronology_lines,
        "",
    ])


def render_report_series_page(series: str, bundles: Sequence[RecordBundle]) -> str:
    sorted_bundles = sorted(bundles, key=lambda b: (b.parsed_date.sort_date, b.record.title.lower(), b.record.doc_id))
    topic_counter: Dict[str, int] = collections.Counter()
    lines: List[str] = []
    for bundle in sorted_bundles:
        for topic in bundle.record.topics:
            topic_counter[topic] += 1
        line = f"- [[../documents/{bundle.record.doc_id}.md|{bundle.record.title}]]"
        if bundle.record.date_text:
            line += f" - {bundle.record.date_text}"
        if bundle.record.report_number:
            line += f" - {bundle.record.report_number}"
        lines.append(line)
    topic_lines = [f"- {topic} ({count})" for topic, count in sorted(topic_counter.items(), key=lambda kv: (-kv[1], kv[0]))[:10]] or ["- none"]
    return "\n".join([f"# {series}", "", f"- Documents: {len(sorted_bundles)}", "", "## Topic Profile", "", *topic_lines, "", "## Documents", "", *lines, ""])


def render_timeline_page(name: str, bundles: Sequence[RecordBundle]) -> str:
    title = TIMELINE_TITLES.get(name, name.replace("-", " ").title())
    grouped: Dict[str, List[RecordBundle]] = collections.defaultdict(list)
    for bundle in bundles:
        if bundle.parsed_date.precision == "unknown":
            grouped["unknown"].append(bundle)
        else:
            grouped[str(bundle.parsed_date.sort_date.year)].append(bundle)
    year_keys = sorted((key for key in grouped if key != "unknown"), key=int)
    if "unknown" in grouped:
        year_keys.append("unknown")
    lines: List[str] = [f"# {title}", "", f"- Documents: {len(bundles)}", ""]
    for year in year_keys:
        lines.append(f"## {year}")
        lines.append("")
        year_bundles = sorted(grouped[year], key=lambda b: (b.parsed_date.sort_date, b.record.title.lower(), b.record.doc_id))
        for bundle in year_bundles:
            rec = bundle.record
            line = f"- [[../documents/{rec.doc_id}.md|{rec.title}]]"
            if rec.date_text:
                line += f" - {rec.date_text}"
            if rec.report_number:
                line += f" - {rec.report_number}"
            if rec.report_series:
                line += f" - {rec.report_series}"
            if rec.topics:
                line += f" - topics: {', '.join(rec.topics[:4])}"
            lines.append(line)
        lines.append("")
    return "\n".join(lines)


def render_timelines_index(buckets_to_bundles: Dict[str, List[RecordBundle]]) -> str:
    lines = ["# Timelines", ""]
    for name in sorted(buckets_to_bundles):
        lines.append(f"- [[../timelines/{name}.md|{TIMELINE_TITLES.get(name, name)}]] - documents: {len(buckets_to_bundles[name])}")
    lines.append("")
    return "\n".join(lines)


def render_report_series_index(series_to_bundles: Dict[str, List[RecordBundle]]) -> str:
    lines = ["# Report Series", ""]
    for series in sorted(series_to_bundles):
        slug = compiler.slugify(series)
        lines.append(f"- [[../report-series/{slug}.md|{series}]] - documents: {len(series_to_bundles[series])}")
    lines.append("")
    return "\n".join(lines)


def parse_args(argv: Optional[Sequence[str]] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Synthesize entity and chronology pages from deterministic compiler output.")
    parser.add_argument("--kb-root", type=Path, default=Path("kb"), help="Knowledge-base root directory.")
    parser.add_argument("--entity-patterns-json", type=Path, default=None, help="Optional JSON file overriding entity patterns.")
    return parser.parse_args(argv)


def main(argv: Optional[Sequence[str]] = None) -> int:
    args = parse_args(argv)
    kb_root = args.kb_root
    docs_root = kb_root / "normalized" / "docs"
    if not docs_root.exists() or not docs_root.is_dir():
        raise SystemExit(f"Missing normalized docs directory: {docs_root}")

    bundles = load_bundles(kb_root)
    bundles_by_id = {bundle.record.doc_id: bundle for bundle in bundles}
    entity_patterns = compiler.load_override_json(args.entity_patterns_json) or compiler.DEFAULT_ENTITY_PATTERNS
    matchers = build_entity_matchers(entity_patterns)
    entity_index = normalize_entity_refs(bundles)

    safe_rmtree(kb_root / "wiki" / "entities")
    safe_rmtree(kb_root / "wiki" / "timelines")
    safe_rmtree(kb_root / "wiki" / "report-series")

    entity_page_count = 0
    for entity_type, entity_map in entity_index.items():
        for entity_name, refs in entity_map.items():
            write_text(kb_root / "wiki" / "entities" / f"{compiler.slugify(entity_name)}.md", render_entity_page(entity_type, entity_name, refs, bundles_by_id, matchers))
            entity_page_count += 1

    series_to_bundles: Dict[str, List[RecordBundle]] = collections.defaultdict(list)
    for bundle in bundles:
        if bundle.record.report_series:
            series_to_bundles[bundle.record.report_series].append(bundle)
    for series, series_bundles in series_to_bundles.items():
        slug = compiler.slugify(series)
        write_text(kb_root / "wiki" / "report-series" / f"{slug}.md", render_report_series_page(series, series_bundles))

    buckets_to_bundles: Dict[str, List[RecordBundle]] = collections.defaultdict(list)
    for bundle in bundles:
        for bucket in determine_timeline_buckets(bundle):
            buckets_to_bundles[bucket].append(bundle)
    for bucket, bucket_bundles in buckets_to_bundles.items():
        write_text(kb_root / "wiki" / "timelines" / f"{bucket}.md", render_timeline_page(bucket, bucket_bundles))

    write_text(kb_root / "wiki" / "indices" / "timelines.md", render_timelines_index(buckets_to_bundles))
    write_text(kb_root / "wiki" / "indices" / "report-series.md", render_report_series_index(series_to_bundles))

    coverage = {
        "generated_at": dt.datetime.utcnow().isoformat() + "Z",
        "document_count": len(bundles),
        "entity_page_count": entity_page_count,
        "timeline_count": len(buckets_to_bundles),
        "report_series_count": len(series_to_bundles),
        "documents_with_unknown_date": sorted(bundle.record.doc_id for bundle in bundles if bundle.parsed_date.precision == "unknown"),
        "documents_without_report_series": sorted(bundle.record.doc_id for bundle in bundles if not bundle.record.report_series),
        "documents_without_claims": sorted(bundle.record.doc_id for bundle in bundles if not bundle.claims),
    }
    write_json(kb_root / "reports" / "synthesis_coverage.json", coverage)
    print(f"done: documents={len(bundles)} entity_pages={entity_page_count} timelines={len(buckets_to_bundles)} report_series={len(series_to_bundles)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
