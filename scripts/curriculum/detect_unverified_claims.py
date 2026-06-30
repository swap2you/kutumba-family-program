#!/usr/bin/env python3
"""Fail on scripture-text claims without valid source keys (C1 modules enforced)."""
from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parents[2]
WEEKLY = REPO / "11-weekly-program-library" / "first-six-months"

from module_utils import iter_modules  # noqa: E402


def load_matrix_keys(d: Path) -> set[str]:
    matrix = d / "research" / "SOURCE-MATRIX.md"
    if not matrix.exists():
        return set()
    return set(re.findall(r"\|\s*([A-Z0-9-]+)\s*\|", matrix.read_text(encoding="utf-8")))


def main() -> int:
    failures = []
    for d in iter_modules(WEEKLY):
        cr = d / "research" / "CLAIM-REGISTER.yaml"
        if not cr.exists():
            continue
        data = yaml.safe_load(cr.read_text(encoding="utf-8"))
        matrix_keys = load_matrix_keys(d)
        enforce_matrix = d.name.startswith("c1-w")
        for claim in data.get("claims", []):
            if claim.get("claim_type") != "scripture-text":
                continue
            keys = claim.get("primary_source_keys") or []
            if not keys:
                failures.append(f"{d.name}: {claim.get('claim_id')} scripture-text without source keys")
                continue
            if enforce_matrix:
                for k in keys:
                    if matrix_keys and k not in matrix_keys:
                        failures.append(f"{d.name}: {claim.get('claim_id')} key {k} not in SOURCE-MATRIX")
    if failures:
        for f in failures:
            sys.stdout.buffer.write((f"FAIL: {f}\n").encode("utf-8", errors="replace"))
        print("Result: structurally traceable — human doctrinal review required (FAILED structural gate)")
        return 1
    sys.stdout.buffer.write(
        b"PASS: scripture claims have source keys \xe2\x80\x94 structurally traceable; human doctrinal review required\n"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
