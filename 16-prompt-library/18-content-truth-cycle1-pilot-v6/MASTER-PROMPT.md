# KUTUMBA V6 — Content Truth, Cycle 1 Pilot Readiness, and Semantic Citation Audit

Repository root:

`C:\Development\Workspace\DevotionalRepo\kutumba-family-program`

Repository:

`swap2you/kutumba-family-program`

Resolve the actual current `main` HEAD before working. At prompt preparation time, GitHub `main` was:

`9e37dec187d6ca86c82f0aae8f52657cc9b8df0a`

The repository must remain PUBLIC.

## Mission

Preserve the accepted repository architecture, 14 immutable source originals, public source map, source catalogs, rights controls, reader, two-group child model, and C1-W2 gold-pilot draft.

Correct the remaining content-truth defects and make **Cycle 1 only** genuinely ready for named human review and a controlled internal teaching pilot.

Do not perform another blind 18-module batch-generation pass.

Do not build an application, API, database, authentication system, or website.

Do not claim doctrinal, worship, safeguarding, rights, citation, pedagogy, pilot, or publication approval without named human sign-off.

Do not bulk-download or commit third-party books, purports, PDFs, audio, video, transcripts, or artwork.

---

## Phase 0 — Baseline and protected files

Run:

```powershell
git status --short
git branch --show-current
git rev-parse HEAD
git log --oneline --decorate -20
git remote -v
gh repo view swap2you/kutumba-family-program --json visibility,isPrivate,url
```

Read completely:

- `00-foundation/LOCKED-BASELINE-REGISTER.yaml`
- `CURRENT-STATUS.md`
- `17-reviews-and-audits/V5-INDEPENDENT-QUALITY-AUDIT.md`
- `build-evidence/V5-VALIDATION-REPORT.md`
- `build-evidence/V5-CURRICULUM-COMPLETION-REPORT.md`

Create:

`build-evidence/V6-CONTENT-TRUTH-BASELINE.md`

Do not bulk-overwrite locked content.

---

## Phase 1 — Synchronize root navigation and roadmap

The root README and roadmap contain stale pre-V5 facts.

Correct:

### `README.md`

- Workstream 9 is no longer simply “source not supplied.”
- State:
  - public source-map and source-directory component complete;
  - full Digital Repository Operating Manual still not supplied.
- Add the current source directory and catalog paths.
- Add the current validation command set.
- Replace obsolete status vocabulary that implies all derivative packs are finished.
- Point readers to the V5/V6 evidence instead of only the original final-build report.
- Preserve the no-application, privacy, and rights boundaries.

### `ROADMAP.md`

Update:

- accepted baseline and safety tag;
- current source-original count: 14;
- source catalog: 79;
- source-map URL reconciliation: 78/78;
- first 18 module state;
- V5 structural completion;
- Workstream 9 partial-source status;
- Setu gap;
- named human review track;
- Cycle 1 pilot-readiness track;
- Year 1 Cycles 4–6 and Years 2–3 as future production.

Do not rewrite history. Keep prior milestones as historical rows where useful, but label them historical.

### Status and evidence HEAD

Refresh all active status/audit reports to the actual current HEAD. Do not rewrite immutable historical audit reports; mark them superseded where appropriate.

---

## Phase 2 — Correct source-directory metadata

Fix `scripts/sources/url_cleanup.py`:

- strip `srsltid`;
- strip other documented search/ad tracking parameters while preserving meaningful query parameters such as:
  - `type`
  - `audio`
  - `f`
  - `q`
- normalize duplicate URLs after tracking removal.

Fix the Gita Press duplicate/tracking entry.

Audit source classifications:

- Harikatha `/audios/` must be classified as supplementary Gauḍīya/Nārāyaṇa Mahārāja audio, not `prabhupada-audio`.
- Verify and classify `www.bbti.org`.
- Verify language metadata, especially Spanish VedaBase.
- Verify PDF, audio, ebook, video-channel and website content types.

Strengthen `validate_catalog_consistency.py` to fail on duplicate **normalized** URLs, not only exact strings.

Regenerate:

