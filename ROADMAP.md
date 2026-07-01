# KUTUMBA Repository Roadmap

Controlled execution roadmap for the public documentation and curriculum-development repository at `kutumba-family-program`. This document sequences remaining production, human review, publication preparation, and multi-year curriculum work. It does not assign calendar dates; sequence numbers express dependency order only.

**Baseline commit:** `0c08d04` (`docs: add independent repository audit report and update evidence timestamps`)  
**Repository visibility:** Public by intentional decision during development (`https://github.com/swap2you/kutumba-family-program.git`)  
**Status vocabulary:** `COMPLETE` · `IN PROGRESS` · `PENDING` · `BLOCKED`

**V10A.1 safe pause (2026-07-01):** V8 structural remediation is preserved as historical evidence, but V9 found unresolved substantive gaps. Current phase is `internal-development-paused`; internal pilot, family-facing distribution, and public publication are all `NO GO` until blocking gates in `17-reviews-and-audits/PILOT-READINESS-GATE-REGISTER.yaml` close with named reviewer evidence. Resume from [PROJECT-PAUSE-HANDOFF.md](PROJECT-PAUSE-HANDOFF.md).

---

## 1. Purpose and scope

### 1.1 Purpose

This roadmap governs controlled completion of the KUTUMBA documentation knowledge base: canonical operating documents, weekly lesson packs, missing workstreams, human review gates, family- and facilitator-facing publication indexes, founding-pilot readiness, and three-year curriculum production. It aligns with [GOVERNANCE.md](GOVERNANCE.md), [CURRENT-STATUS.md](CURRENT-STATUS.md), and [AGENTS.md](AGENTS.md).

### 1.2 In scope

| Area | Primary paths |
|---|---|
| Source provenance and manifests | `00-source-materials/`, `build-evidence/SOURCE-INGESTION-REPORT.md` |
| Canonical operating documents (workstreams 0–8) | `00-foundation/` … `08-festivals-yatras-calendar/` |
| Missing workstreams | `09-digital-repository-publishing/`, `10-kutumba-setu/` |
| Weekly program library | `11-weekly-program-library/` |
| Publication indexes | `12-family-facing-library/`, `13-facilitator-library/`, `18-published-exports/` |
| Curriculum architecture and backlog | `02-curriculum-architecture/` |
| Production prompts and audits | `16-prompt-library/`, `17-reviews-and-audits/` |
| Validation and evidence | `scripts/`, `build-evidence/` |

### 1.3 Out of scope

- Application, API, database, authentication, or public website implementation
- Bulk copying of copyrighted PDF libraries or legacy training packs
- Fabrication of complete documents where source is not supplied
- Commit of private participant records, credentials, or completed personal forms
- Unapproved worship procedures presented as temple-approved

### 1.4 Roadmap phase metadata (applies to all phases below)

Every phase row includes: **Phase ID**, **Outcome**, **Deliverables**, **Source dependency**, **Owner role**, **Reviewers**, **Status**, **Prerequisites**, **Exit criteria**, **Blocked-by**, **Target sequence**, **Git milestone**, **Publication consequence**.

---

## 2. Current baseline

**V6 content-truth baseline (2026-06-29):** see `build-evidence/V6-CONTENT-TRUTH-BASELINE.md` and `17-reviews-and-audits/V6-INDEPENDENT-PILOT-READINESS-AUDIT.md`.

| Metric | Value | Evidence path |
|---|---|---|
| Source originals ingested | **14** | `00-source-materials/SOURCE-MANIFEST.yaml` |
| Authoritative source-map URLs | **77** | `09-digital-repository-publishing/PUBLIC-SOURCE-MAP-FOR-PRABHUPADA-AND-SANATANA-CONTENT.md` |
| Master source catalog entries | **78** | `14-research-source-register/public-source-catalog/MASTER-SOURCE-CATALOG.yaml` |
| Authoritative URLs catalogued | **77/77** | `build-evidence/SOURCE-MAP-URL-RECONCILIATION.md` |
| First-six-month active weeks | 18 (C1-W1 … C3-W6) | `11-weekly-program-library/first-six-months/` |
| Cycle 1 pilot pack | draft internal | `13-facilitator-library/cycle-1-pilot/` |
| C1-W2 gold pilot | preserved | `c1-w2-i-am-not-this-body/` |
| Workstream 9 | partial — map/directory complete; manual gap | `09-digital-repository-publishing/` |
| KUTUMBA Setu | not approved | `10-kutumba-setu/` |
| Human review gates | open all modules | `00-foundation/REVIEW-QUEUE.md` |
| Publication readiness | **not-ready** | `CURRENT-STATUS.md` |
| Internal pilot readiness | **NO GO** | `17-reviews-and-audits/PILOT-READINESS-GATE-REGISTER.yaml` |
| Family-facing distribution | **NO GO** | `CURRENT-STATUS.md` |
| Public publication | **NO GO** | `CURRENT-STATUS.md` |

### Historical baseline (pre-v5)

Independent audit at `17-reviews-and-audits/INDEPENDENT-REPOSITORY-AUDIT.md` records verdict **GO WITH CONDITIONS** at baseline commit `0c08d04`.

| Metric | Value | Evidence path |
|---|---|---|
| Source originals ingested (historical) | 12 | superseded — now 14 |
| Legacy/reference indexed | 1,773 (metadata only) | `00-source-materials/03-external-reference-index/` |
| Canonical MD operating documents | 9 | `build-evidence/DOCUMENT-PARITY-REPORT.md` |
| Three-year active-week architecture | 120 weeks | `02-curriculum-architecture/THREE-YEAR-CURRICULUM-ARCHITECTURE.md` |
| Production prompts | 19+ | `16-prompt-library/` |

### Phase: RM-BASE

| Field | Value |
|---|---|
| **Phase ID** | RM-BASE |
| **Outcome** | Audited, validated public documentation repository at known commit |
| **Deliverables** | `CURRENT-STATUS.md`, `build-evidence/FINAL-BUILD-REPORT.md`, `17-reviews-and-audits/INDEPENDENT-REPOSITORY-AUDIT.md`, `VALIDATION-REPORT.md` |
| **Source dependency** | All 12 KUT-SRC originals per `SOURCE-MANIFEST.yaml` |
| **Owner role** | Repository Maintainer |
| **Reviewers** | Independent auditor (Prompt 10) |
| **Status** | COMPLETE |
| **Prerequisites** | Phases RM-FND-01 … RM-FND-09 complete |
| **Exit criteria** | Validation PASS; audit report filed; baseline commit tagged in roadmap |
| **Blocked-by** | — |
| **Target sequence** | 0 |
| **Git milestone** | `0c08d04` |
| **Publication consequence** | Public repo exposes canonical MD and weekly packs under CC BY-NC-SA 4.0; worship/safeguarding content marked review-required, not publication-approved |

