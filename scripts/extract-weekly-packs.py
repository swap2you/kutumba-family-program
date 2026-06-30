#!/usr/bin/env python3
"""Extract first-six-month weekly derivative packs from the monolithic curriculum."""

from __future__ import annotations

import re
from datetime import date
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
MONOLITH = REPO / "03-first-six-months" / "FIRST-SIX-MONTH-DETAILED-CURRICULUM.md"
WEEKLY_ROOT = REPO / "11-weekly-program-library" / "first-six-months"
CANONICAL = "03-first-six-months/FIRST-SIX-MONTH-DETAILED-CURRICULUM.md"
SOURCE_ID = "KUT-SRC-0004"
SOURCE_HASH = "7123781051c732bc82baee084284d0bcac6c6b5011baf12d07216c2e503a7f58"
EXTRACTION_DATE = date.today().isoformat()

SECTION_RULES: list[tuple[str, str]] = [
    (r"^## Learning Outcomes\b", "learning-outcomes.md"),
    (r"^## Prem-k", "prem-ki-katha.md"),
    (r"^## Parent Lesson\b", "parent-lesson.md"),
    (r"^## Children", "children/lesson.md"),
    (r"^## Analogy and Practical Example\b", "analogy-and-application.md"),
    (r"^## Questions:", "questions.md"),
    (r"^## Bhakti Laboratory\b", "bhakti-lab.md"),
    (r"^## Family Home Practice\b", "family-home-practice.md"),
    (r"^## Slide Outline\b", "slide-outline.md"),
    (r"^## Teacher Preparation\b", "facilitator-guide.md"),
    (r"^## Required Materials\b", "materials.md"),
    (r"^## Assessment\b", "assessment.md"),
    (r"^## Newcomer Adaptation\b", "newcomer-adaptation.md"),
    (r"^## Risks and Sensitive Points\b", "risks-and-sensitive-points.md"),
    (r"^## This Week", "sankalpa.md"),
    (r"^# Printable Worksheet\b", "worksheet.md"),
]

REQUIRED_FILES = [
    "complete-week.md",
    "overview.md",
    "learning-outcomes.md",
    "prem-ki-katha.md",
    "parent-lesson.md",
    "children/lesson.md",
    "analogy-and-application.md",
    "questions.md",
    "bhakti-lab.md",
    "family-home-practice.md",
    "facilitator-guide.md",
    "materials.md",
    "assessment.md",
    "newcomer-adaptation.md",
    "risks-and-sensitive-points.md",
    "worksheet.md",
    "slide-outline.md",
    "sources.yaml",
    "review-status.yaml",
    "README.md",
]


def frontmatter(week_code: str, week_title: str, heading: str, component: str) -> str:
    return (
        "---\n"
        f"week_code: {week_code}\n"
        f"week_title: {week_title}\n"
        f"derived_from:\n"
        f"  canonical_file: {CANONICAL}\n"
        f"  source_id: {SOURCE_ID}\n"
        f"  source_hash: {SOURCE_HASH}\n"
        f"  extraction_heading: \"{heading}\"\n"
        f"  extraction_date: {EXTRACTION_DATE}\n"
        f"  component: {component}\n"
        "---\n\n"
    )


def split_weeks(text: str) -> list[tuple[str, str, str]]:
    pattern = re.compile(r"^# (C\d+-W\d+ — .+)$", re.MULTILINE)
    matches = list(pattern.finditer(text))
    weeks: list[tuple[str, str, str]] = []
    for i, match in enumerate(matches):
        start = match.start()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        block = text[start:end].rstrip() + "\n"
        heading = match.group(1)
        code_match = re.match(r"(C\d+-W\d+) — (.+)", heading)
        if not code_match:
            continue
        weeks.append((code_match.group(1), code_match.group(2).strip(), block))
    return weeks


def section_spans(block: str) -> list[tuple[int, int, str, str]]:
    lines = block.splitlines(keepends=True)
    hits: list[tuple[int, str, str]] = []
    for idx, line in enumerate(lines):
        for pattern, filename in SECTION_RULES:
            if re.match(pattern, line):
                hits.append((idx, pattern, filename))
                break
    spans: list[tuple[int, int, str, str]] = []
    for i, (start_idx, pattern, filename) in enumerate(hits):
        end_idx = hits[i + 1][0] if i + 1 < len(hits) else len(lines)
        content = "".join(lines[start_idx:end_idx]).rstrip() + "\n"
        spans.append((start_idx, end_idx, filename, content))
    return spans


def parse_metadata_table(block: str) -> dict[str, str]:
    meta: dict[str, str] = {}
    for line in block.splitlines():
        m = re.match(r"\| \*\*(.+?)\*\* \| (.+?) \|", line)
        if m:
            meta[m.group(1).strip()] = m.group(2).strip()
    return meta


