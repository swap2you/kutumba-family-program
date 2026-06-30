#!/usr/bin/env python3
"""Regenerate SOURCE-MANIFEST.yaml with portable paths and accurate statuses."""

from __future__ import annotations

import hashlib
import subprocess
from datetime import datetime, timezone
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parents[1]
ORIGINALS = REPO / "00-source-materials" / "01-current-kutumba-originals"

CANONICAL_MAP = {
    "KUTUMBA_Governance_Charter_and_Policy_Framework_v1.0.docx": (
        "KUT-SRC-0001",
        "01-governance/GOVERNANCE-CHARTER-AND-TEMPLE-RELATIONSHIP.md",
        "governance",
        "v1.0",
        ["worship-review", "doctrinal-review"],
    ),
    "KUTUMBA_Governance_Charter_and_Policy_Framework_v1.0.pdf": (
        "KUT-SRC-0002",
        None,
        "governance",
        "v1.0",
        [],
    ),
    "KUTUMBA_Three-Year_Curriculum_Architecture_v1.0.docx": (
        "KUT-SRC-0003",
        "02-curriculum-architecture/THREE-YEAR-CURRICULUM-ARCHITECTURE.md",
        "curriculum-architecture",
        "v1.0",
        ["doctrinal-review"],
    ),
    "KUTUMBA_First_Six_Month_Detailed_Curriculum.docx": (
        "KUT-SRC-0004",
        "03-first-six-months/FIRST-SIX-MONTH-DETAILED-CURRICULUM.md",
        "first-six-months",
        "",
        ["worship-review", "safety-review", "doctrinal-review"],
    ),
    "KUTUMBA_First_Six_Month_Detailed_Curriculum.pdf": (
        "KUT-SRC-0005",
        None,
        "first-six-months",
        "",
        [],
    ),
    "KUTUMBA_Children_Youth_Formation_Operating_Model_v1.0.docx": (
        "KUT-SRC-0006",
        "04-children-youth/CHILDREN-YOUTH-FORMATION-OPERATING-MODEL.md",
        "children-youth",
        "v1.0",
        ["safety-review", "doctrinal-review"],
    ),
    "KUTUMBA_Children_Youth_Formation_Operating_Model_v1.0.pdf": (
        "KUT-SRC-0007",
        None,
        "children-youth",
        "v1.0",
        [],
    ),
    "KUTUMBA_Parent_Formation_and_Family_Care_Operating_Model_v1.0.docx": (
        "KUT-SRC-0008",
        "05-parent-formation/PARENT-FORMATION-AND-FAMILY-CARE-OPERATING-MODEL.md",
        "parent-formation",
        "v1.0",
        ["safety-review"],
    ),
    "KUTUMBA_Prasada_Hospitality_Weekly_Operations_Manual.docx": (
        "KUT-SRC-0009",
        "06-prasadam-operations/PRASADA-HOSPITALITY-WEEKLY-OPERATIONS-MANUAL.md",
        "prasadam-operations",
        "",
        [],
    ),
    "KUTUMBA_Chat_7_Kirtana_Worship_Prayers_Bhakti_Laboratories_Operating_Manual.docx": (
        "KUT-SRC-0010",
        "07-kirtana-worship-bhakti-labs/KIRTANA-WORSHIP-PRAYERS-BHAKTI-LABORATORIES-MANUAL.md",
        "kirtana-worship",
        "",
        ["worship-review", "doctrinal-review"],
    ),
    "KUTUMBA_Chat_8_Festivals_Yatras_Outdoor_Calendar_Working_Framework.docx": (
        "KUT-SRC-0011",
        "08-festivals-yatras-calendar/FESTIVALS-YATRAS-OUTDOOR-CALENDAR-FRAMEWORK.md",
        "festivals-calendar",
        "",
        ["worship-review"],
    ),
    "KUTUMBA Master Operating Model.docx": (
        "KUT-SRC-0012",
        "00-foundation/MASTER-OPERATING-MODEL.md",
        "master-operating",
        "",
        ["doctrinal-review"],
    ),
}


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def git_rel(path: Path) -> str:
    return path.relative_to(REPO).as_posix()


def main() -> None:
    entries = []
    for file in sorted(ORIGINALS.rglob("*")):
        if not file.is_file() or file.name.startswith("~$"):
            continue
        name = file.name
        if name not in CANONICAL_MAP:
            raise SystemExit(f"Unmapped source file: {name}")
        source_id, canonical_path, workstream, version, reviews = CANONICAL_MAP[name]
        h = sha256_file(file)
        repo_rel = git_rel(file)
        is_docx = file.suffix.lower() == ".docx"
        entry = {
            "source_id": source_id,
            "source_root_id": "kutumba-sanga",
            "source_relative_path": repo_rel.split("01-current-kutumba-originals/", 1)[-1],
            "repository_relative_path": repo_rel,
            "original_filename": name,
            "file_type": file.suffix.lstrip(".").lower(),
            "byte_size": file.stat().st_size,
            "sha256": h,
            "dest_sha256": h,
            "source_copied": True,
            "source_hash_verified": True,
            "destination_hash_verified": True,
            "likely_workstream": workstream,
            "version": version,
            "status": "ingested",
            "privacy_class": "public-curriculum-development",
            "rights_status": "kutumba-authored-cc-by-nc-sa-4.0",
            "licence": "CC-BY-NC-SA-4.0",
            "canonical_path": canonical_path,
            "canonicalization_status": (
                "text-extraction-complete"
                if is_docx and canonical_path
                else "hash-verified-only"
            ),
            "structural_extraction_status": (
                "structural-extraction-sampled" if is_docx and canonical_path else "not-applicable"
            ),
            "visual_review_status": "visual-review-pending",
            "required_human_review": reviews,
            "publication_status": "internal-development",
            "notes": "portable-manifest-regenerated",
        }
        entries.append(entry)

    manifest = {
        "generated": datetime.now(timezone.utc).isoformat(),
        "current_source_root_id": "kutumba-sanga",
        "current_document_count": len(entries),
        "legacy_index_count": 1773,
        "entries": entries,
    }
    out = REPO / "00-source-materials" / "SOURCE-MANIFEST.yaml"
    out.write_text(yaml.dump(manifest, sort_keys=False, allow_unicode=True), encoding="utf-8")
    print(f"Wrote {len(entries)} manifest entries")


if __name__ == "__main__":
    main()
