#!/usr/bin/env python3
"""
Deterministic compiler for MinerU-converted MSR/scientific documents.

Input layout:
    pdf/<document_name>/

Output layout:
    kb/
      normalized/
      wiki/
      reports/
      manifests/
"""

from __future__ import annotations

import argparse
import collections
import dataclasses
import datetime as dt
import hashlib
import json
import re
import sys
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence, Tuple


DEFAULT_ENTITY_PATTERNS: Dict[str, Dict[str, Sequence[str]]] = {
    "reactor": {
        "ARE": [r"\bARE\b", r"aircraft reactor experiment"],
        "MSRE": [r"\bMSRE\b", r"molten[- ]salt reactor experiment"],
        "MSBR": [r"\bMSBR\b", r"molten[- ]salt breeder reactor"],
        "MSCR": [r"\bMSCR\b", r"molten[- ]salt converter reactor"],
        "DMSR": [r"\bDMSR\b", r"denatured molten[- ]salt reactor"],
        "HRE": [r"\bHRE(?:-1|-2)?\b", r"homogeneous reactor experiment"],
        "ART": [r"\bART\b", r"aircraft reactor test"],
        "LMFR": [r"\bLMFR\b", r"liquid[- ]metal fuel reactor"],
        "AHR": [r"\bAHR\b", r"aqueous homogeneous reactor"],
        # New reactor concept based on document analysis
        "MOSEL": [r"\bMOSEL\b", r"MOluten Salt ExperimentaL"],
        "MSBE": [r"\bMSBE\b", r"molten salt breeder experiment"],
        "MCFR": [r"\bMCFR(?:\((?:Th|Pu|U/Pu)\))?s?\b", r"molten[- ]chloride fast reactor"],
    },
    "reactor-concept": {
        "two-fluid breeder": [r"two[- ]fluid breeder", r"two[- ]region breeder"],
        "one-fluid breeder": [r"one[- ]fluid breeder"],
        "single-fluid breeder": [r"single[- ]fluid breeder"],
        "converter reactor": [r"converter reactor"],
        "aircraft propulsion reactor": [r"aircraft propulsion reactor", r"nuclear aircraft"],
        "fluid-fuel reactor": [r"fluid[- ]fuel reactor"],
        "BATR": [r"\bBATR\b", r"broad(?:[- ]application)? testing reactor"],
    },
    "salt-system": {
        "FLiBe": [r"\bFLiBe\b", r"\bLiF[- /]BeF2\b"],
        "FLiNaK": [
            r"\bFLiNaK\b",
            r"\bLiF[- /]NaF[- /]KF\b(?![- /](?:UF4|ThF4)\b)",
            r"\bNaF[- /]KF[- /]LiF\b(?![- /](?:UF4|ThF4)\b)",
            r"\bNaF[- /]LiF[- /]KF\b(?![- /](?:UF4|ThF4)\b)",
            r"\bLiF[- /]KF[- /]NaF\b(?![- /](?:UF4|ThF4)\b)",
        ],
        "LiF-BeF2-UF4": [r"\bLiF[- /]BeF2[- /]UF4\b"],
        "LiF-BeF2-ThF4": [r"\bLiF[- /]BeF2[- /]ThF4\b(?![- /]UF4\b)"],
        "LiF-BeF2-ThF4-UF4": [r"\bLiF[- /]BeF2[- /]ThF4[- /]UF4\b"],
        "LiF-BeF2-ZrF4-UF4": [r"\bLiF[- /]BeF2[- /]ZrF4[- /]UF4\b"],
        "LiF-NaF-ZrF4": [r"\bLiF[- /]NaF[- /]ZrF4\b(?![- /]UF4\b)", r"\bNaF[- /]LiF[- /]ZrF4\b(?![- /]UF4\b)"],
        "LiF-ThF4": [r"\bLiF[- /]ThF4\b"],
        "NaF-ZrF4": [r"\bNaF[- /]ZrF4\b(?![- /]UF[34]\b)"],
        "NaF-ZrF4-UF4": [r"\bNaF[- /]ZrF4[- /]UF4\b"],
        "NaBF4-NaF": [
            r"\bNaBF4[- /]NaF\b",
            r"\bsodium fluoroborate(?:[- ]sodium fluoride)?\b",
            r"\bfluoroborate(?:-type)?\b",
        ],
        "chloride salt": [r"chloride salt", r"molten chlorides?"],
        "fluoride salt": [r"fluoride salt", r"molten fluorides?"],
        "UF4": [r"\bUF4\b", r"uranium tetrafluoride"],
        "UF3": [r"\bUF3\b"],
        "ThF4": [r"\bThF4\b", r"thorium tetrafluoride"],
        "ZrF4": [r"\bZrF4\b", r"zirconium tetrafluoride"],
        "BeF2": [r"\bBeF2\b", r"beryllium fluoride"],
        "LiF": [r"\bLiF\b", r"lithium fluoride"],
        "NaF": [r"\bNaF\b", r"sodium fluoride"],
        "KF": [r"\bKF\b", r"potassium fluoride"],
        "RbF": [r"\bRbF\b", r"rubidium fluoride"],
    },
    "alloy-material": {
        "INOR-8": [r"\bINOR[- ]?8\b"],
        "Hastelloy N": [r"\bHastelloy[- ]?N\b"],
        "Hastelloy B": [r"\bHastelloy[- ]?B\b"],
        "Hastelloy W": [r"\bHastelloy[- ]?W\b"],
        "Hastelloy N-W": [r"\bHastelloy[- ]?N[- ]?W\b"],
        "Hastelloy C": [r"\bHastelloy[- ]?C\b"],
        "Hastelloy F": [r"\bHastelloy[- ]?F\b"],
        "Hastelloy X": [r"\bHastelloy[- ]?X\b"],
        "Inconel 600": [r"\bInconel[- ]?600\b"],
        "Inconel 601": [r"\bInconel[- ]?601\b"],
        "Inconel 625": [r"\bInconel[- ]?625\b"],
        "Inconel X": [r"\bInconel[- ]?X\b"],
        "INCO-61": [r"\bINCO[- ]?61\b"],
        "Incoloy 800": [r"\bIncoloy[- ]?800\b"],
        "Monel": [r"\bMonel\b"],
        "HC-2000": [r"\bHC[- ]?2000\b"],
        "titanium-modified Hastelloy-N": [r"(?:Ti|Titanium)[- ]modified\s+Hastelloy[- ]?N"],
        "nickel": [r"\bnickel\b"],
        "molybdenum": [r"\bmolybdenum\b"],
        "graphite": [r"\bgraphite\b"],
        "pyrolytic graphite": [r"pyrolytic graphite"],
        "beryllium": [r"\bberyllium\b"],
        "zirconium": [r"\bzirconium\b"],
        "niobium": [r"\bniobium\b"],
        "titanium": [r"\btitanium\b"],
        "stainless steel 304": [r"stainless steel 304", r"\b304L?\b"],
        "stainless steel 316": [r"stainless steel 316", r"\b316L?\b"],
    },
    "component": {
        "pump": [r"\bpump\b", r"circulating pump"],
        "heat exchanger": [r"heat exchanger"],
        "freeze valve": [r"freeze valve"],
        "drain tank": [r"drain tank"],
        "off-gas system": [r"off[- ]gas"],
        "sampler": [r"\bsampler\b", r"sampling system"],
        "control rod": [r"control rod"],
        "graphite moderator": [r"graphite moderator"],
        "loop": [r"\bloop\b", r"test loop"],
        "steam generator": [r"steam generator"],
        # New components for salt handling
        "salt pump": [r"salt\s+pump", r"\bmelt\s+pump"],
        "sparger": [r"\bsparger\b"],
        "intermediate heat exchanger": [r"intermediate\s+heat\s+exchanger", r"IHX"],
    },
    "organization": {
        "ORNL": [r"\bORNL\b", r"oak ridge national laboratory"],
        "AEC": [r"\bAEC\b", r"atomic energy commission", r"usaec", r"u\.?\s*s\.?\s*atomic energy commission"],
        "Union Carbide": [r"union carbide", r"union carbide corporation"],
        "UCCND": [r"\bUCCND\b", r"union carbide corporation nuclear division"],
        "ANL": [r"\bANL\b", r"argonne national laboratory"],
        "Pratt and Whitney Aircraft": [r"pratt\s*&\s*whitney aircraft", r"pratt and whitney aircraft"],
        "General Electric": [r"general electric(?: company)?", r"\bGE[- ]ANP(?:D|P)?\b"],
        "US Air Force": [r"u\.?\s*s\.?\s*air force", r"air force"],
        "Oak Ridge School of Reactor Technology": [r"oak ridge school of reactor technology"],
        # New organizations based on document analysis
        "Foster Wheeler": [r"Foster[- ]+Wheeler(?:\s+Corporation)?", r"\bFWC\b"],
        "EIR": [r"Eld\.?\s*Institut\s*für\s+Reaktorforschung", r"\bEIR\b"],
        "Forschungszentrum Jülich": [r"Kernforschungsanlage\s+Jülich", r"Forschungszentrum\s+Jülich"],
        "University of California": [r"University\s+of\s+California", r"\bUC\s+Berkeley"],
        "Martin Marietta": [r"Martin[- ]Marietta(?:\s+Energy\s+Systems(?:,?\s*Inc\.?)?)?"],
        "Lockheed Martin": [r"Lockheed Martin Energy Research(?:\s+Corp\.?|\s+Corporation)?", r"Lockheed Martin Energy Systems(?:,?\s*Inc\.?)?"],
        # BNL removed - too many false positives with other BNL uses
    },
    "report-series": {
        "MSR Program Semiannual Progress Report": [r"molten[- ]salt reactor program semiannual progress report"],
        "MSR Program Quarterly Progress Report": [r"molten[- ]salt reactor program quarterly progress report"],
        "ANP Quarterly Progress Report": [r"aircraft nuclear propulsion project quarterly progress report"],
        "Fluid Fuel Reactors": [r"fluid fuel reactors?"],
        "Nuclear Science and Engineering": [r"nuclear science and engineering"],
        "Nuclear Applications and Technology": [r"nuclear applications and technology"],
        "ORNL Technical Memorandum": [r"technical memorandum"],
        "ORNL Central Files": [r"central files?"],
    },
}