---

## 3. Completed repository foundation

Build phases 02–08 and git publish are complete per `CURRENT-STATUS.md` and `build-evidence/FINAL-BUILD-REPORT.md`.

| Phase ID | Outcome | Deliverables | Source dependency | Owner role | Reviewers | Status | Prerequisites | Exit criteria | Blocked-by | Target sequence | Git milestone | Publication consequence |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| RM-FND-01 | Sources ingested with SHA-256 provenance | `00-source-materials/01-current-kutumba-originals/`, `SOURCE-MANIFEST.yaml`, `build-evidence/SOURCE-INGESTION-REPORT.md` | 12 project originals from controlled download location | Repository Maintainer | — | COMPLETE | Canonical git root | All hashes verified | — | 1 | phase commit | Originals available for traceability; no new public content |
| RM-FND-02 | Repository folder structure and navigation | `README.md`, 23 workstream folders, `build-evidence/REPOSITORY-TREE.txt` | — | Repository Maintainer | — | COMPLETE | RM-FND-01 | Tree matches README map | — | 2 | phase commit | Public folder map accurate |
| RM-FND-03 | DOCX → canonical Markdown normalization | 9 workstream MD files (`00-foundation/` … `08-festivals-yatras-calendar/`) | KUT-SRC-0001 … KUT-SRC-0009 equivalents per manifest | Canonical Editor | Doctrinal reviewer (deferred) | COMPLETE | RM-FND-01 | `DOCUMENT-PARITY-REPORT.md` 9/9 OK | — | 3 | phase commit | Full-depth operating models publicly readable |
| RM-FND-04 | First-six-month monolith preserved | `03-first-six-months/FIRST-SIX-MONTH-DETAILED-CURRICULUM.md` | KUT-SRC first-six-months source | Curriculum Lead | — | COMPLETE | RM-FND-03 | ~5,000-line monolith intact | — | 4 | phase commit | Canonical detailed curriculum public |
| RM-FND-05 | Weekly library split and assembly | 18 folders under `11-weekly-program-library/first-six-months/` | Monolith + split script | Curriculum Lead | — | COMPLETE | RM-FND-04 | 18 `complete-week.md` + component files | — | 5 | phase commit | Weekly packs browsable in public repo |
| RM-FND-06 | Legacy analysis (reference-only) | `14-research-source-register/`, `00-source-materials/03-external-reference-index/`, crosswalks | External collections (metadata only) | Research Lead | Rights reviewer | COMPLETE | RM-FND-01 | No bulk PDF copy; adoption default reference-only | — | 6 | phase commit | Index metadata public; no copyrighted bulk |
| RM-FND-07 | Prompt library v1.0.0 | `16-prompt-library/` (19 prompts), external bootstrap pack | Internal authoring | Prompt Maintainer | — | COMPLETE | RM-FND-02 | Version tagged in library README | — | 7 | phase commit | Production prompts available to contributors |
| RM-FND-08 | Validation and cleanup | `scripts/Validate-KutumbaRepository.ps1`, `build-evidence/VALIDATION-REPORT.md`, archived duplicates in `99-archive/` | — | Repository Maintainer | — | COMPLETE | RM-FND-03 … RM-FND-05 | 0 critical validation failures | — | 8 | phase commit | CI-style gate documented |
| RM-FND-09 | Git publish and independent review handoff | Push to `origin/main`, `17-reviews-and-audits/INDEPENDENT-REVIEW-STARTUP.md` | — | Repository Maintainer | — | COMPLETE | RM-FND-08 | Remote synced; handoff doc present | — | 9 | `91cb3ab` … `0c08d04` | Public remote live |

---

## 4. Remaining document-production work

Summary of open production lanes. Detailed phases appear in sections 5–7 and 15–18.

| Gap | Path | Status | Review queue |
|---|---|---|---|
| Workstream 9 — Digital Repository/Publishing | `09-digital-repository-publishing/` | SOURCE NOT YET SUPPLIED | RQ-001 |
| KUTUMBA Setu | `10-kutumba-setu/` | DRAFT REQUIRED | RQ-002 |
| Year 1 cycles 4–6 detailed lessons | `02-curriculum-architecture/LESSON-PRODUCTION-BACKLOG.md` | architecture-approved; draft-required | — |
| Year 2 all cycles | same backlog | architecture-approved; draft-required | — |
| Year 3 all cycles | same backlog | architecture-approved; draft-required | — |
| Family-facing derivatives | `12-family-facing-library/` | planned — not yet published | worship + safeguarding |
| Facilitator publication layer | `13-facilitator-library/` | internal-development | worship + safeguarding |
| Controlled exports | `18-published-exports/` | deferred | Publishing Lead |

### Phase: RM-PROD-OVERVIEW

| Field | Value |
|---|---|
| **Phase ID** | RM-PROD-OVERVIEW |
| **Outcome** | All gaps tracked with honest status; no fabricated complete documents |
| **Deliverables** | `00-foundation/REVIEW-QUEUE.md`, workstream `GAP-RECORD.md` files, this roadmap |
| **Source dependency** | Supplied sources only |
| **Owner role** | Program Director |
| **Reviewers** | Independent auditor |
| **Status** | IN PROGRESS |
| **Prerequisites** | RM-BASE |
| **Exit criteria** | Every gap has owner, path, and sequence; no false COMPLETE labels |
| **Blocked-by** | — |
| **Target sequence** | 10 |
| **Git milestone** | next docs commit after phase closure |
| **Publication consequence** | Public readers see explicit gaps, not placeholder doctrine |

---

## 5. Workstream 9 production

**Path:** `09-digital-repository-publishing/`  
**Gap record:** `09-digital-repository-publishing/GAP-RECORD.md`  
**Review owner:** Digital Lead (per workstream README)

