#!/usr/bin/env python3
"""V11 / V11.1 Cycle 1 Saturday launch readiness validator (structural + semantic)."""
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

CODES = ["C1-W1", "C1-W2", "C1-W3", "C1-W4", "C1-W5", "C1-W6"]

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
    re.compile(r"\b\d{3}[-.]?\d{3}[-.]?\d{4}\b"),
    re.compile(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", re.I),
]

FORBIDDEN_LAUNCH = [
    (re.compile(r"\bFriday\b", re.I), "active Friday assumption"),
    (re.compile(r"(?<!\bno )(?<!\bNo )(?<!\bnot a )(?<!\bNot a )weekly meal", re.I), "weekly meal assumption"),
    (re.compile(r"(?<!\bnot )(?<!\bNot )\bapproved for (pilot|publication|distribution)\b", re.I), "unsupported approval claim"),
]

SCAFFOLD_PATTERNS = [
    (re.compile(r"If a printable puzzle is generated later", re.I), "puzzle-later scaffold"),
    (re.compile(r"Word search or matching:", re.I), "word-search scaffold"),
    (re.compile(r"Short bullets on", re.I), "short-bullets scaffold"),
    (re.compile(r"Teach week's conclusion without overclaiming", re.I), "generic gamma scaffold"),
    (re.compile(r"Example slots", re.I), "generic example slots"),
    (re.compile(r"TODO if link not verified", re.I), "TODO link scaffold"),
]

FACILITATOR_REQUIRED = [
    "15-minute night-before",
    "60-minute deep prep",
    "One-page speaking map",
    "Exact opening script",
    "Discovery questions",
    "Understanding questions",
    "Application questions",
    "Common misconceptions",
]

YOUNGER_REQUIRED = [
    "Exact memory phrase",
    "Freeze and Remember",
    "Wonder questions",
    "Backup low-prep",
]

OLDER_ACTIVITY_FORBIDDEN = [
    re.compile(r"If a printable puzzle is generated later", re.I),
    re.compile(r"Word search or matching:", re.I),
]


def nontrivial(path: Path) -> bool:
    text = path.read_text(encoding="utf-8", errors="ignore")
    lines = [ln for ln in text.splitlines() if ln.strip() and not ln.strip().startswith("#")]
    return len(text) >= 400 and len(lines) >= 8


def slide_count(path: Path) -> int:
    text = path.read_text(encoding="utf-8", errors="ignore")
    return len(re.findall(r"^### Slide\s+\d+", text, flags=re.M))


def fingerprint(path: Path) -> str:
    text = path.read_text(encoding="utf-8", errors="ignore")
    # ignore week codes and titles for identity comparison
    text = re.sub(r"C1-W[1-6]", "", text)
    text = re.sub(r"https://vedabase\.io/\S+", "", text)
    return re.sub(r"\s+", " ", text).strip()[:1200]


