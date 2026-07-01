#!/usr/bin/env python3
"""Validate priority module MEDIA-INDEX.yaml candidate records."""
from __future__ import annotations

import sys
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parents[2]
PRIORITY = [
    "c1-w1-what-is-kutumba-and-why-are-we-here",
    "c1-w2-i-am-not-this-body",
    "c1-w3-the-nature-of-the-soul",
    "c1-w4-why-human-life-is-rare-and-valuable",
    "c1-w5-the-temporary-world-and-the-search-for-permanent-happiness",
    "c1-w6-integration-night-who-am-i-and-how-should-our-family-live",
    "c3-w2-who-is-kṛṣṇa-the-supreme-personality-of-godhead",
]


def main() -> int:
    failures = []
    for slug in PRIORITY:
        idx = REPO / "11-weekly-program-library" / "first-six-months" / slug / "audio-video" / "MEDIA-INDEX.yaml"
        if not idx.exists():
            failures.append(f"{slug}: missing MEDIA-INDEX.yaml")
            continue
        data = yaml.safe_load(idx.read_text(encoding="utf-8"))
        candidates = data.get("candidates", data.get("media_candidates", data.get("media", [])))
        if not candidates:
            failures.append(f"{slug}: no media candidates")
            continue
        for c in candidates:
            if not c.get("rights_posture") and not c.get("rights_status"):
                failures.append(f"{slug}: candidate missing rights")
    if failures:
        for f in failures:
            print(f"FAIL: {f}")
        return 1
    print(f"PASS: media candidate records ({len(PRIORITY)} modules)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
