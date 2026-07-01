# V10A.2 Owner Usability Validation

Validation date: 2026-07-01.

Starting HEAD: `72202eaafbf836c39386d4966682c939426ffa04`.

Validation HEAD for automated commands: `e1123caba80d06158ca99add81729f182fe383e6`.

## Automated validation

| Check | Result |
|---|---|
| `python scripts/curriculum/validate_internal_links.py` | PASS: UTF-8/NFC, 0 broken links, 0 mojibake links |
| `python scripts/curriculum/validate_v10a_truth_freeze.py` | PASS with duplicate visual hash warning preserved from existing evidence |
| `powershell -File scripts/Validate-KutumbaRepository.ps1` | PASS, 0 failures, 0 warnings |

Tracked validation reports regenerated during this pass:

- `build-evidence/VALIDATION-REPORT.md`
- `build-evidence/PRIVACY-AND-RIGHTS-SCAN.md`

## Navigation integrity checks

| Check | Result |
|---|---|
| New links resolve on Windows/GitHub-style relative paths | PASS |
| Weekly program index rows | PASS: 18 |
| Local absolute paths in navigation pages | PASS: none found |
| Navigation pages link to archived content as canonical | PASS: none found |
| Navigation pages call drafts approved | PASS: no approval claim found |
| Phase consistency across README, START-HERE, reader home, current status, and pause handoff | PASS: `internal-development-paused` |

## Owner scenario results

| Scenario | Result | Evidence |
|---|---|---|
| From README, reach current status in one click | PASS | README links `CURRENT-STATUS.md` in current status section |
| From README, reach START-HERE in one click | PASS | README owner callout links `START-HERE.md` near top |
| From START-HERE, reach any of the 18 weeks in no more than two clicks | PASS | START-HERE -> weekly program index -> module row |
| From a weekly index row, reach parent, both child bands, facilitator and complete-week content | PASS | Every row links parent lesson, Lala-Lali, Kisora-Kisori, facilitator guide, and complete week |
| From START-HERE, reach safeguarding review packet in no more than two clicks | PASS | START-HERE -> human review start page -> safeguarding packet |
| From START-HERE, reach pause/resume instructions in one click | PASS | START-HERE links `PROJECT-PAUSE-HANDOFF.md` |
| No page implies pilot approval | PASS | Navigation pages state browse/review only and NO GO verdicts |
| No page requires knowing folder numbering before finding a week | PASS | START-HERE routes to weekly program index by task |

## Readiness verdicts

- Internal pilot: NO GO.
- Family-facing distribution: NO GO.
- Public publication: NO GO.
- Human approval claimed: none.

## V10A.2.1 closure

| Check | Result |
|---|---|
| README directly links weekly index | PASS |
| Historical build report is clearly superseded | PASS |
| Child-program restriction is explicit | PASS |
| All 18 module READMEs expose available age-band child links | PASS |
| Duplicate START-HERE task rows are removed | PASS |
| Readiness verdicts remain unchanged | PASS: internal pilot NO GO; family-facing distribution NO GO; public publication NO GO |
