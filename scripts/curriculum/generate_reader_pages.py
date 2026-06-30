#!/usr/bin/env python3
"""Generate KUTUMBA-READER-HOME.md and cycle reader pages."""
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
WEEKLY = REPO / "11-weekly-program-library" / "first-six-months"

MODULES = sorted([d for d in WEEKLY.iterdir() if d.is_dir() and d.name.startswith("c")])

def code(name: str) -> str:
    p = name.split("-")
    return f"{p[0].upper()}-{p[1].upper()}"

def title_from_readme(d: Path) -> str:
    r = d / "README.md"
    if not r.exists():
        return d.name
    for line in r.read_text(encoding="utf-8").splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return d.name

def main() -> None:
    mod_lines = []
    for d in MODULES:
        c = code(d.name)
        t = title_from_readme(d)
        rs = (d / "review-status.yaml").read_text(encoding="utf-8") if (d / "review-status.yaml").exists() else ""
        status = "enhancement-complete" if "enhancement-complete" in rs else "scaffold"
        mod_lines.append(
            f"| {c} | {t} | [{c} README](11-weekly-program-library/first-six-months/{d.name}/README.md) | {status} |"
        )

    home = f"""# KUTUMBA Reader Home

Comfortable reading entry point for the family program documentation.

## Start here

| Document | Link |
|---|---|
| Current status | [CURRENT-STATUS.md](CURRENT-STATUS.md) |
| Roadmap | [ROADMAP.md](ROADMAP.md) |
| Master operating model | [00-foundation/MASTER-OPERATING-MODEL.md](00-foundation/MASTER-OPERATING-MODEL.md) |
| Governance | [GOVERNANCE.md](GOVERNANCE.md) |
| Three-year curriculum | [02-curriculum-architecture/THREE-YEAR-CURRICULUM-ARCHITECTURE.md](02-curriculum-architecture/THREE-YEAR-CURRICULUM-ARCHITECTURE.md) |
| How to read (preview setup) | [docs/READING-KUTUMBA-DOCUMENTS.md](docs/READING-KUTUMBA-DOCUMENTS.md) |

## Cycles (first six months)

| Cycle | Reader page |
|---|---|
| Cycle 1 — Identity | [CYCLE-1-READER.md](11-weekly-program-library/first-six-months/CYCLE-1-READER.md) |
| Cycle 2 — Karma & modes | [CYCLE-2-READER.md](11-weekly-program-library/first-six-months/CYCLE-2-READER.md) |
| Cycle 3 — Bhakti | [CYCLE-3-READER.md](11-weekly-program-library/first-six-months/CYCLE-3-READER.md) |

## All 18 modules

| Code | Title | README | Depth |
|---|---|---|---|
{chr(10).join(mod_lines)}

## Libraries and evidence

| Resource | Link |
|---|---|
| Family library | [12-family-facing-library/README.md](12-family-facing-library/README.md) |
| Facilitator library | [13-facilitator-library/README.md](13-facilitator-library/README.md) |
| Source register | [14-research-source-register/SOURCE-AUTHORITY-POLICY.md](14-research-source-register/SOURCE-AUTHORITY-POLICY.md) |
| Media library | [14-research-source-register/media-library/README.md](14-research-source-register/media-library/README.md) |
| Visual gallery index | [build-evidence/VISUAL-AND-RIGHTS-AUDIT.md](build-evidence/VISUAL-AND-RIGHTS-AUDIT.md) |
| Reviews and audits | [17-reviews-and-audits/README.md](17-reviews-and-audits/README.md) |

## Status legend

| Label | Meaning |
|---|---|
| enhancement-complete | Gold-standard depth; human review still required |
| scaffold | Directory present; deepen before publication |
| human-review-required | No named human approval yet |
"""
    (REPO / "KUTUMBA-READER-HOME.md").write_text(home, encoding="utf-8")

    for cycle in (1, 2, 3):
        mods = [d for d in MODULES if d.name.startswith(f"c{cycle}-")]
        lines = [
            f"# Cycle {cycle} Reader",
            "",
            f"Purpose: see [THREE-YEAR-CURRICULUM-ARCHITECTURE.md](../../02-curriculum-architecture/THREE-YEAR-CURRICULUM-ARCHITECTURE.md)",
            "",
            "## Module sequence",
            "",
        ]
        for d in mods:
            c = code(d.name)
            t = title_from_readme(d)
            base = d.name
            lines += [
                f"### {c} — {t}",
                "",
                "**Two-minute summary:** see module README.",
                "",
                "| Asset | Link |",
                "|---|---|",
                f"| Parent lesson | [{base}/parent-lesson.md]({base}/parent-lesson.md) |",
                f"| Lala-Lali | [{base}/children/lala-lali-lesson.md]({base}/children/lala-lali-lesson.md) |",
                f"| Kisora-Kisori | [{base}/children/kisora-kisori-lesson.md]({base}/children/kisora-kisori-lesson.md) |",
                f"| Prem-ki-Katha | [{base}/prem-ki-katha.md]({base}/prem-ki-katha.md) |",
                f"| Opening hook | [{base}/opening-hook.md]({base}/opening-hook.md) |",
                f"| Visuals | [{base}/visuals/VISUAL-PLAN.md]({base}/visuals/VISUAL-PLAN.md) |",
                f"| Gamma | [{base}/gamma/GAMMA-MASTER-DECK-BRIEF.md]({base}/gamma/GAMMA-MASTER-DECK-BRIEF.md) |",
                f"| Project | [{base}/project/MODULE-PROJECT-BRIEF.md]({base}/project/MODULE-PROJECT-BRIEF.md) |",
                f"| Review status | [{base}/review-status.yaml]({base}/review-status.yaml) |",
                "",
            ]
        (WEEKLY / f"CYCLE-{cycle}-READER.md").write_text("\n".join(lines), encoding="utf-8")
    print("Reader pages generated")

if __name__ == "__main__":
    main()