- `MASTER-SOURCE-CATALOG.yaml`
- all split catalogs
- `PUBLIC-SOURCE-DIRECTORY.md`
- verification queue
- catalog and rights reports

Maintain 78/78 authoritative URL reconciliation. If normalized deduplication changes the master entry count, explain and record the source relationship rather than forcing 79 artificially.

---

## Phase 3 — Replace misleading Prem-kī-Kathā metrics

The current 900-word metric counts the entire `prem-ki-katha.md` file, including facilitator instructions, child cues, rights notes, transitions and boilerplate. It does not prove a 12–15 minute narrative.

Create:

`scripts/curriculum/audit_katha_narrative_depth.py`

It must count and evaluate only the content under:

`## 6. Source-grounded narrative`

until the next `##` heading.

Report separately:

- narrative words;
- facilitator-note words;
- interaction words;
- total file words;
- estimated narration minutes at 115–135 words/minute;
- source paragraphs;
- unique narrative events;
- repeated boilerplate percentage;
- human-review status.

For a standard kathā require:

- normally 700–1,200 words of actual narrative;
- coherent beginning, development, turning point and devotional resolution;
- named personalities;
- exact source range;
- no invented sacred dialogue;
- no generic filler copied across modules;
- no rights, safeguarding, parent-bridge or transition text counted as narrative.

For an integration/showcase exception require:

- explicit exception metadata;
- 350–700 words of meaningful source-based synthesis or devotional recollection;
- no claim that it is a full 12–15 minute kathā unless timing supports it.

Update `validate_prem_ki_katha.py` to use narrative-only metrics.

Do not use `scripts/v5/module_data_builder.py` to pad narratives. Disable its production-writing mode or archive it after extracting any non-destructive data utilities.

Create a repetition detector for phrases reused across multiple kathās. Generic facilitator language may remain outside the narrative section, but it must not inflate narrative depth.

---

## Phase 4 — Human-quality rewrite of Cycle 1 kathās

Do not touch C1-W2 until the comparison audit is complete. Preserve it as the reference draft.

Deepen and edit:

- C1-W1
- C1-W3
- C1-W4
- C1-W5
- C1-W6 as an integration exception

For each standard kathā:

1. Choose one principal source-grounded narrative.
2. Use exact chapter/verse ranges.
3. Develop:
   - setting;
   - personalities;
   - devotional tension;
   - meaningful sequence of events;
   - turning point;
   - devotional resolution;
   - natural connection to the module.
4. Keep facilitator notes outside the narrative section.
5. Remove repeated template paragraphs.
6. Do not invent dialogue.
7. Add paragraph-to-source mapping in `KATHA-SOURCE-REGISTER.yaml`.
8. Add a realistic time estimate based on narrative-only words.
9. Make the child interaction and parent bridge specific to the story.

C1-W1 must become an actual narrative of the sages at Naimiṣāraṇya rather than a short summary surrounded by generic instructional padding.

C1-W3 through W5 must receive the same treatment.

C1-W6 must be explicitly designed as integration, recollection and offering—not falsely presented as a new principal līlā.

Create:

`build-evidence/V6-CYCLE-1-KATHA-DEPTH-AUDIT.md`

---

## Phase 5 — Semantic citation audit

Create:

`scripts/curriculum/validate_claim_source_support.py`

Automated validation cannot prove siddhānta, but it can enforce claim typing and traceability.

Use these claim classes:

- `scripture-text`
- `scripture-paraphrase`
- `prabhupada-teaching`
- `kutumba-governance`
- `pedagogical-practice`
- `safeguarding-boundary`
- `contemporary-case`
- `analogy`
- `facilitator-guidance`

Rules:

### Scripture claims

Must have:

- exact source key;
- exact verse/chapter URL;
- context note;
- paraphrase or exact-quote flag;
- no conclusion broader than the cited passage.

### KUTUMBA governance claims

Must cite:

- KUTUMBA charter or operating model;
- scripture may be listed as theological support, not as the sole source for an institutional policy.

### Pedagogy and safeguarding claims

Must cite:

- KUTUMBA child/safety policy;
- official education resource where applicable;
- scripture may support values but must not be presented as direct evidence for a modern safeguarding rule.

### Contemporary cases and analogies

