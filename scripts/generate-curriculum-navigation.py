#!/usr/bin/env python3
"""Generate curriculum navigation artifacts from canonical architecture."""

from __future__ import annotations

from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
ARCH = REPO / "02-curriculum-architecture" / "THREE-YEAR-CURRICULUM-ARCHITECTURE.md"
OUT = REPO / "02-curriculum-architecture"

CYCLES = [
    ("Y1", 1, "Sambandha", "Identity and the Human Problem", "Who am I, and why does ordinary material success not solve the deepest human problems?"),
    ("Y1", 2, "Sambandha", "Karma, Rebirth and Material Nature", "How do choices shape consciousness and future experience?"),
    ("Y1", 3, "Sambandha", "Kṛṣṇa, Guru and the Process of Bhakti", "Who is the Supreme Person, and how can finite people know Him reliably?"),
    ("Y1", 4, "Sambandha", "Śrī Caitanya, the Holy Name and Nine Processes", "How does the holy name and the nine processes of bhakti work in family life?"),
    ("Y1", 5, "Sambandha", "The Devotional Home", "How does a family build a sustainable devotional home rhythm?"),
    ("Y1", 6, "Sambandha", "Vaiṣṇava Culture, ISKCON Belonging and Sacred Time", "How do families belong to ISKCON culture without confusion or comparison?"),
    ("Y2", 1, "Abhidheya", "Bhagavad-gītā 1–6: Duty, Self-Knowledge and Action", "How does the first half of the Gītā reshape duty, knowledge and action?"),
    ("Y2", 2, "Abhidheya", "Bhagavad-gītā 7–12: Knowing and Loving Kṛṣṇa", "How do we move from knowing about Kṛṣṇa to loving Him?"),
    ("Y2", 3, "Abhidheya", "Bhagavad-gītā 13–18: Nature, Qualities and Surrender", "How do nature, modes and surrender integrate?"),
    ("Y2", 4, "Abhidheya", "Regulated Practice: Mind, Senses, Association and Japa", "How do mind, senses and association support japa?"),
    ("Y2", 5, "Abhidheya", "Vaiṣṇava Relationships and Family Cooperation", "How do Vaiṣṇava relationships sustain family cooperation?"),
    ("Y2", 6, "Abhidheya", "Śrī Īśopaniṣad, Sacred Vision and Pilgrimage", "How do sacred vision and pilgrimage deepen practice?"),
    ("Y3", 1, "Śāstric readiness", "How to Study Śrīla Prabhupāda’s Books", "How do we read deeply, accurately and honestly enough to learn and teach?"),
    ("Y3", 2, "Śāstric readiness", "The Nectar of Devotion: Foundations of Pure Bhakti", "What are the foundations of pure bhakti from NOD?"),
    ("Y3", 3, "Śāstric readiness", "Guru-tattva, Nāma-tattva and Paramparā", "How do guru, nāma and paramparā interrelate at depth?"),
    ("Y3", 4, "Śāstric readiness", "Śrīmad-Bhāgavatam and Caitanya-caritāmṛta Orientation", "How do families orient to Bhāgavatam and CC study?"),
    ("Y3", 5, "Śāstric readiness", "Service Ethics, Devotee Care and Servant Leadership", "What ethics govern service and leadership?"),
    ("Y3", 6, "Śāstric readiness", "Capstone, Readiness and the Continuing Path", "What evidence shows real formation, and what should each family do next?"),
]

WEEK_FUNCTIONS = [
    "Foundational principle",
    "Scriptural narrative and application",
    "Practical bhakti laboratory",
    "Parent and child formation",
    "Case study, practice or service",
    "Integration and evidence",
]

FESTIVALS = [
    ("Y1-F1", 1, "Festival/service/pilgrimage replacement week 1"),
    ("Y1-F2", 1, "Festival/service/pilgrimage replacement week 2"),
    ("Y1-F3", 1, "Festival/service/pilgrimage replacement week 3"),
    ("Y1-F4", 1, "Festival/service/pilgrimage replacement week 4"),
    ("Y2-F1", 2, "Festival/service/pilgrimage replacement week 1"),
    ("Y2-F2", 2, "Festival/service/pilgrimage replacement week 2"),
    ("Y2-F3", 2, "Festival/service/pilgrimage replacement week 3"),
    ("Y2-F4", 2, "Festival/service/pilgrimage replacement week 4"),
    ("Y3-F1", 3, "Festival/service/pilgrimage replacement week 1"),
    ("Y3-F2", 3, "Festival/service/pilgrimage replacement week 2"),
    ("Y3-F3", 3, "Festival/service/pilgrimage replacement week 3"),
    ("Y3-F4", 3, "Festival/service/pilgrimage replacement week 4"),
]

