#!/usr/bin/env python3
"""Validate Prem-kī-Kathā structure and substance."""

from __future__ import annotations

import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
WEEKLY = REPO / "11-weekly-program-library" / "first-six-months"

from module_utils import iter_modules, module_count  # noqa: E402

INTEGRATION_SLUGS = {
    "c1-w6-integration-night-who-am-i-and-how-should-our-family-live",
    "c2-w6-integration-night-choice-consequence-and-the-modes",
    "c3-w6-bhakti-mela-kirtana-drama-and-family-presentation",
}

MODERN_ONLY = [
    "a child finds an old family photo",
    "opening hook (modern scenario)",
]


def word_count(text: str) -> int:
    return len(re.findall(r"\b\w+\b", text))


def min_words_for(d: Path, body: str) -> int:
    if "integration_exception:" in body[:400] or d.name in INTEGRATION_SLUGS:
        return 600
    if d.name == "c1-w2-i-am-not-this-body":
        return 900
    return 900


def main() -> int:
    failures = []
    for d in iter_modules(WEEKLY):
        prem = d / "prem-ki-katha.md"
        reg = d / "katha" / "KATHA-SOURCE-REGISTER.yaml"
        rs_path = d / "review-status.yaml"
        if not prem.exists():
            failures.append(f"{d.name}: missing prem-ki-katha.md")
            continue
        raw = prem.read_text(encoding="utf-8")
        text = raw.lower()
        body = re.sub(r"^---.*?---\s*", "", raw, count=1, flags=re.DOTALL)
        wc = word_count(body)
        min_w = min_words_for(d, raw)
        if wc < min_w:
            failures.append(f"{d.name}: prem-ki-katha too thin ({wc} words, need {min_w}+)")
        if any(m in text for m in MODERN_ONLY) and wc < 500:
            failures.append(f"{d.name}: prem-ki-katha appears to be modern hook only")
        if not reg.exists():
            failures.append(f"{d.name}: missing katha/KATHA-SOURCE-REGISTER.yaml")
        if "vedabase.io" not in text and "sb " not in text and "bhagavad" not in text:
            failures.append(f"{d.name}: no stable primary source link in prem-ki-katha")
        for sec in [
            "katha title", "module connection", "primary source", "source-grounded narrative",
            "parent bridge", "transition",
        ]:
            if sec not in text:
                failures.append(f"{d.name}: missing section '{sec}' in prem-ki-katha")
        if rs_path.exists() and "approval_status: approved" in rs_path.read_text(encoding="utf-8"):
            failures.append(f"{d.name}: false approved status in review-status")

    if failures:
        for f in failures[:40]:
            print(f"FAIL: {f}")
        print(f"Total failures: {len(failures)}")
        return 1
    print(f"PASS: Prem-ki-Katha checks OK ({module_count(WEEKLY)} modules scanned)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
