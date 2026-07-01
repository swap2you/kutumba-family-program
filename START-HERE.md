# KUTUMBA Start Here

Primary owner and reviewer entry point.

## Current truth

| Area | Status |
|---|---|
| Phase | `internal-development-paused` |
| Repository preservation | GO |
| Repository development controls | GO WITH CONDITIONS |
| Internal pilot | NO GO |
| Family-facing distribution | NO GO |
| Public publication | NO GO |
| Human approval claimed | none |

Read the controlling status files:

- [CURRENT-STATUS.md](CURRENT-STATUS.md)
- [PROJECT-PAUSE-HANDOFF.md](PROJECT-PAUSE-HANDOFF.md)
- [PILOT-READINESS-GATE-REGISTER.yaml](17-reviews-and-audits/PILOT-READINESS-GATE-REGISTER.yaml)

## Choose what you need to do

| I need to... | Open |
|---|---|
| Understand the project | [Master operating model](00-foundation/MASTER-OPERATING-MODEL.md) |
| Browse or open any of the 18 weeks | [Weekly program index](11-weekly-program-library/first-six-months/WEEKLY-PROGRAM-INDEX.md) |
| Review parent and age-band child content | [Weekly program index](11-weekly-program-library/first-six-months/WEEKLY-PROGRAM-INDEX.md) |
| Review safety and approvals | [Human review start page](17-reviews-and-audits/HUMAN-REVIEW-START-HERE.md) |
| Understand what is blocked | [Current status](CURRENT-STATUS.md) and [gate register](17-reviews-and-audits/PILOT-READINESS-GATE-REGISTER.yaml) |
| Resume repository work later | [Project pause handoff](PROJECT-PAUSE-HANDOFF.md) |
| Run validation | [Validation](#validation) |
| Add or correct a source | [How to add a source](README.md#how-to-add-a-source) |

## Safe-to-use boundary

Materials may be browsed and reviewed as internal development drafts. They may not be treated as approved pilot materials, family-facing materials, or publication-ready materials.

## Five-minute orientation

1. Read [CURRENT-STATUS.md](CURRENT-STATUS.md).
2. Skim the [master operating model](00-foundation/MASTER-OPERATING-MODEL.md).
3. Open the [weekly program index](11-weekly-program-library/first-six-months/WEEKLY-PROGRAM-INDEX.md).
4. Open the [human review start page](17-reviews-and-audits/HUMAN-REVIEW-START-HERE.md).
5. Read the [pause handoff](PROJECT-PAUSE-HANDOFF.md).

## Repository owner shortcuts

| Shortcut | File |
|---|---|
| Comfortable reading home | [KUTUMBA-READER-HOME.md](KUTUMBA-READER-HOME.md) |
| First-six-month weekly index | [WEEKLY-PROGRAM-INDEX.md](11-weekly-program-library/first-six-months/WEEKLY-PROGRAM-INDEX.md) |
| Human review entry point | [HUMAN-REVIEW-START-HERE.md](17-reviews-and-audits/HUMAN-REVIEW-START-HERE.md) |
| Pause/resume instructions | [PROJECT-PAUSE-HANDOFF.md](PROJECT-PAUSE-HANDOFF.md) |
| Roadmap | [ROADMAP.md](ROADMAP.md) |
| Source authority policy | [SOURCE-AUTHORITY-POLICY.md](14-research-source-register/SOURCE-AUTHORITY-POLICY.md) |

## Validation

```powershell
python scripts/curriculum/validate_internal_links.py
python scripts/curriculum/validate_v10a_truth_freeze.py
powershell -File scripts/Validate-KutumbaRepository.ps1
```
