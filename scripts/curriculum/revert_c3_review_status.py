#!/usr/bin/env python3
"""Revert C3 modules to honest baseline-scaffold review-status."""

from __future__ import annotations

import re
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
WEEKLY = REPO / "11-weekly-program-library" / "first-six-months"

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


def main() -> None:
    for d in sorted(WEEKLY.iterdir()):
        if d.name.startswith("c3-w"):
            m = re.match(r"(c\d-w\d+)", d.name)
            code = m.group(1).upper().replace("c", "C").replace("-w", "-W") if m else d.name
            (d / "review-status.yaml").write_text(BASELINE.format(code=code), encoding="utf-8", newline="\n")
            print(f"reverted {code}")


if __name__ == "__main__":
    main()
