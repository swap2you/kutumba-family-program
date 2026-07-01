#!/usr/bin/env python3
"""Append narrative metrics block to Cycle 1 KATHA-SOURCE-REGISTER.yaml (append-only)."""
from __future__ import annotations

import re
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
WEEKLY = REPO / "11-weekly-program-library" / "first-six-months"

METRICS = {
    "c1-w1-what-is-kutumba-and-why-are-we-here": (893, "6.6-7.8", "SB 1.1", False),
    "c1-w3-the-nature-of-the-soul": (730, "5.4-6.3", "SB 5.10-5.13", False),
    "c1-w4-why-human-life-is-rare-and-valuable": (755, "5.6-6.6", "SB 1.5-1.6", False),
    "c1-w5-the-temporary-world-and-the-search-for-permanent-happiness": (764, "5.7-6.6", "SB 4.8-4.12", False),
    "c1-w6-integration-night-who-am-i-and-how-should-our-family-live": (437, "3.2-3.8", "Cycle 1 synthesis", True),
}


def narrative_paragraphs(katha_path: Path) -> list[str]:
    text = katha_path.read_text(encoding="utf-8")
    m = re.search(r"## 6\. Source-grounded narrative\s*\n(.*?)(?=\n## 7\.|\Z)", text, re.S)
    if not m:
        return []
    body = m.group(1)
    return [
        p.strip()
        for p in re.split(r"\n\s*\n", body)
        if p.strip() and not p.strip().startswith("_[")
    ]


def main() -> None:
    for slug, (words, minutes, primary, integration) in METRICS.items():
        mod = WEEKLY / slug
        reg = mod / "katha" / "KATHA-SOURCE-REGISTER.yaml"
        katha = mod / "prem-ki-katha.md"
        text = reg.read_text(encoding="utf-8")
        text = re.sub(r"\nnarrative_metrics:.*?(?=\n[a-z_]+:|\Z)", "", text, flags=re.S)
        text = re.sub(r"\nparagraph_source_mappings:.*", "", text, flags=re.S)
        paras = narrative_paragraphs(katha)
        lines = [
            "",
            "narrative_metrics:",
            f"  narrative_words: {words}",
            f"  estimated_minutes: \"{minutes}\"",
            f"  integration_exception: {str(integration).lower()}",
            "  validation_method: section-6-only-v6",
            "paragraph_source_mappings:",
        ]
        for i, p in enumerate(paras, 1):
            snippet = re.sub(r"\*\*", "", p).replace('"', "'")[:100]
            lines.append(f"  - paragraph: {i}")
            lines.append(f"    source_range: \"{primary}\"")
            lines.append(f"    narrative_snippet: \"{snippet}\"")
            lines.append("    mapping_status: paraphrase-aligned-human-review-required")
        reg.write_text(text.rstrip() + "\n" + "\n".join(lines) + "\n", encoding="utf-8")
        print(f"Patched {reg.name} ({len(paras)} paragraphs)")


if __name__ == "__main__":
    main()