DEFAULT_TOPIC_KEYWORDS: Dict[str, Sequence[str]] = {
    "program-history": [
        "semiannual progress report", "quarterly progress report", "development program", "status report", "history"
    ],
    "aircraft-nuclear-propulsion": [
        "aircraft nuclear propulsion", "anp", "aircraft reactor experiment", "aircraft reactor test", "nuclear aircraft"
    ],
    "aqueous-homogeneous-reactors": [
        "aqueous homogeneous reactor", "homogeneous reactor experiment", "uranyl sulfate", "water boiler"
    ],
    "reactor-operations": [
        "operation", "operating experience", "maintenance", "shutdown", "startup", "availability", "operating performance"
    ],
    "reactor-physics-neutronics": [
        "neutronic", "nuclear analysis", "cross section", "reactivity", "breeding ratio", "criticality", "flux", "buckling"
    ],
    "breeder-and-converter-design": [
        "breeder", "converter", "doubling time", "breeding blanket", "blanket salt", "core design", "two-fluid", "one-fluid", "single-fluid"
    ],
    "salt-chemistry-and-redox": [
        "salt chemistry", "redox", "fluoride chemistry", "oxidation", "reduction", "equilibrium", "solubility", "thermodynamic"
    ],
    "salt-systems-and-thermophysics": [
        "flibe", "flinak", "viscosity", "density", "liquidus", "melting point", "heat capacity", "thermal conductivity"
    ],
    "materials-and-corrosion": [
        "corrosion", "alloy", "metallurgy", "inor-8", "hastelloy", "mass transfer", "intergranular", "specimen", "compatibility"
    ],
    "graphite-and-moderator-behavior": [
        "graphite", "moderator", "dimensional change", "permeation", "xenon poisoning"
    ],
    "fuel-processing-and-reprocessing": [
        "fuel processing", "reprocessing", "fluorination", "reductive extraction", "protactinium", "separation"
    ],
    "off-gas-fission-products-and-tritium": [
        "off-gas", "fission product", "xenon", "krypton", "tritium", "noble gas", "charcoal bed"
    ],
    "instrumentation-and-controls": [
        "instrumentation", "control system", "control systems", "reactor control", "transmitter", "sensor", "probe", "thermocouple", "level measurement"
    ],
    "pumps-loops-and-heat-exchangers": [
        "pump", "loop", "circulator", "heat exchanger", "steam generator", "piping", "freeze valve", "drain tank"
    ],
    "irradiation-and-damage": [
        "irradiation", "radiation damage", "helium embrittlement", "specimen irradiation", "neutron damage"
    ],
    "safety-shielding-and-remote-maintenance": [
        "safety", "shielding", "remote maintenance", "containment", "hazard", "accident", "decontamination"
    ],
}

REPORT_ID_PATTERNS: Sequence[Tuple[str, re.Pattern[str]]] = (
    ("ornl_tm_modern", re.compile(r"\bORNL/TM-\d{4}/\d{1,5}\b", re.IGNORECASE)),
    ("ornl_tm_legacy", re.compile(r"\bORNL-TM-\d{1,5}[A-Z]?\b", re.IGNORECASE)),
    ("ornl_cf_legacy", re.compile(r"\bORNL-CF-\d{2}-\d{1,2}-\d{1,3}[A-Z]?\b", re.IGNORECASE)),
    ("ornl_numeric", re.compile(r"\bORNL-\d{3,5}[A-Z]?\b", re.IGNORECASE)),
    ("cf_numeric", re.compile(r"\bCF-\d{2}-\d{1,2}-\d{1,3}[A-Z]?\b", re.IGNORECASE)),
    ("anp_numeric", re.compile(r"\bANP-\d{2,5}[A-Z]?\b", re.IGNORECASE)),
    ("anl_numeric", re.compile(r"\bANL-\d{3,5}[A-Z]?\b", re.IGNORECASE)),
    ("y_numeric", re.compile(r"\bY-\d{3,5}[A-Z]?\b", re.IGNORECASE)),
    ("k_numeric", re.compile(r"\bK-\d{3,5}[A-Z]?\b", re.IGNORECASE)),
    # Phase 2: Additional series patterns
    ("eir_numeric", re.compile(r"\bEIR[- ]?\d{3,5}[A-Z]?\b", re.IGNORECASE)),
    ("eir_tm_numeric", re.compile(r"\bEIR[- ]?(?:TM|AN|AW)(?:[- ]?[A-Z]{1,3})?[- ]?\d{3,6}\b", re.IGNORECASE)),
    ("nas_ns_numeric", re.compile(r"\bNAS[- ]?NS[- ]?\d{4,5}\b", re.IGNORECASE)),
    ("nd_numeric", re.compile(r"\bND[- /]\d{2}[- /]\d{2}\b", re.IGNORECASE)),
)