| Phase ID | Outcome | Deliverables | Source dependency | Owner role | Reviewers | Status | Prerequisites | Exit criteria | Blocked-by | Target sequence | Git milestone | Publication consequence |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| RM-WS9-01 | Authoritative source supplied and ingested | New original in `01-current-kutumba-originals/`, manifest entry, ingestion report update | Dedicated KUTUMBA Digital Repository/Publishing source document (not yet in KUTUMBA SANGA set) | Digital Lead | Repository Maintainer | BLOCKED | RM-BASE | Source file received; SHA-256 in manifest | Missing source document | 11 | `ingest-ws9-source` | Enables workstream content to exist |
| RM-WS9-02 | Canonical Markdown normalization | `09-digital-repository-publishing/*.md` with `source_id` frontmatter | RM-WS9-01 output | Canonical Editor | Digital Lead, Program Director | PENDING | RM-WS9-01 | Parity report row OK; README status → active | RM-WS9-01 | 12 | `canonicalize-ws9` | Digital policy publicly documented |
| RM-WS9-03 | Alignment with master model and privacy policy | Cross-links to `00-foundation/MASTER-OPERATING-MODEL.md`, `SECURITY-PRIVACY.md`, `RIGHTS-AND-USE.md` | RM-WS9-02 | Digital Lead | Governance reviewer | PENDING | RM-WS9-02 | No conflict with privacy exclusions; RQ-001 closable | RM-WS9-01 | 13 | `integrate-ws9` | Clarifies what may never enter Git |
| RM-WS9-04 | Review and closure | Updated `REVIEW-QUEUE.md`, workstream README publication status | RM-WS9-03 | Digital Lead | Program Director | PENDING | RM-WS9-03 | RQ-001 closed; validation PASS | RM-WS9-01 | 14 | `close-ws9-gap` | Workstream 9 treated as canonical operating doc |

---

## 6. KUTUMBA Setu production

**Path:** `10-kutumba-setu/`  
**Gap record:** `10-kutumba-setu/GAP-RECORD.md`  
**Cross-references:** `05-parent-formation/PARENT-FORMATION-AND-FAMILY-CARE-OPERATING-MODEL.md`, `12-family-facing-library/kutumba-setu/INDEX.md`  
**Review owner:** Setu Lead

| Phase ID | Outcome | Deliverables | Source dependency | Owner role | Reviewers | Status | Prerequisites | Exit criteria | Blocked-by | Target sequence | Git milestone | Publication consequence |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| RM-SETU-01 | Setu scope and outline approved | `10-kutumba-setu/SETU-OUTLINE.md` (or equivalent structured draft) | Master Operating Model Setu references; parent formation model | Setu Lead | Program Director, Parent-Track Lead | PENDING | RM-BASE | Outline covers orientation, covenant, modules, starter practice | — | 15 | `setu-outline` | Internal draft only |
| RM-SETU-02 | Full Setu canonical document drafted | `10-kutumba-setu/KUTUMBA-SETU.md` (+ module files if split) | RM-SETU-01; `16-prompt-library/` production prompts | Setu Lead | Doctrinal reviewer, Worship Lead (where liturgical) | PENDING | RM-SETU-01 | DRAFT REQUIRED → draft-complete in README | — | 16 | `setu-draft` | Draft visible in public repo marked unapproved |
| RM-SETU-03 | Worship and newcomer-safety review | Review notes; updated `review-status` metadata | RM-SETU-02 | Setu Lead | Worship Lead, Children Formation Lead | PENDING | RM-SETU-02; RM-WOR-02 progress | Worship/safeguarding gates satisfied for Setu-specific content | RM-WOR-02, RM-SAFE-02 | 17 | `setu-reviewed` | Setu may be cited in weekly newcomer-adaptation tables |
| RM-SETU-04 | Family-facing index linkage | `12-family-facing-library/kutumba-setu/INDEX.md` updated | RM-SETU-03 | Setu Lead | Publishing Lead | PENDING | RM-SETU-03; RM-FAM-01 | Index points to approved sections only | RM-FAM-01 | 18 | `setu-index-linked` | Setu derivative publication when family layer approved |
| RM-SETU-05 | Queue closure | RQ-002 closed in `REVIEW-QUEUE.md` | RM-SETU-03 | Setu Lead | Program Director | PENDING | RM-SETU-03 | RQ-002 status closed | RM-SETU-02 | 19 | `close-setu-gap` | Setu treated as supplied workstream |

---

## 7. First-six-month weekly-pack completion

**Paths:** `11-weekly-program-library/first-six-months/c1-w1-*` … `c3-w6-*`  
**Backlog:** `02-curriculum-architecture/LESSON-PRODUCTION-BACKLOG.md` (C1-W1 … C3-W6 rows)  
**Templates:** `15-templates/`

| Phase ID | Outcome | Deliverables | Source dependency | Owner role | Reviewers | Status | Prerequisites | Exit criteria | Blocked-by | Target sequence | Git milestone | Publication consequence |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| RM-FSM-01 | Monolith canonical blocks verified | `03-first-six-months/FIRST-SIX-MONTH-DETAILED-CURRICULUM.md` | KUT-SRC first-six-months | Curriculum Lead | — | COMPLETE | RM-FND-04 | All 18 week blocks present | — | 5 | phase commit | Source of truth for splits |
| RM-FSM-02 | Derivative pack files per week | Per week: `complete-week.md`, `overview.md`, `parent-lesson.md`, `children/lesson.md`, `facilitator-guide.md`, `bhakti-lab.md`, `prem-ki-katha.md`, `worksheet.md`, `family-home-practice.md`, `assessment.md`, `materials.md`, `questions.md`, `analogy-and-application.md`, `sankalpa.md`, `newcomer-adaptation.md`, `risks-and-sensitive-points.md`, `slide-outline.md`, `sources.yaml`, `review-status.yaml`, `README.md` | Monolith extraction | Curriculum Lead | — | COMPLETE | RM-FSM-01 | All 18 folders; backlog status `weekly-derivative-pack-complete` | — | 5 | phase commit | Full facilitator pack public (review-required) |
| RM-FSM-03 | Facilitator library index sync | `13-facilitator-library/weekly-packs/INDEX.md` | RM-FSM-02 | Facilitator Lead | — | COMPLETE | RM-FSM-02 | Index lists 18 complete packs | — | 20 | phase commit | Facilitators can navigate packs |
| RM-FSM-04 | Enhanced `sources.yaml` traceability (optional hardening) | Per-week `sources.yaml` with scripture/citation pointers beyond monolith link | Monolith + architecture | Curriculum Lead | Doctrinal reviewer | PENDING | RM-FSM-02 | Audit note on minimal sources addressed or accepted | — | 21 | `fsm-sources-hardening` | Stronger public citation traceability |
| RM-FSM-05 | Re-validation after any pack edits | `build-evidence/VALIDATION-REPORT.md` | — | Repository Maintainer | — | PENDING | Any RM-FSM-04 change | Validation PASS | — | 22 | post-edit validation commit | Changed packs safe to rely on |

---

## 8. Worship review

**Primary sources:** `07-kirtana-worship-bhakti-labs/KIRTANA-WORSHIP-PRAYERS-BHAKTI-LABORATORIES-MANUAL.md` (Chat 7 manual)  
**Weekly touchpoints:** `11-weekly-program-library/first-six-months/*/bhakti-lab.md`, `facilitator-guide.md`, `prem-ki-katha.md`  
**Index:** `13-facilitator-library/worship-review/INDEX.md`  
**Prompt:** `16-prompt-library/11-quality-review/review-worship-content.md`  
**Queue:** RQ-005 in `00-foundation/REVIEW-QUEUE.md`

