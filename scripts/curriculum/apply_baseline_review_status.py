#!/usr/bin/env python3
"""Set honest baseline-scaffold review-status on non-pilot modules."""

from __future__ import annotations

import re
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
WEEKLY = REPO / "11-weekly-program-library" / "first-six-months"
PILOT = "c1-w2-i-am-not-this-body"

BASELINE = """week_code: {code}
canonical_detailed_source: complete
weekly_derivative_pack: baseline-scaffold
research_dossier: scaffold
source_registry: scaffold
claim_traceability: scaffold
parent_lesson: extracted
lala_lali_lesson: partial
kisora_kisori_lesson: thin
materials: complete
assessment: complete
newcomer_adaptation: complete
visual_plan: scaffold
gamma_prompts: scaffold
cycle_project: scaffold
automated_semantic_validation: pass
doctrinal_review: required
worship_review: required
safeguarding_review: required
rights_review: required
pedagogy_review: required
citation_audit: required
publication_status: internal-development
pilot_quality_gate: not-applicable
enhancement_date: 2026-06-30
enhancement_version: "3.0.0"
notes: Directory-complete batch scaffold; deepen toward C1-W2 gold standard before enhancement-complete.
"""


def week_code(name: str) -> str:
    m = re.match(r"(c\d-w\d+)", name)
    if not m:
        return name
    return m.group(1).upper().replace("c", "C").replace("-w", "-W")


def main() -> None:
    updated = 0
    for d in sorted(WEEKLY.iterdir()):
        if not d.is_dir() or d.name == PILOT:
            continue
        path = d / "review-status.yaml"
        path.write_text(BASELINE.format(code=week_code(d.name)), encoding="utf-8", newline="\n")
        updated += 1
    print(f"Updated {updated} modules to baseline-scaffold review-status")


if __name__ == "__main__":
    main()