REPORT_SERIES_HINTS: Sequence[Tuple[str, Sequence[str]]] = (
    ("msr-program-semiannual-progress-report", (r"molten[- ]salt reactor program semiannual progress report",)),
    ("msr-program-quarterly-progress-report", (r"molten[- ]salt reactor program quarterly progress report",)),
    ("anp-quarterly-progress-report", (r"aircraft nuclear propulsion project quarterly progress report",)),
    ("ornl-technical-memorandum", (r"\btechnical memorandum\b",)),
    ("ornl-central-files", (r"\bcentral files?\b",)),
    ("fluid-fuel-reactors", (r"fluid fuel reactors?",)),
    ("nuclear-science-and-engineering", (r"nuclear science and engineering",)),
    ("nuclear-applications-and-technology", (r"nuclear applications and technology",)),
    # Phase 2: New series based on document analysis
    ("eir-series", (
    r"(?:^|\s)eidg\.?\s*institut\s*f[üue]r\s*reakt erforschung",  # Exact spelling
    r"\beir[- ]?bericht\s*nr?\.?\s*\d+",  # EIR-Bericht format
    r"\beir[- ]?(\d{3,5}|(?:tm|an|aw)(?:[- ]?[a-z]{1,3})?[- ]?\d+)\b"  # EIR-XXX with variants
  )),
    ("nas-ns-series", (r"\bnational academy of sciences", r"\bnuclear science", r"\bnas[- ]?ns[- ]?\d+")),
    ("natural-language-summaries", (r"\bnew developments in materials", r"\bnew developments in technology", r"\bassessment of [A-Z][a-z]+")),
    ("ornl-review-series", (r"\b\vol\.?\s*\d+\s*,\s*no\.?\s*\d+", r"\bornl review")),
)

DOC_ID_REPORT_SERIES_PREFIXES: Sequence[Tuple[str, str]] = (
    ("ornl-tm-", "ornl-technical-memorandum"),
    ("ornl-cf-", "ornl-central-files"),
    ("cf-", "ornl-central-files"),
    ("nas-ns-", "nas-ns-series"),
    ("nat-", "natural-language-summaries"),
    ("nse-", "nuclear-science-and-engineering"),
    ("eir-", "eir-series"),
    ("ffr-", "fluid-fuel-reactors"),
    ("chapter-", "fluid-fuel-reactors"),
)

DOC_ID_REPORT_SERIES_EXACT: Dict[str, str] = {
    "fluid-fuel-reactors": "fluid-fuel-reactors",
    "molten-salt-reactors": "fluid-fuel-reactors",
    "part-iii": "fluid-fuel-reactors",
    "parti-index": "fluid-fuel-reactors",
}

SOURCE_NAME_REPORT_SERIES_PREFIXES: Sequence[Tuple[str, str]] = (
    ("nat_", "natural-language-summaries"),
    ("nat-", "natural-language-summaries"),
    ("eir-an-", "eir-series"),
    ("eir-aw-", "eir-series"),
    ("eir-tm-", "eir-series"),
    ("nse_", "nuclear-science-and-engineering"),
    ("nse-", "nuclear-science-and-engineering"),
)

DATE_PATTERNS = [
    re.compile(r"\b(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2},\s+\d{4}\b"),
    re.compile(r"\b(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{4}\b"),
    re.compile(r"\b\d{4}-\d{2}-\d{2}\b"),
    re.compile(r"\b19\d{2}\b"),
]

PAGE_MARKER_PATTERNS = [
    re.compile(r"\bpage\s+(\d{1,4})\b", re.IGNORECASE),
    re.compile(r"\bp\.?\s*(\d{1,4})\b", re.IGNORECASE),
]

TITLE_SKIP_PREFIXES = (
    "abstract", "contents", "table of contents", "foreword", "preface", "summary", "references", "distribution"
)

AUTHOR_STOPWORDS = {
    "oak ridge national laboratory",
    "atomic energy commission",
    "prepared by",
    "prepared for",
    "distribution",
    "contents",
    "abstract",
    "summary",
    "report",
    "division",
    "laboratory",
    "school of reactor technology",
}

TECHNICAL_UNITS_RE = re.compile(
    r"\b(?:deg\.?\s*C|C|K|psi|psia|psig|atm|MW|kW|W|BTU|Btu|A|V|mV|ppm|ppb|wt\.?%|mol\.?%|g/cm3|g/cc|cm/s|ft/s|cm|mm|in\.|mil|hr|hrs|hours?|days?|years?)\b",
    re.IGNORECASE,
)
FORMULA_TOKEN_RE = re.compile(r"\b(?:LiF|BeF2|NaF|KF|RbF|ZrF4|UF4|UF3|ThF4|PuF3|PuF4|MgF2|NaBF4)\b")
NUMERIC_RE = re.compile(r"\b\d+(?:\.\d+)?\b")


@dataclasses.dataclass
class Section:
    heading: str
    level: int
    start_line: int
    end_line: int
    anchor: str


@dataclasses.dataclass
class Claim:
    text: str
    line_start: int
    line_end: int
    section: str
    page_hint: Optional[int]
    claim_type: str


@dataclasses.dataclass
class DocumentRecord:
    doc_id: str
    source_dir: str
    markdown_path: str
    file_hash: str
    title: str
    report_number: Optional[str]
    report_numbers: List[str]
    report_series: Optional[str]
    date_text: Optional[str]
    authors: List[str]
    document_type: str
    section_count: int
    sections: List[Dict[str, object]]
    topics: List[str]
    entities: Dict[str, List[Dict[str, object]]]
    claims_path: str
    figures: List[str]
    tables: List[str]
    warnings: List[str]


def slugify(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    value = re.sub(r"-+", "-", value).strip("-")
    return value or "untitled"


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def write_json(path: Path, obj: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2, sort_keys=True), encoding="utf-8")


def load_override_json(path: Optional[Path]) -> Optional[Dict[str, object]]:
    if not path:
        return None
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def iter_document_dirs(root: Path) -> Iterable[Path]:
    for child in sorted(root.iterdir()):
        if child.is_dir():
            yield child


def find_primary_markdown(doc_dir: Path) -> Optional[Path]:
    preferred_names = ["document.md", "content.md", "output.md", f"{doc_dir.name}.md"]
    for name in preferred_names:
        candidate = doc_dir / name
        if candidate.exists():
            return candidate
    md_files = sorted(doc_dir.rglob("*.md"))
    if not md_files:
        return None
    return max(md_files, key=lambda p: p.stat().st_size)


