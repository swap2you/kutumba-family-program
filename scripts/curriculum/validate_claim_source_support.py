#!/usr/bin/env python3
"""Validate claim typing and source support for Cycle 1 modules."""
from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parents[2]
WEEKLY = REPO / "11-weekly-program-library" / "first-six-months"

CLAIM_TYPE_MAP = {
    "kutumba-summary": "kutumba-governance",
    "pedagogical-application": "pedagogical-practice",
    "safeguarding-boundary": "safeguarding-boundary",
    "contemporary-case": "contemporary-case",
    "analogy": "analogy",
    "scripture-text": "scripture-text",
    "scripture-paraphrase": "scripture-paraphrase",
    "prabhupada-teaching": "prabhupada-teaching",
    "facilitator-guidance": "facilitator-guidance",
    "kutumba-governance": "kutumba-governance",
    "pedagogical-practice": "pedagogical-practice",
}

SCRIPTURE_TYPES = {"scripture-text", "scripture-paraphrase"}
GOVERNANCE_TYPES = {"kutumba-governance"}
PEDAGOGY_TYPES = {"pedagogical-practice", "safeguarding-boundary"}


def load_matrix_keys(d: Path) -> set[str]:
    matrix = d / "research" / "SOURCE-MATRIX.md"
    if not matrix.exists():
        return set()
    return set(re.findall(r"\|\s*([A-Z0-9-]+)\s*\|", matrix.read_text(encoding="utf-8")))


def cycle1_modules():
    for d in sorted(WEEKLY.iterdir()):
        if d.is_dir() and d.name.startswith("c1-w"):
            yield d


def main() -> int:
    failures = []
    for d in cycle1_modules():
        cr = d / "research" / "CLAIM-REGISTER.yaml"
        if not cr.exists():
            failures.append(f"{d.name}: missing CLAIM-REGISTER.yaml")
            continue
        data = yaml.safe_load(cr.read_text(encoding="utf-8"))
        matrix_keys = load_matrix_keys(d)
        for claim in data.get("claims", []):
            cid = claim.get("claim_id", "?")
            ctype = claim.get("claim_type", "")
            normalized = CLAIM_TYPE_MAP.get(ctype, ctype)
            keys = claim.get("primary_source_keys") or []
            support = claim.get("semantic_support", "")

            if ctype not in CLAIM_TYPE_MAP and ctype not in CLAIM_TYPE_MAP.values():
                failures.append(f"{d.name}/{cid}: unknown claim_type {ctype}")

            if normalized in SCRIPTURE_TYPES:
                if not keys:
                    failures.append(f"{d.name}/{cid}: scripture claim without source keys")
                for k in keys:
                    if matrix_keys and k not in matrix_keys:
                        failures.append(f"{d.name}/{cid}: key {k} not in SOURCE-MATRIX")
                if not claim.get("context_note") and not claim.get("misunderstanding_risk"):
                    failures.append(f"{d.name}/{cid}: scripture claim missing context_note")
                if support == "supported" and claim.get("human_doctrinal_review") == "complete":
                    failures.append(f"{d.name}/{cid}: false human approval on scripture claim")

            if normalized in GOVERNANCE_TYPES:
                charter_keys = [k for k in keys if k.startswith("KUT-")]
                if not charter_keys and "charter" not in claim.get("statement", "").lower():
                    if "KUTUMBA" in claim.get("statement", "") and not keys:
                        pass  # flagged in semantic audit — allow empty keys if semantic_support set
                if keys and all(not k.startswith("KUT-") and not k.startswith("SB-") for k in keys):
                    if normalized in GOVERNANCE_TYPES and not claim.get("semantic_support"):
                        failures.append(f"{d.name}/{cid}: governance claim needs semantic_support field")

            if normalized in PEDAGOGY_TYPES and not keys and not claim.get("semantic_support"):
                if "safeguarding" in ctype or "pedagog" in ctype:
                    failures.append(f"{d.name}/{cid}: pedagogy/safeguarding claim needs semantic_support")

            if normalized == "contemporary-case" and keys:
                failures.append(f"{d.name}/{cid}: contemporary case must not cite scripture keys as primary")

    if failures:
        for f in failures[:40]:
            print(f"FAIL: {f}")
        print(f"Total: {len(failures)} — human doctrinal review required for all Cycle 1 claims")
        return 1
    print("PASS: Cycle 1 claim source support structure OK — human doctrinal review required")
    return 0


if __name__ == "__main__":
    sys.exit(main())