def find_folder(week_code: str) -> Path | None:
    prefix = week_code.lower().replace("-", "-")  # C1-W1 -> c1-w1
    slug = prefix.lower()
    for child in WEEKLY_ROOT.iterdir():
        if child.is_dir() and child.name.startswith(slug.replace("c", "c")):
            # match c1-w1 at start of folder name
            if child.name.startswith(week_code.lower()):
                return child
    for child in WEEKLY_ROOT.iterdir():
        if child.is_dir() and child.name.startswith(week_code.lower()):
            return child
    return None


def write_component(path: Path, week_code: str, title: str, heading: str, component: str, body: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(frontmatter(week_code, title, heading, component) + body, encoding="utf-8")


def build_readme(week_code: str, title: str, meta: dict[str, str], folder: Path) -> str:
    cycle = "1" if week_code.startswith("C1") else "2" if week_code.startswith("C2") else "3"
    key_verse = meta.get("Key verse", "See overview")
    home_practice = meta.get("Minimum home practice", "See family-home-practice.md")
    links = "\n".join(f"- [{f}]({f})" for f in REQUIRED_FILES if f != "README.md")
    return f"""# {week_code} — {title}

## Purpose

{meta.get('Purpose', 'See overview.md')}

## Cycle

Cycle {cycle} — first six months (Year 1 foundation)

## Key verse

{key_verse}

## Minimum home practice

{home_practice}

## Review status

- `canonical-detailed-source-complete`
- `weekly-derivative-pack-complete` (after validation)
- worship review: required
- safeguarding review: required
- doctrinal review: required

## Canonical source

`{CANONICAL}` — monolithic authoritative block also preserved in [complete-week.md](complete-week.md)

## Navigation

{links}
"""


def build_sources_yaml(week_code: str, title: str) -> str:
    return (
        f"week_code: {week_code}\n"
        f"title: \"{title}\"\n"
        f"canonical: {CANONICAL}\n"
        f"source_id: {SOURCE_ID}\n"
        f"source_hash: {SOURCE_HASH}\n"
    )


def build_review_status(week_code: str) -> str:
    return (
        f"week_code: {week_code}\n"
        "canonical_detailed_source: complete\n"
        "weekly_derivative_pack: complete\n"
        "worship_review: required\n"
        "safety_review: required\n"
        "doctrinal_review: required\n"
        "rights_review: not-applicable\n"
        "publication_status: internal-development\n"
    )


def main() -> None:
    text = MONOLITH.read_text(encoding="utf-8")
    weeks = split_weeks(text)
    if len(weeks) != 18:
        raise SystemExit(f"Expected 18 weeks, found {len(weeks)}")

    for week_code, title, block in weeks:
        folder = find_folder(week_code)
        if folder is None:
            raise SystemExit(f"No folder for {week_code}")

        heading = f"{week_code} — {title}"
        meta = parse_metadata_table(block)

        # complete-week.md — exact block
        complete_path = folder / "complete-week.md"
        complete_path.write_text(
            frontmatter(week_code, title, heading, "complete-week") + block,
            encoding="utf-8",
        )

        # overview — from block start through first ## Learning Outcomes
        learn_idx = block.find("## Learning Outcomes")
        overview_body = block if learn_idx == -1 else block[:learn_idx].rstrip() + "\n"
        # strip leading # heading line for overview (kept in complete-week)
        overview_lines = overview_body.splitlines()
        if overview_lines and overview_lines[0].startswith("# "):
            overview_body = "\n".join(overview_lines[1:]).lstrip() + "\n"
        write_component(folder / "overview.md", week_code, title, heading, "overview", overview_body)

        spans = section_spans(block)
        written: set[str] = set()
        for _, _, filename, content in spans:
            target = folder / filename
            write_component(target, week_code, title, heading, filename.replace("/", "-"), content)
            written.add(filename)

        for pattern, filename in SECTION_RULES:
            if filename not in written:
                placeholder = f"_No `{pattern}` section found in canonical block._\n"
                write_component(folder / filename, week_code, title, heading, filename.replace("/", "-"), placeholder)

        (folder / "sources.yaml").write_text(build_sources_yaml(week_code, title), encoding="utf-8")
        (folder / "review-status.yaml").write_text(build_review_status(week_code), encoding="utf-8")
        (folder / "README.md").write_text(build_readme(week_code, title, meta, folder), encoding="utf-8")

        print(f"OK {week_code} -> {folder.name} ({len(written)} sections)".encode("ascii", "replace").decode())


if __name__ == "__main__":
    main()