| Phase ID | Outcome | Deliverables | Source dependency | Owner role | Reviewers | Status | Prerequisites | Exit criteria | Blocked-by | Target sequence | Git milestone | Publication consequence |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| RM-WOR-01 | Worship review inventory | `13-facilitator-library/worship-review/INDEX.md` complete item list | Canonical worship manual + 18 weekly packs | Worship Lead | Temple Liaison | PENDING | RM-BASE | All liturgical touchpoints listed | — | 23 | `worship-inventory` | No change to public approval status |
| RM-WOR-02 | Chat 7 manual temple-alignment review | Annotated review record in `17-reviews-and-audits/` or workstream folder | `07-kirtana-worship-bhakti-labs/` | Worship Lead | Temple Liaison, Program Director | PENDING | RM-WOR-01 | Manual approved or change list merged | — | 24 | `worship-manual-reviewed` | Worship manual may be cited as reviewed |
| RM-WOR-03 | Weekly pack worship sign-off | All 18 `review-status.yaml` → `worship_review: approved` with reviewer metadata | RM-WOR-02 | Worship Lead | Temple Liaison | PENDING | RM-WOR-02 | 18/18 weekly worship fields approved | RM-WOR-02 | 25 | `weekly-worship-approved` | Weekly worship-touched files eligible for family publication |
| RM-WOR-04 | Queue closure and governance update | RQ-005 closed; `GOVERNANCE.md` cross-reference if needed | RM-WOR-03 | Worship Lead | Program Director | PENDING | RM-WOR-03 | RQ-005 closed | RM-WOR-02 | 26 | `close-worship-rq` | Unconditional GO worship condition cleared |

---

## 9. Safeguarding review

**Primary sources:** `04-children-youth/CHILDREN-YOUTH-FORMATION-OPERATING-MODEL.md`  
**Weekly touchpoints:** `11-weekly-program-library/first-six-months/*/children/lesson.md`, `risks-and-sensitive-points.md`  
**Index:** `13-facilitator-library/safeguarding-review/INDEX.md`  
**Prompt:** `16-prompt-library/11-quality-review/review-safeguarding-content.md`  
**Queue:** RQ-006 in `00-foundation/REVIEW-QUEUE.md`

| Phase ID | Outcome | Deliverables | Source dependency | Owner role | Reviewers | Status | Prerequisites | Exit criteria | Blocked-by | Target sequence | Git milestone | Publication consequence |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| RM-SAFE-01 | Safeguarding review inventory | `13-facilitator-library/safeguarding-review/INDEX.md` | Children/youth model + 18 children lessons | Children Formation Lead | Governance reviewer | PENDING | RM-BASE | All child-facing items listed | — | 27 | `safeguarding-inventory` | No publication approval yet |
| RM-SAFE-02 | Operating model safeguarding sign-off | Review record; model status metadata | `04-children-youth/` | Children Formation Lead | Program Director, Temple Liaison | PENDING | RM-SAFE-01 | Formation model approved or amended | — | 28 | `safeguarding-model-reviewed` | Children/youth policy publicly defensible |
| RM-SAFE-03 | Weekly children lesson sign-off | 18 `review-status.yaml` → `safety_review: approved` | RM-SAFE-02 | Children Formation Lead | Program Director | PENDING | RM-SAFE-02 | 18/18 safety fields approved | RM-SAFE-02 | 29 | `weekly-safety-approved` | Children lessons eligible for family worksheets export |
| RM-SAFE-04 | Queue closure | RQ-006 closed | RM-SAFE-03 | Children Formation Lead | Program Director | PENDING | RM-SAFE-03 | RQ-006 closed | RM-SAFE-02 | 30 | `close-safeguarding-rq` | Unconditional GO safeguarding condition cleared |

---

## 10. Rights and citation review

**Policy:** [RIGHTS-AND-USE.md](RIGHTS-AND-USE.md)  
**Legacy:** `17-reviews-and-audits/LEGACY-ADOPTION-REVIEW.md`, `14-research-source-register/`  
**Scan evidence:** `build-evidence/PRIVACY-AND-RIGHTS-SCAN.md`  
**Queues:** RQ-003, RQ-004 in `REVIEW-QUEUE.md`

| Phase ID | Outcome | Deliverables | Source dependency | Owner role | Reviewers | Status | Prerequisites | Exit criteria | Blocked-by | Target sequence | Git milestone | Publication consequence |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| RM-RIGHTS-01 | Confirm no prohibited bulk in Git | Updated `PRIVACY-AND-RIGHTS-SCAN.md` | Repository tree | Research Lead | Repository Maintainer | COMPLETE | RM-FND-06 | Scan clean; audit F-009 pass | — | 6 | phase commit | Public repo free of bulk copyrighted PDFs |
| RM-RIGHTS-02 | Legacy Bhaktivriksha disposition | Decision log per `LEGACY-ADOPTION-REVIEW.md` | `LEGACY-BHAKTIVRIKSHA-FILE-INDEX.csv` | Research Lead | Rights reviewer, Doctrinal reviewer | PENDING | RM-RIGHTS-01 | RQ-003 resolved (remain reference-only or explicit adoption list) | — | 31 | `legacy-bv-rights` | No silent legacy adoption |
| RM-RIGHTS-03 | Granth PDF redistribution boundary | RQ-004 disposition documented | `GRANTH-PDF-CATALOG.csv` | Research Lead | Rights reviewer | PENDING | RM-RIGHTS-01 | RQ-004 closed; catalog stays metadata-only unless licensed | — | 32 | `granth-rights` | Scripture PDFs not redistributed from repo |
| RM-RIGHTS-04 | Citation traceability acceptance | Decision on `sources.yaml` hardening (RM-FSM-04) | Weekly packs + monolith | Curriculum Lead | Doctrinal reviewer | PENDING | RM-FSM-02 | Traceability standard documented in architecture | — | 33 | `citation-standard` | Public citations meet stated standard |
| RM-RIGHTS-05 | Pre-export rights gate | Checklist in `18-published-exports/README.md` | RM-RIGHTS-02 … RM-RIGHTS-04 | Publishing Lead | Research Lead | PENDING | RM-PUB-01 prerequisites | Export blocked until rights checklist pass | RM-PUB-01 | 34 | `export-rights-gate` | No published export violates RIGHTS-AND-USE |

---

## 11. Family-facing publication preparation

**Path:** `12-family-facing-library/`  
**Prompt:** `16-prompt-library/11-quality-review/generate-family-facing-derivative.md`  
**Status:** `planned — not yet published` (all index sections)

