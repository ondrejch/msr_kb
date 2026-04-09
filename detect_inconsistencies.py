#!/usr/bin/env python3
"""
Deterministic contradiction / duplicate detector for the compiled KB.
"""

from __future__ import annotations

import argparse
import collections
import dataclasses
import datetime as dt
import json
import re
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence, Tuple

import deterministic_compiler_v2 as compiler

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

STOPWORDS = {
    "a", "an", "and", "are", "as", "at", "be", "by", "for", "from", "in", "into", "is", "it", "of", "on", "or", "that", "the", "their", "this", "to", "was", "were", "with", "report", "reports", "study", "paper", "document", "program", "progress", "reactor", "salt", "system", "using", "used", "than", "then", "has", "had", "have",
}

NUMERIC_TOKEN_RE = re.compile(r"[-+]?\d+(?:\.\d+)?(?:[Ee][-+]?\d+)?")
UNIT_TOKEN_RE = re.compile(r"\b(?:deg\.?\s*C|C|K|psi|psia|psig|atm|MW|kW|W|BTU|Btu|A|V|mV|ppm|ppb|wt\.?%|mol\.?%|g/cm3|g/cc|cm/s|ft/s|cm|mm|in\.|mil|hr|hrs|hours?|days?|years?)\b", re.IGNORECASE)
TOKEN_RE = re.compile(r"[A-Za-z][A-Za-z0-9\-/.]*")


@dataclasses.dataclass
class ParsedDate:
    original: Optional[str]
    sort_date: dt.date
    precision: str
    display: str


@dataclasses.dataclass
class Bundle:
    record: compiler.DocumentRecord
    claims: List[Dict[str, object]]
    markdown_text: str
    parsed_date: ParsedDate
    normalized_title: str


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


def write_json(path: Path, obj: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2, sort_keys=True), encoding="utf-8")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def normalize_title(title: str) -> str:
    title = title.lower().strip()
    title = re.sub(r"\b(?:ornl|anp|anl|cf|tm|msr|aec)[-/ ]?\d+[a-z]?\b", " ", title)
    title = re.sub(r"[^a-z0-9]+", " ", title)
    title = re.sub(r"\s+", " ", title).strip()
    return title


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


def load_bundles(kb_root: Path) -> List[Bundle]:
    bundles: List[Bundle] = []
    for path in iter_doc_json_paths(kb_root):
        raw = read_json(path)
        if not isinstance(raw, dict):
            continue
        record = compiler.DocumentRecord(**raw)
        claims = read_jsonl(Path(record.claims_path))
        markdown_path = Path(record.markdown_path)
        markdown_text = markdown_path.read_text(encoding="utf-8", errors="replace") if markdown_path.exists() else ""
        bundles.append(Bundle(record=record, claims=claims, markdown_text=markdown_text, parsed_date=parse_date_text(record.date_text), normalized_title=normalize_title(record.title)))
    bundles.sort(key=lambda b: (b.parsed_date.sort_date, b.record.title.lower(), b.record.doc_id))
    return bundles


def build_entity_matchers(entity_patterns: Dict[str, Dict[str, Sequence[str]]]) -> Dict[Tuple[str, str], List[re.Pattern[str]]]:
    out: Dict[Tuple[str, str], List[re.Pattern[str]]] = {}
    for entity_type, entities in entity_patterns.items():
        for entity_name, patterns in entities.items():
            out[(entity_type, entity_name)] = [re.compile(pattern, re.IGNORECASE) for pattern in patterns]
    return out


def flexible_entity_regex(entity_name: str) -> Optional[re.Pattern[str]]:
    tokens = re.findall(r"[A-Za-z]+|\d+", entity_name)
    if not tokens:
        return None
    needs_variant_tracking = ("-" in entity_name) or (" " in entity_name) or bool(re.search(r"[A-Za-z].*\d|\d.*[A-Za-z]", entity_name))
    if not needs_variant_tracking:
        return None
    pattern = r"\b" + r"[-\s/]*".join(re.escape(tok) for tok in tokens) + r"\b"
    return re.compile(pattern, re.IGNORECASE)


