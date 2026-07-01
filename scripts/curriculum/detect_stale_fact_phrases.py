#!/usr/bin/env python3
"""Detect stale prohibited fact phrases in active files."""
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
SKIP = (
    "16-prompt-library",
    "99-archive",
    "build-evidence/",
    "canonical-facts/",
    "17-reviews-and-audits/V7-",
    "17-reviews-and-audits/V6-",
    "scripts/v7/",
)
SCAN_SUFFIXES = {".md", ".yaml", ".yml", ".mmd", ".svg", ".html", ".txt", ".csv", ".json", ".py"}

PHRASES = [
    ("Bhāgavata as the ripened fruit of Vedic knowledge", "V7-F001"),
    ("Kṛṣṇa's birth in Vṛndāvana", "V7-F004"),
    ("born in Vṛndāvana", "V7-F004"),
    ("Devotion fixed after taste develops", "V7-F002"),
]


def main() -> int:
    failures = []
    for p in REPO.rglob("*"):
        if not p.is_file() or p.suffix.lower() not in SCAN_SUFFIXES:
            continue
        if p.suffix.lower() == ".py":
            rel_parts = p.as_posix()
            if "scripts/curriculum" not in rel_parts and "scripts/v8" not in rel_parts:
                continue
        rel = p.as_posix()
        if p.name == "detect_stale_fact_phrases.py":
            continue
        if any(s in rel for s in SKIP):
            continue
        text = p.read_text(encoding="utf-8", errors="ignore")
        for phrase, fid in PHRASES:
            if phrase in text:
                failures.append(f"{rel}: stale phrase [{fid}] {phrase[:40]}...")
    if failures:
        for f in failures[:30]:
            sys.stdout.buffer.write(f"FAIL: {f}\n".encode("utf-8", errors="replace"))
        print(f"Total: {len(failures)}")
        return 1
    print("PASS: no stale fact phrases in active files")
    return 0


if __name__ == "__main__":
    sys.exit(main())
