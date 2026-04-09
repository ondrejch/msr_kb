#!/usr/bin/env python3
"""
Build a distilled, provenance-backed research layer from deterministic KB outputs.

This script intentionally reads only normalized deterministic outputs under kb/ and
produces a second-layer research view under kb/distilled/ plus generated guide pages
 under kb/wiki/research-guides/.
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
from typing import DefaultDict, Dict, Iterable, List, Optional, Sequence, Tuple

import deterministic_compiler_v2 as compiler


CATEGORY_DEFINITIONS: Sequence[Dict[str, object]] = (
    {
        "id": "salt-systems",
        "kind": "catalog",
        "description": "Canonical salt-system subjects used by the distilled research layer.",
        "outputs": ["catalogs/salt_systems.json", "wiki/research-guides/salt-systems.md"],
    },
    {
        "id": "materials-and-alloys",
        "kind": "catalog",
        "description": "Canonical materials and alloy subjects used by the distilled research layer.",
        "outputs": ["catalogs/materials.json", "wiki/research-guides/materials-and-compatibility.md"],
    },
    {
        "id": "program-families",
        "kind": "catalog",
        "description": "Deterministic family views that group distilled claims into ANP/precursor fluid-fuel, civilian molten-salt power-reactor, and fast-spectrum/chloride strands.",
        "outputs": [
            "catalogs/program_families.json",
            "wiki/research-guides/anp-and-precursor-fluid-fuel.md",
            "wiki/research-guides/civilian-molten-salt-power-reactors.md",
            "wiki/research-guides/fast-spectrum-and-chlorides.md",
        ],
    },
    {
        "id": "benchmark-packs",
        "kind": "catalog",
        "description": "Deterministic benchmark packs for named historical reactors with emphasis on reactor physics and system dynamics.",
        "outputs": [
            "catalogs/benchmark_packs.json",
            "benchmarks/are.json",
            "benchmarks/msbr.json",
            "benchmarks/msre.json",
            "wiki/research-guides/are-benchmark-pack.md",
            "wiki/research-guides/msbr-benchmark-pack.md",
            "wiki/research-guides/msre-benchmark-pack.md",
        ],
    },
    {
        "id": "comparison-matrices",
        "kind": "claims",
        "description": "Aggregated compatibility, property, and reactor-family comparison matrices derived from distilled claims.",
        "outputs": [
            "matrices/compatibility_matrix.json",
            "matrices/reactor_family_comparison.json",
            "matrices/salt_property_table.json",
            "wiki/research-guides/compatibility-matrix.md",
            "wiki/research-guides/property-tables.md",
            "wiki/research-guides/reactor-family-comparison.md",
        ],
    },
    {
        "id": "thermophysical-properties",
        "kind": "claims",
        "description": "Deterministic property claims for salts and materials with explicit conditions and evidence.",
        "outputs": ["claims/properties.jsonl"],
    },
    {
        "id": "salt-material-compatibility",
        "kind": "claims",
        "description": "Compatibility, corrosion, cracking, and embrittlement observations for materials in molten salts.",
        "outputs": ["claims/compatibility.jsonl", "wiki/research-guides/materials-and-compatibility.md"],
    },
    {
        "id": "msr-reactor-physics",
        "kind": "claims",
        "description": "MSR reactor-physics claims such as breeding ratio, coefficients, neutron lifetime, inventory, and xenon effects.",
        "outputs": ["claims/physics.jsonl", "wiki/research-guides/reactor-physics.md"],
    },
    {
        "id": "msr-system-dynamics",
        "kind": "claims",
        "description": "MSR system-dynamics claims such as transient response, stability, transport delays, controllers, and frequency response.",
        "outputs": ["claims/dynamics.jsonl", "wiki/research-guides/system-dynamics.md"],
    },
)

INTERESTING_ENTITY_TYPES: Sequence[str] = (
    "salt-system",
    "alloy-material",
    "reactor",
    "reactor-concept",
    "component",
)

REFERENCE_SECTION_HINTS = (
    "references",
    "external distribution",
    "internal distribution",
    "distribution",
)

TARGET_REACTORS = {
    "ARE",
    "ART",
    "MSRE",
    "MSBR",
    "MSCR",
    "DMSR",
    "MCFR",
    "MSBE",
    "MOSEL",
}

TARGET_REACTOR_CONCEPTS = {
    "BATR",
    "fluid-fuel reactor",
}

MSR_CONTEXT_REACTOR_CONCEPTS = {
    "single-fluid breeder",
    "two-fluid breeder",
    "one-fluid breeder",
    "converter reactor",
}

FAST_CONTEXT_PATTERN = re.compile(
    r"molten[- ]salt fast|molten chlorides?|chloride salt|chloride[- ]fast|fast[- ]spectrum|fast flux|plutonium chloride|fueled with molten chlorides|very fast neutron spectrum|\bMSFR(?:-\d+)?\b|\bMCFR\b|\bMCFBR\b|\bBATR\b",
    re.IGNORECASE,
)

PROGRAM_FAMILY_DEFINITIONS: Sequence[Dict[str, str]] = (
    {
        "description": "Aircraft Nuclear Propulsion and precursor fluid-fuel reactor work, including ARE, ART, aqueous homogeneous, and early circulating-fuel studies.",
        "guide": "anp-and-precursor-fluid-fuel.md",
        "id": "anp-and-precursor-fluid-fuel",
        "title": "ANP and Precursor Fluid-Fuel",
    },
    {
        "description": "Civilian molten-salt power-reactor work centered on MSRE, MSBR, MSCR, DMSR, and related ORNL power-reactor development.",
        "guide": "civilian-molten-salt-power-reactors.md",
        "id": "civilian-molten-salt-power-reactors",
        "title": "Civilian Molten-Salt Power Reactors",
    },
    {
        "description": "Fast-spectrum molten-salt and chloride research, including MCFR, MSFR, BATR, chloride salts, and molten-salt fast-reactor studies.",
        "guide": "fast-spectrum-and-chlorides.md",
        "id": "fast-spectrum-and-chlorides",
        "title": "Fast-Spectrum and Chlorides",
    },
)

PROGRAM_FAMILY_MAP: Dict[str, Dict[str, str]] = {row["id"]: row for row in PROGRAM_FAMILY_DEFINITIONS}

BENCHMARK_DEFINITIONS: Sequence[Dict[str, object]] = (
    {
        "aliases": (r"\bARE\b", r"aircraft reactor experiment"),
        "guide": "are-benchmark-pack.md",
        "id": "are",
        "reactor": "ARE",
        "title": "Aircraft Reactor Experiment (ARE)",
    },
    {
        "aliases": (r"\bMSRE\b", r"molten[- ]salt reactor experiment"),
        "guide": "msre-benchmark-pack.md",
        "id": "msre",
        "reactor": "MSRE",
        "title": "Molten-Salt Reactor Experiment (MSRE)",
    },
    {
        "aliases": (r"\bMSBR\b", r"molten[- ]salt breeder reactor"),
        "guide": "msbr-benchmark-pack.md",
        "id": "msbr",
        "reactor": "MSBR",
        "title": "Molten-Salt Breeder Reactor (MSBR)",
    },
)

ANP_REACTORS = {"ARE", "ART", "HRE", "AHR", "LMFR"}
CIVILIAN_REACTORS = {"MSRE", "MSBR", "MSCR", "DMSR", "MSBE", "MOSEL"}
FAST_REACTORS = {"MCFR"}

GENERIC_TITLE_PATTERNS = tuple(
    re.compile(pattern, re.IGNORECASE)
    for pattern in (
        r"^declas+sified$",
        r"^clas+sified$",
        r"^master copy$",
        r"^master$",
        r"^ornl master copy$",
        r"^legal notice$",
        r"^general information$",
        r"^secret(?:.*information)?$",
        r"^received by .*",
        r"^for internal use only$",
        r"^unclassified$",
        r"^assified$",
        r"^central research library(?:.*)$",
        r"^martin marietta energy systems libraries$",
        r"^oak ridge national laboratory(?: libraries)?$",
        r"^aec research and development report(?:.*)$",
        r"^united states atomic energy commission$",
        r"^copy no\.?$",
        r"^date:.*$",
    )
)

GENERIC_AUTHOR_PATTERNS = tuple(
    re.compile(pattern, re.IGNORECASE)
    for pattern in (
        r"^operated by$",
        r"^document collection$",
        r"^from:.*$",
        r"^progress$",
        r"^master$",
        r"^tennessee$",
        r"^classified$",
        r"^declas+sified$",
        r"^resecrn.*$",
        r"^.*research and development.*$",
        r"^central research.*$",
        r"^union carbide.*$",
        r"^oak ridge national laboratory.*$",
        r"^martin marietta.*$",
        r"^post office box.*$",
        r"^contract no\.? .*",
        r"^u\.?s\.? atomic energy commission$",
        r"^copy no\.?$",
    )
)

GENERIC_SALT_NAMES = {
    "fluoride salt",
    "chloride salt",
    "LiF",
    "NaF",
    "KF",
    "RbF",
    "UF4",
    "UF3",
    "ThF4",
    "ZrF4",
    "BeF2",
}

GENERIC_MATERIAL_NAMES = {
    "nickel",
    "molybdenum",
    "zirconium",
    "beryllium",
    "niobium",
    "titanium",
}


def _compile_rules(raw_rules: Sequence[Tuple[str, Sequence[str]]]) -> Sequence[Tuple[str, Sequence[re.Pattern[str]]]]:
    return [(name, tuple(re.compile(pattern, re.IGNORECASE) for pattern in patterns)) for name, patterns in raw_rules]


PROPERTY_RULES = _compile_rules(
    (
        ("liquidus-temperature", (r"\bliquidus\b",)),
        ("density", (r"\bdensity\b", r"\\rho", r"g\s*/\s*cm\^?3", r"g\s*/\s*c\s*m")),
        ("viscosity", (r"\bviscosity\b", r"centipoises?", r"centistokes?", r"\bmu\s*=")),
        ("heat-capacity", (r"heat capacity", r"\bc\s*_?\{?p\}?\b")),
        ("thermal-conductivity", (r"thermal conductivity",)),
        ("thermal-expansion", (r"volumetric coefficient of liquid expansion", r"\bexpansivit(?:y|ies)\b", r"\bexpansion\b")),
        ("molar-volume", (r"molar volume",)),
        ("surface-tension", (r"surface tension",)),
        ("heat-of-fusion", (r"heat of fusion",)),
    )
)

COMPATIBILITY_RULES = _compile_rules(
    (
        ("tellurium-embrittlement", (r"tellur(?:ium|ide)",)),
        ("grain-boundary-cracking", (r"grain boundary", r"intergranular", r"\bcrack(?:ing|ed)?\b")),
        ("corrosion-or-attack", (r"\bcorrosion\b", r"\battack(?:ed)?\b", r"penetration", r"weight increase")),
        ("compatibility", (r"compatible", r"used to contain", r"resist", r"not attacked", r"did not show intergranular cracking", r"absence of grain boundary cracks")),
    )
)

PHYSICS_RULES = _compile_rules(
    (
        ("breeding-ratio", (r"breeding ratio",)),
        ("conversion-ratio", (r"conversion ratio",)),
        ("doubling-time", (r"doubling time",)),
        ("fuel-reactivity-coefficient", (r"fuel reactivity coefficient", r"fuel temperature coefficient")),
        ("graphite-reactivity-coefficient", (r"graphite reactivity coefficient", r"graphite temperature coefficient")),
        ("temperature-coefficient", (r"temperature coefficient",)),
        ("delayed-neutron-fraction", (r"delayed[ -]neutron fraction", r"effective delayed[ -]neutron fraction", r"delayed neutron constants.*β\s*=", r"delayed neutron constants.*beta\s*=")),
        ("neutron-lifetime", (r"neutron generation time", r"thermal neutron lifetime", r"prompt neutron lifetime", r"neutron lifetime")),
        ("fissile-inventory", (r"specific fissile inventory", r"fissile inventory", r"inventory, fissile", r"fuel specific inventory")),
        ("fuel-cycle-cost", (r"fuel cycle cost", r"fuel-cycle cost", r"mill/kwh",)),
        ("power-density", (r"power density",)),
        ("salt-volume-fraction", (r"salt volume fraction", r"salt fraction")),
        ("flux", (r"damage flux", r"neutron flux", r"peak flux", r"flux distribution", r"fast-neutron fluence")),
        ("xenon-poisoning-effect", (r"xenon", r"poisoning effect", r"residual poisoning")),
        ("criticality", (r"criticality was first achieved", r"critical mass", r"\bcriticality\b")),
    )
)

DYNAMICS_RULES = _compile_rules(
    (
        ("kinetics-model", (r"kinetics model", r"nuclear kinetics model", r"state variable model", r"two-delay-group", r"MATEXP", r"SFR-III", r"MSFR")),
        ("transient-response", (r"transient response", r"step input", r"step reactivity", r"reactivity input", r"perturbation", r"startup transient", r"shutdown transient")),
        ("frequency-response", (r"frequency response", r"autocorrelation", r"cross-correlation", r"PRBS", r"PRTS")),
        ("stability", (r"stability analysis", r"Nyquist", r"Mikhailov", r"eigenvalue", r"no encirclements", r"stable system", r"stable operation", r"well-behaved system", r"dynamics or stability problems")),
        ("transport-delay", (r"transit time", r"loop time", r"time delay", r"time delays", r"core transit time", r"external loop transit time")),
        ("control-system", (r"controller", r"control rod drive", r"flux demand", r"rod-demand", r"power demand", r"temperature controller", r"flow controller")),
        ("mixing-recirculation", (r"fuel recirculation", r"recirculation effect", r"mixing in headers and piping", r"mixing chamber", r"circulating loop")),
    )
)

CONDITION_PATTERNS = tuple(
    re.compile(pattern, re.IGNORECASE)
    for pattern in (
        r"\d+(?:\.\d+)?\s*(?:mole\s*%|mol\s*%|vol\s*%|ppm|psia|MW\(e\)|MW\(t\)|MWth|MW|MWd/T|rad/sec|hours?|hrs?|days?|sec|seconds?)",
        r"\d+(?:\.\d+)?\s*(?:\^\{\\circ\}|°)\s*(?:\\mathrm\{)?[CFK]",
        r"\d+(?:\.\d+)?\s*[CFK]\b",
        r"U\(IV\)\s*/\s*U\(III\)(?:\s*ratio)?(?:[^0-9]{0,16})[~≈]?\s*\d+(?:\.\d+)?",
        r"\d+(?:\.\d+)?\s*%\s*(?:δ\s*ρ|δ\s*k\s*/\s*k|\\delta\s*\\rho|\\delta\s*k\s*/\s*k)",
    )
)

VALUE_PATTERNS = {
    "breeding-ratio": tuple(re.compile(p, re.IGNORECASE) for p in (
        r"breeding ratio(?:[^0-9<>=~±-]{0,40}|</td><td>)([~≈±+\-]?\s*\d+(?:\.\d+)?)",
    )),
    "conversion-ratio": tuple(re.compile(p, re.IGNORECASE) for p in (
        r"conversion ratio(?:[^0-9<>=~±-]{0,40})([~≈±+\-]?\s*\d+(?:\.\d+)?)",
    )),
    "doubling-time": tuple(re.compile(p, re.IGNORECASE) for p in (
        r"doubling time(?:, system)?(?:[^0-9]{0,20}|</td><td>)([~≈±+\-]?\s*\d+(?:\.\d+)?\s*(?:years?|year)?)",
        r"fuel doubling time of\s*([~≈±+\-]?\s*\d+(?:\.\d+)?\s*(?:years?|year))",
    )),
    "fuel-cycle-cost": tuple(re.compile(p, re.IGNORECASE) for p in (
        r"([~≈±+\-]?\s*\d+(?:\.\d+)?\s*mill\s*/\s*kWh\(e\))",
    )),
    "delayed-neutron-fraction": tuple(re.compile(p, re.IGNORECASE) for p in (
        r"delayed[ -]neutron fraction(?:[^0-9]{0,20})([0-9.]+)",
        r"β\s*=\s*([0-9.]+)",
        r"beta\s*=\s*([0-9.]+)",
    )),
    "neutron-lifetime": tuple(re.compile(p, re.IGNORECASE) for p in (
        r"(?:neutron generation time|thermal neutron lifetime|prompt neutron lifetime)(?:[^0-9]{0,24})([0-9.]+\s*(?:[×x]\s*10\s*[-+]?\d+)?\s*(?:sec|s)?)",
    )),
    "fissile-inventory": tuple(re.compile(p, re.IGNORECASE) for p in (
        r"(?:specific fissile inventory of|inventory, fissile, kg</td><td>|fuel specific inventory, kg/MW\(e\)</td><td>)([~≈±+\-]?\s*\d+(?:\.\d+)?)",
    )),
    "power-density": tuple(re.compile(p, re.IGNORECASE) for p in (
        r"power density(?:[^0-9]{0,24}|</td><td>)([~≈±+\-]?\s*\d+(?:\.\d+)?)",
    )),
    "salt-volume-fraction": tuple(re.compile(p, re.IGNORECASE) for p in (
        r"(?:salt volume fraction|salt fraction)(?:[^0-9]{0,24})([0-9.]+(?:\s*to\s*[0-9.]+)?(?:\s*(?:vol)?\s*%?)?)",
    )),
    "transport-delay": tuple(re.compile(p, re.IGNORECASE) for p in (
        r"([0-9]+(?:\.[0-9]+)?\s*sec)",
        r"([0-9]+(?:\.[0-9]+)?\s*rad/sec)",
    )),
}


@dataclasses.dataclass
class ClaimBlock:
    claim_types: List[str]
    line_start: int
    line_end: int
    page_hint: Optional[str]
    section: str
    text: str


@dataclasses.dataclass
class Bundle:
    record: Dict[str, object]
    claims: List[ClaimBlock]
    entity_names: Dict[str, List[str]]
    entity_counts: Dict[str, Dict[str, int]]
    line_index: Dict[str, Dict[int, List[str]]]
    title_compact: str


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


def write_jsonl(path: Path, rows: Sequence[Dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def safe_rmtree(path: Path) -> None:
    if path.exists() and path.is_dir():
        shutil.rmtree(path)


def compact(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", text.lower())


def clean_ws(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def strip_markup(text: str) -> str:
    text = text.replace("$", " ")
    text = re.sub(r"!\[[^\]]*\]\([^)]*\)", " ", text)
    text = re.sub(r"<[^>]+>", " ", text)
    return clean_ws(text)


def truncate(text: str, limit: int = 220) -> str:
    plain = clean_ws(text)
    if len(plain) <= limit:
        return plain
    return plain[: limit - 1].rstrip() + "…"


def report_label_from_record(record: Dict[str, object]) -> str:
    source_dir = Path(str(record.get("source_dir") or "")).name
    if source_dir:
        return source_dir.replace("_", "-")
    report_numbers = record.get("report_numbers") if isinstance(record.get("report_numbers"), list) else []
    for value in report_numbers:
        if isinstance(value, str) and clean_ws(value):
            return clean_ws(value)
    return str(record.get("doc_id") or "unknown")


def is_bad_display_title(title: str) -> bool:
    raw = clean_ws(title)
    plain = strip_markup(title)
    if not plain:
        return True
    if raw.startswith("!["):
        return True
    return any(pattern.match(plain) for pattern in GENERIC_TITLE_PATTERNS)


def author_title_candidate(record: Dict[str, object]) -> Optional[str]:
    authors = record.get("authors") if isinstance(record.get("authors"), list) else []
    for value in authors:
        if not isinstance(value, str):
            continue
        if "\\" in value:
            continue
        candidate = strip_markup(value)
        if len(candidate) < 6:
            continue
        alpha_chunks = re.findall(r"[A-Za-z]{2,}", candidate)
        if len("".join(alpha_chunks)) < 8:
            continue
        if any(pattern.match(candidate) for pattern in GENERIC_AUTHOR_PATTERNS):
            continue
        return candidate
    return None


def display_title_from_record(record: Dict[str, object]) -> str:
    title = str(record.get("title") or "")
    clean_title = strip_markup(title)
    if clean_title and not is_bad_display_title(title):
        return clean_title
    report_label = report_label_from_record(record)
    candidate = author_title_candidate(record)
    if candidate and compact(candidate) != compact(report_label):
        return f"{report_label} — {candidate}"
    return report_label


def unique_preserve(values: Iterable[str]) -> List[str]:
    seen = set()
    result: List[str] = []
    for value in values:
        if value in seen:
            continue
        seen.add(value)
        result.append(value)
    return result


def iter_doc_json_paths(kb_root: Path) -> Iterable[Path]:
    docs_root = kb_root / "normalized" / "docs"
    if not docs_root.exists():
        return []
    return sorted(docs_root.glob("*.json"))


def is_reference_like_section(section: str) -> bool:
    low = section.lower().strip()
    return any(hint in low for hint in REFERENCE_SECTION_HINTS)


def has_numeric_signal(text: str) -> bool:
    return bool(re.search(r"\d", text))


def is_specific_salt(name: str) -> bool:
    return name not in GENERIC_SALT_NAMES


def is_specific_material(name: str) -> bool:
    return name not in GENERIC_MATERIAL_NAMES


def is_target_reactor_name(name: str, entity_type: str) -> bool:
    if entity_type == "reactor":
        return name in TARGET_REACTORS
    if entity_type == "reactor-concept":
        return name in TARGET_REACTOR_CONCEPTS
    return False


def is_allowed_msr_concept(name: str, text: str) -> bool:
    if name in TARGET_REACTOR_CONCEPTS:
        return True
    if name not in MSR_CONTEXT_REACTOR_CONCEPTS:
        return False
    return bool(re.search(r"molten[- ]salt|fuel salt|fluoride fuel|\bMSR\b|\bMSBR\b|\bMSCR\b|\bDMSR\b", text, flags=re.IGNORECASE))


def entity_sort_key(bundle: Bundle, entity_type: str, name: str) -> Tuple[int, int, str]:
    return (
        0 if name.lower() not in {"fluoride salt", "chloride salt"} else 1,
        -len(compact(name)),
        -bundle.entity_counts.get(entity_type, {}).get(name, 0),
        name.lower(),
    )


def prune_substring_matches(bundle: Bundle, entity_type: str, names: Iterable[str]) -> List[str]:
    ordered = sorted(set(names), key=lambda name: entity_sort_key(bundle, entity_type, name))
    kept: List[str] = []
    kept_compact: List[str] = []
    for name in ordered:
        c_name = compact(name)
        if any(c_name != other and c_name and c_name in other for other in kept_compact):
            continue
        kept.append(name)
        kept_compact.append(c_name)
    return kept


def name_mentioned_in_text(name: str, text: str) -> bool:
    if not name:
        return False
    escaped = re.escape(name)
    flexible = escaped.replace(r"\-", r"[- ]?").replace(r"\ ", r"[- ]?")
    if len(compact(name)) <= 4 and name.upper() == name and re.fullmatch(r"[A-Z0-9]+", name):
        return bool(re.search(rf"\b{re.escape(name)}\b", text))
    if len(compact(name)) <= 4 and re.fullmatch(r"[A-Za-z0-9]+", name):
        return bool(re.search(rf"\b{re.escape(name)}\b", text, flags=re.IGNORECASE))
    if re.search(flexible, text, flags=re.IGNORECASE):
        return True
    return compact(name) in compact(text)


def group_claim_rows(rows: Sequence[Dict[str, object]]) -> List[ClaimBlock]:
    grouped: List[ClaimBlock] = []
    current_key: Optional[Tuple[int, int, Optional[str], str]] = None
    current_types: List[str] = []
    current_texts: List[str] = []
    for row in sorted(rows, key=lambda item: (
        int(item.get("line_start", 0) or 0),
        int(item.get("line_end", 0) or 0),
        str(item.get("section") or ""),
        str(item.get("claim_type") or ""),
    )):
        line_start = int(row.get("line_start", 0) or 0)
        line_end = int(row.get("line_end", line_start) or line_start)
        page_hint = row.get("page_hint") if isinstance(row.get("page_hint"), str) else None
        section = str(row.get("section") or "")
        key = (line_start, line_end, page_hint, section)
        text = strip_markup(str(row.get("text") or ""))
        claim_type = str(row.get("claim_type") or "unknown")
        if current_key is None or key != current_key:
            if current_key is not None:
                grouped.append(
                    ClaimBlock(
                        claim_types=sorted(set(current_types)),
                        line_start=current_key[0],
                        line_end=current_key[1],
                        page_hint=current_key[2],
                        section=current_key[3],
                        text=clean_ws(" ".join(unique_preserve(current_texts))),
                    )
                )
            current_key = key
            current_types = [claim_type]
            current_texts = [text]
        else:
            current_types.append(claim_type)
            current_texts.append(text)
    if current_key is not None:
        grouped.append(
            ClaimBlock(
                claim_types=sorted(set(current_types)),
                line_start=current_key[0],
                line_end=current_key[1],
                page_hint=current_key[2],
                section=current_key[3],
                text=clean_ws(" ".join(unique_preserve(current_texts))),
            )
        )
    return grouped


def build_bundle(record: Dict[str, object], claim_rows: Sequence[Dict[str, object]]) -> Bundle:
    entity_names: Dict[str, List[str]] = {}
    entity_counts: Dict[str, Dict[str, int]] = {}
    line_index: Dict[str, Dict[int, List[str]]] = {}
    entities = record.get("entities", {}) if isinstance(record.get("entities"), dict) else {}
    for entity_type in INTERESTING_ENTITY_TYPES:
        entries = entities.get(entity_type, []) if isinstance(entities.get(entity_type), list) else []
        counts: Dict[str, int] = {}
        per_line: DefaultDict[int, List[str]] = collections.defaultdict(list)
        for entry in entries:
            if not isinstance(entry, dict):
                continue
            name = entry.get("name")
            if not isinstance(name, str):
                continue
            counts[name] = int(entry.get("count", 0) or 0)
            for hit in entry.get("line_hits", []):
                if isinstance(hit, int):
                    per_line[hit].append(name)
        entity_names[entity_type] = [name for name, _ in sorted(counts.items(), key=lambda item: (-item[1], item[0].lower()))]
        entity_counts[entity_type] = counts
        line_index[entity_type] = {line: sorted(set(names)) for line, names in per_line.items()}
    return Bundle(
        record=record,
        claims=group_claim_rows(claim_rows),
        entity_names=entity_names,
        entity_counts=entity_counts,
        line_index=line_index,
        title_compact=compact(str(record.get("title") or "")),
    )


def load_bundles(kb_root: Path) -> List[Bundle]:
    bundles: List[Bundle] = []
    for doc_path in iter_doc_json_paths(kb_root):
        raw = read_json(doc_path)
        if not isinstance(raw, dict):
            continue
        claims_path_value = raw.get("claims_path")
        claims_path = kb_root / "normalized" / "claims" / f"{doc_path.stem}.jsonl"
        if isinstance(claims_path_value, str):
            candidate = Path(claims_path_value)
            if candidate.is_absolute():
                claims_path = candidate
            else:
                claims_path = Path(kb_root.parent / candidate)
        bundles.append(build_bundle(raw, read_jsonl(claims_path)))
    return bundles


def explicit_entity_names(bundle: Bundle, block: ClaimBlock, entity_type: str, window: int = 3) -> List[str]:
    names: List[str] = []
    for line_no in range(block.line_start - window, block.line_end + window + 1):
        names.extend(bundle.line_index.get(entity_type, {}).get(line_no, []))
    for name in bundle.entity_names.get(entity_type, []):
        if name_mentioned_in_text(name, block.text):
            names.append(name)
    if entity_type in {"reactor", "reactor-concept"}:
        names = [name for name in names if len(compact(name)) > 4 or name_mentioned_in_text(name, block.text)]
    return prune_substring_matches(bundle, entity_type, names)


def direct_entity_names(bundle: Bundle, block: ClaimBlock, entity_type: str) -> List[str]:
    names = [name for name in bundle.entity_names.get(entity_type, []) if name_mentioned_in_text(name, block.text)]
    if entity_type in {"reactor", "reactor-concept"}:
        names = [name for name in names if len(compact(name)) > 4 or name_mentioned_in_text(name, block.text)]
    return prune_substring_matches(bundle, entity_type, names)


def fallback_entity_names(bundle: Bundle, entity_type: str) -> List[str]:
    names = bundle.entity_names.get(entity_type, [])
    title_matches = [name for name in names if name_mentioned_in_text(name, str(bundle.record.get("title") or ""))]
    if title_matches:
        return prune_substring_matches(bundle, entity_type, title_matches)
    if entity_type in {"reactor", "reactor-concept"}:
        return []
    if len(names) == 1:
        return [names[0]]
    return []


def resolve_entity_names(
    bundle: Bundle,
    block: ClaimBlock,
    entity_type: str,
    section_context: Dict[str, Dict[str, Tuple[int, List[str]]]],
    global_context: Dict[str, Tuple[int, List[str]]],
    max_section_gap: int = 48,
    max_global_gap: int = 20,
) -> List[str]:
    explicit = explicit_entity_names(bundle, block, entity_type)
    if explicit:
        return explicit
    section_entry = section_context.get(block.section, {}).get(entity_type)
    if section_entry and block.line_start - section_entry[0] <= max_section_gap:
        return section_entry[1]
    global_entry = global_context.get(entity_type)
    if global_entry and block.line_start - global_entry[0] <= max_global_gap:
        return global_entry[1]
    return fallback_entity_names(bundle, entity_type)


def resolve_reactor_subject(
    bundle: Bundle,
    block: ClaimBlock,
    section_context: Dict[str, Dict[str, Tuple[int, List[str]]]],
    global_context: Dict[str, Tuple[int, List[str]]],
) -> Optional[Tuple[str, str]]:
    combined = f"{bundle.record.get('title') or ''} {block.section} {block.text}"
    explicit_reactors = [name for name in direct_entity_names(bundle, block, "reactor") if is_target_reactor_name(name, "reactor")]
    if explicit_reactors:
        return ("reactor", explicit_reactors[0])
    explicit_concepts = [name for name in direct_entity_names(bundle, block, "reactor-concept") if is_allowed_msr_concept(name, combined)]
    if explicit_concepts:
        return ("reactor-concept", explicit_concepts[0])
    if re.search(r"molten[- ]salt reactor|fluid[- ]fuel reactor", combined, flags=re.IGNORECASE):
        return ("reactor-concept", "fluid-fuel reactor")
    reactors = [name for name in resolve_entity_names(bundle, block, "reactor", section_context, global_context) if is_target_reactor_name(name, "reactor")]
    if reactors:
        return ("reactor", reactors[0])
    concepts = [name for name in resolve_entity_names(bundle, block, "reactor-concept", section_context, global_context) if is_allowed_msr_concept(name, combined)]
    if concepts:
        return ("reactor-concept", concepts[0])
    return None


def has_target_reactor_context(
    bundle: Bundle,
    block: ClaimBlock,
    section_context: Dict[str, Dict[str, Tuple[int, List[str]]]],
    global_context: Dict[str, Tuple[int, List[str]]],
) -> bool:
    combined = f"{bundle.record.get('title') or ''} {block.section} {block.text}"
    explicit_reactors = [name for name in direct_entity_names(bundle, block, "reactor") if is_target_reactor_name(name, "reactor")]
    explicit_concepts = [name for name in direct_entity_names(bundle, block, "reactor-concept") if is_allowed_msr_concept(name, combined)]
    if explicit_reactors or explicit_concepts:
        return True
    title = str(bundle.record.get("title") or "")
    source_dir = Path(str(bundle.record.get("source_dir") or "")).name
    title_and_source = f"{title} {source_dir}"
    if re.search(r"molten[- ]salt reactor|molten[- ]salt breeder|\bMSRE\b|\bMSBR\b|\bMSCR\b|\bDMSR\b|\bMCFR\b|\bARE\b|\bART\b", title_and_source, flags=re.IGNORECASE):
        return True
    subject = resolve_reactor_subject(bundle, block, section_context, global_context)
    return subject is not None and name_mentioned_in_text(subject[1], block.text)


def detect_relations(text: str, rules: Sequence[Tuple[str, Sequence[re.Pattern[str]]]]) -> List[str]:
    matches: List[str] = []
    for relation, patterns in rules:
        if any(pattern.search(text) for pattern in patterns):
            matches.append(relation)
    if "fuel-reactivity-coefficient" in matches or "graphite-reactivity-coefficient" in matches:
        matches = [relation for relation in matches if relation != "temperature-coefficient"]
    return matches


def detect_first_relation(text: str, rules: Sequence[Tuple[str, Sequence[re.Pattern[str]]]]) -> Optional[str]:
    for relation, patterns in rules:
        if any(pattern.search(text) for pattern in patterns):
            return relation
    return None


def extract_conditions(text: str) -> List[str]:
    fragments: List[str] = []
    for pattern in CONDITION_PATTERNS:
        for match in pattern.finditer(text):
            fragments.append(clean_ws(match.group(0)))
    return unique_preserve(fragment for fragment in fragments if fragment)[:8]


def extract_value_text(text: str, relation: str) -> str:
    patterns = VALUE_PATTERNS.get(relation, ())
    for pattern in patterns:
        match = pattern.search(text)
        if not match:
            continue
        groups = [clean_ws(group) for group in match.groups() if isinstance(group, str) and clean_ws(group)]
        if groups:
            return truncate("; ".join(groups), limit=140)
        return truncate(clean_ws(match.group(0)), limit=140)
    return truncate(text, limit=180)


def infer_source_kind(record: Dict[str, object]) -> str:
    series = str(record.get("report_series") or "")
    source_dir = Path(str(record.get("source_dir") or "")).name.lower()
    if series in {"nuclear-science-and-engineering", "nuclear-applications-and-technology"}:
        return "journal-article"
    if series == "natural-language-summaries" or source_dir.startswith("nat_"):
        return "conference-paper"
    if "progress-report" in series:
        return "progress-report"
    if series in {"ornl-technical-memorandum", "ornl-central-files"}:
        return "memo"
    if source_dir.startswith("nse_"):
        return "journal-article"
    if bool(record.get("document_type") == "paper"):
        return "paper"
    return "report"


def infer_program_family(
    bundle: Bundle,
    block: ClaimBlock,
    subject_type: str,
    subject_name: str,
    object_type: Optional[str] = None,
    object_name: Optional[str] = None,
) -> str:
    record = bundle.record
    title = str(record.get("title") or "")
    source_dir = Path(str(record.get("source_dir") or "")).name
    topics = record.get("topics", []) if isinstance(record.get("topics"), list) else []
    context = f"{title} {source_dir} {block.section}"
    combined = f"{title} {source_dir} {block.section} {block.text}"
    combined_low = combined.lower()

    if subject_type == "reactor":
        if subject_name in FAST_REACTORS:
            return "fast-spectrum-and-chlorides"
        if subject_name in ANP_REACTORS:
            return "anp-and-precursor-fluid-fuel"
        if subject_name in CIVILIAN_REACTORS:
            return "civilian-molten-salt-power-reactors"
    if subject_type == "reactor-concept":
        if subject_name == "BATR":
            return "fast-spectrum-and-chlorides"
        if subject_name in MSR_CONTEXT_REACTOR_CONCEPTS:
            if FAST_CONTEXT_PATTERN.search(context):
                return "fast-spectrum-and-chlorides"
            if "aircraft-nuclear-propulsion" in topics or "aqueous-homogeneous-reactors" in topics:
                return "anp-and-precursor-fluid-fuel"
            if re.search(r"aircraft|homogeneous reactor|aqueous homogeneous|\bARE\b|\bART\b|\bHRE\b|\bAHR\b|\bANP\b", combined, flags=re.IGNORECASE):
                return "anp-and-precursor-fluid-fuel"
            return "civilian-molten-salt-power-reactors"
        if subject_name == "fluid-fuel reactor":
            if FAST_CONTEXT_PATTERN.search(context):
                return "fast-spectrum-and-chlorides"
            if "aircraft-nuclear-propulsion" in topics or "aqueous-homogeneous-reactors" in topics:
                return "anp-and-precursor-fluid-fuel"
            if re.search(r"aircraft|homogeneous reactor|aqueous homogeneous|\bARE\b|\bART\b|\bHRE\b|\bAHR\b|\bANP\b", combined, flags=re.IGNORECASE):
                return "anp-and-precursor-fluid-fuel"
            return "civilian-molten-salt-power-reactors"

    salt_names = {name for name in (subject_name, object_name or "") if name}
    if object_type == "salt-system" and object_name:
        salt_names.add(object_name)
    if "chloride salt" in salt_names or FAST_CONTEXT_PATTERN.search(context):
        return "fast-spectrum-and-chlorides"

    if "aircraft-nuclear-propulsion" in topics or "aqueous-homogeneous-reactors" in topics:
        return "anp-and-precursor-fluid-fuel"
    if re.search(r"aircraft nuclear propulsion|aircraft reactor|homogeneous reactor|aqueous homogeneous|\bANP\b|\bARE\b|\bART\b|\bHRE\b|\bAHR\b", combined, flags=re.IGNORECASE):
        return "anp-and-precursor-fluid-fuel"

    if re.search(r"molten[- ]salt reactor|molten[- ]salt breeder|\bMSRE\b|\bMSBR\b|\bMSCR\b|\bDMSR\b|msr program|fuel salt", combined, flags=re.IGNORECASE):
        return "civilian-molten-salt-power-reactors"

    if subject_type == "salt-system" and subject_name in {"FLiBe", "FLiNaK", "LiF-BeF2-ThF4", "LiF-BeF2-UF4", "LiF-BeF2-ThF4-UF4", "NaBF4-NaF"}:
        return "civilian-molten-salt-power-reactors"
    if subject_type == "alloy-material" and subject_name in {"Hastelloy N", "INOR-8", "graphite", "Hastelloy B", "Inconel X"}:
        return "civilian-molten-salt-power-reactors"

    if "molten salt" in combined_low:
        return "civilian-molten-salt-power-reactors"
    return "anp-and-precursor-fluid-fuel"


def make_claim(
    bundle: Bundle,
    block: ClaimBlock,
    category: str,
    relation: str,
    subject_type: str,
    subject_name: str,
    object_type: Optional[str] = None,
    object_name: Optional[str] = None,
    extra_fields: Optional[Dict[str, object]] = None,
) -> Dict[str, object]:
    record = bundle.record
    claim_id_parts = [
        compiler.slugify(category),
        compiler.slugify(subject_name),
        compiler.slugify(relation),
        str(record.get("doc_id") or "unknown"),
        str(block.line_start),
    ]
    if object_name:
        claim_id_parts.insert(2, compiler.slugify(object_name))
    claim: Dict[str, object] = {
        "category": category,
        "claim_id": ":".join(claim_id_parts),
        "conditions": extract_conditions(block.text),
        "evidence": {
            "claim_text": block.text,
            "date_text": record.get("date_text"),
            "display_title": display_title_from_record(record),
            "doc_id": record.get("doc_id"),
            "line_end": block.line_end,
            "line_start": block.line_start,
            "page_hint": block.page_hint,
            "section": block.section,
            "title": record.get("title"),
        },
        "object": {"name": object_name, "type": object_type} if object_name and object_type else None,
        "program_family": infer_program_family(bundle, block, subject_type, subject_name, object_type=object_type, object_name=object_name),
        "relation": relation,
        "source_claim_types": block.claim_types,
        "source_kind": infer_source_kind(record),
        "subject": {"name": subject_name, "type": subject_type},
        "value_text": extract_value_text(block.text, relation),
    }
    if extra_fields:
        claim.update(extra_fields)
    return claim


def property_subjects(
    bundle: Bundle,
    block: ClaimBlock,
    section_context: Dict[str, Dict[str, Tuple[int, List[str]]]],
    global_context: Dict[str, Tuple[int, List[str]]],
) -> List[Tuple[str, str]]:
    explicit_salts = explicit_entity_names(bundle, block, "salt-system")
    explicit_materials = explicit_entity_names(bundle, block, "alloy-material")
    subjects: List[Tuple[str, str]] = [("salt-system", name) for name in explicit_salts]
    subjects.extend(("alloy-material", name) for name in explicit_materials)
    if subjects:
        return subjects[:6]
    salts = [name for name in resolve_entity_names(bundle, block, "salt-system", section_context, global_context) if is_specific_salt(name)]
    materials = [name for name in resolve_entity_names(bundle, block, "alloy-material", section_context, global_context) if is_specific_material(name)]
    if salts:
        subjects.extend(("salt-system", name) for name in salts[:2])
    if materials:
        subjects.extend(("alloy-material", name) for name in materials[:2])
    return subjects[:4]


def compatibility_outcome(text: str) -> str:
    low = text.lower()
    favorable_terms = (
        "did not show intergranular cracking",
        "not attacked",
        "absence of grain boundary cracks",
        "reduced the cracking",
        "reduced embrittlement",
        "resist",
        "compatible",
        "used to contain",
        "complete absence of grain boundary cracks",
    )
    adverse_terms = (
        "embrittlement",
        "grain boundary",
        "intergranular",
        "crack",
        "attack",
        "corrosion",
        "penetration",
        "weight increase",
    )
    if any(term in low for term in favorable_terms):
        return "favorable"
    if any(term in low for term in adverse_terms):
        return "adverse"
    return "mixed"


def extract_property_claims(
    bundle: Bundle,
    block: ClaimBlock,
    section_context: Dict[str, Dict[str, Tuple[int, List[str]]]],
    global_context: Dict[str, Tuple[int, List[str]]],
) -> List[Dict[str, object]]:
    if is_reference_like_section(block.section):
        return []
    combined = f"{block.section} {block.text}"
    relations = detect_relations(combined, PROPERTY_RULES)
    if not relations or not has_numeric_signal(block.text):
        return []
    if any(term in combined.lower() for term in ("error analysis", "accuracy", "accuracies", "standard error", "in error")):
        return []
    subjects = property_subjects(bundle, block, section_context, global_context)
    if not subjects:
        return []
    claims: List[Dict[str, object]] = []
    for relation in relations:
        for subject_type, subject_name in subjects:
            claims.append(make_claim(bundle, block, "thermophysical-properties", relation, subject_type, subject_name))
    return claims


def extract_compatibility_claims(
    bundle: Bundle,
    block: ClaimBlock,
    section_context: Dict[str, Dict[str, Tuple[int, List[str]]]],
    global_context: Dict[str, Tuple[int, List[str]]],
) -> List[Dict[str, object]]:
    if is_reference_like_section(block.section):
        return []
    combined = f"{block.section} {block.text}"
    relation = detect_first_relation(combined, COMPATIBILITY_RULES)
    if not relation:
        return []
    materials = [
        name for name in (explicit_entity_names(bundle, block, "alloy-material") or resolve_entity_names(bundle, block, "alloy-material", section_context, global_context))
        if is_specific_material(name) or name == "graphite"
    ]
    salts = [
        name for name in (explicit_entity_names(bundle, block, "salt-system") or resolve_entity_names(bundle, block, "salt-system", section_context, global_context))
        if is_specific_salt(name)
    ]
    if not materials or not salts:
        return []
    claims: List[Dict[str, object]] = []
    for material_name in materials[:4]:
        for salt_name in salts[:3]:
            claims.append(
                make_claim(
                    bundle,
                    block,
                    "salt-material-compatibility",
                    relation,
                    "alloy-material",
                    material_name,
                    object_type="salt-system",
                    object_name=salt_name,
                    extra_fields={"outcome": compatibility_outcome(block.text)},
                )
            )
    return claims


def extract_physics_claims(
    bundle: Bundle,
    block: ClaimBlock,
    section_context: Dict[str, Dict[str, Tuple[int, List[str]]]],
    global_context: Dict[str, Tuple[int, List[str]]],
) -> List[Dict[str, object]]:
    if is_reference_like_section(block.section):
        return []
    combined = f"{bundle.record.get('title') or ''} {block.section} {block.text}"
    relations = detect_relations(combined, PHYSICS_RULES)
    if not relations:
        return []
    if not has_target_reactor_context(bundle, block, section_context, global_context):
        return []
    subject = resolve_reactor_subject(bundle, block, section_context, global_context)
    if subject is None:
        return []
    if not has_numeric_signal(block.text) and all(relation not in {"criticality", "xenon-poisoning-effect"} for relation in relations):
        return []
    claims: List[Dict[str, object]] = []
    for relation in relations:
        claims.append(make_claim(bundle, block, "msr-reactor-physics", relation, subject[0], subject[1]))
    return claims


def extract_dynamics_claims(
    bundle: Bundle,
    block: ClaimBlock,
    section_context: Dict[str, Dict[str, Tuple[int, List[str]]]],
    global_context: Dict[str, Tuple[int, List[str]]],
    physics_relations: Sequence[str],
) -> List[Dict[str, object]]:
    if is_reference_like_section(block.section):
        return []
    combined = f"{bundle.record.get('title') or ''} {block.section} {block.text}"
    relations = detect_relations(combined, DYNAMICS_RULES)
    if not relations:
        return []
    if not has_target_reactor_context(bundle, block, section_context, global_context):
        return []
    if physics_relations and not any(relation in {"transient-response", "frequency-response", "stability", "transport-delay", "control-system", "mixing-recirculation"} for relation in relations):
        return []
    subject = resolve_reactor_subject(bundle, block, section_context, global_context)
    if subject is None:
        return []
    claims: List[Dict[str, object]] = []
    for relation in relations:
        claims.append(make_claim(bundle, block, "msr-system-dynamics", relation, subject[0], subject[1]))
    return claims


def dedupe_claims(claims: Sequence[Dict[str, object]]) -> List[Dict[str, object]]:
    deduped: Dict[str, Dict[str, object]] = {}
    for claim in claims:
        deduped[str(claim["claim_id"])] = claim
    return [deduped[key] for key in sorted(deduped.keys())]


def distill_claims(bundles: Sequence[Bundle]) -> Dict[str, List[Dict[str, object]]]:
    properties: List[Dict[str, object]] = []
    compatibility: List[Dict[str, object]] = []
    physics: List[Dict[str, object]] = []
    dynamics: List[Dict[str, object]] = []

    for bundle in bundles:
        section_context: Dict[str, Dict[str, Tuple[int, List[str]]]] = {}
        global_context: Dict[str, Tuple[int, List[str]]] = {}
        for block in bundle.claims:
            explicit_by_type = {
                entity_type: explicit_entity_names(bundle, block, entity_type)
                for entity_type in INTERESTING_ENTITY_TYPES
            }
            for entity_type, names in explicit_by_type.items():
                if not names:
                    continue
                section_context.setdefault(block.section, {})[entity_type] = (block.line_start, names)
                global_context[entity_type] = (block.line_start, names)

            property_claims = extract_property_claims(bundle, block, section_context, global_context)
            compatibility_claims = extract_compatibility_claims(bundle, block, section_context, global_context)
            physics_claims = extract_physics_claims(bundle, block, section_context, global_context)
            dynamics_claims = extract_dynamics_claims(
                bundle,
                block,
                section_context,
                global_context,
                [claim["relation"] for claim in physics_claims],
            )

            properties.extend(property_claims)
            compatibility.extend(compatibility_claims)
            physics.extend(physics_claims)
            dynamics.extend(dynamics_claims)

    return {
        "properties": dedupe_claims(properties),
        "compatibility": dedupe_claims(compatibility),
        "physics": dedupe_claims(physics),
        "dynamics": dedupe_claims(dynamics),
    }


def build_entity_catalog(claims: Sequence[Dict[str, object]], target_type: str) -> List[Dict[str, object]]:
    buckets: DefaultDict[str, Dict[str, object]] = collections.defaultdict(
        lambda: {
            "category_counts": collections.Counter(),
            "document_refs": {},
            "relation_counts": collections.Counter(),
            "roles": collections.Counter(),
        }
    )
    for claim in claims:
        for role in ("subject", "object"):
            entity = claim.get(role)
            if not isinstance(entity, dict) or entity.get("type") != target_type:
                continue
            name = str(entity.get("name") or "")
            if not name:
                continue
            bucket = buckets[name]
            bucket["category_counts"][str(claim.get("category") or "unknown")] += 1
            bucket["relation_counts"][str(claim.get("relation") or "unknown")] += 1
            bucket["roles"][role] += 1
            evidence = claim.get("evidence") if isinstance(claim.get("evidence"), dict) else {}
            doc_id = str(evidence.get("doc_id") or "")
            title = str(evidence.get("display_title") or evidence.get("title") or doc_id)
            if doc_id:
                bucket["document_refs"][doc_id] = title
    rows: List[Dict[str, object]] = []
    for name, bucket in buckets.items():
        rows.append(
            {
                "category_counts": dict(sorted(bucket["category_counts"].items())),
                "claim_count": int(sum(bucket["relation_counts"].values())),
                "document_count": len(bucket["document_refs"]),
                "documents": [
                    {"doc_id": doc_id, "title": bucket["document_refs"][doc_id]}
                    for doc_id in sorted(bucket["document_refs"].keys())
                ],
                "name": name,
                "relation_counts": dict(sorted(bucket["relation_counts"].items())),
                "roles": dict(sorted(bucket["roles"].items())),
            }
        )
    return sorted(rows, key=lambda row: (-int(row["claim_count"]), str(row["name"]).lower()))


def build_phenomena_catalog(claim_groups: Dict[str, Sequence[Dict[str, object]]]) -> List[Dict[str, object]]:
    buckets: DefaultDict[Tuple[str, str], Dict[str, object]] = collections.defaultdict(
        lambda: {"document_refs": {}, "subjects": collections.Counter()}
    )
    for key in ("compatibility", "physics", "dynamics"):
        for claim in claim_groups.get(key, []):
            relation = str(claim.get("relation") or "unknown")
            category = str(claim.get("category") or "unknown")
            bucket = buckets[(relation, category)]
            evidence = claim.get("evidence") if isinstance(claim.get("evidence"), dict) else {}
            doc_id = str(evidence.get("doc_id") or "")
            title = str(evidence.get("display_title") or evidence.get("title") or doc_id)
            if doc_id:
                bucket["document_refs"][doc_id] = title
            subject = claim.get("subject") if isinstance(claim.get("subject"), dict) else {}
            subject_name = str(subject.get("name") or "")
            if subject_name:
                bucket["subjects"][subject_name] += 1
    rows: List[Dict[str, object]] = []
    for (name, category), bucket in buckets.items():
        rows.append(
            {
                "category": category,
                "claim_count": int(sum(bucket["subjects"].values())),
                "document_count": len(bucket["document_refs"]),
                "documents": [
                    {"doc_id": doc_id, "title": bucket["document_refs"][doc_id]}
                    for doc_id in sorted(bucket["document_refs"].keys())
                ],
                "name": name,
                "top_subjects": [
                    {"count": count, "name": subject_name}
                    for subject_name, count in bucket["subjects"].most_common(8)
                ],
            }
        )
    return sorted(rows, key=lambda row: (-int(row["claim_count"]), str(row["name"]).lower()))


def normalize_conflict_value(value: str) -> str:
    return clean_ws(value).lower().strip(".;, ")


def build_conflict_report(claim_groups: Dict[str, Sequence[Dict[str, object]]]) -> Dict[str, object]:
    buckets: DefaultDict[Tuple[str, str, str, str], List[Dict[str, object]]] = collections.defaultdict(list)
    for key in ("properties", "physics", "dynamics"):
        for claim in claim_groups.get(key, []):
            value_text = str(claim.get("value_text") or "")
            if len(value_text) > 80 or not re.search(r"\d", value_text):
                continue
            subject = claim.get("subject") if isinstance(claim.get("subject"), dict) else {}
            obj = claim.get("object") if isinstance(claim.get("object"), dict) else {}
            bucket_key = (
                str(claim.get("category") or ""),
                str(subject.get("name") or ""),
                str(claim.get("relation") or ""),
                str(obj.get("name") or ""),
            )
            buckets[bucket_key].append(claim)
    groups: List[Dict[str, object]] = []
    for (category, subject_name, relation, object_name), items in buckets.items():
        distinct_values = collections.OrderedDict()
        distinct_docs = set()
        for claim in items:
            value_text = str(claim.get("value_text") or "")
            normalized = normalize_conflict_value(value_text)
            if normalized and normalized not in distinct_values:
                distinct_values[normalized] = value_text
            evidence = claim.get("evidence") if isinstance(claim.get("evidence"), dict) else {}
            doc_id = str(evidence.get("doc_id") or "")
            if doc_id:
                distinct_docs.add(doc_id)
        if len(distinct_values) < 2 or len(distinct_docs) < 2:
            continue
        groups.append(
            {
                "category": category,
                "documents": sorted(distinct_docs),
                "object": object_name or None,
                "relation": relation,
                "sample_claims": [
                    {
                        "doc_id": str((claim.get("evidence") or {}).get("doc_id") or ""),
                        "section": str((claim.get("evidence") or {}).get("section") or ""),
                        "value_text": str(claim.get("value_text") or ""),
                    }
                    for claim in items[:8]
                ],
                "subject": subject_name,
                "value_count": len(distinct_values),
                "values": list(distinct_values.values())[:12],
            }
        )
    groups.sort(key=lambda row: (-int(row["value_count"]), row["category"], row["subject"], row["relation"]))
    return {
        "candidate_conflict_count": len(groups),
        "generated_at": dt.datetime.utcnow().isoformat() + "Z",
        "groups": groups[:200],
    }


def group_claims_by_family(claim_groups: Dict[str, Sequence[Dict[str, object]]]) -> Dict[str, Dict[str, List[Dict[str, object]]]]:
    grouped: Dict[str, Dict[str, List[Dict[str, object]]]] = {
        family["id"]: {category: [] for category in claim_groups.keys()} for family in PROGRAM_FAMILY_DEFINITIONS
    }
    for category, claims in claim_groups.items():
        for claim in claims:
            family_id = str(claim.get("program_family") or "civilian-molten-salt-power-reactors")
            if family_id not in grouped:
                grouped[family_id] = {name: [] for name in claim_groups.keys()}
            grouped[family_id][category].append(claim)
    return grouped


def build_program_family_catalog(family_claim_groups: Dict[str, Dict[str, List[Dict[str, object]]]]) -> List[Dict[str, object]]:
    rows: List[Dict[str, object]] = []
    for family in PROGRAM_FAMILY_DEFINITIONS:
        family_id = family["id"]
        grouped = family_claim_groups.get(family_id, {})
        doc_counter: collections.Counter[str] = collections.Counter()
        doc_titles: Dict[str, str] = {}
        claim_counts = {category: len(grouped.get(category, [])) for category in grouped.keys()}
        for claims in grouped.values():
            for claim in claims:
                evidence = claim.get("evidence") if isinstance(claim.get("evidence"), dict) else {}
                doc_id = str(evidence.get("doc_id") or "")
                if not doc_id:
                    continue
                doc_counter[doc_id] += 1
                doc_titles[doc_id] = str(evidence.get("display_title") or evidence.get("title") or doc_id)
        rows.append(
            {
                "claim_counts": claim_counts,
                "claim_total": sum(claim_counts.values()),
                "description": family["description"],
                "document_count": len(doc_counter),
                "documents": [
                    {"claim_count": count, "doc_id": doc_id, "title": doc_titles.get(doc_id, doc_id)}
                    for doc_id, count in doc_counter.most_common(20)
                ],
                "guide": family["guide"],
                "id": family_id,
                "title": family["title"],
            }
        )
    return rows


def top_documents_from_claims(claims: Sequence[Dict[str, object]], limit: int = 12) -> List[Dict[str, object]]:
    doc_counter: collections.Counter[str] = collections.Counter()
    doc_titles: Dict[str, str] = {}
    for claim in claims:
        evidence = claim.get("evidence") if isinstance(claim.get("evidence"), dict) else {}
        doc_id = str(evidence.get("doc_id") or "")
        if not doc_id:
            continue
        doc_counter[doc_id] += 1
        doc_titles[doc_id] = str(evidence.get("display_title") or evidence.get("title") or doc_id)
    return [
        {"claim_count": count, "doc_id": doc_id, "title": doc_titles.get(doc_id, doc_id)}
        for doc_id, count in doc_counter.most_common(limit)
    ]


def representative_claims(claims: Sequence[Dict[str, object]], limit: int = 12) -> List[Dict[str, object]]:
    selected: List[Dict[str, object]] = []
    seen: set[Tuple[str, str]] = set()
    for claim in claims:
        evidence = claim.get("evidence") if isinstance(claim.get("evidence"), dict) else {}
        key = (str(claim.get("relation") or "unknown"), str(evidence.get("doc_id") or "unknown"))
        if key in seen:
            continue
        seen.add(key)
        selected.append(claim)
        if len(selected) >= limit:
            break
    return selected


def claim_matches_benchmark(claim: Dict[str, object], benchmark: Dict[str, object]) -> bool:
    subject = claim.get("subject") if isinstance(claim.get("subject"), dict) else {}
    if str(subject.get("name") or "") == str(benchmark["reactor"]):
        return True
    evidence = claim.get("evidence") if isinstance(claim.get("evidence"), dict) else {}
    combined = " ".join(
        part for part in (
            str(evidence.get("doc_id") or ""),
            str(evidence.get("title") or ""),
            str(evidence.get("display_title") or ""),
            str(evidence.get("section") or ""),
        )
        if part
    )
    reactor = str(benchmark["reactor"])
    if reactor and re.search(rf"\b{re.escape(reactor)}\b", combined):
        return True
    aliases = benchmark.get("aliases") if isinstance(benchmark.get("aliases"), tuple) else tuple(benchmark.get("aliases") or ())
    for alias in aliases:
        if not isinstance(alias, str):
            continue
        if alias == rf"\b{reactor}\b":
            continue
        if re.search(alias, combined, flags=re.IGNORECASE):
            return True
    return False


def build_benchmark_packs(claim_groups: Dict[str, Sequence[Dict[str, object]]]) -> List[Dict[str, object]]:
    rows: List[Dict[str, object]] = []
    for benchmark in BENCHMARK_DEFINITIONS:
        physics_claims = [claim for claim in claim_groups.get("physics", []) if claim_matches_benchmark(claim, benchmark)]
        dynamics_claims = [claim for claim in claim_groups.get("dynamics", []) if claim_matches_benchmark(claim, benchmark)]
        all_claims = physics_claims + dynamics_claims
        family_counts = collections.Counter(str(claim.get("program_family") or "unknown") for claim in all_claims)
        rows.append(
            {
                "document_count": len({str((claim.get("evidence") or {}).get("doc_id") or "") for claim in all_claims if str((claim.get("evidence") or {}).get("doc_id") or "")}),
                "dynamics_claim_count": len(dynamics_claims),
                "family_counts": dict(sorted(family_counts.items())),
                "guide": str(benchmark["guide"]),
                "id": str(benchmark["id"]),
                "physics_claim_count": len(physics_claims),
                "reactor": str(benchmark["reactor"]),
                "relation_counts": {
                    "dynamics": dict(sorted(collections.Counter(str(claim.get("relation") or "unknown") for claim in dynamics_claims).items())),
                    "physics": dict(sorted(collections.Counter(str(claim.get("relation") or "unknown") for claim in physics_claims).items())),
                },
                "sample_dynamics_claims": representative_claims(dynamics_claims, limit=10),
                "sample_physics_claims": representative_claims(physics_claims, limit=10),
                "title": str(benchmark["title"]),
                "top_documents": top_documents_from_claims(all_claims, limit=12),
            }
        )
    return rows


def build_compatibility_matrix(claims: Sequence[Dict[str, object]]) -> List[Dict[str, object]]:
    buckets: DefaultDict[Tuple[str, str], Dict[str, object]] = collections.defaultdict(
        lambda: {"documents": {}, "outcomes": collections.Counter(), "relations": collections.Counter(), "sample_values": []}
    )
    for claim in claims:
        subject = claim.get("subject") if isinstance(claim.get("subject"), dict) else {}
        obj = claim.get("object") if isinstance(claim.get("object"), dict) else {}
        material = str(subject.get("name") or "")
        salt = str(obj.get("name") or "")
        if not material or not salt:
            continue
        bucket = buckets[(material, salt)]
        bucket["outcomes"][str(claim.get("outcome") or "mixed")] += 1
        bucket["relations"][str(claim.get("relation") or "unknown")] += 1
        evidence = claim.get("evidence") if isinstance(claim.get("evidence"), dict) else {}
        doc_id = str(evidence.get("doc_id") or "")
        if doc_id:
            bucket["documents"][doc_id] = str(evidence.get("display_title") or evidence.get("title") or doc_id)
        value_text = str(claim.get("value_text") or "")
        if value_text and value_text not in bucket["sample_values"]:
            bucket["sample_values"].append(value_text)
    rows: List[Dict[str, object]] = []
    for (material, salt), bucket in buckets.items():
        rows.append(
            {
                "claim_count": int(sum(bucket["outcomes"].values())),
                "document_count": len(bucket["documents"]),
                "documents": [
                    {"doc_id": doc_id, "title": bucket["documents"][doc_id]}
                    for doc_id in sorted(bucket["documents"].keys())
                ],
                "material": material,
                "outcomes": dict(sorted(bucket["outcomes"].items())),
                "relations": dict(sorted(bucket["relations"].items())),
                "salt": salt,
                "sample_values": bucket["sample_values"][:5],
            }
        )
    return sorted(rows, key=lambda row: (-int(row["claim_count"]), -int(row["document_count"]), str(row["material"]).lower(), str(row["salt"]).lower()))


def build_salt_property_table(claims: Sequence[Dict[str, object]]) -> List[Dict[str, object]]:
    buckets: DefaultDict[Tuple[str, str], Dict[str, object]] = collections.defaultdict(
        lambda: {"claim_count": 0, "documents": {}, "sample_values": []}
    )
    for claim in claims:
        subject = claim.get("subject") if isinstance(claim.get("subject"), dict) else {}
        if subject.get("type") != "salt-system":
            continue
        salt = str(subject.get("name") or "")
        relation = str(claim.get("relation") or "unknown")
        if not salt:
            continue
        bucket = buckets[(salt, relation)]
        bucket["claim_count"] += 1
        evidence = claim.get("evidence") if isinstance(claim.get("evidence"), dict) else {}
        doc_id = str(evidence.get("doc_id") or "")
        if doc_id:
            bucket["documents"][doc_id] = str(evidence.get("display_title") or evidence.get("title") or doc_id)
        value_text = str(claim.get("value_text") or "")
        if value_text and value_text not in bucket["sample_values"]:
            bucket["sample_values"].append(value_text)
    rows: List[Dict[str, object]] = []
    for (salt, relation), bucket in buckets.items():
        rows.append(
            {
                "claim_count": int(bucket["claim_count"]),
                "document_count": len(bucket["documents"]),
                "documents": [
                    {"doc_id": doc_id, "title": bucket["documents"][doc_id]}
                    for doc_id in sorted(bucket["documents"].keys())
                ],
                "relation": relation,
                "salt": salt,
                "sample_values": bucket["sample_values"][:6],
            }
        )
    return sorted(rows, key=lambda row: (str(row["salt"]).lower(), str(row["relation"]).lower()))


def build_reactor_family_comparison(
    claim_groups: Dict[str, Sequence[Dict[str, object]]],
    coverage: Optional[Dict[str, object]] = None,
) -> Dict[str, object]:
    rows_by_subject: DefaultDict[Tuple[str, str], Dict[str, object]] = collections.defaultdict(
        lambda: {
            "document_ids": set(),
            "family_category_counts": collections.defaultdict(collections.Counter),
            "totals": collections.Counter(),
        }
    )
    for category in ("physics", "dynamics"):
        for claim in claim_groups.get(category, []):
            subject = claim.get("subject") if isinstance(claim.get("subject"), dict) else {}
            subject_type = str(subject.get("type") or "")
            subject_name = str(subject.get("name") or "")
            if subject_type not in {"reactor", "reactor-concept"} or not subject_name:
                continue
            family = str(claim.get("program_family") or "unknown")
            bucket = rows_by_subject[(subject_type, subject_name)]
            bucket["family_category_counts"][family][category] += 1
            bucket["totals"][category] += 1
            evidence = claim.get("evidence") if isinstance(claim.get("evidence"), dict) else {}
            doc_id = str(evidence.get("doc_id") or "")
            if doc_id:
                bucket["document_ids"].add(doc_id)
    rows: List[Dict[str, object]] = []
    for (subject_type, subject_name), bucket in rows_by_subject.items():
        family_counts = {
            family: {category: int(counter.get(category, 0)) for category in ("physics", "dynamics")}
            for family, counter in sorted(bucket["family_category_counts"].items())
        }
        rows.append(
            {
                "document_count": len(bucket["document_ids"]),
                "family_counts": family_counts,
                "subject_name": subject_name,
                "subject_type": subject_type,
                "totals": {category: int(bucket["totals"].get(category, 0)) for category in ("physics", "dynamics")},
            }
        )
    rows.sort(key=lambda row: (-sum(int(v) for v in row["totals"].values()), str(row["subject_name"]).lower()))
    return {
        "family_claim_counts": dict(coverage.get("family_claim_counts", {})) if isinstance(coverage, dict) else {},
        "rows": rows,
    }


def build_coverage_report(
    bundles: Sequence[Bundle],
    claim_groups: Dict[str, Sequence[Dict[str, object]]],
    catalogs: Dict[str, Sequence[Dict[str, object]]],
    guide_names: Sequence[str],
) -> Dict[str, object]:
    category_document_ids: Dict[str, set[str]] = {key: set() for key in claim_groups.keys()}
    relation_counts: Dict[str, Dict[str, int]] = {}
    top_documents: Dict[str, List[Dict[str, object]]] = {}
    for key, claims in claim_groups.items():
        rel_counter: collections.Counter[str] = collections.Counter()
        doc_counter: collections.Counter[str] = collections.Counter()
        doc_titles: Dict[str, str] = {}
        for claim in claims:
            rel_counter[str(claim.get("relation") or "unknown")] += 1
            evidence = claim.get("evidence") if isinstance(claim.get("evidence"), dict) else {}
            doc_id = str(evidence.get("doc_id") or "")
            if doc_id:
                category_document_ids[key].add(doc_id)
                doc_counter[doc_id] += 1
                doc_titles[doc_id] = str(evidence.get("display_title") or evidence.get("title") or doc_id)
        relation_counts[key] = dict(sorted(rel_counter.items()))
        top_documents[key] = [
            {"claim_count": count, "doc_id": doc_id, "title": doc_titles.get(doc_id, doc_id)}
            for doc_id, count in doc_counter.most_common(20)
        ]
    family_claim_groups = group_claims_by_family(claim_groups)
    family_claim_counts: Dict[str, Dict[str, int]] = {}
    family_document_counts: Dict[str, int] = {}
    family_top_documents: Dict[str, List[Dict[str, object]]] = {}
    for family_id, grouped in family_claim_groups.items():
        doc_counter: collections.Counter[str] = collections.Counter()
        doc_titles: Dict[str, str] = {}
        family_claim_counts[family_id] = {category: len(rows) for category, rows in grouped.items()}
        for rows in grouped.values():
            for claim in rows:
                evidence = claim.get("evidence") if isinstance(claim.get("evidence"), dict) else {}
                doc_id = str(evidence.get("doc_id") or "")
                if not doc_id:
                    continue
                doc_counter[doc_id] += 1
                doc_titles[doc_id] = str(evidence.get("display_title") or evidence.get("title") or doc_id)
        family_document_counts[family_id] = len(doc_counter)
        family_top_documents[family_id] = [
            {"claim_count": count, "doc_id": doc_id, "title": doc_titles.get(doc_id, doc_id)}
            for doc_id, count in doc_counter.most_common(12)
        ]
    return {
        "catalog_counts": {name: len(rows) for name, rows in catalogs.items()},
        "claim_counts": {name: len(rows) for name, rows in claim_groups.items()},
        "documents_scanned": len(bundles),
        "documents_with_source_claims": sum(1 for bundle in bundles if bundle.claims),
        "documents_with_distilled_claims": {name: len(doc_ids) for name, doc_ids in category_document_ids.items()},
        "family_claim_counts": family_claim_counts,
        "family_document_counts": family_document_counts,
        "family_top_documents": family_top_documents,
        "generated_at": dt.datetime.utcnow().isoformat() + "Z",
        "guide_count": len(guide_names),
        "guides": list(guide_names),
        "relation_counts": relation_counts,
        "top_documents": top_documents,
    }


def entity_link(name: str) -> str:
    return f"[[../entities/{compiler.slugify(name)}.md|{name}]]"


def doc_link(doc_id: str, title: str) -> str:
    return f"[[../documents/{doc_id}.md|{title}]]"


def relation_label(relation: str) -> str:
    return relation.replace("-", " ").title()


def render_claim_bullet(claim: Dict[str, object]) -> str:
    subject = claim.get("subject") if isinstance(claim.get("subject"), dict) else {}
    obj = claim.get("object") if isinstance(claim.get("object"), dict) else None
    evidence = claim.get("evidence") if isinstance(claim.get("evidence"), dict) else {}
    subject_text = entity_link(str(subject.get("name") or "unknown"))
    if isinstance(obj, dict) and obj.get("name"):
        subject_text += f" × {entity_link(str(obj.get('name')))}"
    value_text = truncate(str(claim.get("value_text") or ""), limit=150)
    link = doc_link(str(evidence.get("doc_id") or "unknown"), str(evidence.get("display_title") or evidence.get("title") or evidence.get("doc_id") or "unknown"))
    section = str(evidence.get("section") or "")
    lines = ""
    if evidence.get("line_start"):
        lines = f"lines {evidence.get('line_start')}-{evidence.get('line_end')}"
    detail = ", ".join(part for part in (section, lines) if part)
    suffix = f" ({detail})" if detail else ""
    return f"- {subject_text} — {value_text} — {link}{suffix}"


def render_reactor_physics_guide(claims: Sequence[Dict[str, object]], coverage: Dict[str, object]) -> str:
    relation_counts = coverage.get("relation_counts", {}).get("physics", {}) if isinstance(coverage.get("relation_counts"), dict) else {}
    by_relation: DefaultDict[str, List[Dict[str, object]]] = collections.defaultdict(list)
    for claim in claims:
        by_relation[str(claim.get("relation") or "unknown")].append(claim)
    lines = [
        "# Distilled Guide: MSR Reactor Physics",
        "",
        f"- Distilled claims: {len(claims)}",
        f"- Source documents: {coverage.get('documents_with_distilled_claims', {}).get('physics', 0)}",
        "- Scope: deterministic reactor-physics claims extracted from normalized document claims with explicit provenance.",
        "",
        "## Relations",
        "",
    ]
    for relation in sorted(by_relation.keys(), key=lambda name: (-len(by_relation[name]), name)):
        lines.append(f"### {relation_label(relation)}")
        lines.append("")
        for claim in by_relation[relation][:14]:
            lines.append(render_claim_bullet(claim))
        lines.append("")
    return "\n".join(lines)


def render_system_dynamics_guide(claims: Sequence[Dict[str, object]], coverage: Dict[str, object]) -> str:
    by_relation: DefaultDict[str, List[Dict[str, object]]] = collections.defaultdict(list)
    for claim in claims:
        by_relation[str(claim.get("relation") or "unknown")].append(claim)
    lines = [
        "# Distilled Guide: MSR System Dynamics",
        "",
        f"- Distilled claims: {len(claims)}",
        f"- Source documents: {coverage.get('documents_with_distilled_claims', {}).get('dynamics', 0)}",
        "- Scope: deterministic transient, stability, transport-delay, controller, and frequency-response claims with provenance.",
        "",
        "## Relations",
        "",
    ]
    for relation in sorted(by_relation.keys(), key=lambda name: (-len(by_relation[name]), name)):
        lines.append(f"### {relation_label(relation)}")
        lines.append("")
        for claim in by_relation[relation][:14]:
            lines.append(render_claim_bullet(claim))
        lines.append("")
    return "\n".join(lines)


def render_salt_guide(catalog: Sequence[Dict[str, object]], property_claims: Sequence[Dict[str, object]], compatibility_claims: Sequence[Dict[str, object]]) -> str:
    by_salt_property: DefaultDict[str, List[Dict[str, object]]] = collections.defaultdict(list)
    by_salt_compat: DefaultDict[str, List[Dict[str, object]]] = collections.defaultdict(list)
    for claim in property_claims:
        subject = claim.get("subject") if isinstance(claim.get("subject"), dict) else {}
        if subject.get("type") == "salt-system" and subject.get("name"):
            by_salt_property[str(subject.get("name"))].append(claim)
    for claim in compatibility_claims:
        obj = claim.get("object") if isinstance(claim.get("object"), dict) else {}
        if obj.get("type") == "salt-system" and obj.get("name"):
            by_salt_compat[str(obj.get("name"))].append(claim)
    lines = [
        "# Distilled Guide: Salt Systems",
        "",
        f"- Salt systems with distilled claims: {len(catalog)}",
        f"- Thermophysical-property claims: {len(property_claims)}",
        f"- Compatibility observations involving salts: {len(compatibility_claims)}",
        "- Scope: canonical salt-system subjects, example property claims, and compatibility observations with provenance.",
        "",
    ]
    ordered_catalog = sorted(catalog, key=lambda row: (0 if is_specific_salt(str(row.get("name") or "")) else 1, -int(row.get("claim_count", 0)), str(row.get("name") or "").lower()))
    for row in ordered_catalog[:18]:
        name = str(row.get("name") or "unknown")
        lines.append(f"## {entity_link(name)}")
        lines.append("")
        lines.append(f"- Distilled claims: {row.get('claim_count', 0)}")
        relations = row.get("relation_counts") if isinstance(row.get("relation_counts"), dict) else {}
        if relations:
            relation_text = ", ".join(f"{key}: {value}" for key, value in list(relations.items())[:8])
            lines.append(f"- Relations: {relation_text}")
        lines.append("")
        if by_salt_property.get(name):
            lines.append("### Example Property Claims")
            lines.append("")
            for claim in by_salt_property[name][:6]:
                lines.append(render_claim_bullet(claim))
            lines.append("")
        if by_salt_compat.get(name):
            lines.append("### Example Compatibility Observations")
            lines.append("")
            for claim in by_salt_compat[name][:4]:
                lines.append(render_claim_bullet(claim))
            lines.append("")
    return "\n".join(lines)


def render_materials_guide(catalog: Sequence[Dict[str, object]], property_claims: Sequence[Dict[str, object]], compatibility_claims: Sequence[Dict[str, object]]) -> str:
    by_material_property: DefaultDict[str, List[Dict[str, object]]] = collections.defaultdict(list)
    by_material_compat: DefaultDict[str, List[Dict[str, object]]] = collections.defaultdict(list)
    for claim in property_claims:
        subject = claim.get("subject") if isinstance(claim.get("subject"), dict) else {}
        if subject.get("type") == "alloy-material" and subject.get("name"):
            by_material_property[str(subject.get("name"))].append(claim)
    for claim in compatibility_claims:
        subject = claim.get("subject") if isinstance(claim.get("subject"), dict) else {}
        if subject.get("type") == "alloy-material" and subject.get("name"):
            by_material_compat[str(subject.get("name"))].append(claim)
    lines = [
        "# Distilled Guide: Materials and Compatibility",
        "",
        f"- Materials with distilled claims: {len(catalog)}",
        f"- Thermophysical-property claims for materials: {sum(1 for claim in property_claims if (claim.get('subject') or {}).get('type') == 'alloy-material')}",
        f"- Compatibility observations: {len(compatibility_claims)}",
        "- Scope: canonical materials, example property claims, and salt-exposure observations with provenance.",
        "",
    ]
    ordered_catalog = sorted(catalog, key=lambda row: (0 if is_specific_material(str(row.get("name") or "")) or str(row.get("name") or "") == "graphite" else 1, -int(row.get("claim_count", 0)), str(row.get("name") or "").lower()))
    for row in ordered_catalog[:18]:
        name = str(row.get("name") or "unknown")
        lines.append(f"## {entity_link(name)}")
        lines.append("")
        lines.append(f"- Distilled claims: {row.get('claim_count', 0)}")
        relations = row.get("relation_counts") if isinstance(row.get("relation_counts"), dict) else {}
        if relations:
            relation_text = ", ".join(f"{key}: {value}" for key, value in list(relations.items())[:8])
            lines.append(f"- Relations: {relation_text}")
        lines.append("")
        if by_material_property.get(name):
            lines.append("### Example Property Claims")
            lines.append("")
            for claim in by_material_property[name][:4]:
                lines.append(render_claim_bullet(claim))
            lines.append("")
        if by_material_compat.get(name):
            lines.append("### Example Compatibility Observations")
            lines.append("")
            for claim in by_material_compat[name][:6]:
                lines.append(render_claim_bullet(claim))
            lines.append("")
    return "\n".join(lines)


def render_guides_index(guide_names: Sequence[str]) -> str:
    lines = ["# Research Guides", "", "- Generated, provenance-backed distilled guides.", ""]
    guide_title_overrides = {
        "salt-systems.md": "Salt Systems",
        "materials-and-compatibility.md": "Materials and Compatibility",
        "reactor-physics.md": "Reactor Physics",
        "system-dynamics.md": "System Dynamics",
        "compatibility-matrix.md": "Compatibility Matrix",
        "property-tables.md": "Property Tables",
        "reactor-family-comparison.md": "Reactor and Family Comparison",
        **{family["guide"]: family["title"] for family in PROGRAM_FAMILY_DEFINITIONS},
        **{benchmark["guide"]: f"{benchmark['title']} Benchmark Pack" for benchmark in BENCHMARK_DEFINITIONS},
    }
    core_guides = [
        "salt-systems.md",
        "materials-and-compatibility.md",
        "reactor-physics.md",
        "system-dynamics.md",
        "compatibility-matrix.md",
        "property-tables.md",
        "reactor-family-comparison.md",
    ]
    family_guides = [family["guide"] for family in PROGRAM_FAMILY_DEFINITIONS]
    benchmark_guides = [benchmark["guide"] for benchmark in BENCHMARK_DEFINITIONS]
    lines.append("## Core Guides")
    lines.append("")
    for filename in core_guides:
        if filename not in guide_names:
            continue
        title = guide_title_overrides.get(filename, filename.replace(".md", "").replace("-", " ").title())
        lines.append(f"- [[{filename}|{title}]]")
    lines.append("")
    lines.append("## Program Families")
    lines.append("")
    for filename in family_guides:
        if filename not in guide_names:
            continue
        title = guide_title_overrides.get(filename, filename.replace(".md", "").replace("-", " ").title())
        lines.append(f"- [[{filename}|{title}]]")
    lines.append("")
    lines.append("## Benchmark Packs")
    lines.append("")
    for filename in benchmark_guides:
        if filename not in guide_names:
            continue
        title = guide_title_overrides.get(filename, filename.replace(".md", "").replace("-", " ").title())
        lines.append(f"- [[{filename}|{title}]]")
    lines.append("")
    return "\n".join(lines)


def render_program_family_guide(
    family: Dict[str, str],
    grouped_claims: Dict[str, List[Dict[str, object]]],
    coverage: Dict[str, object],
) -> str:
    family_id = family["id"]
    total_claims = sum(len(rows) for rows in grouped_claims.values())
    family_counts = coverage.get("family_claim_counts", {}).get(family_id, {}) if isinstance(coverage.get("family_claim_counts"), dict) else {}
    top_documents = coverage.get("family_top_documents", {}).get(family_id, []) if isinstance(coverage.get("family_top_documents"), dict) else []
    lines = [
        f"# Distilled Guide: {family['title']}",
        "",
        f"- Distilled claims: {total_claims}",
        f"- Source documents: {coverage.get('family_document_counts', {}).get(family_id, 0)}",
        f"- Scope: {family['description']}",
        "",
        "## Claim Counts by Category",
        "",
    ]
    for category in ("properties", "compatibility", "physics", "dynamics"):
        lines.append(f"- {category}: {family_counts.get(category, 0)}")
    lines.extend(["", "## Representative Source Documents", ""])
    for row in top_documents[:10]:
        lines.append(f"- {doc_link(str(row.get('doc_id') or 'unknown'), str(row.get('title') or row.get('doc_id') or 'unknown'))} (claims: {row.get('claim_count', 0)})")
    for heading, category in (
        ("Example Reactor Physics Claims", "physics"),
        ("Example System Dynamics Claims", "dynamics"),
        ("Example Compatibility Observations", "compatibility"),
        ("Example Property Claims", "properties"),
    ):
        rows = grouped_claims.get(category, [])
        if not rows:
            continue
        lines.extend(["", f"## {heading}", ""])
        for claim in rows[:12]:
            lines.append(render_claim_bullet(claim))
    lines.append("")
    return "\n".join(lines)


def render_benchmark_guide(benchmark: Dict[str, object], pack: Dict[str, object]) -> str:
    reactor = str(benchmark["reactor"])
    lines = [
        f"# Distilled Benchmark Pack: {benchmark['title']}",
        "",
        f"- Reactor: {entity_link(reactor)}",
        f"- Reactor-physics claims: {pack.get('physics_claim_count', 0)}",
        f"- System-dynamics claims: {pack.get('dynamics_claim_count', 0)}",
        f"- Source documents: {pack.get('document_count', 0)}",
        "- Scope: deterministic claims selected for this named historical reactor benchmark from the distilled physics and dynamics layers.",
        "",
        "## Relation Counts",
        "",
    ]
    relation_counts = pack.get("relation_counts", {}) if isinstance(pack.get("relation_counts"), dict) else {}
    for category in ("physics", "dynamics"):
        counts = relation_counts.get(category, {}) if isinstance(relation_counts.get(category), dict) else {}
        relation_text = ", ".join(f"{relation}: {count}" for relation, count in counts.items()) if counts else "none"
        lines.append(f"- {category}: {relation_text}")
    lines.extend(["", "## Representative Source Documents", ""])
    for row in pack.get("top_documents", [])[:10]:
        lines.append(f"- {doc_link(str(row.get('doc_id') or 'unknown'), str(row.get('title') or row.get('doc_id') or 'unknown'))} (claims: {row.get('claim_count', 0)})")
    sample_physics = pack.get("sample_physics_claims", []) if isinstance(pack.get("sample_physics_claims"), list) else []
    if sample_physics:
        lines.extend(["", "## Example Reactor Physics Claims", ""])
        for claim in sample_physics[:10]:
            lines.append(render_claim_bullet(claim))
    sample_dynamics = pack.get("sample_dynamics_claims", []) if isinstance(pack.get("sample_dynamics_claims"), list) else []
    if sample_dynamics:
        lines.extend(["", "## Example System Dynamics Claims", ""])
        for claim in sample_dynamics[:10]:
            lines.append(render_claim_bullet(claim))
    lines.append("")
    return "\n".join(lines)


def render_compatibility_matrix_guide(rows: Sequence[Dict[str, object]]) -> str:
    lines = [
        "# Distilled Guide: Compatibility Matrix",
        "",
        f"- Material × salt pairs: {len(rows)}",
        "- Scope: aggregated salt-material compatibility rows derived deterministically from compatibility claims.",
        "",
        "| Material | Salt | Claims | Docs | Outcomes |",
        "|---|---|---:|---:|---|",
    ]
    for row in rows[:30]:
        outcomes = row.get("outcomes", {}) if isinstance(row.get("outcomes"), dict) else {}
        outcome_text = ", ".join(f"{key}:{value}" for key, value in outcomes.items())
        lines.append(
            f"| {row.get('material')} | {row.get('salt')} | {row.get('claim_count', 0)} | {row.get('document_count', 0)} | {outcome_text} |"
        )
    lines.append("")
    return "\n".join(lines)


def render_property_tables_guide(rows: Sequence[Dict[str, object]]) -> str:
    grouped: DefaultDict[str, List[Dict[str, object]]] = collections.defaultdict(list)
    for row in rows:
        grouped[str(row.get("salt") or "unknown")].append(row)
    ordered_salts = sorted(
        grouped.keys(),
        key=lambda salt: (0 if is_specific_salt(salt) else 1, salt.lower()),
    )
    lines = [
        "# Distilled Guide: Property Tables",
        "",
        f"- Salt-property rows: {len(rows)}",
        "- Scope: aggregated salt-system property rows derived deterministically from distilled property claims.",
        "",
    ]
    for salt in ordered_salts[:18]:
        lines.append(f"## {entity_link(salt)}")
        lines.append("")
        for row in grouped[salt][:10]:
            sample_values = row.get("sample_values", []) if isinstance(row.get("sample_values"), list) else []
            value_text = "; ".join(sample_values[:3]) if sample_values else "no sampled value text"
            lines.append(f"- {relation_label(str(row.get('relation') or 'unknown'))}: {value_text} (claims: {row.get('claim_count', 0)}, docs: {row.get('document_count', 0)})")
        lines.append("")
    return "\n".join(lines)


def render_reactor_family_comparison_guide(matrix: Dict[str, object]) -> str:
    rows = matrix.get("rows", []) if isinstance(matrix.get("rows"), list) else []
    family_claim_counts = matrix.get("family_claim_counts", {}) if isinstance(matrix.get("family_claim_counts"), dict) else {}
    lines = [
        "# Distilled Guide: Reactor and Family Comparison",
        "",
        f"- Reactor/concept rows: {len(rows)}",
        "- Scope: reactor-subject comparison across ANP, civilian molten-salt power-reactor, and fast-spectrum/chloride families for physics and dynamics claims.",
        "",
        "## Family Totals",
        "",
    ]
    for family in PROGRAM_FAMILY_DEFINITIONS:
        counts = family_claim_counts.get(family["id"], {}) if isinstance(family_claim_counts.get(family["id"]), dict) else {}
        lines.append(f"- {family['title']}: physics {counts.get('physics', 0)}, dynamics {counts.get('dynamics', 0)}")
    lines.extend(["", "## Reactor Rows", "", "| Subject | Physics | Dynamics | Families | Docs |", "|---|---:|---:|---|---:|"])
    for row in rows[:20]:
        families = row.get("family_counts", {}) if isinstance(row.get("family_counts"), dict) else {}
        family_text = ", ".join(
            f"{PROGRAM_FAMILY_MAP.get(family_id, {'title': family_id})['title']}: {counts.get('physics', 0)}/{counts.get('dynamics', 0)}"
            for family_id, counts in families.items()
        )
        lines.append(
            f"| {row.get('subject_name')} | {row.get('totals', {}).get('physics', 0)} | {row.get('totals', {}).get('dynamics', 0)} | {family_text} | {row.get('document_count', 0)} |"
        )
    lines.append("")
    return "\n".join(lines)


def build_distilled_outputs(kb_root: Path) -> Dict[str, object]:
    bundles = load_bundles(kb_root)
    claim_groups = distill_claims(bundles)
    family_claim_groups = group_claims_by_family(claim_groups)
    benchmark_packs = build_benchmark_packs(claim_groups)

    all_claims = [claim for rows in claim_groups.values() for claim in rows]
    catalogs = {
        "salt_systems": build_entity_catalog(all_claims, "salt-system"),
        "materials": build_entity_catalog(all_claims, "alloy-material"),
        "reactors": build_entity_catalog(all_claims, "reactor"),
        "reactor_concepts": build_entity_catalog(all_claims, "reactor-concept"),
        "phenomena": build_phenomena_catalog(claim_groups),
        "program_families": build_program_family_catalog(family_claim_groups),
        "benchmark_packs": [
            {
                "document_count": row["document_count"],
                "dynamics_claim_count": row["dynamics_claim_count"],
                "guide": row["guide"],
                "id": row["id"],
                "physics_claim_count": row["physics_claim_count"],
                "reactor": row["reactor"],
                "title": row["title"],
            }
            for row in benchmark_packs
        ],
    }

    distilled_root = kb_root / "distilled"
    guides_root = kb_root / "wiki" / "research-guides"
    safe_rmtree(distilled_root)
    safe_rmtree(guides_root)

    write_json(distilled_root / "catalogs" / "categories.json", list(CATEGORY_DEFINITIONS))
    write_json(distilled_root / "catalogs" / "salt_systems.json", catalogs["salt_systems"])
    write_json(distilled_root / "catalogs" / "materials.json", catalogs["materials"])
    write_json(distilled_root / "catalogs" / "reactors.json", catalogs["reactors"])
    write_json(distilled_root / "catalogs" / "reactor_concepts.json", catalogs["reactor_concepts"])
    write_json(distilled_root / "catalogs" / "phenomena.json", catalogs["phenomena"])
    write_json(distilled_root / "catalogs" / "program_families.json", catalogs["program_families"])
    write_json(distilled_root / "catalogs" / "benchmark_packs.json", catalogs["benchmark_packs"])

    for row in benchmark_packs:
        write_json(distilled_root / "benchmarks" / f"{row['id']}.json", row)

    write_jsonl(distilled_root / "claims" / "properties.jsonl", claim_groups["properties"])
    write_jsonl(distilled_root / "claims" / "compatibility.jsonl", claim_groups["compatibility"])
    write_jsonl(distilled_root / "claims" / "physics.jsonl", claim_groups["physics"])
    write_jsonl(distilled_root / "claims" / "dynamics.jsonl", claim_groups["dynamics"])

    guide_names = [
        "index.md",
        "salt-systems.md",
        "materials-and-compatibility.md",
        "reactor-physics.md",
        "system-dynamics.md",
        "anp-and-precursor-fluid-fuel.md",
        "civilian-molten-salt-power-reactors.md",
        "fast-spectrum-and-chlorides.md",
        "compatibility-matrix.md",
        "property-tables.md",
        "reactor-family-comparison.md",
        "are-benchmark-pack.md",
        "msre-benchmark-pack.md",
        "msbr-benchmark-pack.md",
    ]

    coverage = build_coverage_report(bundles, claim_groups, catalogs, guide_names)
    conflicts = build_conflict_report(claim_groups)
    compatibility_matrix = build_compatibility_matrix(claim_groups["compatibility"])
    salt_property_table = build_salt_property_table(claim_groups["properties"])
    reactor_family_comparison = build_reactor_family_comparison(claim_groups, coverage)
    write_json(distilled_root / "reports" / "distilled_coverage.json", coverage)
    write_json(distilled_root / "reports" / "distilled_conflicts.json", conflicts)
    write_json(distilled_root / "matrices" / "compatibility_matrix.json", compatibility_matrix)
    write_json(distilled_root / "matrices" / "salt_property_table.json", salt_property_table)
    write_json(distilled_root / "matrices" / "reactor_family_comparison.json", reactor_family_comparison)

    write_text(guides_root / "reactor-physics.md", render_reactor_physics_guide(claim_groups["physics"], coverage))
    write_text(guides_root / "system-dynamics.md", render_system_dynamics_guide(claim_groups["dynamics"], coverage))
    write_text(guides_root / "salt-systems.md", render_salt_guide(catalogs["salt_systems"], claim_groups["properties"], claim_groups["compatibility"]))
    write_text(guides_root / "materials-and-compatibility.md", render_materials_guide(catalogs["materials"], claim_groups["properties"], claim_groups["compatibility"]))
    write_text(guides_root / "compatibility-matrix.md", render_compatibility_matrix_guide(compatibility_matrix))
    write_text(guides_root / "property-tables.md", render_property_tables_guide(salt_property_table))
    write_text(guides_root / "reactor-family-comparison.md", render_reactor_family_comparison_guide(reactor_family_comparison))
    for family in PROGRAM_FAMILY_DEFINITIONS:
        write_text(
            guides_root / family["guide"],
            render_program_family_guide(family, family_claim_groups.get(family["id"], {}), coverage),
        )
    for benchmark in BENCHMARK_DEFINITIONS:
        row = next((entry for entry in benchmark_packs if entry["id"] == benchmark["id"]), None)
        if row is None:
            continue
        write_text(guides_root / str(benchmark["guide"]), render_benchmark_guide(benchmark, row))
    write_text(guides_root / "index.md", render_guides_index(guide_names[1:]))

    return {
        "catalog_count": len(catalogs),
        "claim_counts": {name: len(rows) for name, rows in claim_groups.items()},
        "documents_scanned": len(bundles),
        "guide_count": len(guide_names),
        "guide_names": guide_names,
    }


def parse_args(argv: Optional[Sequence[str]] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build distilled research primitives from normalized KB outputs.")
    parser.add_argument("--kb-root", type=Path, default=Path("kb"), help="Knowledge-base root directory.")
    return parser.parse_args(argv)


def main(argv: Optional[Sequence[str]] = None) -> int:
    args = parse_args(argv)
    if not args.kb_root.exists() or not args.kb_root.is_dir():
        raise SystemExit(f"KB root does not exist or is not a directory: {args.kb_root}")
    summary = build_distilled_outputs(args.kb_root)
    counts = summary.get("claim_counts", {}) if isinstance(summary.get("claim_counts"), dict) else {}
    print(
        "done:"
        f" documents={summary.get('documents_scanned', 0)}"
        f" properties={counts.get('properties', 0)}"
        f" compatibility={counts.get('compatibility', 0)}"
        f" physics={counts.get('physics', 0)}"
        f" dynamics={counts.get('dynamics', 0)}"
        f" guides={summary.get('guide_count', 0)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
