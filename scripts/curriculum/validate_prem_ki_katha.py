#!/usr/bin/env python3
"""Validate Prem-kī-Kathā structure and substance."""

from __future__ import annotations

import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
WEEKLY = REPO / "11-weekly-program-library" / "first-six-months"

REQUIRED_SECTIONS = [
    "katha title", "module connection", "primary source", "setting",
    "main personalities", "source-grounded narrative", "turning point",
    "central teaching", "heart reflection", "lāla", "kiśora", "parent bridge",
    "transition", "narration cautions", "visual", "rights", "human doctrinal",
]

MODERN_ONLY = [
    "a child finds an old family photo",
    "opening hook (modern scenario)",
]


def word_count(text: str) -> int:
    return len(re.findall(r"\b\w+\b", text))


def main() -> int:
    failures = []
    for d in sorted(WEEKLY.iterdir()):
        if not d.is_dir():
            continue
        prem = d / "prem-ki-katha.md"
        reg = d / "katha" / "KATHA-SOURCE-REGISTER.yaml"
        rs = d / "review-status.yaml"
        if not prem.exists():
            failures.append(f"{d.name}: missing prem-ki-katha.md")
            continue
        text = prem.read_text(encoding="utf-8").lower()
        body = re.sub(r"^---.*?---\s*", "", prem.read_text(encoding="utf-8"), count=1, flags=re.DOTALL)
        wc = word_count(body)
        rs = d / "review-status.yaml"
        pack = ""
        if rs.exists():
            for line in rs.read_text(encoding="utf-8").splitlines():
                if line.startswith("weekly_derivative_pack:"):
                    pack = line.split(":", 1)[1].strip()
        min_words = 600 if d.name == "c1-w2-i-am-not-this-body" else 350
        if wc < min_words:
            failures.append(f"{d.name}: prem-ki-katha too thin ({wc} words, need {min_words}+)")
        if any(m in text for m in MODERN_ONLY) and wc < 500:
            failures.append(f"{d.name}: prem-ki-katha appears to be modern hook only")
        if not reg.exists():
            failures.append(f"{d.name}: missing katha/KATHA-SOURCE-REGISTER.yaml")
        if "vedabase.io" not in text and "sb " not in text and "bhagavad" not in text:
            failures.append(f"{d.name}: no stable primary source link in prem-ki-katha")
        for sec in ["katha title", "module connection", "primary source", "source-grounded narrative", "parent bridge", "transition"]:
            if sec not in text:
                failures.append(f"{d.name}: missing section '{sec}' in prem-ki-katha")
        if rs.exists() and "approval_status: approved" in rs.read_text(encoding="utf-8"):
            failures.append(f"{d.name}: false approved status in review-status")

    pilot = WEEKLY / "c1-w2-i-am-not-this-body" / "prem-ki-katha.md"
    if pilot.exists() and word_count(re.sub(r"^---.*?---\s*", "", pilot.read_text(encoding="utf-8"), count=1, flags=re.DOTALL)) < 600:
        failures.append("C1-W2 pilot katha below minimum")

    if failures:
        for f in failures[:40]:
            print(f"FAIL: {f}")
        print(f"Total failures: {len(failures)}")
        return 1
    print(f"PASS: Prem-ki-Katha checks OK ({len(list(WEEKLY.iterdir()))} modules scanned)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