def detect_assets(doc_dir: Path, kind: str) -> List[str]:
    root = doc_dir / kind
    if not root.exists():
        return []
    return sorted(str(p.relative_to(doc_dir)) for p in root.rglob("*") if p.is_file())


def normalize_text(text: str) -> str:
    replacements = {
        "\u2010": "-",
        "\u2011": "-",
        "\u2012": "-",
        "\u2013": "-",
        "\u2014": "-",
        "\u2212": "-",
        "\u00ad": "",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    text = re.sub(r"[ \t]+", " ", text)
    return text


def clean_line(line: str) -> str:
    line = re.sub(r"\s+", " ", line)
    return line.strip(" #\t\r\n")


def split_lines(text: str) -> List[str]:
    return text.splitlines()


def first_nonempty_lines(text: str, limit: int = 80) -> List[Tuple[int, str]]:
    lines = split_lines(text)
    out: List[Tuple[int, str]] = []
    for i, raw in enumerate(lines[:limit], start=1):
        line = clean_line(raw)
        if line:
            out.append((i, line))
    return out


def canonicalize_report_token(token: str) -> str:
    token = token.upper()
    token = token.replace(" ", "")
    token = token.replace("--", "-")
    token = token.replace("/ ", "/")
    token = token.replace(" /", "/")
    token = re.sub(r"\s*-\s*", "-", token)
    token = re.sub(r"-{2,}", "-", token)
    token = token.strip(".,;:")
    # Normalize leading zeros in numbers (e.g., ORNL-0528 -> ORNL-528)
    token = re.sub(r"-0+(\d+)", r"-\1", token)
    token = re.sub(r"^(ORNL|ANL|Y|K|CF|ANP|EIR|NAS|TID|WASH|UC)0+(\d+)", r"\1\2", token)
    return token


def extract_report_numbers(text: str) -> List[str]:
    normalized = normalize_text(text[:30000])
    search_text = re.sub(r"\b([A-Z]{1,8})\s*-\s*([A-Z]{1,8})\s*-\s*(\d)", r"\1-\2-\3", normalized)
    search_text = re.sub(r"\b([A-Z]{1,8})\s*-\s*(\d)", r"\1-\2", search_text)
    search_text = re.sub(r"\b([A-Z]{1,8})\s*/\s*([A-Z]{1,8})\s*-\s*(\d{4})\s*/\s*(\d{1,5})", r"\1/\2-\3/\4", search_text)

    found: List[Tuple[int, str]] = []
    for _, pattern in REPORT_ID_PATTERNS:
        for match in pattern.finditer(search_text):
            found.append((match.start(), canonicalize_report_token(match.group(0))))

    deduped: List[str] = []
    seen = set()
    for _, token in sorted(found, key=lambda item: item[0]):
        if token not in seen:
            seen.add(token)
            deduped.append(token)
    return deduped[:10]


def detect_date(text: str) -> Optional[str]:
    snippet = text[:12000]
    for pattern in DATE_PATTERNS:
        matches = pattern.findall(snippet)
        if matches:
            return matches[0]
    return None


def detect_title(text: str, fallback_name: str) -> str:
    for _, line in first_nonempty_lines(text, limit=60):
        low = line.lower()
        if any(low.startswith(prefix) for prefix in TITLE_SKIP_PREFIXES):
            continue
        if len(line) < 8 or len(line) > 220:
            continue
        if re.fullmatch(r"[A-Z0-9\- ,./()]+", line) or re.search(r"[a-z]", line):
            return re.sub(r"\s+", " ", line).strip()
    return fallback_name


def looks_like_person_name(line: str) -> bool:
    if not line or len(line) > 120:
        return False
    low = line.lower()
    if any(stop in low for stop in AUTHOR_STOPWORDS):
        return False
    if any(ch.isdigit() for ch in line):
        return False
    parts = [p for p in re.split(r"[,;]|\band\b", line) if p.strip()]
    if not parts:
        return False
    score = 0
    for part in parts:
        tokens = [t for t in part.strip().split() if t]
        if 1 <= len(tokens) <= 4 and sum(tok[:1].isupper() for tok in tokens) >= max(1, len(tokens) - 1):
            score += 1
    return score > 0


def detect_authors(text: str) -> List[str]:
    lines = first_nonempty_lines(text, limit=90)
    candidates: List[str] = []
    for _, line in lines[1:18]:
        if looks_like_person_name(line):
            candidates.append(line)
    authors: List[str] = []
    for line in candidates[:6]:
        parts = [clean_line(p) for p in re.split(r",|;|\band\b", line) if clean_line(p)]
        for part in parts:
            if looks_like_person_name(part) and part not in authors:
                authors.append(part)
    return authors[:16]


def detect_report_series_from_doc_id(doc_id: Optional[str]) -> Optional[str]:
    if not doc_id:
        return None
    doc_id_lower = doc_id.lower()
    if doc_id_lower in DOC_ID_REPORT_SERIES_EXACT:
        return DOC_ID_REPORT_SERIES_EXACT[doc_id_lower]
    for prefix, series in DOC_ID_REPORT_SERIES_PREFIXES:
        if doc_id_lower.startswith(prefix):
            return series
    return None


def detect_report_series_from_source_name(source_name: Optional[str]) -> Optional[str]:
    if not source_name:
        return None
    source_lower = source_name.lower()
    for prefix, series in SOURCE_NAME_REPORT_SERIES_PREFIXES:
        if source_lower.startswith(prefix):
            return series
    return None


def detect_report_series(text: str, report_numbers: Sequence[str], doc_id: Optional[str] = None, source_name: Optional[str] = None) -> Optional[str]:
    snippet = normalize_text(text[:12000]).lower()

    source_series = detect_report_series_from_source_name(source_name)
    if source_series:
        return source_series

    # Directory/doc_id is authoritative for report identity in this corpus.
    doc_id_series = detect_report_series_from_doc_id(doc_id)
    if doc_id_series:
        return doc_id_series
    
    # Exclude EIR series for documents with non-EIR report numbers (avoid false positives)
    has_eir_rn = any(rn.upper().startswith("EIR") for rn in report_numbers)
    has_non_eir_rn = any(rn.upper().startswith("ANL") or rn.upper().startswith("ORNL") or rn.upper().startswith("NAS") for rn in report_numbers)
    
    for series, patterns in REPORT_SERIES_HINTS:
        # Skip EIR series detection if document has non-EIR report number
        if series == "eir-series" and has_non_eir_rn:
            continue
        if any(re.search(pattern, snippet, flags=re.IGNORECASE) for pattern in patterns):
            return series
    
    # Fallback classification based on report number prefixes
    for rn in report_numbers:
        rn_upper = rn.upper()
        # EIR: Only match if specifically EIR prefix (not ANL which might have EIR-related text)
        if rn_upper.startswith("EIR-") or rn_upper.startswith("EIRTM"):
            if not rn_upper.startswith("ANL"):  # Exclude false positives
                return "eir-series"
        if rn_upper.startswith("ORNL-TM-") or rn_upper.startswith("ORNL/TM-") or rn_upper.startswith("ORNLTM"):
            return "ornl-technical-memorandum"
        if rn_upper.startswith("ORNL-CF-") or rn_upper.startswith("CF-") or rn_upper.startswith("ORNLCF"):
            return "ornl-central-files"
        if rn_upper.startswith("NAS-NS-") or rn_upper.startswith("NASNS"):
            return "nas-ns-series"
        if rn_upper.startswith("NAT-") or rn_upper.startswith("NAT "):
            return "natural-language-summaries"
        if rn_upper.startswith("NSE-") and ("nuclear science" in snippet.lower()):
            return "nuclear-science-and-engineering"
        if rn_upper.startswith("FLUID-FUEL"):
            return "fluid-fuel-reactors"
        if rn_upper.startswith("ORNL-REVIEW"):
            return "ornl-review-series"
    
    # Check for FFR chapters by text content (Phase 2 addition)
    snippet_lower = snippet.lower()
    if "fluid fuel reactors" in snippet_lower or "part i" in snippet_lower or "part ii" in snippet_lower:
        if "chapter" in snippet_lower or ("part" in snippet_lower and ("editor" in snippet_lower or "author" in snippet_lower)):
            return "fluid-fuel-reactors"
    
    return None


def detect_document_type(text: str, report_series: Optional[str]) -> str:
    head = text[:10000].lower()
    if report_series == "msr-program-semiannual-progress-report":
        return "semiannual-progress-report"
    if report_series in {"msr-program-quarterly-progress-report", "anp-quarterly-progress-report"}:
        return "quarterly-progress-report"
    if "monthly progress report" in head:
        return "monthly-progress-report"
    if "quarterly progress report" in head:
        return "quarterly-progress-report"
    if "semiannual progress report" in head:
        return "semiannual-progress-report"
    if "progress report" in head:
        return "progress-report"
    if report_series == "ornl-technical-memorandum" or "technical memorandum" in head:
        return "technical-memorandum"
    if "report" in head:
        return "report"
    if "paper" in head:
        return "paper"
    if "lecture" in head:
        return "lecture"
    return "document"


def section_anchor(heading: str) -> str:
    return slugify(heading)


def extract_sections(text: str) -> List[Section]:
    lines = split_lines(text)
    sections: List[Section] = []
    for idx, raw in enumerate(lines, start=1):
        line = raw.rstrip()
        md = re.match(r"^(#{1,6})\s+(.*?)\s*$", line)
        if md:
            heading = clean_line(md.group(2))
            sections.append(Section(heading=heading, level=len(md.group(1)), start_line=idx, end_line=idx, anchor=section_anchor(heading)))
            continue

        normalized = clean_line(line)
        if not normalized or len(normalized) > 120:
            continue
        if re.match(r"^(\d+(?:\.\d+){0,3}|[IVXLC]+)\.?\s+[A-Z][A-Z0-9\- ,()/]{3,}$", normalized):
            sections.append(Section(heading=normalized, level=2, start_line=idx, end_line=idx, anchor=section_anchor(normalized)))
            continue
        if normalized.isupper() and 4 <= len(normalized) <= 80 and len(normalized.split()) <= 12:
            sections.append(Section(heading=normalized.title(), level=2, start_line=idx, end_line=idx, anchor=section_anchor(normalized)))

    deduped: List[Section] = []
    seen = set()
    for sec in sections:
        key = (sec.start_line, sec.heading.lower())
        if key in seen:
            continue
        seen.add(key)
        deduped.append(sec)
    for i, sec in enumerate(deduped):
        next_start = deduped[i + 1].start_line if i + 1 < len(deduped) else len(lines) + 1
        sec.end_line = next_start - 1
    return deduped


def line_to_section_map(sections: Sequence[Section], total_lines: int) -> List[str]:
    current = "(front matter)"
    out = [current] * (total_lines + 1)
    section_iter = iter(sorted(sections, key=lambda s: s.start_line))
    next_section = next(section_iter, None)
    for line_no in range(1, total_lines + 1):
        while next_section and line_no >= next_section.start_line:
            current = next_section.heading
            next_section = next(section_iter, None)
        out[line_no] = current
    return out


def detect_page_hint(line: str) -> Optional[int]:
    for pattern in PAGE_MARKER_PATTERNS:
        m = pattern.search(line)
        if m:
            try:
                return int(m.group(1))
            except ValueError:
                return None
    return None


def sentence_split(text: str) -> List[str]:
    text = re.sub(r"\s+", " ", text.strip())
    if not text:
        return []
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+(?=[A-Z0-9(])", text) if s.strip()]


def extract_entities(text: str, entity_patterns: Dict[str, Dict[str, Sequence[str]]]) -> Dict[str, List[Dict[str, object]]]:
    lines = split_lines(text)
    result: Dict[str, List[Dict[str, object]]] = {}
    for entity_type, entities in entity_patterns.items():
        hits: List[Dict[str, object]] = []
        for canonical_name, patterns in sorted(entities.items()):
            line_hits: List[int] = []
            for i, raw in enumerate(lines, start=1):
                line = raw.strip()
                if not line:
                    continue
                for pattern in patterns:
                    if re.search(pattern, line, flags=re.IGNORECASE):
                        line_hits.append(i)
                        break
            if line_hits:
                hits.append({"name": canonical_name, "count": len(line_hits), "line_hits": line_hits[:50]})
        if hits:
            result[entity_type] = sorted(hits, key=lambda x: (-int(x["count"]), str(x["name"])))
    return result


def classify_topics(text: str, topic_keywords: Dict[str, Sequence[str]], sections: Sequence[Section], entities: Dict[str, List[Dict[str, object]]]) -> List[str]:
    corpus = normalize_text(text).lower()
    heading_text = " ".join(sec.heading.lower() for sec in sections)
    scores: Dict[str, int] = {}
    for topic, keywords in topic_keywords.items():
        score = 0
        for kw in keywords:
            kw_low = kw.lower()
            score += corpus.count(kw_low)
            score += 2 * heading_text.count(kw_low)
        if score > 0:
            scores[topic] = score

    reactor_names = {item["name"] for item in entities.get("reactor", [])}
    material_names = {item["name"] for item in entities.get("alloy-material", [])}
    salt_names = {item["name"] for item in entities.get("salt-system", [])}
    if reactor_names & {"ARE", "ART"}:
        scores["aircraft-nuclear-propulsion"] = scores.get("aircraft-nuclear-propulsion", 0) + 5
    if reactor_names & {"HRE"}:
        scores["aqueous-homogeneous-reactors"] = scores.get("aqueous-homogeneous-reactors", 0) + 5
    if reactor_names & {"MSBR", "MSCR", "DMSR"}:
        scores["breeder-and-converter-design"] = scores.get("breeder-and-converter-design", 0) + 4
    if material_names & {"INOR-8", "Hastelloy N", "graphite"}:
        scores["materials-and-corrosion"] = scores.get("materials-and-corrosion", 0) + 3
    if salt_names & {"FLiBe", "FLiNaK", "LiF-BeF2-UF4", "LiF-BeF2-ThF4-UF4", "NaBF4-NaF"}:
        scores["salt-systems-and-thermophysics"] = scores.get("salt-systems-and-thermophysics", 0) + 3

    ranked = sorted(scores.items(), key=lambda kv: (-kv[1], kv[0]))
    return [topic for topic, _ in ranked[:8]]


def infer_claim_type(sentence: str) -> str:
    low = sentence.lower()
    if "table" in low:
        return "table-reference"
    if "figure" in low:
        return "figure-reference"
    if "breeding ratio" in low or "reactivity" in low or "critical" in low:
        return "reactor-physics"
    if FORMULA_TOKEN_RE.search(sentence):
        return "salt-chemistry"
    if TECHNICAL_UNITS_RE.search(sentence):
        return "measurement"
    if any(token in low for token in ["conclusion", "conclude", "showed", "demonstrated", "observed"]):
        return "finding"
    return "technical-statement"


def extract_claims(text: str, sections: Sequence[Section]) -> List[Claim]:
    lines = split_lines(text)
    section_map = line_to_section_map(sections, len(lines))
    claims: List[Claim] = []
    for i, raw in enumerate(lines, start=1):
        line = clean_line(raw)
        if len(line) < 25 or not NUMERIC_RE.search(line):
            continue
        if not (TECHNICAL_UNITS_RE.search(line) or FORMULA_TOKEN_RE.search(line)):
            continue
        for sentence in sentence_split(line):
            if len(sentence) < 25 or not NUMERIC_RE.search(sentence):
                continue
            claims.append(Claim(text=sentence, line_start=i, line_end=i, section=section_map[i], page_hint=detect_page_hint(sentence), claim_type=infer_claim_type(sentence)))
    return claims[:800]


def summarize_document(text: str, title: str, topics: Sequence[str], max_sentences: int = 6) -> List[str]:
    lines = [clean_line(x) for x in split_lines(text[:20000]) if clean_line(x)]
    candidate_sentences: List[str] = []
    topic_tokens = [topic.replace("-", " ") for topic in topics]
    for line in lines:
        if len(line) < 40 or len(line) > 280:
            continue
        low = line.lower()
        if title.lower() in low:
            continue
        if any(tok in low for tok in ["abstract", "summary", "purpose", "objective", "scope", "report"]):
            candidate_sentences.append(line)
        elif any(topic in low for topic in topic_tokens):
            candidate_sentences.append(line)
        elif FORMULA_TOKEN_RE.search(line) and NUMERIC_RE.search(line):
            candidate_sentences.append(line)
        elif re.search(r"\b(is|are|was|were|describes?|reports?|presents?|summarizes?)\b", low):
            candidate_sentences.append(line)
    deduped: List[str] = []
    seen = set()
    for s in candidate_sentences:
        key = s.lower()
        if key in seen:
            continue
        seen.add(key)
        deduped.append(s)
        if len(deduped) >= max_sentences:
            break
    return deduped


def extract_doc_id(doc_dir: Path, title: str, report_number: Optional[str]) -> str:
    """
    Extract document ID, prioritizing directory name as the canonical source.
    
    Directory names (e.g., ORNL-1947, ORNL-TM-0728) are typically the correct report identifier.
    Extracted report numbers from text often cite OTHER documents (e.g., bibliographies)
    and should only be used as a fallback when the directory name is not report-like.
    """
    # Normalize directory name if it looks like a report number
    dir_name = doc_dir.name if doc_dir.name else ""
    # Check if directory name matches known report number patterns (including ORNL-TM-XXXX format)
    # Phase 2: Added NAS-NS, MUC-LAO, NAT, ND patterns
    if re.match(r"^(ORNL|ANL|Y|K|CF|ANP|EIR|NAS|TID|WASH|UC|NAT|MUC|NSE|ND|PNL|BMI|AEEW)(?:-[A-Z]+)?-?\d+", dir_name, re.IGNORECASE):
        # Normalize leading zeros in the directory name
        normalized_dir = re.sub(r"-0+(\d+)", r"-\1", dir_name)
        normalized_dir = re.sub(r"^(ORNL|ANL|Y|K|CF|ANP|EIR|NAS|TID|WASH|UC)0+(\d+)", r"\1\2", normalized_dir, flags=re.IGNORECASE)
        normalized_dir = re.sub(r"-(TM|CF|RF)-0+", r"-\1-", normalized_dir, flags=re.IGNORECASE)
        return slugify(normalized_dir)
    # Fall back to extracted report number
    if report_number:
        return slugify(report_number.replace("/", "-"))
    return slugify(title) if title else slugify(dir_name) if dir_name else "unknown"


<<<<<<< HEAD
def render_document_page(record: DocumentRecord, text: str) -> str:
    summary = summarize_document(text, record.title, record.topics)
=======
def repo_relative_link(path_str: Optional[str]) -> Optional[str]:
    if not path_str:
        return None
    path = Path(path_str)
    if path.is_absolute():
        return path.as_posix()
    return (Path("..") / Path("..") / path).as_posix()


def rewrite_ocr_asset_links(text: str, markdown_path: Optional[str]) -> str:
    if not text or not markdown_path:
        return text
    markdown_dir = Path(markdown_path).parent

    def _replace_markdown(match: re.Match[str]) -> str:
        asset_rel = match.group(1)
        asset_path = (Path("..") / Path("..") / markdown_dir / asset_rel).as_posix()
        return f"({asset_path})"

    def _replace_html(match: re.Match[str]) -> str:
        asset_rel = match.group(1)
        asset_path = (Path("..") / Path("..") / markdown_dir / asset_rel).as_posix()
        return f'src="{asset_path}"'

    text = re.sub(r"\((?:\./)?(images/[^)]+)\)", _replace_markdown, text)
    text = re.sub(r'src="(?:\./)?(images/[^"]+)"', _replace_html, text)
    return text


def render_document_page(record: DocumentRecord, text: str) -> str:
    summary = [rewrite_ocr_asset_links(item, record.markdown_path) for item in summarize_document(text, record.title, record.topics)]
>>>>>>> 69f00500a (Initial commit: MSR Knowledge Base pipeline)
    entity_lines: List[str] = []
    for entity_type, entries in sorted(record.entities.items()):
        entity_lines.append(f"### {entity_type.title()}")
        entity_lines.append("")
        for item in entries[:24]:
            entity_lines.append(f"- {item['name']} (mentions: {item['count']})")
        entity_lines.append("")

<<<<<<< HEAD
    section_lines = [f"- {sec['heading']} (lines {sec['start_line']}-{sec['end_line']})" for sec in record.sections[:100]]
    lines: List[str] = [
        f"# {record.title}",
=======
    section_lines = [
        f"- {rewrite_ocr_asset_links(sec['heading'], record.markdown_path)} (lines {sec['start_line']}-{sec['end_line']})"
        for sec in record.sections[:100]
    ]
    source_markdown_link = repo_relative_link(record.markdown_path)
    source_ocr_dir_link = repo_relative_link(str(Path(record.markdown_path).parent)) if record.markdown_path else None
    source_images_link = repo_relative_link(str(Path(record.markdown_path).parent / "images")) if record.markdown_path else None
    source_markdown_label = Path(record.markdown_path).name if record.markdown_path else "source.md"
    lines: List[str] = [
        f"# {rewrite_ocr_asset_links(record.title, record.markdown_path)}",
>>>>>>> 69f00500a (Initial commit: MSR Knowledge Base pipeline)
        "",
        "## Metadata",
        "",
        f"- Doc ID: `{record.doc_id}`",
        f"- Primary report number: {record.report_number or 'unknown'}",
        f"- All report numbers: {', '.join(record.report_numbers) if record.report_numbers else 'none detected'}",
        f"- Report series: {record.report_series or 'unknown'}",
        f"- Date: {record.date_text or 'unknown'}",
        f"- Authors: {', '.join(record.authors) if record.authors else 'unknown'}",
        f"- Document type: {record.document_type}",
<<<<<<< HEAD
        f"- Source markdown: `{record.markdown_path}`",
=======
        f"- Source markdown: [{source_markdown_label}]({source_markdown_link})" if source_markdown_link else "- Source markdown: unknown",
        f"- Source OCR folder: [hybrid_ocr/]({source_ocr_dir_link})" if source_ocr_dir_link else "- Source OCR folder: unknown",
        f"- Source images: [images/]({source_images_link})" if source_images_link else "- Source images: unknown",
>>>>>>> 69f00500a (Initial commit: MSR Knowledge Base pipeline)
        f"- SHA256: `{record.file_hash}`",
        "",
        "## Topics",
        "",
    ]
    if record.topics:
        for topic in record.topics:
            lines.append(f"- [[../topics/{topic}.md|{topic}]]")
    else:
        lines.append("- none detected")

    lines.extend(["", "## Summary", ""])
    if summary:
        for item in summary:
            lines.append(f"- {item}")
    else:
        lines.append("- No deterministic summary sentences found.")

    lines.extend(["", "## Sections", ""])
    if section_lines:
        lines.extend(section_lines)
    else:
        lines.append("- none detected")

    lines.extend(["", "## Entities", ""])
    if entity_lines:
        lines.extend(entity_lines)
    else:
        lines.append("- none detected")

<<<<<<< HEAD
    lines.extend(["", "## Assets", "", f"- Figures: {len(record.figures)}", f"- Tables: {len(record.tables)}", "", "## Warnings", ""])
=======
    lines.extend([
        "",
        "## Assets",
        "",
        f"- OCR fulltext: [{source_markdown_label}]({source_markdown_link})" if source_markdown_link else "- OCR fulltext: unknown",
        f"- OCR images directory: [images/]({source_images_link})" if source_images_link else "- OCR images directory: unknown",
        f"- Figures: {len(record.figures)}",
        f"- Tables: {len(record.tables)}",
        "",
        "## Warnings",
        "",
    ])
>>>>>>> 69f00500a (Initial commit: MSR Knowledge Base pipeline)
    if record.warnings:
        for warning in record.warnings:
            lines.append(f"- {warning}")
    else:
        lines.append("- none")
    lines.append("")
    return "\n".join(lines)


def render_entity_page(entity_name: str, entity_type: str, refs: Sequence[Dict[str, object]]) -> str:
    rows = []
    for ref in refs:
        rows.append(f"- [[../documents/{ref['doc_id']}.md|{ref['title']}]] - mentions: {ref['count']} - lines: {', '.join(map(str, ref['line_hits'][:8]))}")
    return "\n".join([f"# {entity_name}", "", f"- Type: {entity_type}", f"- Documents: {len(refs)}", "", "## Mentions", "", *rows, ""])


def render_topic_page(topic: str, refs: Sequence[Dict[str, object]]) -> str:
    refs = sorted(refs, key=lambda x: ((x.get("date_text") or ""), x["title"]))
    lines = []
    for ref in refs:
        line = f"- [[../documents/{ref['doc_id']}.md|{ref['title']}]]"
        if ref.get("date_text"):
            line += f" - {ref['date_text']}"
        if ref.get("report_number"):
            line += f" - {ref['report_number']}"
        lines.append(line)
    return "\n".join([f"# {topic}", "", f"- Documents: {len(refs)}", "", "## Source Documents", "", *lines, ""])


def render_documents_index(records: Sequence[DocumentRecord]) -> str:
    lines = ["# Documents", ""]
    for rec in sorted(records, key=lambda r: ((r.date_text or ""), r.title.lower())):
        line = f"- [[../documents/{rec.doc_id}.md|{rec.title}]]"
        if rec.date_text:
            line += f" - {rec.date_text}"
        if rec.report_number:
            line += f" - {rec.report_number}"
        if rec.report_series:
            line += f" - {rec.report_series}"
        lines.append(line)
    lines.append("")
    return "\n".join(lines)


def render_entities_index(entity_index: Dict[str, Dict[str, List[Dict[str, object]]]]) -> str:
    lines = ["# Entities", ""]
    for entity_type in sorted(entity_index):
        lines.append(f"## {entity_type.title()}")
        lines.append("")
        for entity_name in sorted(entity_index[entity_type]):
            slug = slugify(entity_name)
            count = len(entity_index[entity_type][entity_name])
            lines.append(f"- [[../entities/{slug}.md|{entity_name}]] - documents: {count}")
        lines.append("")
    return "\n".join(lines)


def render_topics_index(topic_index: Dict[str, List[Dict[str, object]]]) -> str:
    lines = ["# Topics", ""]
    for topic in sorted(topic_index):
        lines.append(f"- [[../topics/{topic}.md|{topic}]] - documents: {len(topic_index[topic])}")
    lines.append("")
    return "\n".join(lines)


def compile_document(doc_dir: Path, out_root: Path, entity_patterns: Dict[str, Dict[str, Sequence[str]]], topic_keywords: Dict[str, Sequence[str]]) -> Optional[DocumentRecord]:
    markdown_path = find_primary_markdown(doc_dir)
    if markdown_path is None:
        return None

    text = normalize_text(read_text(markdown_path))
    digest = sha256_bytes(text.encode("utf-8", errors="replace"))
    report_numbers = extract_report_numbers(text)
    report_number = report_numbers[0] if report_numbers else None
    title = detect_title(text, fallback_name=doc_dir.name)
    doc_id = extract_doc_id(doc_dir, title, report_number)
    authors = detect_authors(text)
    date_text = detect_date(text)
    report_series = detect_report_series(text, report_numbers, doc_id=doc_id, source_name=doc_dir.name)
    document_type = detect_document_type(text, report_series)
    sections = extract_sections(text)
    entities = extract_entities(text, entity_patterns)
    topics = classify_topics(text, topic_keywords, sections, entities)
    claims = extract_claims(text, sections)
    figures = detect_assets(doc_dir, "figures")
    tables = detect_assets(doc_dir, "tables")

    warnings: List[str] = []
    if title == doc_dir.name:
        warnings.append("title_fallback_used")
    if not authors:
        warnings.append("authors_not_detected")
    if not sections:
        warnings.append("no_sections_detected")
    if not topics:
        warnings.append("no_topics_detected")
    if not claims:
        warnings.append("no_claims_detected")
    if not report_numbers:
        warnings.append("report_number_not_detected")
    if not report_series:
        warnings.append("report_series_not_detected")

    claims_path = out_root / "normalized" / "claims" / f"{doc_id}.jsonl"
    claims_path.parent.mkdir(parents=True, exist_ok=True)
    with claims_path.open("w", encoding="utf-8") as f:
        for claim in claims:
            f.write(json.dumps({
                "text": claim.text,
                "line_start": claim.line_start,
                "line_end": claim.line_end,
                "section": claim.section,
                "page_hint": claim.page_hint,
                "claim_type": claim.claim_type,
            }, ensure_ascii=False, sort_keys=True) + "\n")

    record = DocumentRecord(
        doc_id=doc_id,
        source_dir=str(doc_dir),
        markdown_path=str(markdown_path),
        file_hash=digest,
        title=title,
        report_number=report_number,
        report_numbers=list(report_numbers),
        report_series=report_series,
        date_text=date_text,
        authors=authors,
        document_type=document_type,
        section_count=len(sections),
        sections=[dataclasses.asdict(s) for s in sections],
        topics=list(topics),
        entities=entities,
        claims_path=str(claims_path),
        figures=figures,
        tables=tables,
        warnings=warnings,
    )

    write_json(out_root / "normalized" / "docs" / f"{doc_id}.json", dataclasses.asdict(record))
    write_json(out_root / "normalized" / "entities" / f"{doc_id}.json", entities)
    write_text(out_root / "wiki" / "documents" / f"{doc_id}.md", render_document_page(record, text))
    return record


def build_aggregate_pages(records: Sequence[DocumentRecord], out_root: Path) -> None:
    entity_index: Dict[str, Dict[str, List[Dict[str, object]]]] = collections.defaultdict(lambda: collections.defaultdict(list))
    topic_index: Dict[str, List[Dict[str, object]]] = collections.defaultdict(list)
    for rec in records:
        ref_base = {
            "doc_id": rec.doc_id,
            "title": rec.title,
            "date_text": rec.date_text,
            "report_number": rec.report_number,
            "report_series": rec.report_series,
        }
        for topic in rec.topics:
            topic_index[topic].append(ref_base)
        for entity_type, entries in rec.entities.items():
            for item in entries:
                entity_index[entity_type][str(item["name"])].append({**ref_base, "count": int(item["count"]), "line_hits": list(item["line_hits"])})

    for entity_type, entities in entity_index.items():
        for entity_name, refs in entities.items():
            write_text(out_root / "wiki" / "entities" / f"{slugify(entity_name)}.md", render_entity_page(entity_name, entity_type, refs))
    for topic, refs in topic_index.items():
        write_text(out_root / "wiki" / "topics" / f"{topic}.md", render_topic_page(topic, refs))

    write_text(out_root / "wiki" / "indices" / "documents.md", render_documents_index(records))
    write_text(out_root / "wiki" / "indices" / "entities.md", render_entities_index(entity_index))
    write_text(out_root / "wiki" / "indices" / "topics.md", render_topics_index(topic_index))


def build_lint_report(records: Sequence[DocumentRecord], out_root: Path) -> None:
    issues = []
    seen_hashes: Dict[str, List[str]] = collections.defaultdict(list)
    seen_titles: Dict[str, List[str]] = collections.defaultdict(list)
    seen_report_numbers: Dict[str, List[str]] = collections.defaultdict(list)
    for rec in records:
        seen_hashes[rec.file_hash].append(rec.doc_id)
        seen_titles[rec.title.strip().lower()].append(rec.doc_id)
        if rec.report_number:
            seen_report_numbers[rec.report_number].append(rec.doc_id)
        if "title_fallback_used" in rec.warnings:
            issues.append({"severity": "warning", "doc_id": rec.doc_id, "issue": "title_fallback_used"})
        if "authors_not_detected" in rec.warnings:
            issues.append({"severity": "warning", "doc_id": rec.doc_id, "issue": "authors_not_detected"})
        if rec.section_count == 0:
            issues.append({"severity": "warning", "doc_id": rec.doc_id, "issue": "no_sections_detected"})
        if not rec.topics:
            issues.append({"severity": "warning", "doc_id": rec.doc_id, "issue": "no_topics_detected"})
        if not rec.report_number:
            issues.append({"severity": "warning", "doc_id": rec.doc_id, "issue": "report_number_not_detected"})
        if not rec.report_series:
            issues.append({"severity": "info", "doc_id": rec.doc_id, "issue": "report_series_not_detected"})

    for digest, doc_ids in seen_hashes.items():
        if len(doc_ids) > 1:
            issues.append({"severity": "info", "issue": "duplicate_content_hash", "file_hash": digest, "doc_ids": sorted(doc_ids)})
    for title, doc_ids in seen_titles.items():
        if len(doc_ids) > 1:
            issues.append({"severity": "info", "issue": "duplicate_title", "title": title, "doc_ids": sorted(doc_ids)})
    for report_number, doc_ids in seen_report_numbers.items():
        if len(doc_ids) > 1:
            issues.append({"severity": "info", "issue": "duplicate_report_number", "report_number": report_number, "doc_ids": sorted(doc_ids)})

    report = {
        "generated_at": dt.datetime.utcnow().isoformat() + "Z",
        "document_count": len(records),
        "issues": sorted(issues, key=lambda x: (x.get("doc_id", ""), x["issue"])),
    }
    write_json(out_root / "reports" / "lint.json", report)


def parse_args(argv: Optional[Sequence[str]] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Compile MinerU output into a deterministic knowledge base.")
    parser.add_argument("--input-root", type=Path, default=Path("pdf"), help="Root directory containing pdf/<document_name>/ folders.")
    parser.add_argument("--output-root", type=Path, default=Path("kb"), help="Output root directory.")
    parser.add_argument("--entity-patterns-json", type=Path, default=None, help="Optional JSON file overriding entity patterns.")
    parser.add_argument("--topic-keywords-json", type=Path, default=None, help="Optional JSON file overriding topic keywords.")
    return parser.parse_args(argv)


def main(argv: Optional[Sequence[str]] = None) -> int:
    args = parse_args(argv)
    if not args.input_root.exists() or not args.input_root.is_dir():
        print(f"Input root does not exist or is not a directory: {args.input_root}", file=sys.stderr)
        return 2

    entity_patterns = load_override_json(args.entity_patterns_json) or DEFAULT_ENTITY_PATTERNS
    topic_keywords = load_override_json(args.topic_keywords_json) or DEFAULT_TOPIC_KEYWORDS

    records: List[DocumentRecord] = []
    skipped: List[str] = []
    for doc_dir in iter_document_dirs(args.input_root):
        rec = compile_document(doc_dir, args.output_root, entity_patterns, topic_keywords)
        if rec is None:
            skipped.append(str(doc_dir))
            continue
        records.append(rec)
        print(f"compiled {rec.doc_id}: {rec.title}")

    build_aggregate_pages(records, args.output_root)
    build_lint_report(records, args.output_root)
    manifest = {
        "generated_at": dt.datetime.utcnow().isoformat() + "Z",
        "input_root": str(args.input_root),
        "output_root": str(args.output_root),
        "document_count": len(records),
        "skipped_dirs": skipped,
        "doc_ids": sorted(rec.doc_id for rec in records),
    }
    write_json(args.output_root / "manifests" / "build_manifest.json", manifest)
    print(f"done: compiled {len(records)} documents")
    if skipped:
        print(f"skipped {len(skipped)} directories with no markdown", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