| Phase ID | Outcome | Deliverables | Source dependency | Owner role | Reviewers | Status | Prerequisites | Exit criteria | Blocked-by | Target sequence | Git milestone | Publication consequence |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| RM-FAM-01 | Publication policy and index baseline | `12-family-facing-library/README.md`, section INDEX files | Canonical workstreams | Publishing Lead | Program Director | COMPLETE | RM-FND-02 | Index structure live | — | 35 | phase commit | Indexes public; content not yet approved |
| RM-FAM-02 | Weekly parent handout derivatives | `12-family-facing-library/weekly-parent-handouts/` entries linked to `parent-lesson.md` | 18 weekly packs | Publishing Lead | Parent-Track Lead | PENDING | RM-WOR-03, RM-SAFE-03 | Handouts marked publication-ready in index | RM-WOR-03, RM-SAFE-03 | 36 | `family-parent-handouts` | Parents may receive trimmed handouts |
| RM-FAM-03 | Child worksheet derivatives | `12-family-facing-library/child-worksheets/` | `worksheet.md`, `children/lesson.md` | Publishing Lead | Children Formation Lead | PENDING | RM-SAFE-03 | Worksheets approved for distribution | RM-SAFE-03 | 37 | `family-worksheets` | Child worksheets distributable |
| RM-FAM-04 | Family home practice cards | `12-family-facing-library/family-home-practices/` | `family-home-practice.md` | Publishing Lead | Parent-Track Lead | PENDING | RM-WOR-03 | Home practices without unapproved worship | RM-WOR-03 | 38 | `family-home-practices` | Home practice cards distributable |
| RM-FAM-05 | Prayers, festivals, prasāda, policies summaries | Subfolders: `prayers-and-slokas/`, `festivals-and-yatras/`, `prasada/`, `policies-and-safety/` | Workstreams 06–08, 07, 04, 01 | Publishing Lead | Worship Lead, Children Formation Lead | PENDING | RM-WOR-03, RM-SAFE-02 | Each index section has approved subset | RM-WOR-03 | 39 | `family-topic-summaries` | Topic summaries safe for families |
| RM-FAM-06 | Family library publication status flip | README publication status → approved subset documented | RM-FAM-02 … RM-FAM-05 | Publishing Lead | Program Director | PENDING | All RM-FAM-02 … RM-FAM-05 | Explicit list of published vs withheld items | RM-FAM-02 … RM-FAM-05 | 40 | `family-library-published` | Family-facing layer officially open |

---

## 12. Facilitator-library preparation

**Path:** `13-facilitator-library/`  
**Status:** `internal-development`

| Phase ID | Outcome | Deliverables | Source dependency | Owner role | Reviewers | Status | Prerequisites | Exit criteria | Blocked-by | Target sequence | Git milestone | Publication consequence |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| RM-FAC-01 | Weekly pack index complete | `13-facilitator-library/weekly-packs/INDEX.md` | RM-FSM-02 | Facilitator Lead | — | COMPLETE | RM-FSM-02 | 18 packs indexed | — | 41 | phase commit | Facilitators navigate weekly packs |
| RM-FAC-02 | Teacher preparation index | `13-facilitator-library/teacher-preparation/INDEX.md` | `facilitator-guide.md` × 18 | Facilitator Lead | Parent-Track Lead | IN PROGRESS | RM-FSM-02 | All facilitator guides indexed | — | 42 | `facilitator-prep-index` | Internal facilitator onboarding |
| RM-FAC-03 | Prem-kī-Kathā, bhakti lab, materials, assessment indexes | respective `INDEX.md` under `13-facilitator-library/` | Weekly component files | Facilitator Lead | Worship Lead (bhakti labs) | IN PROGRESS | RM-FSM-02 | Section indexes complete | RM-WOR-02 (bhakti labs) | 43 | `facilitator-component-indexes` | Component-level navigation |
| RM-FAC-04 | Worship and safeguarding review indexes synced | `worship-review/`, `safeguarding-review/` INDEX files | RM-WOR-01, RM-SAFE-01 | Facilitator Lead | Worship Lead, Children Formation Lead | PENDING | RM-WOR-01, RM-SAFE-01 | Indexes match review outcomes | — | 44 | `facilitator-review-indexes` | Review status visible to facilitators |
| RM-FAC-05 | Facilitator publication tier (optional) | Status decision in README: internal vs temple-partner | RM-FAC-02 … RM-FAC-04; reviews complete | Program Director | Governance reviewer | PENDING | RM-WOR-04, RM-SAFE-04 | Documented access tier; no private data | RM-WOR-04, RM-SAFE-04 | 45 | `facilitator-tier-defined` | Clarifies who may use full facilitator pack off-repo |

---

## 13. Founding-pilot readiness

**Governance:** `01-governance/GOVERNANCE-CHARTER-AND-TEMPLE-RELATIONSHIP.md` (founding pilot, ~5–6 families)  
**Parent model:** `05-parent-formation/PARENT-FORMATION-AND-FAMILY-CARE-OPERATING-MODEL.md` (launch gates G1–G10, pilot review §34)

| Phase ID | Outcome | Deliverables | Source dependency | Owner role | Reviewers | Status | Prerequisites | Exit criteria | Blocked-by | Target sequence | Git milestone | Publication consequence |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| RM-PILOT-01 | Repository content sufficient for Cycle 1 | C1-W1 … C1-W6 packs + operating docs | RM-FSM-02 | Program Director | Core Team | COMPLETE | RM-FSM-02 | Cycle 1 materials present | — | 46 | `0c08d04` | Pilot may use Cycle 1 from public repo |
| RM-PILOT-02 | Human review gates for Cycle 1 facilitation | Worship + safeguarding progress on Cycle 1 weeks | RM-WOR-03, RM-SAFE-03 (subset or full) | Program Director | Worship Lead, Children Formation Lead | PENDING | RM-PILOT-01 | Cycle 1 `review-status.yaml` approved OR explicit pilot waiver recorded in governance | RM-WOR-02, RM-SAFE-02 | 47 | `pilot-cycle1-reviewed` | Cycle 1 facilitation theologically and safely cleared |
| RM-PILOT-03 | Setu pathway available for late joiners | RM-SETU-02 minimum draft | Setu materials | Setu Lead | Parent-Track Lead | PENDING | RM-SETU-02 | Newcomer-adaptation tables reference live Setu doc | RM-SETU-02 | 48 | `pilot-setu-available` | Late joiners have orientation path |
| RM-PILOT-04 | Launch gates G1–G10 checklist | Evidence against parent model §launch gates | All workstreams 0–8 | Program Director | Core Team, Temple Liaison | PENDING | RM-PILOT-02, temple arrangements | Checklist in governance charter satisfied | Temple/facility external | 49 | `pilot-launch-gates` | Formal pilot authorized per charter |
| RM-PILOT-05 | Pilot documentation handoff | Facilitator + family indexes for Cycle 1; `CURRENT-STATUS.md` pilot note | RM-FAC-02, RM-FAM-02 (Cycle 1 subset) | Program Director | Publishing Lead | PENDING | RM-PILOT-04 | Handoff package defined (repo paths + any off-repo distribution) | RM-PILOT-04 | 50 | `pilot-handoff` | Pilot cohort receives approved materials |

