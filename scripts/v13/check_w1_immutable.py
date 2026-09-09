#!/usr/bin/env python3
"""Fail if any protected C1-W1 file hash diverges from the V13 immutable baseline."""
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
BASELINE = REPO / "build-evidence" / "V13-W1-IMMUTABLE-BASELINE.json"


def main() -> int:
    data = json.loads(BASELINE.read_text(encoding="utf-8"))
    mismatches = []
    missing = []
    checked = 0
    for item in data["files"]:
        path = REPO / item["path"]
        if item.get("missing"):
            continue
        if not path.is_file():
            missing.append(item["path"])
            continue
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        checked += 1
        if digest != item["sha256"]:
            mismatches.append(item["path"])
    print(f"W1 immutable checked={checked} mismatches={len(mismatches)} missing={len(missing)}")
    for path in missing:
        print(f"MISSING: {path}")
    for path in mismatches:
        print(f"MISMATCH: {path}")
    if missing or mismatches:
        return 1
    print("W1 IMMUTABLE PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