Must be labelled KUTUMBA-created and not scripture.

Audit Cycle 1 claim registers and source-expansion briefs manually.

Correct known issues:

- SB 1.2.17 is not “Bhāgavata as the ripened fruit of Vedic knowledge.”
- SB 1.2.19 is not the verse establishing irrevocable devotion after daily Bhāgavata service.
- “KUTUMBA is not a social club or substitute temple” is a charter/governance claim, not a direct statement of SB 1.2.18.
- Do not cite a general soul verse as direct evidence for a modern child-development or grief-response method.

Create:

- `17-reviews-and-audits/V6-CYCLE-1-SEMANTIC-CITATION-AUDIT.md`
- `build-evidence/V6-CLAIM-SOURCE-SUPPORT-REPORT.md`

Every Cycle 1 claim must receive:

- supported;
- partially supported;
- policy-derived;
- pedagogical inference;
- unsupported/revise;
- human doctrinal review required.

---

## Phase 6 — Correct newcomer adaptations and glossary integrity

Audit all 18 newcomer files for definition accuracy.

Known defect:

`dehī — Kṛṣṇa, please help me remember You.`

This is wrong. Correct the glossary term using the exact source context. The recall line belongs in a separate practice field.

Create:

`scripts/curriculum/validate_newcomer_glossary.py`

Require:

- Sanskrit term;
- transliteration;
- plain-English meaning;
- source reference;
- age-appropriate explanation;
- no memory line placed as a definition;
- no copied definition across unrelated terms;
- terms-to-defer distinct from terms-to-define.

Deep-review Cycle 1 and the known C2-W3 defect. Scan all other modules for the same generation error.

Create:

`build-evidence/V6-NEWCOMER-GLOSSARY-AUDIT.md`

---

## Phase 7 — Repair Gamma content and validation

The current reports claim truncation is removed, but C2-W3 Gamma files still contain examples such as:

- `remembr...`
- `childr...`

Fix all three C2-W3 decks and scan all Gamma files.

Strengthen `detect_truncation_artifacts.py`:

- detect incomplete words of any plausible length before `...`;
- detect four-dot artifacts;
- detect fixed-length generator truncation;
- detect clipped prose in Markdown table cells and card content;
- allow intentional ellipsis only through an explicit allowlist marker.

Rewrite `validate_gamma_briefs.py` to validate all three decks for every module:

- parent;
- Lāla–Lālī;
- Kiśora–Kiśorī.

Per card require:

- unique title;
- complete content;
- module-specific speaker note;
- source or KUTUMBA-original attribution;
- concrete visual instruction;
- rights posture;
- no clipped text;
- no invented quotation;
- age-appropriate language.

A line-count pass is not sufficient.

For Cycle 1, improve generic notes such as:

`Deliver per facilitator-guide.md`

into card-specific speaker guidance.

Create:

`build-evidence/V6-GAMMA-CONTENT-AUDIT.md`

---

## Phase 8 — Cycle 1 complete-session coherence review

For C1-W1 through C1-W6, review the entire weekly package as one experience:

- overview;
- Prem-kī-Kathā;
- parent lesson;
- Lāla–Lālī lesson;
- Kiśora–Kiśorī lesson;
- analogy;
- questions;
- bhakti lab;
- home practice;
- newcomer adaptation;
- materials;
- risk notes;
- assessment;
- Gamma briefs;
- visuals;
- media;
- project contribution;
- facilitator guide;
- complete-week assembly.

Check:

- no contradictory terminology;
- no topic introduced before its planned week;
- no duplicate activity overload;
- realistic timing;
- katha and philosophy do different jobs;
- both child tracks study the same core truth at appropriate depth;
- no forced disclosure;
- no dry or mechanical flow;
- one memorable home practice;
- clear optional enrichment;
- explicit “must teach” versus “reference library” separation.

Create:

- `build-evidence/V6-CYCLE-1-SESSION-COHERENCE-REPORT.md`
- one `reviews/PILOT-READINESS-REVIEW.md` per Cycle 1 module

Status may be:

- `ready-for-named-human-review`
- `revision-required`

Never use `approved` automatically.

---