---

## 14. Cycle-review process

**Governance:** `01-governance/GOVERNANCE-CHARTER-AND-TEMPLE-RELATIONSHIP.md` §60  
**Parent model:** `05-parent-formation/...` §34 Cycle review  
**Worship manual:** `07-kirtana-worship-bhakti-labs/...` §19.4 Cycle Review Questions

| Phase ID | Outcome | Deliverables | Source dependency | Owner role | Reviewers | Status | Prerequisites | Exit criteria | Blocked-by | Target sequence | Git milestone | Publication consequence |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| RM-CYCLE-01 | Cycle review template in repo | `13-facilitator-library/` or `01-governance/` cycle-review checklist (extracted from charter) | Governance charter | Program Director | Core Team | PENDING | RM-PILOT-04 | Single canonical checklist path documented | — | 51 | `cycle-review-template` | Facilitators have consistent review tool |
| RM-CYCLE-02 | Post–Cycle 1 review execution | Review record (off-repo or `17-reviews-and-audits/` if non-personal) | Pilot Cycle 1 data | Parent-Track Lead | Core Team | PENDING | RM-PILOT-05; Cycle 1 complete | Continue/stop/simplify/correct/defer decisions logged | Pilot not started | 52 | `cycle1-review-record` | Curriculum/ops changes fed back to repo |
| RM-CYCLE-03 | Repository updates from Cycle 1 review | PRs to weekly packs or operating docs as needed | RM-CYCLE-02 decisions | Curriculum Lead | Worship/safeguarding reviewers if touched | PENDING | RM-CYCLE-02 | Changes merged; validation PASS | — | 53 | `post-cycle1-updates` | Public repo reflects pilot learnings |
| RM-CYCLE-04 | Rolling cycle review rhythm | Standing agenda linked from `CURRENT-STATUS.md` | Charter review cycle | Program Director | Core Team | PENDING | RM-CYCLE-02 | Process documented for cycles 2–18 | — | 54 | `cycle-review-rhythm` | Each cycle closes with documented review |

---

## 15. Year 1 remaining curriculum production

**Architecture:** `02-curriculum-architecture/THREE-YEAR-CURRICULUM-ARCHITECTURE.md`  
**Backlog:** `02-curriculum-architecture/LESSON-PRODUCTION-BACKLOG.md` — Year 1 cycles 4–6 (week IDs `Y1-C4-W1` … `Y1-C6-W6`, 18 weeks)  
**Coverage map:** `02-curriculum-architecture/SOURCE-COVERAGE-MAP.md`  
**Target library path:** `11-weekly-program-library/year-1/` (to be created per production convention)

| Phase ID | Outcome | Deliverables | Source dependency | Owner role | Reviewers | Status | Prerequisites | Exit criteria | Blocked-by | Target sequence | Git milestone | Publication consequence |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| RM-Y1-01 | Year 1 Cycle 4 detailed authoring | 6 week folders + monolith section or year-1 canonical file | Architecture + doctrinal sources per coverage map | Curriculum Lead | Doctrinal reviewer | PENDING | RM-FSM-05; architecture stable | Y1-C4-W1 … W6 → `canonical-detailed-source-complete` | Doctrinal source allocation | 55 | `y1-c4-detailed` | 6 new weeks public when drafted |
| RM-Y1-02 | Year 1 Cycle 4 derivative packs | 6 weekly derivative folders | RM-Y1-01 | Curriculum Lead | Worship, safety reviewers | PENDING | RM-Y1-01 | `weekly-derivative-pack-complete` × 6 | RM-Y1-01 | 56 | `y1-c4-packs` | Facilitator-ready Cycle 4 |
| RM-Y1-03 | Year 1 Cycle 5 detailed authoring | 6 week detailed modules | RM-Y1-01 pattern | Curriculum Lead | Doctrinal reviewer | PENDING | RM-Y1-02 | Y1-C5 complete in backlog | RM-Y1-01 | 57 | `y1-c5-detailed` | 6 additional weeks |
| RM-Y1-04 | Year 1 Cycle 5 derivative packs | 6 weekly folders | RM-Y1-03 | Curriculum Lead | Worship, safety reviewers | PENDING | RM-Y1-03 | 6 packs complete | RM-Y1-03 | 58 | `y1-c5-packs` | Facilitator-ready Cycle 5 |
| RM-Y1-05 | Year 1 Cycle 6 detailed authoring | 6 week detailed modules | RM-Y1-03 pattern | Curriculum Lead | Doctrinal reviewer | PENDING | RM-Y1-04 | Y1-C6 complete in backlog | RM-Y1-03 | 59 | `y1-c6-detailed` | Year 1 detailed source complete (40 weeks) |
| RM-Y1-06 | Year 1 Cycle 6 derivative packs | 6 weekly folders | RM-Y1-05 | Curriculum Lead | Worship, safety reviewers | PENDING | RM-Y1-05 | 6 packs complete; Year 1 all derivative complete | RM-Y1-05 | 60 | `y1-c6-packs` | Full Year 1 library public |

---

## 16. Year 2 production

**Backlog weeks:** `Y2-C1-W1` … `Y2-C6-W6` (40 active weeks)  
**Emphasis per architecture:** abhidheya; Bhagavad-gītā thematic survey  
**Target library path:** `11-weekly-program-library/year-2/`