def main() -> int:
    failures: list[str] = []
    warnings: list[str] = []

    for name in LAUNCH_FILES:
        p = LAUNCH / name
        if not p.exists():
            failures.append(f"missing launch/{name}")

    # Orientation / handbook depth
    for name, min_chars in [
        ("KUTUMBA-C1-FAMILY-ORIENTATION.md", 3500),
        ("KUTUMBA-C1-TEACHER-HANDBOOK.md", 3500),
    ]:
        p = LAUNCH / name
        if p.exists() and len(p.read_text(encoding="utf-8")) < min_chars:
            failures.append(f"launch/{name} too shallow for V11.1 (<{min_chars} chars)")

    w1_script = WEEKLY / SLUGS[0] / "launch-pack" / "MAIN-FACILITATOR-SCRIPT.md"
    if w1_script.exists() and len(w1_script.read_text(encoding="utf-8")) < 2500:
        failures.append("W1 MAIN-FACILITATOR-SCRIPT.md too shallow for V11.1")

    w1 = WEEKLY / SLUGS[0] / "launch-pack"
    for name in W1_LAUNCH_PACK:
        if not (w1 / name).exists():
            failures.append(f"missing W1 launch-pack/{name}")

    master_fps: list[str] = []
    parent_fps: list[str] = []
    younger_fps: list[str] = []
    older_fps: list[str] = []
    diagram_fps: list[str] = []
    line_fps: list[str] = []

    for slug, code in zip(SLUGS, CODES):
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
            elif p.suffix in {".md", ".yaml", ".yml", ".svg", ".mmd"}:
                text = p.read_text(encoding="utf-8", errors="ignore")
                for rx, label in SCAFFOLD_PATTERNS:
                    if rx.search(text):
                        failures.append(f"{slug}/{rel}: {label}")

        # facilitator depth
        fac = base / "teacher" / "MAIN-FACILITATOR-GUIDE-V11.md"
        if fac.exists():
            ft = fac.read_text(encoding="utf-8", errors="ignore")
            for req in FACILITATOR_REQUIRED:
                if req.lower() not in ft.lower():
                    failures.append(f"{code}: facilitator missing '{req}'")
            if len(ft) < 2500:
                failures.append(f"{code}: facilitator guide too short")

        yng = base / "teacher" / "YOUNGER-TEACHER-GUIDE.md"
        if yng.exists():
            yt = yng.read_text(encoding="utf-8", errors="ignore")
            for req in YOUNGER_REQUIRED:
                if req.lower() not in yt.lower():
                    failures.append(f"{code}: younger guide missing '{req}'")

        act = base / "activities" / "OLDER-ACTIVITY-PACK.md"
        key = base / "activities" / "OLDER-ANSWER-KEY.md"
        if act.exists():
            at = act.read_text(encoding="utf-8", errors="ignore")
            for rx in OLDER_ACTIVITY_FORBIDDEN:
                if rx.search(at):
                    failures.append(f"{code}: older activity still scaffold")
            if "Matching puzzle" not in at and "matching" not in at.lower():
                failures.append(f"{code}: older activity missing matching puzzle")
        if key.exists():
            kt = key.read_text(encoding="utf-8", errors="ignore")
            if "Matching key" not in kt and "matching" not in kt.lower():
                failures.append(f"{code}: answer key missing matching key")
            if "If a printable puzzle is generated later" in kt:
                failures.append(f"{code}: answer key still has puzzle-later scaffold")

        # research depth
        scriptural = base / "research" / "SCRIPTURAL-EXAMPLES.md"
        if scriptural.exists():
            st = scriptural.read_text(encoding="utf-8", errors="ignore")
            if "https://vedabase.io/en/library/" in st and st.count("https://vedabase.io/en/library/") == 1:
                # sole root link only
                if "https://vedabase.io/en/library/" in st and not re.search(
                    r"https://vedabase\.io/en/library/(sb|bg)/", st
                ):
                    failures.append(f"{code}: scriptural examples use library root only")
            if re.search(r"https://vedabase\.io/en/library/?\s*\|", st):
                failures.append(f"{code}: VedaBase library root used as sole supporting source row")

        sci = base / "research" / "SCIENCE-AND-APPLICATION.md"
        if sci.exists():
            sct = sci.read_text(encoding="utf-8", errors="ignore")
            if code == "C1-W3":
                if "not used this week" not in sct.lower() and "not used" not in sct.lower():
                    # allow explicit no-science decision language
                    if "doi" not in sct.lower() and "explicit" not in sct.lower():
                        failures.append(f"{code}: science file neither cites nor explicitly declines")
            elif "doi" not in sct.lower() and "10." not in sct and "explicit" not in sct.lower():
                # W3 handled; others should have citation or explicit decline
                if "not used" not in sct.lower() and "Authors:" not in sct:
                    failures.append(f"{code}: science file lacks citation or explicit decline")

        # Gamma slide counts
        master = base / "gamma" / "V11-GAMMA-MASTER-DECK-PROMPT.md"
        parent = base / "gamma" / "V11-GAMMA-PARENT-DECK-PROMPT.md"
        younger = base / "gamma" / "V11-GAMMA-YOUNGER-DECK-PROMPT.md"
        older = base / "gamma" / "V11-GAMMA-OLDER-DECK-PROMPT.md"
        if master.exists():
            sc = slide_count(master)
            need = 20 if code == "C1-W1" else 12
            if sc < need:
                failures.append(f"{code}: master Gamma slides {sc} < {need}")
            master_fps.append(fingerprint(master))
        for label, path, need in [
            ("parent", parent, 10),
            ("younger", younger, 8),
            ("older", older, 10),
        ]:
            if path.exists():
                sc = slide_count(path)
                if sc < need:
                    failures.append(f"{code}: {label} Gamma slides {sc} < {need}")
                if label == "parent":
                    parent_fps.append(fingerprint(path))
                elif label == "younger":
                    younger_fps.append(fingerprint(path))
                else:
                    older_fps.append(fingerprint(path))

        # audience decks must differ within week
        if parent.exists() and younger.exists() and older.exists():
            fp_set = {fingerprint(parent), fingerprint(younger), fingerprint(older)}
            if len(fp_set) < 3:
                failures.append(f"{code}: audience Gamma decks effectively identical")

        # visuals specificity
        line = base / "visuals" / "V11" / "line-art-younger.svg"
        diag = base / "visuals" / "V11" / "concept-diagram.svg"
        if line.exists():
            lt = line.read_text(encoding="utf-8", errors="ignore")
            if code != "C1-W1" and "Family hearing and practice — color the scene" in lt:
                failures.append(f"{code}: generic W1 line-art caption reused")
            line_fps.append(fingerprint(line))
        if diag.exists():
            diagram_fps.append(fingerprint(diag))

        # exports
        for doc in [
            f"{code}-MAIN-FACILITATOR-GUIDE.docx",
            f"{code}-YOUNGER-TEACHER-GUIDE.docx",
            f"{code}-OLDER-TEACHER-GUIDE.docx",
            f"{code}-FAMILY-HANDOUT.docx",
        ]:
            dp = base / "exports" / doc
            alt = base / "exports" / doc.replace(".docx", "-V11_1.docx")
            target = dp if dp.exists() else alt
            if not target.exists() or target.stat().st_size < 1000:
                failures.append(f"{slug}: missing/small DOCX {doc}")
            else:
                # light substance: docx is zip; size alone insufficient — require >3KB for guides
                if "FAMILY" not in doc and target.stat().st_size < 3000:
                    failures.append(f"{slug}: DOCX likely shallow {doc} ({target.stat().st_size} bytes)")

        # W5 / W6 source chain
        if code == "C1-W5":
            st = (base / "research" / "SCRIPTURAL-EXAMPLES.md").read_text(encoding="utf-8", errors="ignore")
            if "BG 8.15" not in st or "Primary anchor" not in st:
                failures.append("C1-W5: primary anchor must be BG 8.15")
            # primary table row should feature 8.15 before supporting 5.22 as primary
            primary_section = st.split("## Supporting")[0] if "## Supporting" in st else st
            if "BG 5.22" in primary_section and "BG 8.15" not in primary_section:
                failures.append("C1-W5: BG 5.22 appears as primary instead of BG 8.15")
            sm = (base / "gamma" / "V11-GAMMA-SOURCE-MAP.yaml").read_text(encoding="utf-8", errors="ignore")
            if "BG 8.15" not in sm:
                failures.append("C1-W5: Gamma source map missing BG 8.15")

        if code == "C1-W6":
            for rel in [
                "research/SCRIPTURAL-EXAMPLES.md",
                "project/PRESENTATION-RUBRIC.md",
                "project/MODULE-PROJECT-BRIEF.md",
                "gamma/V11-GAMMA-SOURCE-MAP.yaml",
                "activities/OLDER-ANSWER-KEY.md",
            ]:
                p = base / rel
                if not p.exists():
                    continue
                t = p.read_text(encoding="utf-8", errors="ignore")
                if "BG 5.22" in t and "BG 8.15" not in t:
                    failures.append(f"C1-W6 {rel}: chain still uses BG 5.22 without BG 8.15")
                if re.search(r"SB 11\.9\.29 · BG 5\.22", t) or re.search(
                    r"SB 11\.9\.29 · BG 5\.22", t
                ):
                    failures.append(f"C1-W6 {rel}: concept chain lists BG 5.22 as W5 primary")
                if "BG 5.22" in t and "8.15" not in t:
                    failures.append(f"C1-W6 {rel}: missing BG 8.15 in chain")

    # diagrams must not all be identical
    if len(set(diagram_fps)) < 5:
        failures.append("concept diagrams appear semantically reused across weeks")
    if len(set(line_fps)) < 5:
        failures.append("younger line art appears reused across weeks")

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
                    if "historical" in text.lower() and label.startswith("active Friday"):
                        continue
                    failures.append(f"{rel}: {label}")
            for rx in PRIVATE_PATTERNS:
                if rx.search(text):
                    failures.append(f"{rel}: possible private contact data")

    for name in [
        "KUTUMBA-C1-FAMILY-ORIENTATION.docx",
        "KUTUMBA-C1-TEACHER-HANDBOOK.docx",
        "OPENING-MANTRAS-HANDOUT.docx",
    ]:
        p = LAUNCH / name
        if not p.exists() or p.stat().st_size < 1000:
            failures.append(f"missing/small launch/{name}")
        elif name != "OPENING-MANTRAS-HANDOUT.docx" and p.stat().st_size < 4000:
            failures.append(f"launch/{name} likely shallow DOCX ({p.stat().st_size} bytes)")

    if not (WEEKLY / "C1-V11-OWNER-INDEX.md").exists():
        failures.append("missing C1-V11-OWNER-INDEX.md")

    if failures:
        for f in failures[:80]:
            print(f"FAIL: {f}")
        print(f"Total failures: {len(failures)}")
        return 1
    for w in warnings:
        print(f"WARN: {w}")
    print("PASS: V11.1 C1 launch readiness structural + semantic checks")
    return 0


if __name__ == "__main__":
    sys.exit(main())
