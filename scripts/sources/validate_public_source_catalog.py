#!/usr/bin/env python3
"""Validate public source catalog YAML structure."""

from __future__ import annotations

import sys
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parents[2]
CATALOG_DIR = REPO / "14-research-source-register/public-source-catalog"
REQUIRED_FILES = [
    "MASTER-SOURCE-CATALOG.yaml",
    "PRABHUPADA-PRIMARY-AND-ARCHIVAL.yaml",
    "PRABHUPADA-STRUCTURED-SECONDARY.yaml",
    "ISKCON-EDUCATION-AND-CONGREGATION.yaml",
    "SUPPLEMENTARY-GAUDIYA-SANATANA.yaml",
    "MEDIA-AND-YOUTUBE-DISCOVERY.yaml",
    "RIGHTS-AND-PERMISSIONS-REGISTER.yaml",
    "SOURCE-ALIAS-AND-MIRROR-MAP.yaml",
    "SOURCE-VERIFICATION-QUEUE.yaml",
]
REQUIRED_FIELDS = [
    "source_id",
    "exact_entry_url",
    "authority_tier",
    "rights_posture",
]


def main() -> int:
    failures = []
    for name in REQUIRED_FILES:
        path = CATALOG_DIR / name
        if not path.exists():
            failures.append(f"missing {name}")
            continue
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
        if not data:
            failures.append(f"empty {name}")
    master = yaml.safe_load((CATALOG_DIR / "MASTER-SOURCE-CATALOG.yaml").read_text(encoding="utf-8"))
    entries = master.get("entries", [])
    ids = set()
    for e in entries:
        for f in REQUIRED_FIELDS:
            if f not in e:
                failures.append(f"{e.get('source_id', '?')}: missing {f}")
        sid = e.get("source_id")
        if sid in ids:
            failures.append(f"duplicate source_id {sid}")
        ids.add(sid)
        if "utm_source=chatgpt" in e.get("exact_entry_url", ""):
            failures.append(f"{sid}: tracking query string present")
    if failures:
        for f in failures[:30]:
            print(f"FAIL: {f}")
        return 1
    print(f"PASS: public source catalog ({len(entries)} entries)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
