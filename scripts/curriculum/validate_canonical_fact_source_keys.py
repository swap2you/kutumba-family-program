#!/usr/bin/env python3
"""Resolve canonical fact primary_source_keys to governed source-matrix IDs."""
from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parents[2]
REGISTRY = REPO / "14-research-source-register" / "canonical-facts" / "CANONICAL-FACT-REGISTRY.yaml"
WEEKLY = REPO / "11-weekly-program-library" / "first-six-months"

GOVERNED = {"KUT-CHARTER", "KUT-SRC-0001", "KUT-SRC-0013"}
KEY_RE = re.compile(r"\b(SB-\d+-\d+-\d+|BG-\d+-\d+|CC-[A-Z]+-\d+-\d+|KUT-[A-Z0-9-]+)\b")


def collect_matrix_keys() -> set[str]:
    keys = set(GOVERNED)
    for p in WEEKLY.rglob("SOURCE-MATRIX.md"):
        for line in p.read_text(encoding="utf-8", errors="ignore").splitlines():
            if line.startswith("|") and not line.startswith("| ---"):
                parts = [c.strip() for c in line.split("|")]
                if len(parts) > 2 and parts[1] and parts[1] != "Source key":
                    keys.add(parts[1])
    return keys


def main() -> int:
    governed = collect_matrix_keys()
    data = yaml.safe_load(REGISTRY.read_text(encoding="utf-8"))
    failures = []
    for fact in data.get("facts", []):
        fid = fact.get("fact_id", "?")
        for key in fact.get("primary_source_keys", []):
            if key in governed:
                continue
            if key.startswith("PSC-"):
                failures.append(f"{fid}: unresolved PSC key {key}")
                continue
            if key.startswith("SB-") and not re.match(r"SB-\d+-\d+-\d+", key):
                if key not in governed:
                    failures.append(f"{fid}: chapter-level key {key} not in matrix")
            elif key not in governed and not KEY_RE.fullmatch(key):
                failures.append(f"{fid}: unknown key {key}")
    if failures:
        for f in failures:
            print(f"FAIL: {f}")
        return 1
    print(f"PASS: canonical fact keys resolve ({len(data.get('facts', []))} facts)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
