#!/usr/bin/env python3
"""V11 Cycle 1 Saturday launch readiness validator (read-only checks)."""
from __future__ import annotations

import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
WEEKLY = REPO / "11-weekly-program-library" / "first-six-months"
LAUNCH = REPO / "launch"

SLUGS = [
    "c1-w1-what-is-kutumba-and-why-are-we-here",
    "c1-w2-i-am-not-this-body",
    "c1-w3-the-nature-of-the-soul",
    "c1-w4-why-human-life-is-rare-and-valuable",
    "c1-w5-the-temporary-world-and-the-search-for-permanent-happiness",
    "c1-w6-integration-night-who-am-i-and-how-should-our-family-live",
]

LAUNCH_FILES = [
    "FAMILY-COVENANT.md",
    "FAMILY-COVENANT-ACKNOWLEDGEMENT-TEMPLATE.md",
    "CHILD-HOUSE-RULES.md",
    "TEACHER-READINESS-STANDARD.md",
    "TEACHER-PRE-WEEK-CHECKLIST.md",
    "OPENING-MANTRAS-HANDOUT.md",
    "C1-SATURDAY-CALENDAR.md",
    "KUTUMBA-C1-FAMILY-ORIENTATION.md",
    "KUTUMBA-C1-TEACHER-HANDBOOK.md",
]

W1_LAUNCH_PACK = [
    "SATURDAY-RUN-OF-SHOW.md",
    "MAIN-FACILITATOR-SCRIPT.md",
    "PARENT-ORIENTATION-HANDOUT.md",
    "SIX-MONTH-ROADMAP-HANDOUT.md",
    "CHILD-RULES-YOUNGER.md",
    "CHILD-RULES-OLDER.md",
    "TEACHER-BRIEFING.md",
    "PRINT-CHECKLIST.md",
    "ROOM-SETUP.md",
    "SNACK-AND-ALLERGY-CHECKLIST-TEMPLATE.md",
    "FAMILY-SANKALPA-CARD.md",
    "CYCLE-1-PROJECT-INTRO.md",
    "WEEK-1-HOME-PRACTICE.md",
    "OWNER-NIGHT-BEFORE-CHECKLIST.md",
    "OWNER-60-MINUTE-PREP-PLAN.md",
]

PER_WEEK = [
    "teacher/MAIN-FACILITATOR-GUIDE-V11.md",
    "teacher/YOUNGER-TEACHER-GUIDE.md",
    "teacher/OLDER-TEACHER-GUIDE.md",
    "teacher/PRE-WEEK-CHECKLIST.md",
    "research/SCRIPTURAL-EXAMPLES.md",
    "research/DEVOTIONAL-AND-HISTORICAL-EXAMPLES.md",
    "research/CASE-STUDIES.md",
    "research/SCIENCE-AND-APPLICATION.md",
    "research/ANALOGIES-AND-LIMITS.md",
    "project/MODULE-PROJECT-BRIEF.md",
    "project/CYCLE-CONTRIBUTION.md",
    "project/PRESENTATION-RUBRIC.md",
    "activities/YOUNGER-ACTIVITY-PACK.md",
    "activities/OLDER-ACTIVITY-PACK.md",
    "activities/OLDER-ANSWER-KEY.md",
    "gamma/V11-GAMMA-MASTER-DECK-PROMPT.md",
    "gamma/V11-GAMMA-PARENT-DECK-PROMPT.md",
    "gamma/V11-GAMMA-YOUNGER-DECK-PROMPT.md",
    "gamma/V11-GAMMA-OLDER-DECK-PROMPT.md",
    "gamma/V11-GAMMA-SOURCE-MAP.yaml",
    "visuals/V11/concept-diagram.svg",
    "visuals/V11/line-art-younger.svg",
    "visuals/V11/concept-diagram.mmd",
    "visuals/V11/IMAGE-GENERATION-PROMPTS.md",
    "visuals/V11/VISUAL-RIGHTS-REGISTER.yaml",
]

