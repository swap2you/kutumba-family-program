#!/usr/bin/env python3
"""Verify V8 independent audit commit follows production commits."""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
AUDIT_MARKER = "V8-INDEPENDENT-REAL-VISUAL-CITATION-MEDIA-AUDIT.md"
LEDGER = REPO / "build-evidence" / "V8-AUDIT-COMMIT-ORDER.yaml"


def git(*args: str) -> str:
    return subprocess.run(["git", *args], cwd=REPO, capture_output=True, text=True).stdout.strip()


def main() -> int:
    if not LEDGER.exists():
        print("SKIP: V8-AUDIT-COMMIT-ORDER.yaml not yet recorded")
        return 0
    import yaml

    data = yaml.safe_load(LEDGER.read_text(encoding="utf-8"))
    prod_head = data.get("production_complete_head", "")
    audit_head = data.get("audit_commit_head", "")
    if not prod_head or not audit_head:
        print("FAIL: ledger missing heads")
        return 1
    if prod_head == audit_head:
        print("FAIL: audit commit must differ from production head")
        return 1
    merge_base = git("merge-base", prod_head, audit_head)
    if merge_base != prod_head:
        print(f"FAIL: audit {audit_head[:8]} not descended from production {prod_head[:8]}")
        return 1
    if AUDIT_MARKER not in git("show", "--name-only", audit_head):
        print("FAIL: audit commit missing audit report")
        return 1
    print("PASS: audit commit ordering")
    return 0


if __name__ == "__main__":
    sys.exit(main())
