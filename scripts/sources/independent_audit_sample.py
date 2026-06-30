#!/usr/bin/env python3
"""Independent sample metrics for audit — read-only."""
from __future__ import annotations

import re
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parents[2]
WEEKLY = REPO / "11-weekly-program-library/first-six-months"
SAMPLE_PREFIXES = [
    "c1-w1", "c1-w2", "c1-w3", "c2-w1", "c2-w3", "c2-w5",
    "c3-w1", "c3-w2", "c3-w3", "c3-w4", "c3-w6",
]


def word_count(path: Path) -> int:
    if not path.exists():
        return 0
    body = re.sub(r"^---.*?---\s*", "", path.read_text(encoding="utf-8"), count=1, flags=re.DOTALL)
    return len(re.findall(r"\b\w+\b", body))


def find_dir(prefix: str) -> Path | None:
    for d in WEEKLY.iterdir():
        if d.is_dir() and d.name.startswith(prefix):
            return d
    return None


def main() -> None:
    import sys
    def out(msg: str) -> None:
        sys.stdout.buffer.write((msg + "\n").encode("utf-8"))

    out("INDEPENDENT MODULE SAMPLE")
    out("-" * 72)
    for prefix in SAMPLE_PREFIXES:
        d = find_dir(prefix)
        if not d:
            out(f"{prefix}: MISSING")
            continue
        rs = yaml.safe_load((d / "review-status.yaml").read_text(encoding="utf-8"))
        prem_wc = word_count(d / "prem-ki-katha.md")
        newcom_lines = len((d / "newcomer-adaptation.md").read_text(encoding="utf-8").splitlines()) if (d / "newcomer-adaptation.md").exists() else 0
        brief = (d / "research/SOURCE-EXPANSION-BRIEF.md").exists()
        reg = (d / "katha/KATHA-SOURCE-REGISTER.yaml").exists()
        code = rs.get("week_code", "?")
        pack = rs.get("weekly_derivative_pack", "?")
        depth = rs.get("prem_katha_depth", "?")
        out(f"{code:6} prem_words={prem_wc:4} newcomer_lines={newcom_lines:3} pack={pack} depth={depth} brief={brief} reg={reg}")

    briefs = list(WEEKLY.glob("*/research/SOURCE-EXPANSION-BRIEF.md"))
    out(f"\nSOURCE-EXPANSION-BRIEF: {len(briefs)}/18")

    checks = [
        ("c1-w2", "BG 2.22", "c1-w2-i-am-not-this-body/katha/KATHA-SOURCE-REGISTER.yaml", None),
        ("c3-w1", "10.24", "c3-w1-who-is-god-the-supreme-enjoyer-proprietor-and-friend/katha/KATHA-SOURCE-REGISTER.yaml", "gopī"),
        ("c3-w2", "Mathurā", "c3-w2-who-is-kṛṣṇa-the-supreme-personality-of-godhead/katha/KATHA-SOURCE-REGISTER.yaml", "birth in Vṛndāvana"),
        ("c3-w3", "1.5", "c3-w3-guru-sādhu-and-śāstra-how-we-receive-spiritual-knowledge/katha/KATHA-SOURCE-REGISTER.yaml", "1.4.25"),
    ]
    out("\nKATHA REGISTER SPOT CHECKS")
    for mod, needle, rel, bad in checks:
        text = (REPO / "11-weekly-program-library/first-six-months" / rel).read_text(encoding="utf-8")
        ok = needle in text and (not bad or bad not in text)
        out(f"  {mod}: {needle} -> {'PASS' if ok else 'FAIL'}")


if __name__ == "__main__":
    main()
