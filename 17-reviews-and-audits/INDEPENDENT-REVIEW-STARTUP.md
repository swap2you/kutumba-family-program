# Independent Repository Review — Startup

## Purpose

This document hands off the completed initial build for independent audit using Prompt 10 (`16-prompt-library/11-quality-review/complete-independent-repository-audit.md` or `KUTUMBA_CURSOR_PROMPT_LIBRARY_v2/.../prompts/10-INDEPENDENT-REVIEW-PROMPT.md`).

## Verdict request

Produce: **GO** / **GO WITH CONDITIONS** / **NO GO**

## What to verify

### 1. Repository identity

- [ ] Git root is `C:\Development\Workspace\DevotionalRepo\kutumba-family-program` with no nested `kutumba-family-program` folder
- [ ] Remote is `https://github.com/swap2you/kutumba-family-program.git` (private)
- [ ] Evidence: `build-evidence/REPOSITORY-TREE.txt`, `git rev-parse --show-toplevel`

### 2. Source parity

- [ ] 12 current KUTUMBA originals copied with SHA-256 in `00-source-materials/SOURCE-MANIFEST.yaml`
- [ ] Original Downloads folder untouched: `C:\Users\swap2\Downloads\Personal\0. KUTUMBA SANGA`
- [ ] Evidence: `build-evidence/SOURCE-INGESTION-REPORT.md`, `build-evidence/DOCUMENT-PARITY-REPORT.md`

### 3. Curriculum integrity

- [ ] Monolithic first-six-month curriculum preserved at full depth
- [ ] 18 active sessions (C1-W1 … C3-W6) present
- [ ] Weekly folders in `11-weekly-program-library/first-six-months/` link to canonical monolith
- [ ] Evidence: `build-evidence/CONTENT-COVERAGE-REPORT.md`, `03-first-six-months/FIRST-SIX-MONTH-DETAILED-CURRICULUM.md`

### 4. Copyright and legacy controls

- [ ] Legacy Bhaktivriksha (1,595), Granth (110), Jayapataka BV (68) indexed only — not bulk-copied
- [ ] No legacy silent adoption
- [ ] Evidence: `00-source-materials/03-external-reference-index/`, `17-reviews-and-audits/LEGACY-ADOPTION-REVIEW.md`

### 5. Privacy and safety

- [ ] No secrets or private family records in Git
- [ ] Worship and safeguarding review gates marked open on children/youth and worship content
- [ ] Evidence: `build-evidence/PRIVACY-AND-RIGHTS-SCAN.md`, `00-foundation/REVIEW-QUEUE.md`

### 6. Missing workstreams (expected gaps)

- [ ] Workstream 9 (Digital Repository) marked SOURCE NOT YET SUPPLIED — not fabricated
- [ ] KUTUMBA Setu marked DRAFT REQUIRED — not fabricated
- [ ] Evidence: `14-research-source-register/SOURCE-GAP-MAP.md`

### 7. Validation

- [ ] Run: `powershell -File scripts/Validate-KutumbaRepository.ps1`
- [ ] Evidence: `build-evidence/VALIDATION-REPORT.md`

### 8. Build completeness

- [ ] `build-evidence/FINAL-BUILD-REPORT.md` reviewed
- [ ] `CURRENT-STATUS.md` reflects latest commit SHA and push status

## Evidence index

| Report | Path |
|---|---|
| Source ingestion | `build-evidence/SOURCE-INGESTION-REPORT.md` |
| Document parity | `build-evidence/DOCUMENT-PARITY-REPORT.md` |
| Content coverage | `build-evidence/CONTENT-COVERAGE-REPORT.md` |
| Validation | `build-evidence/VALIDATION-REPORT.md` |
| Cleanup | `build-evidence/CLEANUP-REPORT.md` |
| Repository tree | `build-evidence/REPOSITORY-TREE.txt` |
| Final build | `build-evidence/FINAL-BUILD-REPORT.md` |
| Build ledger | `build-evidence/BUILD-LEDGER.md` |

## Review context command

Open a **fresh** Cursor chat at the canonical root and paste the contents of:

`16-prompt-library/00-orchestration/external-bootstrap-pack/prompts/10-INDEPENDENT-REVIEW-PROMPT.md`

Or use: `16-prompt-library/11-quality-review/complete-independent-repository-audit.md`

## Required reviewers (ongoing)

- Governance Lead — governance and temple boundaries
- Worship Lead — Chat 7 manual and liturgical content
- Children Formation Lead — safeguarding
- Research Lead — legacy rights before any adoption
- Digital Lead — when Workstream 9 source is supplied
