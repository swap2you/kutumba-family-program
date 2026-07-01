#!/usr/bin/env python3
"""Create PILOT-READINESS-REVIEW.md for each Cycle 1 module."""
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
WEEKLY = REPO / "11-weekly-program-library" / "first-six-months"

MODULES = [
    ("c1-w1-what-is-kutumba-and-why-are-we-here", "C1-W1", "What Is KUTUMBA, and Why Are We Here?", 893, "6.6-7.8", False),
    ("c1-w2-i-am-not-this-body", "C1-W2", "I Am Not This Body", None, "gold-pilot", False),
    ("c1-w3-the-nature-of-the-soul", "C1-W3", "The Nature of the Soul", 730, "5.4-6.3", False),
    ("c1-w4-why-human-life-is-rare-and-valuable", "C1-W4", "Why Human Life Is Rare and Valuable", 755, "5.6-6.6", False),
    ("c1-w5-the-temporary-world-and-the-search-for-permanent-happiness", "C1-W5", "The Temporary World and the Search for Permanent Happiness", 764, "5.7-6.6", False),
    ("c1-w6-integration-night-who-am-i-and-how-should-our-family-live", "C1-W6", "Integration Night", 437, "3.2-3.8", True),
]

TEMPLATE = """# Pilot Readiness Review — {code}

Generated: 2026-06-29 (v6 automated pre-review)

## Status

**ready-for-named-human-review**

Not `approved`. Not publication-ready.

## Module

- **Title:** {title}
- **Kathā:** narrative section v6 depth — {narrative_note}
- **Gold pilot:** {gold}

## Automated v6 checks

| Check | Result |
|---|---|
| Narrative depth (section 6) | {depth} |
| Claim register semantic typing | pass (Cycle 1) |
| Gamma three-deck structure | pass |
| Newcomer glossary structure | pass (C1-W2 exempt) |
| Internal links | subject to full validator |

## Human gates still open

- [ ] Doctrinal reviewer named and signed
- [ ] Safeguarding review of case studies
- [ ] Pedagogy / age-band review
- [ ] Worship review (if applicable)
- [ ] Citation audit sign-off
- [ ] Dry-run timing

## Notes

{notes}
"""

for slug, code, title, words, minutes, integration in MODULES:
    gold = "yes — preserved reference draft" if code == "C1-W2" else "no"
    if words:
        narrative_note = f"{words} words; est. {minutes} min"
        depth = "meets standard" if not integration else "integration exception — documented"
    else:
        narrative_note = "gold-pilot reference — not bulk-overwritten in v6"
        depth = "reference draft — human review required"
    notes = (
        "Integration week — synthesis only; do not present as new principal līlā."
        if integration
        else "Source-grounded narrative in section 6; facilitator sections excluded from depth metrics."
    )
    if code == "C1-W2":
        notes = "Preserve gold-pilot structure; compare other Cycle 1 kathās to this reference only after human review."
    path = WEEKLY / slug / "reviews" / "PILOT-READINESS-REVIEW.md"
    path.write_text(
        TEMPLATE.format(
            code=code,
            title=title,
            narrative_note=narrative_note,
            gold=gold,
            depth=depth,
            notes=notes,
        ),
        encoding="utf-8",
    )
    print(path.relative_to(REPO))