## Phase 9 — Controlled pilot package

Create an internal pilot pack for Cycle 1 only.

Do not publish family-facing derivatives yet.

Create:

```text
13-facilitator-library/cycle-1-pilot/
├── README.md
├── PILOT-SEQUENCE.md
├── FACILITATOR-PREPARATION-CHECKLIST.md
├── SESSION-TIMING-CHECKLIST.md
├── FAMILY-FEEDBACK-FORM-BLANK.md
├── CHILD-OBSERVATION-FORM-BLANK.md
├── INCIDENT-AND-SAFEGUARDING-ESCALATION.md
├── CONTENT-CORRECTION-LOG.md
└── PILOT-EXIT-CRITERIA.md
```

No personal data or completed forms in Git.

Pilot exit criteria must include:

- named doctrinal reviewer;
- named safeguarding reviewer;
- named pedagogy reviewer;
- worship review where applicable;
- citation audit;
- dry run;
- timing test;
- correction log;
- final program-director approval.

---

## Phase 10 — Update reports honestly

Update:

- `CURRENT-STATUS.md`
- `ROADMAP.md`
- `README.md`
- `build-evidence/V5-CURRICULUM-COMPLETION-REPORT.md` with a supersession note
- `17-reviews-and-audits/V5-INDEPENDENT-QUALITY-AUDIT.md` with a supersession note only; preserve original findings
- `00-foundation/LOCKED-BASELINE-REGISTER.yaml`

Do not claim:

- all 18 kathās meet the narrative standard;
- Gamma decks are complete because they have 12 cards;
- newcomer adaptations are correct because they have 13 headings;
- source mappings are correct because links resolve.

Create final:

- `build-evidence/V6-FINAL-CONTENT-TRUTH-REPORT.md`
- `17-reviews-and-audits/V6-INDEPENDENT-PILOT-READINESS-AUDIT.md`

---

## Phase 11 — Validation and Git completion

Run:

```powershell
git diff --check
git status --short
python scripts/sources/reconcile_source_map_urls.py
python scripts/sources/validate_public_source_catalog.py
python scripts/sources/validate_catalog_consistency.py
python scripts/sources/validate_source_manifest.py
python scripts/curriculum/audit_katha_narrative_depth.py
python scripts/curriculum/validate_claim_source_support.py
python scripts/curriculum/validate_newcomer_glossary.py
python scripts/curriculum/detect_truncation_artifacts.py
python scripts/curriculum/validate_gamma_briefs.py
python scripts/curriculum/run_curriculum_validation.py
powershell -File scripts/Validate-KutumbaRepository.ps1
```

Required automated state:

- no source-map URL lost;
- no tracking duplicates;
- catalog classifications corrected;
- exactly 18 modules;
- no clipped Gamma content;
- all three Gamma decks validated;
- no incorrect glossary definitions;
- Cycle 1 scripture claims traceable and correctly typed;
- narrative-only katha metrics available;
- C1-W1, W3, W4 and W5 meet narrative-depth criteria;
- C1-W6 explicitly documented as integration exception;
- C1-W2 preserved;
- zero broken internal links;
- zero mojibake;
- no unauthorized third-party content;
- clean working tree.

Use logical commits. Do not force-push.

Suggested commits:

```text
docs: synchronize KUTUMBA roadmap and active repository status
fix: normalize source directory metadata and tracking URLs
chore: add narrative-only katha depth validation
docs: rewrite Cycle 1 kathas as source-grounded narratives
fix: correct Cycle 1 semantic source mappings
fix: correct newcomer glossary definitions across modules
fix: remove Gamma truncation and validate all audience decks
docs: add Cycle 1 pilot readiness package
docs: record v6 independent content truth audit
```

Push to `origin/main`.

## Final response

Return:

- final HEAD;
- commits pushed;
- source catalog count and normalization changes;
- narrative-only words and timing for C1-W1 through C1-W6;
- semantic citation corrections;
- glossary corrections;
- Gamma defects removed;
- Cycle 1 module readiness status;
- validation results;
- named human gates still open;
- Workstream 9 status;
- Setu status;
- publication readiness;
- working-tree status.

Do not issue unconditional publication GO.