| Phase ID | Outcome | Deliverables | Source dependency | Owner role | Reviewers | Status | Prerequisites | Exit criteria | Blocked-by | Target sequence | Git milestone | Publication consequence |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| RM-Y2-01 | Year 2 production plan and source map | Updated `SOURCE-COVERAGE-MAP.md`, cycle outlines in architecture folder | `THREE-YEAR-CURRICULUM-ARCHITECTURE.md` Year 2 section | Curriculum Lead | Doctrinal reviewer, Program Director | PENDING | RM-Y1-06 | Plan approved; backlog rows unchanged from architecture-approved | RM-Y1-06 | 61 | `y2-plan` | Public visibility of Year 2 scope |
| RM-Y2-02 | Year 2 Cycles 1–2 detailed (12 weeks) | 12 detailed week modules | RM-Y2-01 | Curriculum Lead | Doctrinal reviewer | PENDING | RM-Y2-01 | Y2-C1, Y2-C2 detailed complete | RM-Y2-01 | 62 | `y2-c1-c2-detailed` | 12 weeks drafted |
| RM-Y2-03 | Year 2 Cycles 1–2 derivative packs | 12 weekly folders | RM-Y2-02 | Curriculum Lead | Worship, safety reviewers | PENDING | RM-Y2-02 | 12 packs complete | RM-Y2-02 | 63 | `y2-c1-c2-packs` | Facilitator-ready first half Year 2 |
| RM-Y2-04 | Year 2 Cycles 3–4 detailed (12 weeks) | 12 detailed modules | RM-Y2-02 pattern | Curriculum Lead | Doctrinal reviewer | PENDING | RM-Y2-03 | Y2-C3, Y2-C4 detailed complete | RM-Y2-02 | 64 | `y2-c3-c4-detailed` | 24 cumulative Year 2 weeks |
| RM-Y2-05 | Year 2 Cycles 3–4 derivative packs | 12 weekly folders | RM-Y2-04 | Curriculum Lead | Worship, safety reviewers | PENDING | RM-Y2-04 | 12 packs complete | RM-Y2-04 | 65 | `y2-c3-c4-packs` | Mid Year 2 facilitable |
| RM-Y2-06 | Year 2 Cycles 5–6 detailed (12 weeks) | 12 detailed modules | RM-Y2-04 pattern | Curriculum Lead | Doctrinal reviewer | PENDING | RM-Y2-05 | Y2-C5, Y2-C6 detailed complete | RM-Y2-04 | 66 | `y2-c5-c6-detailed` | Year 2 detailed complete |
| RM-Y2-07 | Year 2 Cycles 5–6 derivative packs | 12 weekly folders | RM-Y2-06 | Curriculum Lead | Worship, safety reviewers | PENDING | RM-Y2-06 | 40/40 Year 2 packs complete | RM-Y2-06 | 67 | `y2-complete` | Full Year 2 library public |

---

## 17. Year 3 production

**Backlog weeks:** `Y3-C1-W1` … `Y3-C6-W6` (40 active weeks)  
**Emphasis per architecture:** śāstric readiness, service ethics, bounded leadership  
**Target library path:** `11-weekly-program-library/year-3/`

| Phase ID | Outcome | Deliverables | Source dependency | Owner role | Reviewers | Status | Prerequisites | Exit criteria | Blocked-by | Target sequence | Git milestone | Publication consequence |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| RM-Y3-01 | Year 3 production plan | Updated coverage map + cycle outlines | Architecture Year 3 section | Curriculum Lead | Doctrinal reviewer, Program Director | PENDING | RM-Y2-07 | Plan approved | RM-Y2-07 | 68 | `y3-plan` | Public Year 3 scope |
| RM-Y3-02 | Year 3 Cycles 1–2 detailed (12 weeks) | 12 detailed modules | RM-Y3-01 | Curriculum Lead | Doctrinal reviewer | PENDING | RM-Y3-01 | Y3-C1, Y3-C2 detailed complete | RM-Y3-01 | 69 | `y3-c1-c2-detailed` | 12 weeks drafted |
| RM-Y3-03 | Year 3 Cycles 1–2 derivative packs | 12 weekly folders | RM-Y3-02 | Curriculum Lead | Worship, safety reviewers | PENDING | RM-Y3-02 | 12 packs complete | RM-Y3-02 | 70 | `y3-c1-c2-packs` | Facilitator-ready first half Year 3 |
| RM-Y3-04 | Year 3 Cycles 3–4 detailed (12 weeks) | 12 detailed modules | RM-Y3-02 pattern | Curriculum Lead | Doctrinal reviewer | PENDING | RM-Y3-03 | Y3-C3, Y3-C4 detailed complete | RM-Y3-02 | 71 | `y3-c3-c4-detailed` | 24 cumulative Year 3 weeks |
| RM-Y3-05 | Year 3 Cycles 3–4 derivative packs | 12 weekly folders | RM-Y3-04 | Curriculum Lead | Worship, safety reviewers | PENDING | RM-Y3-04 | 12 packs complete | RM-Y3-04 | 72 | `y3-c3-c4-packs` | Mid Year 3 facilitable |
| RM-Y3-06 | Year 3 Cycles 5–6 detailed (12 weeks) | 12 detailed modules | RM-Y3-04 pattern | Curriculum Lead | Doctrinal reviewer | PENDING | RM-Y3-05 | Y3-C5, Y3-C6 detailed complete | RM-Y3-04 | 73 | `y3-c5-c6-detailed` | Year 3 detailed complete |
| RM-Y3-07 | Year 3 Cycles 5–6 derivative packs | 12 weekly folders | RM-Y3-06 | Curriculum Lead | Worship, safety reviewers | PENDING | RM-Y3-06 | 40/40 Year 3 packs; **120/120** active weeks in backlog complete | RM-Y3-06 | 74 | `y3-complete` | Full three-year library public |

---

## 18. Deferred digital publishing

Workstream 9 (`09-digital-repository-publishing/`) defines repository/drive/website/digital-library policy. **Application and website implementation remain out of scope** per README and AGENTS.md. Controlled regeneration and export live under `18-published-exports/` and scripts.

| Phase ID | Outcome | Deliverables | Source dependency | Owner role | Reviewers | Status | Prerequisites | Exit criteria | Blocked-by | Target sequence | Git milestone | Publication consequence |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| RM-PUB-01 | Export policy and folder convention | `18-published-exports/README.md` checklist; subfolder convention documented | RM-WS9-03 (preferred) or interim policy from master model | Publishing Lead | Digital Lead | PENDING | RM-RIGHTS-05; RM-FAM-06 (for family exports) | Export types and approval gates defined | RM-WS9-01 (for full digital policy) | 75 | `export-policy` | No uncontrolled DOCX/PDF drops |
| RM-PUB-02 | DOCX regeneration script (controlled) | `scripts/` regeneration capability; evidence in `build-evidence/` | Canonical MD sources | Repository Maintainer | Canonical Editor | PENDING | RM-PUB-01 | Regenerate from MD without manual drift; documented in README | — | 76 | `docx-regen` | Optional offline formats for facilitators |
| RM-PUB-03 | First approved export bundle | Versioned export under `18-published-exports/` (e.g. Cycle 1 family pack) | RM-FAM-06, RM-PILOT-05 | Publishing Lead | Program Director, Rights reviewer | PENDING | RM-PUB-01, RM-FAM-06 | Bundle manifest with source IDs and hashes | RM-FAM-06 | 77 | `export-bundle-v1` | Off-repo distribution allowed for approved bundle |
| RM-PUB-04 | Website/digital library (explicit deferral) | Decision record: remain repo-first; no app/website in this repository | RM-WS9-04 | Digital Lead | Program Director | PENDING | RM-WS9-04 | Deferral documented; external project reference if any | Product decision external | 78 | `digital-website-deferred` | Public repo remains source of truth |