DOMAINS = [
    "philosophy", "scripture", "nāma and japa", "worship", "prasāda", "Vaiṣṇava conduct",
    "family life", "child formation", "service", "festivals", "pilgrimage", "leadership", "study readiness",
]

DOMAIN_YEAR_EMPHASIS = {
    "philosophy": {1: "high", 2: "high", 3: "medium"},
    "scripture": {1: "medium", 2: "high", 3: "high"},
    "nāma and japa": {1: "medium", 2: "high", 3: "high"},
    "worship": {1: "medium", 2: "medium", 3: "medium"},
    "prasāda": {1: "medium", 2: "medium", 3: "low"},
    "Vaiṣṇava conduct": {1: "high", 2: "medium", 3: "medium"},
    "family life": {1: "high", 2: "high", 3: "medium"},
    "child formation": {1: "high", 2: "high", 3: "medium"},
    "service": {1: "medium", 2: "high", 3: "high"},
    "festivals": {1: "medium", 2: "medium", 3: "medium"},
    "pilgrimage": {1: "low", 2: "medium", 3: "medium"},
    "leadership": {1: "low", 2: "medium", 3: "high"},
    "study readiness": {1: "low", 2: "medium", 3: "high"},
}


def write_curriculum_map() -> None:
    lines = [
        "# Three-Year Curriculum Map",
        "",
        "Derived from `THREE-YEAR-CURRICULUM-ARCHITECTURE.md`. Canonical architecture remains authoritative for disputes.",
        "",
        "## Annual rhythm",
        "",
        "| Component | Per year | Three-year total |",
        "|---|---|---|",
        "| Learning-cycle active weeks | 36 | 108 |",
        "| Festival/service/pilgrimage weeks | 4 | 12 |",
        "| Cycle off weeks | 6 | 18 |",
        "| Holiday/buffer weeks | 6 | 18 |",
        "| **Active KUTUMBA program weeks** | **40** | **120** |",
        "",
        "## Year overview",
        "",
        "| Year | Theme | Formation emphasis | Active weeks |",
        "|---|---|---|---|",
        "| 1 | Sambandha | Family foundations and relationship with Kṛṣṇa | 40 |",
        "| 2 | Abhidheya | Regulated practice and deepening sādhana | 40 |",
        "| 3 | Śāstric readiness | Service, leadership, Bhakti Śāstrī readiness boundary | 40 |",
        "",
        "## Cycle map (all years)",
        "",
        "| Cycle ID | Year | Theme track | Cycle title | Cycle question | Integration week | Off week after |",
        "|---|---|---|---|---|---|---|",
    ]
    for idx, (yp, year, theme, title, question) in enumerate(CYCLES, start=1):
        if idx <= 6:
            y, c = 1, idx
        elif idx <= 12:
            y, c = 2, idx - 6
        else:
            y, c = 3, idx - 12
        cid = f"Y{y}-C{c}"
        lines.append(
            f"| {cid} | {y} | {theme} | {title} | {question} | W6 integration | protected off week |"
        )

    lines += [
        "",
        "## First six months (detailed source complete)",
        "",
        "Cycles Y1-C1 through Y1-C3 map to repository week codes C1-W1 … C3-W6 under `11-weekly-program-library/first-six-months/`.",
        "",
        "| Repo week | Cycle week | Function |",
        "|---|---|---|",
    ]
    for c in range(1, 4):
        for w in range(1, 7):
            lines.append(f"| C{c}-W{w} | Y1-C{c}-W{w} | {WEEK_FUNCTIONS[w-1]} |")

    lines += [
        "",
        "## Festival / service / pilgrimage replacements",
        "",
        "| Week ID | Year | Role |",
        "|---|---|---|",
    ]
    for fid, year, desc in FESTIVALS:
        lines.append(f"| {fid} | {year} | {desc} |")

    lines += [
        "",
        "## Week-type legend",
        "",
        "- **Active cycle week** — standard Friday formation session",
        "- **Integration week** — week 6 of each cycle; portfolio and evidence review",
        "- **Off week** — no KUTUMBA meeting; optional continuity practice only",
        "- **Festival week** — replaces normal gathering per calendar framework",
        "",
        "Canonical source: `02-curriculum-architecture/THREE-YEAR-CURRICULUM-ARCHITECTURE.md`",
    ]
    (OUT / "CURRICULUM-MAP.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_domain_matrix() -> None:
    lines = [
        "# Domain Matrix — Years 1–3",
        "",
        "Maps formation domains across the three-year architecture. Intensity: high / medium / low.",
        "",
        "Canonical source: `THREE-YEAR-CURRICULUM-ARCHITECTURE.md`",
        "",
        "| Domain | Year 1 | Year 2 | Year 3 | Primary cycles |",
        "|---|---|---|---|---|",
    ]
    cycle_by_domain = {
        "philosophy": "Y1-C1–C3; Y2-C1–C3",
        "scripture": "Y1-C1–C3; Y2-C1–C6; Y3-C1–C4",
        "nāma and japa": "Y1-C4; Y2-C4",
        "worship": "Y1-C4–C5; Y2-C4; Chat 7 manual",
        "prasāda": "Y1-C5; operations manual",
        "Vaiṣṇava conduct": "Y1-C6",
        "family life": "Y1-C1, C5; Y2-C5",
        "child formation": "all cycles — age-banded parallels",
        "service": "Y1-C5–C6; Y2-C6; Y3-C5",
        "festivals": "festival weeks; Y1-C6",
        "pilgrimage": "Y2-C6; festival/yatra framework",
        "leadership": "Y3-C5–C6",
        "study readiness": "Y3-C1–C4",
    }
    for d in DOMAINS:
        e = DOMAIN_YEAR_EMPHASIS[d]
        lines.append(f"| {d} | {e[1]} | {e[2]} | {e[3]} | {cycle_by_domain.get(d, 'see architecture')} |")
    (OUT / "DOMAIN-MATRIX.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_prerequisite_map() -> None:
    lines = [
        "# Prerequisite Map",
        "",
        "Sequence dependencies from `THREE-YEAR-CURRICULUM-ARCHITECTURE.md` §4.",
        "",
        "## Core sequence",
        "",
        "```",
        "IDENTITY → CONDITIONED STATE → KṛṢṆA → AUTHORISED GUIDANCE → BHAKTI → HOME PRACTICE",
        "→ REGULATION → STUDY → SERVICE → LEADERSHIP",
        "```",
        "",
        "## Cycle prerequisites",
        "",
        "| Cycle | Requires | Setu entry | Cycle-boundary admission |",
        "|---|---|---|---|",
        "| Y1-C1 | KUTUMBA orientation only | Setu may run parallel — not a substitute for C1-W1 | Open at program start |",
        "| Y1-C2 | Y1-C1 body–soul identity | Review Setu completion notes | Document prior exposure if joining at boundary |",
        "| Y1-C3 | Y1-C1–C2 | — | Worship/safety review for children’s parallels |",
        "| Y1-C4 | Y1-C1–C3 | — | Do not skip holy-name depth without C3 |",
        "| Y1-C5 | Y1-C1–C4 | — | Home practice evidence from prior cycles |",
        "| Y1-C6 | Y1-C1–C5 | — | Temple-alignment review |",
        "| Y2-C1 | Year 1 completion or documented equivalent | — | Gītā 1–6 assumes sambandha vocabulary |",
        "| Y2-C2–C6 | Prior Y2 cycles | — | Sequential Gītā map |",
        "| Y3-C1 | Year 2 Gītā map | — | Study-method gate for Year 3 |",
        "| Y3-C2–C6 | Prior Y3 cycles | — | No pseudo-certification |",
        "",
        "## Age-band differentiation",
        "",
        "- Ages 4–6, 7–9, 10–13 receive parallel lessons on the same theme",
        "- Advanced philosophical topics remain facilitator-controlled; not opened to younger bands without adaptation",
        "",
        "## Advanced-topic restrictions",
        "",
        "- Guru selection, initiation candidacy, and rasa topics: **outside general pathway**",
        "- Bhakti Śāstrī referral: capacity review only — attendance insufficient",
        "",
        "## Review requirements at boundaries",
        "",
        "| Boundary | Review |",
        "|---|---|",
        "| Join mid-year | Governance + curriculum lead |",
        "| Skip cycle | Not permitted without documented equivalent pathway |",
        "| Children band change | Children Formation Lead |",
        "| Worship content change | Worship Lead |",
    ]
    (OUT / "PREREQUISITE-MAP.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_source_coverage() -> None:
    lines = [
        "# Source Coverage Map",
        "",
        "Expected scriptural and standards coverage across three years. **No fabricated quotations.**",
        "",
        "| Source | Year 1 emphasis | Year 2 emphasis | Year 3 emphasis | Notes |",
        "|---|---|---|---|---|",
        "| Bhagavad-gītā As It Is | selective verses (cycles 1–3); identity, karma, Kṛṣṇa | full thematic survey C1–C3; regulation C4–C5 | supporting citations in capstone | controlling philosophical source |",
        "| Śrīmad-Bhāgavatam | 1.2.x, introductory narratives | supporting narratives | orientation and study method (C4) | cite book/chapter/verse only |",
        "| Caitanya-caritāmṛta | introductory passages (C3–C4) | supporting | orientation (C4) | subordinate to Prabhupāda books |",
        "| Kṛṣṇa Book | family hearing | supporting | optional stretch | age-appropriate excerpts |",
        "| Nectar of Devotion | — | introductory concepts | Y3-C2 primary | not a substitute for BBT editions |",
        "| Nectar of Instruction | — | supporting | supporting | short-form ethics |",
        "| Śrī Īśopaniṣad | — | Y2-C6 primary | review | with purports |",
        "| ISKCON Disciple Course | transition reference | transition reference | readiness boundary | does not replace KUTUMBA formation |",
        "| Ministry of Education Bhakti Śāstrī guidance | — | — | readiness reference only | optional verse list — not credential |",
        "",
        "## Citation control",
        "",
        "- All quotations must trace to a named BBT/Prabhupāda source",
        "- Unverified claims must be marked for research review",
        "- Legacy Bhaktivriksha/Granth/Jayapataka indexes: **research-only**",
        "",
        "Canonical architecture: `THREE-YEAR-CURRICULUM-ARCHITECTURE.md` §6",
    ]
    (OUT / "SOURCE-COVERAGE-MAP.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_backlog() -> None:
    lines = [
        "# Lesson Production Backlog",
        "",
        "One row per planned active week (120 total). Status vocabulary per repository standards.",
        "",
        "| Week ID | Year | Cycle | Week | Function | Status | Worship | Safety | Doctrinal | Rights |",
        "|---|---|---|---|---|---|---|---|---|---|",
    ]
    # First six months detailed complete
    for c in range(1, 4):
        for w in range(1, 7):
            wid = f"C{c}-W{w}"
            status = "derivative-pack-complete" if True else "detailed-source-complete"
            lines.append(
                f"| {wid} | 1 | {c} | {w} | {WEEK_FUNCTIONS[w-1]} | canonical-detailed-source-complete; weekly-derivative-pack-complete | required | required | required | n/a |"
            )
    # Y1 remaining cycles
    for c in range(4, 7):
        for w in range(1, 7):
            wid = f"Y1-C{c}-W{w}"
            lines.append(
                f"| {wid} | 1 | {c} | {w} | {WEEK_FUNCTIONS[w-1]} | architecture-approved; draft-required | required | required | required | n/a |"
            )
    for y in (2, 3):
        for c in range(1, 7):
            for w in range(1, 7):
                wid = f"Y{y}-C{c}-W{w}"
                lines.append(
                    f"| {wid} | {y} | {c} | {w} | {WEEK_FUNCTIONS[w-1]} | architecture-approved; draft-required | required | required | required | n/a |"
                )
    for fid, year, desc in FESTIVALS:
        lines.append(
            f"| {fid} | {year} | — | festival | {desc} | architecture-approved; source-research-required | required | required | required | rights-review-required |"
        )
    (OUT / "LESSON-PRODUCTION-BACKLOG.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    write_curriculum_map()
    write_domain_matrix()
    write_prerequisite_map()
    write_source_coverage()
    write_backlog()
    print("Curriculum navigation documents generated.")


if __name__ == "__main__":
    main()
