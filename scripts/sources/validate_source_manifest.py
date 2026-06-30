#!/usr/bin/env python3
"""Validate SOURCE-MANIFEST.yaml counts match on-disk originals."""
from __future__ import annotations

import hashlib
import sys
from datetime import datetime, timezone
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parents[2]
MANIFEST = REPO / "00-source-materials" / "SOURCE-MANIFEST.yaml"
ORIGINALS = REPO / "00-source-materials" / "01-current-kutumba-originals"
EXPECTED_COUNT = 14


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> int:
    if not MANIFEST.exists():
        print("FAIL: SOURCE-MANIFEST.yaml missing")
        return 1

    data = yaml.safe_load(MANIFEST.read_text(encoding="utf-8"))
    entries = data.get("entries", [])
    failures = []

    declared = data.get("current_document_count")
    if declared != EXPECTED_COUNT:
        failures.append(f"current_document_count={declared}, expected {EXPECTED_COUNT}")
    if len(entries) != EXPECTED_COUNT:
        failures.append(f"entries list has {len(entries)}, expected {EXPECTED_COUNT}")

    ids = [e.get("source_id") for e in entries]
    if len(ids) != len(set(ids)):
        failures.append("duplicate source_id in manifest")

    on_disk = list(ORIGINALS.rglob("*"))
    files = [p for p in on_disk if p.is_file()]
    if len(files) != EXPECTED_COUNT:
        failures.append(f"on-disk originals={len(files)}, expected {EXPECTED_COUNT}")

    for e in entries:
        sid = e.get("source_id", "?")
        rel = e.get("repository_relative_path")
        if not rel:
            failures.append(f"{sid}: missing repository_relative_path")
            continue
        path = REPO / rel
        if not path.exists():
            failures.append(f"{sid}: file missing at {rel}")
            continue
        expected = e.get("dest_sha256") or e.get("sha256")
        if expected:
            actual = sha256_file(path)
            if actual != expected:
                failures.append(f"{sid}: hash mismatch")

    if failures:
        for f in failures:
            print(f"FAIL: {f}")
        return 1

    print(
        f"PASS: source manifest ({EXPECTED_COUNT} entries, "
        f"generated check {datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')})"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