def canonical_variant_key(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", text.lower())


def doc_ref_dict(bundle: Bundle) -> Dict[str, object]:
    return {"doc_id": bundle.record.doc_id, "title": bundle.record.title, "date_text": bundle.record.date_text, "report_number": bundle.record.report_number}


def scan_entity_variants(bundles: Sequence[Bundle], entity_patterns: Dict[str, Dict[str, Sequence[str]]]) -> List[Dict[str, object]]:
    findings: List[Dict[str, object]] = []
    for entity_type, entities in entity_patterns.items():
        for entity_name in entities:
            regex = flexible_entity_regex(entity_name)
            if regex is None:
                continue
            variant_hits: Dict[str, Dict[str, object]] = {}
            for bundle in bundles:
                for match in regex.finditer(bundle.markdown_text):
                    surface = match.group(0).strip()
                    entry = variant_hits.setdefault(surface, {"surface": surface, "surface_key": canonical_variant_key(surface), "doc_ids": set(), "count": 0})
                    entry["doc_ids"].add(bundle.record.doc_id)
                    entry["count"] += 1
            if len(variant_hits) < 2:
                continue
            findings.append({
                "entity_type": entity_type,
                "entity_name": entity_name,
                "variant_count": len(variant_hits),
                "variants": [
                    {"surface": entry["surface"], "doc_ids": sorted(entry["doc_ids"]), "count": int(entry["count"])}
                    for entry in sorted(variant_hits.values(), key=lambda item: (-int(item["count"]), str(item["surface"])))
                ],
            })
    findings.sort(key=lambda item: (item["entity_type"], item["entity_name"]))
    return findings


def detect_report_number_issues(bundles: Sequence[Bundle]) -> List[Dict[str, object]]:
    by_report: Dict[str, List[Bundle]] = collections.defaultdict(list)
    for bundle in bundles:
        if bundle.record.report_number:
            by_report[bundle.record.report_number].append(bundle)
    issues: List[Dict[str, object]] = []
    for report_number, group in sorted(by_report.items()):
        titles = collections.defaultdict(list)
        dates = collections.defaultdict(list)
        for bundle in group:
            titles[bundle.normalized_title].append(bundle)
            dates[bundle.record.date_text or "unknown"].append(bundle)
        if len(group) > 1:
            issues.append({"type": "duplicate_report_number", "report_number": report_number, "documents": [doc_ref_dict(bundle) for bundle in group]})
        if len(titles) > 1:
            issues.append({
                "type": "report_number_title_conflict",
                "report_number": report_number,
                "titles": {next(iter(title_group)).record.title if title_group else title_key: [doc_ref_dict(bundle) for bundle in title_group] for title_key, title_group in titles.items()},
            })
        known_dates = {date_text: refs for date_text, refs in dates.items() if date_text != "unknown"}
        if len(known_dates) > 1:
            issues.append({"type": "report_number_date_conflict", "report_number": report_number, "dates": {date_text: [doc_ref_dict(bundle) for bundle in refs] for date_text, refs in known_dates.items()}})
    return issues


def detect_title_reuse_issues(bundles: Sequence[Bundle]) -> List[Dict[str, object]]:
    by_title: Dict[str, List[Bundle]] = collections.defaultdict(list)
    for bundle in bundles:
        if bundle.normalized_title:
            by_title[bundle.normalized_title].append(bundle)
    issues: List[Dict[str, object]] = []
    for normalized_title, group in sorted(by_title.items()):
        if len(group) < 2:
            continue
        report_numbers = sorted({bundle.record.report_number or "unknown" for bundle in group})
        titles = sorted({bundle.record.title for bundle in group})
        if len(report_numbers) > 1:
            issues.append({"type": "title_reused_with_multiple_report_numbers", "normalized_title": normalized_title, "display_titles": titles, "report_numbers": report_numbers, "documents": [doc_ref_dict(bundle) for bundle in group]})
    return issues


def detect_possible_duplicates(bundles: Sequence[Bundle]) -> List[Dict[str, object]]:
    by_hash: Dict[str, List[Bundle]] = collections.defaultdict(list)
    for bundle in bundles:
        by_hash[bundle.record.file_hash].append(bundle)
    findings: List[Dict[str, object]] = []
    for digest, group in sorted(by_hash.items()):
        if len(group) > 1:
            findings.append({"type": "duplicate_content_hash", "file_hash": digest, "documents": [doc_ref_dict(bundle) for bundle in group]})
    title_groups: Dict[str, List[Bundle]] = collections.defaultdict(list)
    for bundle in bundles:
        title_groups[bundle.normalized_title].append(bundle)
    for normalized_title, group in sorted(title_groups.items()):
        if len(group) < 2 or not normalized_title:
            continue
        dates = sorted({bundle.record.date_text or "unknown" for bundle in group})
        if len(dates) <= 2:
            findings.append({"type": "possible_duplicate_title_group", "normalized_title": normalized_title, "dates": dates, "documents": [doc_ref_dict(bundle) for bundle in group]})
    return findings


def extract_numeric_values(text: str) -> Tuple[float, ...]:
    values: List[float] = []
    for token in NUMERIC_TOKEN_RE.findall(text):
        try:
            values.append(float(token))
        except ValueError:
            continue
    return tuple(values)


def extract_units(text: str) -> Tuple[str, ...]:
    return tuple(sorted({match.group(0).lower() for match in UNIT_TOKEN_RE.finditer(text)}))


def normalize_claim_template(text: str) -> str:
    text = text.lower()
    text = NUMERIC_TOKEN_RE.sub("<num>", text)
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"[^a-z0-9<>%./\- ]+", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def match_entities_in_text(text: str, matchers: Dict[Tuple[str, str], List[re.Pattern[str]]]) -> List[str]:
    matched: List[str] = []
    for (entity_type, entity_name), patterns in matchers.items():
        if any(pattern.search(text) for pattern in patterns):
            matched.append(f"{entity_type}:{entity_name}")
    return sorted(matched)


def detect_numeric_claim_disagreements(bundles: Sequence[Bundle], matchers: Dict[Tuple[str, str], List[re.Pattern[str]]]) -> List[Dict[str, object]]:
    grouped: Dict[Tuple[str, Tuple[str, ...], Tuple[str, ...], str], List[Dict[str, object]]] = collections.defaultdict(list)
    for bundle in bundles:
        for claim in bundle.claims:
            text = str(claim.get("text", "")).strip()
            if not text:
                continue
            values = extract_numeric_values(text)
            if not values:
                continue
            units = extract_units(text)
            template = normalize_claim_template(text)
            if len(template) < 25 or template.count("<num>") == 0:
                continue
            entities = tuple(match_entities_in_text(text, matchers))
            grouped[(template, units, entities, str(claim.get("claim_type", "technical-statement")))].append({
                "doc_id": bundle.record.doc_id,
                "title": bundle.record.title,
                "date_text": bundle.record.date_text,
                "report_number": bundle.record.report_number,
                "text": text,
                "values": values,
                "units": units,
                "claim_type": str(claim.get("claim_type", "technical-statement")),
                "entities": list(entities),
                "page_hint": claim.get("page_hint") if isinstance(claim.get("page_hint"), int) else None,
                "section": claim.get("section"),
            })
    findings: List[Dict[str, object]] = []
    for (template, units, entities, claim_type), items in grouped.items():
        if len(items) < 2:
            continue
        distinct_values = {tuple(item["values"]) for item in items}
        if len(distinct_values) < 2:
            continue
        if len(items) > 8:
            continue
        findings.append({"type": "numeric_claim_disagreement", "claim_template": template, "units": list(units), "entities": list(entities), "claim_type": claim_type, "occurrences": items})
    findings.sort(key=lambda item: (item["claim_type"], item["claim_template"]))
    return findings


def render_markdown_report(results: Dict[str, object]) -> str:
    lines: List[str] = [
        "# Inconsistency Report",
        "",
        f"Generated: {results['generated_at']}",
        "",
        "## Summary",
        "",
        f"- Documents scanned: {results['document_count']}",
        f"- Report-number issues: {len(results['report_number_issues'])}",
        f"- Title-reuse issues: {len(results['title_reuse_issues'])}",
        f"- Duplicate candidates: {len(results['duplicate_candidates'])}",
        f"- Entity-variant findings: {len(results['entity_variant_findings'])}",
        f"- Numeric-claim disagreements: {len(results['numeric_claim_disagreements'])}",
        "",
    ]
    lines.extend(["## Report Number Issues", ""])
    if results["report_number_issues"]:
        for item in results["report_number_issues"]:
            lines.append(f"### {item['type']} - {item['report_number']}")
            lines.append("")
            if item["type"] == "duplicate_report_number":
                for doc in item["documents"]:
                    lines.append(f"- {doc['doc_id']}: {doc['title']}")
            elif item["type"] == "report_number_title_conflict":
                for title, docs in item["titles"].items():
                    lines.append(f"- {title}")
                    for doc in docs:
                        lines.append(f"  - {doc['doc_id']}: {doc['title']}")
            elif item["type"] == "report_number_date_conflict":
                for date_text, docs in item["dates"].items():
                    lines.append(f"- {date_text}")
                    for doc in docs:
                        lines.append(f"  - {doc['doc_id']}: {doc['title']}")
            lines.append("")
    else:
        lines.extend(["- none", ""])

    lines.extend(["## Title Reuse Issues", ""])
    if results["title_reuse_issues"]:
        for item in results["title_reuse_issues"]:
            lines.append(f"### {item['normalized_title']}")
            lines.append("")
            lines.append(f"- Report numbers: {', '.join(item['report_numbers'])}")
            for doc in item["documents"]:
                lines.append(f"- {doc['doc_id']}: {doc['title']}")
            lines.append("")
    else:
        lines.extend(["- none", ""])

    lines.extend(["## Duplicate Candidates", ""])
    if results["duplicate_candidates"]:
        for item in results["duplicate_candidates"]:
            heading = item.get("file_hash") or item.get("normalized_title") or item["type"]
            lines.append(f"### {item['type']} - {heading}")
            lines.append("")
            for doc in item["documents"]:
                lines.append(f"- {doc['doc_id']}: {doc['title']}")
            lines.append("")
    else:
        lines.extend(["- none", ""])

    lines.extend(["## Entity Variant Findings", ""])
    if results["entity_variant_findings"]:
        for item in results["entity_variant_findings"]:
            lines.append(f"### {item['entity_name']} [{item['entity_type']}]")
            lines.append("")
            for variant in item["variants"]:
                lines.append(f"- {variant['surface']} - count {variant['count']} - docs: {', '.join(variant['doc_ids'])}")
            lines.append("")
    else:
        lines.extend(["- none", ""])

    lines.extend(["## Numeric Claim Disagreements", ""])
    if results["numeric_claim_disagreements"]:
        for item in results["numeric_claim_disagreements"]:
            lines.append(f"### {item['claim_type']}")
            lines.append("")
            lines.append(f"- Template: `{item['claim_template']}`")
            if item["units"]:
                lines.append(f"- Units: {', '.join(item['units'])}")
            if item["entities"]:
                lines.append(f"- Entities: {', '.join(item['entities'])}")
            for occ in item["occurrences"]:
                doc_line = f"- {occ['doc_id']}: {occ['title']}"
                if occ.get("page_hint") is not None:
                    doc_line += f" - page {occ['page_hint']}"
                lines.append(doc_line)
                lines.append(f"  - values: {occ['values']}")
                lines.append(f"  - {occ['text']}")
            lines.append("")
    else:
        lines.extend(["- none", ""])
    return "\n".join(lines)


def parse_args(argv: Optional[Sequence[str]] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Detect deterministic inconsistencies in the compiled KB.")
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
    entity_patterns = compiler.load_override_json(args.entity_patterns_json) or compiler.DEFAULT_ENTITY_PATTERNS
    matchers = build_entity_matchers(entity_patterns)
    results = {
        "generated_at": dt.datetime.utcnow().isoformat() + "Z",
        "document_count": len(bundles),
        "report_number_issues": detect_report_number_issues(bundles),
        "title_reuse_issues": detect_title_reuse_issues(bundles),
        "duplicate_candidates": detect_possible_duplicates(bundles),
        "entity_variant_findings": scan_entity_variants(bundles, entity_patterns),
        "numeric_claim_disagreements": detect_numeric_claim_disagreements(bundles, matchers),
    }
    write_json(kb_root / "reports" / "inconsistencies.json", results)
    write_text(kb_root / "reports" / "inconsistencies.md", render_markdown_report(results))
    print("done: " + f"documents={results['document_count']} " + f"report_issues={len(results['report_number_issues'])} " + f"title_reuse={len(results['title_reuse_issues'])} " + f"duplicates={len(results['duplicate_candidates'])} " + f"entity_variants={len(results['entity_variant_findings'])} " + f"numeric_disagreements={len(results['numeric_claim_disagreements'])}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
