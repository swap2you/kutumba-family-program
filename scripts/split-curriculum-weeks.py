#!/usr/bin/env python3
"""Split first-six-month monolithic curriculum into weekly lesson folders."""

import re
import sys
from pathlib import Path

REPO_ROOT = Path(r"C:\Development\Workspace\DevotionalRepo\kutumba-family-program")
CURRICULUM = REPO_ROOT / "03-first-six-months" / "FIRST-SIX-MONTH-DETAILED-CURRICULUM.md"
WEEK_LIB = REPO_ROOT / "11-weekly-program-library" / "first-six-months"

WEEK_PATTERN = re.compile(r"^# (C\d+-W\d+) — (.+)$", re.MULTILINE)
SECTION_PATTERNS = {
    "parent-lesson": re.compile(r"^## Parent Lesson", re.MULTILINE),
    "children": re.compile(r"^## Children", re.MULTILINE),
    "bhakti-lab": re.compile(r"^## Bhakti Laboratory", re.MULTILINE),
    "family-home-practice": re.compile(r"^## Family Home Practice", re.MULTILINE),
    "worksheet": re.compile(r"^# Printable Worksheet", re.MULTILINE),
    "slide-outline": re.compile(r"^## Slide Outline", re.MULTILINE),
    "facilitator": re.compile(r"^## Teacher Preparation", re.MULTILINE),
}


def slugify(code: str, title: str) -> str:
    s = f"{code}-{title}".lower()
    s = re.sub(r"[^\w\s-]", "", s)
    s = re.sub(r"[\s_]+", "-", s).strip("-")
    return s[:80]


def extract_section(text: str, start_pat: re.Pattern, end_pats: list[re.Pattern]) -> str:
    m = start_pat.search(text)
    if not m:
        return ""
    start = m.start()
    end = len(text)
    for ep in end_pats:
        em = ep.search(text, m.end())
        if em and em.start() < end:
            end = em.start()
    return text[start:end].strip()


def parse_week_block(block: str, code: str, title: str) -> dict:
    sections = {}
    sections["full"] = block
    sections["learning-outcomes"] = extract_section(
        block,
        re.compile(r"^## Learning Outcomes", re.MULTILINE),
        [re.compile(r"^## Primary", re.MULTILINE)],
    )
    sections["parent-lesson"] = extract_section(
        block, SECTION_PATTERNS["parent-lesson"],
        [SECTION_PATTERNS["children"], SECTION_PATTERNS["bhakti-lab"]],
    )
    sections["children"] = extract_section(
        block, SECTION_PATTERNS["children"],
        [re.compile(r"^## Analogy", re.MULTILINE)],
    )
    sections["bhakti-lab"] = extract_section(
        block, SECTION_PATTERNS["bhakti-lab"],
        [SECTION_PATTERNS["family-home-practice"]],
    )
    sections["family-home-practice"] = extract_section(
        block, SECTION_PATTERNS["family-home-practice"],
        [SECTION_PATTERNS["slide-outline"]],
    )
    sections["slide-outline"] = extract_section(
        block, SECTION_PATTERNS["slide-outline"],
        [SECTION_PATTERNS["facilitator"]],
    )
    sections["facilitator"] = extract_section(
        block, SECTION_PATTERNS["facilitator"],
        [re.compile(r"^## Required Materials", re.MULTILINE)],
    )
    sections["worksheet"] = extract_section(
        block, SECTION_PATTERNS["worksheet"],
        [re.compile(r"^## This Week", re.MULTILINE), WEEK_PATTERN],
    )
    return sections


def main():
    text = CURRICULUM.read_text(encoding="utf-8")
    matches = list(WEEK_PATTERN.finditer(text))
    if not matches:
        print("No weeks found", file=sys.stderr)
        return 1

    created = []
    for i, m in enumerate(matches):
        code, title = m.group(1), m.group(2)
        start = m.start()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        block = text[start:end].strip()
        folder_name = slugify(code, title)
        week_dir = WEEK_LIB / folder_name
        week_dir.mkdir(parents=True, exist_ok=True)
        sections = parse_week_block(block, code, title)

        (week_dir / "README.md").write_text(
            f"# {code} — {title}\n\n"
            f"Canonical monolithic source: `03-first-six-months/FIRST-SIX-MONTH-DETAILED-CURRICULUM.md`\n\n"
            f"## Status\n\n- detailed-lesson-complete\n"
            f"- worship-review-required\n"
            f"- safety-review-required\n",
            encoding="utf-8",
        )
        for key, fname in [
            ("facilitator", "facilitator-guide.md"),
            ("parent-lesson", "parent-lesson.md"),
            ("children", "children/lesson.md"),
            ("bhakti-lab", "bhakti-lab.md"),
            ("family-home-practice", "family-home-practice.md"),
            ("worksheet", "worksheet.md"),
            ("slide-outline", "slide-outline.md"),
        ]:
            content = sections.get(key.replace("/lesson", ""), sections.get(key.split("/")[0], ""))
            if not content and key == "children":
                content = sections.get("children", "")
            path = week_dir / fname
            path.parent.mkdir(parents=True, exist_ok=True)
            body = content if content else f"<!-- Section extracted from canonical curriculum — verify in monolithic document -->\n\nSee full week in canonical curriculum.\n"
            if not path.exists() or path.stat().st_size < 50:
                path.write_text(
                    f"---\nweek_code: {code}\nweek_title: {title}\nsource: 03-first-six-months/FIRST-SIX-MONTH-DETAILED-CURRICULUM.md\n---\n\n{body}\n",
                    encoding="utf-8",
                )

        (week_dir / "sources.yaml").write_text(
            f"week_code: {code}\ntitle: \"{title}\"\ncanonical: 03-first-six-months/FIRST-SIX-MONTH-DETAILED-CURRICULUM.md\n",
            encoding="utf-8",
        )
        (week_dir / "review-status.yaml").write_text(
            f"week_code: {code}\nstatus: detailed-lesson-complete\nworship_review: required\nsafety_review: required\ndoctrinal_review: required\n",
            encoding="utf-8",
        )
        created.append(code)

    print(f"Created {len(created)} week folders: {', '.join(created)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