---

## 19. Definition of done

A roadmap phase is **done** when all of the following hold:

| Criterion | Verification |
|---|---|
| Deliverables exist at stated paths | File tree + `build-evidence/REPOSITORY-TREE.txt` or phase exit checklist |
| Source linkage | `source_id` / `source_hash` frontmatter where canonical MD; manifest updated for new originals |
| Review gates | Applicable `review-status.yaml` or `REVIEW-QUEUE.md` items closed with named reviewer |
| Validation | `powershell -File scripts/Validate-KutumbaRepository.ps1` → PASS after substantive changes |
| Status honesty | No `COMPLETE` without exit criteria; gaps use `SOURCE NOT YET SUPPLIED` or `DRAFT REQUIRED` |
| CURRENT-STATUS | `CURRENT-STATUS.md` updated at phase boundary per AGENTS.md |
| Publication labels | Family-facing items not marked published until RM-FAM-06; worship/safeguarding approved |
| No prohibited content | `build-evidence/PRIVACY-AND-RIGHTS-SCAN.md` clean; no private participant data |

### Repository-level definition of done (unconditional GO)

| Criterion | Phase dependency |
|---|---|
| All supplied workstreams canonical | RM-FND-03, RM-WS9-04, RM-SETU-05 |
| 120/120 active weeks produced | RM-Y3-07 |
| Worship review closed | RM-WOR-04 |
| Safeguarding review closed | RM-SAFE-04 |
| Rights disposition for legacy | RM-RIGHTS-02, RM-RIGHTS-03 |
| Independent audit conditions cleared | RM-BASE + remediation of F-001 … F-003 in `INDEPENDENT-REPOSITORY-AUDIT.md` |
| Validation PASS | RM-FND-08 ongoing |

---

## 20. Risks, dependencies and decision gates

### 20.1 Risk register

| Risk ID | Risk | Affected paths | Mitigation | Owner |
|---|---|---|---|---|
| RK-01 | Public repo exposes review-incomplete worship/safeguarding content | `07-kirtana-worship-bhakti-labs/`, weekly `children/` | `review-status.yaml` flags; RM-WOR-*, RM-SAFE-*; README status vocabulary | Worship Lead, Children Formation Lead |
| RK-02 | Workstream 9 never supplied | `09-digital-repository-publishing/` | Honest GAP-RECORD; RM-WS9-01 blocked; interim policy from master model | Digital Lead |
| RK-03 | Setu draft delayed blocks pilot newcomers | `10-kutumba-setu/`, newcomer-adaptation tables | RM-SETU-02 priority; parent model observer rules | Setu Lead |
| RK-04 | Legacy material accidental adoption | `14-research-source-register/` | reference-only default; RM-RIGHTS-02; `LEGACY-ADOPTION-REVIEW.md` | Research Lead |
| RK-05 | Policy drift (public vs private wording) | `SECURITY-PRIVACY.md`, `CURRENT-STATUS.md`, audit F-001 | Align docs with intentional public visibility | Repository Maintainer |
| RK-06 | Three-year production scope creep | `02-curriculum-architecture/` | 120-week backlog; no fabrication; sequence 55–74 | Curriculum Lead |
| RK-07 | Unlicensed export of third-party material | `18-published-exports/`, `RIGHTS-AND-USE.md` | RM-RIGHTS-05 before RM-PUB-03 | Publishing Lead |

### 20.2 Dependency graph (summary)

```text
RM-BASE → RM-WOR-*, RM-SAFE-*, RM-RIGHTS-*
RM-FSM-02 → RM-FAC-*, RM-PILOT-01 → RM-PILOT-02
RM-WOR-03 + RM-SAFE-03 → RM-FAM-02 … RM-FAM-06 → RM-PUB-03
RM-WS9-01 → RM-WS9-04 → RM-PUB-04
RM-SETU-02 → RM-PILOT-03
RM-Y1-06 → RM-Y2-* → RM-Y3-*
```

### 20.3 Decision gates (human)

| Gate ID | Decision | Approver roles | Blocks |
|---|---|---|---|
| DG-01 | Worship content approved for facilitation and publication | Worship Lead, Temple Liaison | RM-WOR-04, RM-FAM-02, RM-FAM-04, RM-FAM-05 |
| DG-02 | Safeguarding content approved | Children Formation Lead, Program Director | RM-SAFE-04, RM-FAM-03, RM-FAM-05 |
| DG-03 | Legacy reference adoption (any file) | Research Lead, Rights reviewer, Doctrinal reviewer | Bulk import, RM-RIGHTS-02 |
| DG-04 | Family-facing publication | Publishing Lead, Program Director | RM-FAM-06, RM-PUB-03 |
| DG-05 | Founding pilot launch | Core Team, Temple Liaison per charter | RM-PILOT-04 |
| DG-06 | Workstream 9 source acceptance | Digital Lead, Program Director | RM-WS9-01 |
| DG-07 | Setu canonical approval | Setu Lead, Program Director, Worship Lead (if applicable) | RM-SETU-05, RM-PILOT-03 |
| DG-08 | Year N curriculum plan approval | Curriculum Lead, Doctrinal reviewer, Program Director | RM-Y2-01, RM-Y3-01 |

### 20.4 Sequence overview

| Sequence band | Focus | Representative phases |
|---|---|---|
| 0–9 | Foundation (complete) | RM-FND-01 … RM-FND-09 |
| 10–22 | Gap closure, FSM hardening | RM-PROD-OVERVIEW, RM-FSM-04 … RM-FSM-05 |
| 11–19 | Workstream 9 + Setu | RM-WS9-*, RM-SETU-* |
| 23–34 | Worship, safeguarding, rights | RM-WOR-*, RM-SAFE-*, RM-RIGHTS-* |
| 35–45 | Family + facilitator publication prep | RM-FAM-*, RM-FAC-* |
| 46–54 | Pilot + cycle review | RM-PILOT-*, RM-CYCLE-* |
| 55–74 | Year 1–3 curriculum production | RM-Y1-* … RM-Y3-* |
| 75–78 | Deferred digital publishing | RM-PUB-* |

---

## Maintenance

- Update this roadmap when phases close; set **Status** to `COMPLETE` only when **Exit criteria** are met.
- Record phase boundaries in [CURRENT-STATUS.md](CURRENT-STATUS.md).
- Re-run validation before git push: `powershell -File scripts/Validate-KutumbaRepository.ps1`.
- Production work should use prompts in `16-prompt-library/` rather than ad-hoc fabrication.

**Document control:** Roadmap version aligned to baseline `0c08d04`. No calendar targets are set in this document.
