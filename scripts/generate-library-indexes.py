#!/usr/bin/env python3
"""Generate family-facing and facilitator library INDEX.md files."""

from pathlib import Path
from urllib.parse import quote

REPO = Path(__file__).resolve().parents[1]
WEEKLY = REPO / "11-weekly-program-library" / "first-six-months"

FAMILY_SECTIONS = {
    "weekly-parent-handouts": ("Weekly parent handouts", "parent-lesson.md"),
    "child-worksheets": ("Child worksheets", "worksheet.md"),
    "family-home-practices": ("Family home practices", "family-home-practice.md"),
}

FACILITATOR_SECTIONS = {
    "weekly-packs": ("Complete weekly packs", "complete-week.md"),
    "teacher-preparation": ("Teacher preparation", "facilitator-guide.md"),
    "prem-ki-katha": ("Prem-kī-Kathā scripts", "prem-ki-katha.md"),
    "child-teaching": ("Child teaching", "children/lesson.md"),
    "bhakti-laboratories": ("Bhakti laboratories", "bhakti-lab.md"),
    "materials": ("Materials lists", "materials.md"),
    "assessment": ("Assessment tools", "assessment.md"),
    "risks-and-sensitive-points": ("Risks and sensitive points", "risks-and-sensitive-points.md"),
}


def week_folders():
    return sorted([d for d in WEEKLY.iterdir() if d.is_dir()])


def write_family_indexes():
    for section, (title, file) in FAMILY_SECTIONS.items():
        base = REPO / "12-family-facing-library" / section
        base.mkdir(parents=True, exist_ok=True)
        lines = [
            f"# {title}",
            "",
            "**Publication status:** planned — not yet published",
            "",
            "| Week | Link | Status |",
            "|---|---|---|",
        ]
        for folder in week_folders():
            rel = f"../../11-weekly-program-library/first-six-months/{quote(folder.name)}/{quote(file)}"
            code = folder.name.split("-")[0].upper() + "-" + folder.name.split("-")[1].upper()
            lines.append(f"| {code} | [{folder.name}]({rel}) | planned — not yet published |")
        (base / "INDEX.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    for section, (title, path) in [
        ("prayers-and-slokas", ("Prayers and ślokas", "../../07-kirtana-worship-bhakti-labs/KIRTANA-WORSHIP-PRAYERS-BHAKTI-LABORATORIES-MANUAL.md")),
        ("festivals-and-yatras", ("Festivals and yātrās", "../../08-festivals-yatras-calendar/FESTIVALS-YATRAS-OUTDOOR-CALENDAR-FRAMEWORK.md")),
        ("kutumba-setu", ("KUTUMBA Setu", "../../10-kutumba-setu/GAP-RECORD.md")),
        ("home-worship", ("Home worship", "../../07-kirtana-worship-bhakti-labs/KIRTANA-WORSHIP-PRAYERS-BHAKTI-LABORATORIES-MANUAL.md")),
        ("prasada", ("Prasāda", "../../06-prasadam-operations/PRASADA-HOSPITALITY-WEEKLY-OPERATIONS-MANUAL.md")),
        ("policies-and-safety", ("Policies and safety summaries", "../../04-children-youth/CHILDREN-YOUTH-FORMATION-OPERATING-MODEL.md")),
    ]:
        base = REPO / "12-family-facing-library" / section
        base.mkdir(parents=True, exist_ok=True)
        (base / "INDEX.md").write_text(
            f"# {title}\n\n**Publication status:** planned — not yet published\n\n"
            f"Canonical source: [{path}]({path})\n",
            encoding="utf-8",
        )


def write_facilitator_indexes():
    for section, (title, file) in FACILITATOR_SECTIONS.items():
        base = REPO / "13-facilitator-library" / section
        base.mkdir(parents=True, exist_ok=True)
        lines = [
            f"# {title}",
            "",
            "| Week | Link |",
            "|---|---|",
        ]
        for folder in week_folders():
            rel = f"../../11-weekly-program-library/first-six-months/{quote(folder.name)}/{quote(file)}"
            lines.append(f"| {folder.name} | [open]({rel}) |")
        (base / "INDEX.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    for section, (title, path) in [
        ("worship-review", ("Worship-review items", "../../07-kirtana-worship-bhakti-labs/KIRTANA-WORSHIP-PRAYERS-BHAKTI-LABORATORIES-MANUAL.md")),
        ("safeguarding-review", ("Safeguarding-review items", "../../04-children-youth/CHILDREN-YOUTH-FORMATION-OPERATING-MODEL.md")),
    ]:
        base = REPO / "13-facilitator-library" / section
        base.mkdir(parents=True, exist_ok=True)
        (base / "INDEX.md").write_text(
            f"# {title}\n\n**Review status:** required\n\nCanonical: [{path}]({path})\n",
            encoding="utf-8",
        )


def main():
    write_family_indexes()
    write_facilitator_indexes()
    print("Library indexes generated.")


if __name__ == "__main__":
    main()
