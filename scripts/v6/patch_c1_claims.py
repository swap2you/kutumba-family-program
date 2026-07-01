#!/usr/bin/env python3
"""Add semantic_support fields to Cycle 1 claim registers."""
from __future__ import annotations

from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parents[2]
WEEKLY = REPO / "11-weekly-program-library" / "first-six-months"

DEFAULTS = {
    "kutumba-summary": "policy-derived",
    "kutumba-governance": "policy-derived",
    "scripture-text": "partially-supported",
    "scripture-paraphrase": "partially-supported",
    "pedagogical-application": "pedagogical-inference",
    "pedagogical-practice": "pedagogical-inference",
    "safeguarding-boundary": "policy-derived",
    "contemporary-case": "kutumba-created",
    "analogy": "kutumba-created",
}


def patch_claim(claim: dict) -> dict:
    ctype = claim.get("claim_type", "")
    if "semantic_support" not in claim:
        claim["semantic_support"] = DEFAULTS.get(ctype, "human doctrinal review required")
    if ctype in ("kutumba-summary",) and "KUTUMBA" in claim.get("statement", ""):
        claim["claim_type"] = "kutumba-governance"
        claim["semantic_support"] = "policy-derived"
        if not claim.get("primary_source_keys"):
            claim["primary_source_keys"] = ["KUT-CHARTER"]
    if ctype == "pedagogical-application":
        claim["claim_type"] = "pedagogical-practice"
    if ctype == "contemporary-case" and claim.get("primary_source_keys"):
        claim["primary_source_keys"] = []
    if ctype == "scripture-text" and not claim.get("context_note"):
        claim["context_note"] = "Paraphrase only — human doctrinal review required; verify verse application"
    claim["human_doctrinal_review"] = "required"
    return claim


def main() -> None:
    for d in sorted(WEEKLY.iterdir()):
        if not d.is_dir() or not d.name.startswith("c1-w"):
            continue
        cr = d / "research" / "CLAIM-REGISTER.yaml"
        if not cr.exists():
            continue
        data = yaml.safe_load(cr.read_text(encoding="utf-8"))
        data["claims"] = [patch_claim(c) for c in data.get("claims", [])]
        cr.write_text(yaml.safe_dump(data, sort_keys=False, allow_unicode=True), encoding="utf-8")
        print(f"Patched {cr.relative_to(REPO)}")


if __name__ == "__main__":
    main()
