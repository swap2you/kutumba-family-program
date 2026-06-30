#!/usr/bin/env python3
"""Scaffold enhanced module folder structure per Prompt 04."""

from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
WEEKLY = REPO / "11-weekly-program-library" / "first-six-months"

SUBDIRS = [
    "research", "visuals/assets", "gamma", "project", "reviews", "audio-video",
]

RESEARCH_FILES = [
    "RESEARCH-DOSSIER.md", "SOURCE-MATRIX.md", "CLAIM-REGISTER.yaml",
    "VERSE-AND-REFERENCE-STUDY.md", "PRABHUPADA-LECTURE-INDEX.md",
    "APPROVED-TEACHER-MEDIA-INDEX.md", "MISCONCEPTIONS-AND-BOUNDARIES.md",
    "CONTEMPORARY-APPLICATIONS.md", "FAQ.md", "BIBLIOGRAPHY.md",
]

VISUAL_FILES = ["VISUAL-PLAN.md", "concept-map.mmd", "process-flow.mmd", "image-rights-register.yaml"]

GAMMA_FILES = [
    "GAMMA-MASTER-DECK-BRIEF.md", "GAMMA-PARENT-DECK-PROMPT.md",
    "GAMMA-LALA-LALI-DECK-PROMPT.md", "GAMMA-KISORA-KISORI-DECK-PROMPT.md", "SPEAKER-NOTES.md",
]

PROJECT_FILES = ["MODULE-PROJECT-BRIEF.md", "CYCLE-CONTRIBUTION.md", "PRESENTATION-RUBRIC.md"]

REVIEW_FILES = [
    "DOCTRINAL-REVIEW.md", "CITATION-AUDIT.md", "SAFEGUARDING-REVIEW.md",
    "RIGHTS-REVIEW.md", "PEDAGOGY-REVIEW.md",
]


def scaffold(folder: Path, week_code: str) -> None:
    for sd in SUBDIRS:
        (folder / sd).mkdir(parents=True, exist_ok=True)
    for name in RESEARCH_FILES:
        p = folder / "research" / name
        if not p.exists():
            p.write_text(f"# {name.replace('-', ' ').replace('.md', '').replace('.yaml', '')}\n\nModule: {week_code}\n\n_Status: pending enhancement_\n", encoding="utf-8")
    for name in VISUAL_FILES:
        p = folder / "visuals" / name
        if not p.exists():
            p.write_text(f"# {name}\n\nModule: {week_code}\n", encoding="utf-8")
    for name in GAMMA_FILES:
        p = folder / "gamma" / name
        if not p.exists():
            p.write_text(f"# {name}\n\nModule: {week_code}\n", encoding="utf-8")
    for name in PROJECT_FILES:
        p = folder / "project" / name
        if not p.exists():
            p.write_text(f"# {name}\n\nModule: {week_code}\n", encoding="utf-8")
    for name in REVIEW_FILES:
        p = folder / "reviews" / name
        if not p.exists():
            p.write_text(f"# {name}\n\nModule: {week_code}\n\nStatus: human-review-required\n", encoding="utf-8")
    av = folder / "audio-video" / "MEDIA-INDEX.yaml"
    if not av.exists():
        av.write_text(f"week_code: {week_code}\nmedia: []\n", encoding="utf-8")
    for child in ["lala-lali-lesson.md", "kisora-kisori-lesson.md", "shared-family-transition.md"]:
        p = folder / "children" / child
        if not p.exists():
            p.write_text(f"# {child}\n\nModule: {week_code}\n\n_Status: pending_\n", encoding="utf-8")


def main() -> None:
    for d in sorted(WEEKLY.iterdir()):
        if d.is_dir() and re_match(d.name):
            code = to_code(d.name)
            scaffold(d, code)
    print("Scaffolded all modules")


def re_match(name: str) -> bool:
    import re
    return bool(re.match(r"c\d+-w\d+", name))


def to_code(name: str) -> str:
    import re
    m = re.match(r"c(\d+)-w(\d+)", name)
    return f"C{m.group(1)}-W{m.group(2)}" if m else name


if __name__ == "__main__":
    main()