PRIVATE_PATTERNS = [
    re.compile(r"\b\d{3}[-.]?\d{3}[-.]?\d{4}\b"),  # phone
    re.compile(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", re.I),
]

FORBIDDEN_LAUNCH = [
    (re.compile(r"\bFriday\b", re.I), "active Friday assumption"),
    (re.compile(r"(?<!\bno )(?<!\bNo )(?<!\bnot a )(?<!\bNot a )weekly meal", re.I), "weekly meal assumption"),
    (re.compile(r"(?<!\bnot )(?<!\bNot )\bapproved for (pilot|publication|distribution)\b", re.I), "unsupported approval claim"),
]


def nontrivial(path: Path) -> bool:
    text = path.read_text(encoding="utf-8", errors="ignore")
    lines = [ln for ln in text.splitlines() if ln.strip() and not ln.strip().startswith("#")]
    return len(text) >= 400 and len(lines) >= 8


def main() -> int:
    failures: list[str] = []
    warnings: list[str] = []

    for name in LAUNCH_FILES:
        p = LAUNCH / name
        if not p.exists():
            failures.append(f"missing launch/{name}")

    w1 = WEEKLY / SLUGS[0] / "launch-pack"
    for name in W1_LAUNCH_PACK:
        if not (w1 / name).exists():
            failures.append(f"missing W1 launch-pack/{name}")

    for slug in SLUGS:
        base = WEEKLY / slug
        if not base.exists():
            failures.append(f"missing week {slug}")
            continue
        for rel in PER_WEEK:
            p = base / rel
            if not p.exists():
                failures.append(f"{slug}: missing {rel}")
            elif "project/" in rel and not nontrivial(p):
                failures.append(f"{slug}: trivial project file {rel}")
        # exports
        code = slug.split("-")[0].upper() + "-" + slug.split("-")[1].upper()
        for doc in [
            f"{code}-MAIN-FACILITATOR-GUIDE.docx",
            f"{code}-YOUNGER-TEACHER-GUIDE.docx",
            f"{code}-OLDER-TEACHER-GUIDE.docx",
            f"{code}-FAMILY-HANDOUT.docx",
        ]:
            dp = base / "exports" / doc
            if not dp.exists() or dp.stat().st_size < 1000:
                failures.append(f"{slug}: missing/small DOCX {doc}")

    # W1 contamination check
    analogy = WEEKLY / SLUGS[0] / "analogy-and-application.md"
    if analogy.exists():
        t = analogy.read_text(encoding="utf-8", errors="ignore")
        if "Changing garments" in t or "BG 2.22" in t or "Driver and vehicle" in t:
            failures.append("W1 analogy-and-application still contains W2 body/soul contamination")

    # Launch-facing Friday / meal / approval scans
    scan_roots = [LAUNCH, WEEKLY / SLUGS[0] / "launch-pack"]
    for slug in SLUGS:
        scan_roots.extend(
            [
                WEEKLY / slug / "teacher",
                WEEKLY / slug / "parent-lesson.md",
                WEEKLY / slug / "family-home-practice.md",
                WEEKLY / slug / "materials.md",
            ]
        )
    for root in scan_roots:
        paths = [root] if root.is_file() else list(root.rglob("*.md")) if root.exists() else []
        for p in paths:
            if not p.is_file():
                continue
            text = p.read_text(encoding="utf-8", errors="ignore")
            rel = p.relative_to(REPO).as_posix()
            for rx, label in FORBIDDEN_LAUNCH:
                if rx.search(text):
                    # allow historical notes explicitly marked
                    if "historical" in text.lower() and label.startswith("active Friday"):
                        continue
                    failures.append(f"{rel}: {label}")
            for rx in PRIVATE_PATTERNS:
                if rx.search(text):
                    failures.append(f"{rel}: possible private contact data")

    # DOCX launch exports
    for name in [
        "KUTUMBA-C1-FAMILY-ORIENTATION.docx",
        "KUTUMBA-C1-TEACHER-HANDBOOK.docx",
        "OPENING-MANTRAS-HANDOUT.docx",
    ]:
        p = LAUNCH / name
        if not p.exists() or p.stat().st_size < 1000:
            failures.append(f"missing/small launch/{name}")

    if not (WEEKLY / "C1-V11-OWNER-INDEX.md").exists():
        failures.append("missing C1-V11-OWNER-INDEX.md")

    if failures:
        for f in failures[:60]:
            print(f"FAIL: {f}")
        print(f"Total failures: {len(failures)}")
        return 1
    for w in warnings:
        print(f"WARN: {w}")
    print("PASS: V11 C1 launch readiness structural checks")
    return 0


if __name__ == "__main__":
    sys.exit(main())
