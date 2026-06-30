# KUTUMBA Curriculum Quality Remediation v4

Repository root:

`C:\Development\Workspace\DevotionalRepo\kutumba-family-program`

Repository:

`swap2you/kutumba-family-program`

Current public baseline:

`acf3edbc6eef7d6a9b04e743e0437fafe96bbad1`

## Purpose

Correct the remaining content-integrity, source-mapping, status, encoding, Prem-kī-Kathā, Gamma, newcomer, and validation defects discovered after the post-audit enhancement.

This is a documentation and curriculum-quality task. Do not build an application, API, database, authentication system, or custom website.

Do not change the repository from public.

Do not claim doctrinal, worship, safeguarding, rights, citation, pedagogy, or publication approval without named human sign-off.

---

## Phase 0 — Baseline and safety

Run and record:

```powershell
git status --short
git branch --show-current
git rev-parse HEAD
git log --oneline --decorate -20
git remote -v
gh repo view swap2you/kutumba-family-program --json visibility,isPrivate,url
python scripts/curriculum/run_curriculum_validation.py
powershell -File scripts/Validate-KutumbaRepository.ps1
```

Create:

`build-evidence/V4-QUALITY-REMEDIATION-BASELINE.md`

Preserve all existing source documents, audit evidence, and commit history.

---

## Phase 1 — Correct status truthfulness

The repository currently contains contradictory status claims:

- `CURRENT-STATUS.md` says 18 authentic Prem-kī-Kathā.
- `CURRICULUM-STATUS-SNAPSHOT.md` says 13 authentic at 600+ words.
- `WEEK-QUALITY-DASHBOARD.md` says C1-W1 and C1-W3 through C1-W6 are partial.
- `EMPTY-AND-THIN-SECTIONS.csv` says 17 modules still have thin `newcomer-adaptation.md`.
- Reader Home defines `enhancement-complete` as gold-standard depth even where modules do not meet the stated Prem-kī-Kathā standard.

Correct the vocabulary.

Use separate fields:

- `structural_pack_complete`
- `automated_enhancement_complete`
- `source_audit_complete`
- `prem_katha_depth`
- `human_review_complete`
- `publication_ready`

Do not use `enhancement-complete` to mean human-approved or gold-standard unless the module meets every defined gate.

Recommended honest statuses:

- C1-W2: `gold-pilot-draft`
- Modules meeting full automated content standard: `deepened-draft`
- Modules with partial kathā or thin required files: `remediation-required`
- All modules: `human-review-required`
- Publication: `not-ready`

Update:

- `CURRENT-STATUS.md`
- `KUTUMBA-READER-HOME.md`
- `build-evidence/CURRICULUM-STATUS-SNAPSHOT.md`
- `build-evidence/CYCLE-COVERAGE-REPORT.md`
- `build-evidence/FIRST-SIX-MONTH-CONTENT-AUDIT.md`
- `build-evidence/FINAL-POST-AUDIT-REPORT.md`
- all affected `review-status.yaml` files

Restore explicit open-gap tracking:

- Workstream 9 — source document not yet supplied
- KUTUMBA Setu — operating package not yet approved

---

## Phase 2 — Fix encoding and link validation

The current repository report lists 53 sampled broken links using mojibake paths such as:

- `mÄyÄ`
- `ká¹›á¹£á¹‡a`
- `sÄdhu`
- `Å›Ästra`
- `Å›rÄ«`
- `kÄ«rtana`

The linked Unicode files exist. The PowerShell validator is reading Markdown without explicit UTF-8 handling.

Update `scripts/Validate-KutumbaRepository.ps1`:

1. Read all Markdown using `-Encoding UTF8`.
2. Normalize both source link and filesystem paths to Unicode Normalization Form C before comparison.
3. Use `Resolve-Path -LiteralPath` safely.
4. Distinguish:
   - actual broken link
   - Unicode decoding failure
   - unsupported link syntax
5. Fail on actual broken internal links.
6. Do not report mojibake as a broken link.
7. Write the complete broken-link list to a CSV, not only the first 15.
8. Remove UTF-8 BOM artifacts where generated reports show `â€”`.

Update `check_external_links.py`:

- do not return PASS when failures are present;
- distinguish VedaBase `HEAD` rejection/403 from an invalid URL;
- retry with a safe GET request where appropriate;
- make its result part of the orchestrator verdict;
- record every checked URL and status;
- do not silently ignore its return code in `run_curriculum_validation.py`.

Rerun validation until internal-link warnings are zero.

---

## Phase 3 — Remove automated false “gold” promotion

The current `sync_gold_review_status.py` marks a module gold using only:

- Gamma parent deck line count
- dossier line count
- claim count
- child lesson line counts
- existence of a katha register

It then marks unrelated fields such as newcomer adaptation, materials, Prem-kī-Kathā, source registry, and semantic validation complete without checking them individually.

Replace this behavior.

Create a field-by-field evaluator. Each status must be derived from the corresponding file and validator.

A module may be promoted only when:

- no required file is thin;
- no truncation artifact exists;
- the full source registry parses;
- source references support the claims they are assigned to;
- claim register entries resolve to valid source keys;
- both child tracks pass pedagogical checks;
- newcomer adaptation is module-specific and substantive;
- Gamma parent, Lāla–Lālī, and Kiśora–Kiśorī decks all contain complete card content;
- Prem-kī-Kathā meets the approved standard or a documented exception;
- media index accurately states content depth;
- visual references resolve;
- review status remains human-review-required until signed.

Retire or rewrite `sync_gold_review_status.py`. Do not let it overwrite human review data.

---

## Phase 4 — Correct confirmed source and doctrinal mapping defects

### 4.1 C1-W2

`prem-ki-katha.md` uses the garment analogy, but `katha/KATHA-SOURCE-REGISTER.yaml` does not include BG 2.22.

Either:

- add BG 2.22 to the katha source register and exact-verse list; or
- remove the garment analogy from the katha block and retain it only in the later teaching section.

Keep the already-corrected BG 13.3 description and KUTUMBA attribution for driver/vehicle.

### 4.2 C2-W3 — Bhārata Mahārāja

The current narrative discusses:

- leaving kingship;
- attachment to the deer;
- remembrance at death;
- the next birth.

But the source list uses only opening verses SB 5.8.1 and SB 5.9.1, which do not by themselves support the entire narrative.

Replace the source map with exact relevant chapter/verse ranges for:

- Bhārata's devotional retirement;
- the deer incident;
- the growth of attachment;
- his consciousness at death;
- the next birth and retained remembrance.

Remove literal truncation artifacts such as:

- `b...`
- `na...`
- clipped sentences ending in `...`

Rewrite the story as a complete narration rather than a generated summary.

### 4.3 C3-W1

The current repository incorrectly identifies ŚB 10.14 as “gopīs' prayers” after Govardhana.

ŚB 10.14 is Brahmā's prayers to Lord Kṛṣṇa after the Brahmā-vimohana episode.

Do not patch only the title. Re-select the katha based on the module objective:

`Who Is God? The Supreme Enjoyer, Proprietor and Friend`

Choose one source-grounded narrative that genuinely supports BG 5.29, such as a carefully reviewed Govardhana/Indra stewardship narrative or another approved account. Map every narrative statement to the correct source range.

### 4.4 C3-W2

Rename:

`Kṛṣṇa's birth in Vṛndāvana`

to a precise title such as:

`Kṛṣṇa's appearance in Mathurā and transfer to Gokula`

Use the congregation's approved geographical terminology consistently. Do not imply that the prison appearance occurred in Vṛndāvana.

### 4.5 C3-W3

The current title and references are inaccurate:

- “How Nārada received the Bhāgavatam”
- SB 1.4.25

SB 1.4.25 concerns Vyāsadeva's compassionate compilation of the Mahābhārata, not Nārada receiving the Bhāgavatam.

Replace the katha with one coherent, accurately sourced option:

- Nārada instructs dissatisfied Vyāsadeva to directly glorify the Supreme Lord — ŚB 1.5; or
- Nārada's childhood hearing and service to the bhaktivedāntas — ŚB 1.5–1.6.

Use exact verses that support the narrative and the guru–sādhu–śāstra teaching.

### 4.6 Full 18-module source audit

For every module:

- verify each katha title;
- verify personalities;
- verify event chronology;
- verify geographic names;
- verify exact verse/chapter ranges;
- verify that each source supports its assigned teaching function;
- verify every claim register key;
- remove generic or incorrect source anchors;
- record all corrections in `17-reviews-and-audits/V4-SOURCE-CORRECTION-REGISTER.md`.

Automated link existence is not source verification.

---

## Phase 5 — Rebuild Prem-kī-Kathā to the actual standard

The governing standard says:

- 12–15 minutes narration;
- normally 900–1,500 words;
- 3–5 minutes interaction;
- source-grounded devotional narrative;
- family heart-opening function.

The current validator allows 350 words for non-pilot modules. This does not meet the standard.

Update `validate_prem_ki_katha.py`:

1. Enforce 900–1,500 words for normal teaching kathas.
2. Allow a documented exception only for:
   - integration/showcase modules;
   - explicitly approved short-katha format.
3. Check every required section in `REQUIRED_SECTIONS`, not only six of them.
4. Detect:
   - clipped fragments;
   - generated ellipses;
   - `...` after partial words;
   - generic placeholders;
   - “see narrative below” without named personalities;
   - identical turning-point paragraphs across modules;
   - identical heart reflections across modules;
   - generic child cues;
   - generic visual plans;
   - unsupported source claims.
5. Require human-review status, not false approval.
6. Require the katha register to contain all narrative sources.
7. Require source-to-paragraph mapping.

Expand and rewrite:

- C1-W1
- C1-W3
- C1-W4
- C1-W5
- C1-W6

These are currently partial.

Review and expand C2/C3 kathas where 600–850 words do not actually provide 12–15 minutes of narration.

Do not inflate word count with generic filler. Add real source-grounded narrative detail, devotional mood, and age-appropriate interaction.

---

## Phase 6 — Remove truncation and template residue everywhere

The generation scripts intentionally create clipped strings with code such as:

- `m["hook"][:200] + "..."`
- `m["lala_story"][:120] + "..."`
- `p[:100] + "..."`

Search the entire repository for sentence fragments introduced by these operations.

Audit:

- `prem-ki-katha.md`
- all Gamma prompts
- katha source registers
- story cues
- opening hooks
- research summaries
- visual descriptions

No production content may contain clipped source text.

Keep ellipses only when grammatically intentional, not as an automated truncation marker.

Create:

`scripts/curriculum/detect_truncation_artifacts.py`

It must fail on:

- a word fragment followed by `...`;
- lines ending in clipped source text;
- suspicious fixed-length excerpts;
- known generator artifacts;
- placeholder phrases such as `See narrative below` where the specific content is required.

Add it to the main validation orchestrator.

---

## Phase 7 — Complete Gamma decks honestly

Current Gamma validators check only the parent deck line count and presence of `### Card`.

Strengthen `validate_gamma_briefs.py` to validate all three decks:

- parent;
- Lāla–Lālī;
- Kiśora–Kiśorī.

Per card require:

- complete content;
- non-generic speaker note;
- source reference;
- specific visual instruction;
- no clipped text;
- no generic `[IMAGE: ... placeholder]` when a concrete original visual exists;
- rights status;
- age-appropriate language;
- no invented quotation.

Validate card count and title uniqueness.

C2-W3 currently contains clipped content in Cards 3, 5 and 6. Fix it and search for the same generator artifact in every deck.

Do not mark Gamma production-ready until all three prompts pass.

Rendered Gamma decks remain a later external production step.

---

## Phase 8 — Complete newcomer adaptations

`EMPTY-AND-THIN-SECTIONS.csv` identifies `newcomer-adaptation.md` as thin in 17 modules.

Each newcomer adaptation must be module-specific and contain:

- minimum concept;
- terms to define;
- terms to defer;
- reduced source load;
- child placement guidance;
- parent participation option;
- bhakti-lab adaptation;
- home-practice minimum;
- sensitive-topic cautions;
- host-family action;
- bridge to KUTUMBA Setu;
- follow-up path.

Do not mark newcomer adaptation complete from a generic six-row table.

---

## Phase 9 — Strengthen source and claim validation

Current source validation checks only whether “vedabase” appears and whether the matrix has enough lines.

Current claim validation mainly counts claim IDs.

Strengthen both.

### Source registry validation

Require:

- valid YAML;
- unique source keys;
- stable URL;
- work;
- exact reference;
- teaching function;
- rights status;
- context-review status;
- source tier;
- no duplicate keys;
- no source used for a claim outside its actual content scope.

### Claim validation

Require:

- valid YAML;
- unique claim IDs;
- nonempty statement;
- valid claim type;
- every source key resolves;
- no empty source list for scriptural claims;
- exact quotation flag;
- misunderstanding risk;
- reviewer status;
- audience;
- context note;
- no boilerplate duplicate claims across unrelated modules.

Automated validation cannot determine siddhānta approval. Label its result:

`structurally traceable — human doctrinal review required`

not:

`source verified`

---

## Phase 10 — Reader and report cleanup

The reader architecture is good. Keep it.

Correct:

- Unicode link checker;
- report mojibake;
- status depth labels;
- open Workstream 9 and Setu gaps;
- exact human-review status;
- katha depth labels.

Reader Home should show:

- structural status;
- katha depth;
- source-audit status;
- human-review status;
- publication status.

Do not display all 18 modules as equivalent when they are not.

---

## Phase 11 — Independent audit and Git completion

Create:

- `build-evidence/V4-QUALITY-REMEDIATION-REPORT.md`
- `build-evidence/V4-WEEK-QUALITY-DASHBOARD.md`
- `build-evidence/V4-PREM-KI-KATHA-AUDIT.md`
- `build-evidence/V4-SOURCE-RELEVANCE-AUDIT.md`
- `build-evidence/V4-GAMMA-QUALITY-AUDIT.md`
- `build-evidence/V4-LINK-AND-ENCODING-AUDIT.md`
- `17-reviews-and-audits/V4-INDEPENDENT-REVIEW-STARTUP.md`

Run all validation.

Required automated result:

- zero actual broken internal links;
- zero mojibake warnings;
- zero truncation artifacts;
- zero false gold statuses;
- all YAML parses;
- all claim keys resolve;
- all katha source mappings are internally consistent;
- all Gamma prompts contain complete content;
- status reports agree.

Human review gates remain open.

Commit logically:

```text
fix: correct Unicode link validation and report encoding
fix: restore truthful curriculum depth statuses
fix: correct katha source mappings and doctrinal references
docs: rebuild Prem-kī-Kathā narratives to approved standard
docs: complete module-specific newcomer adaptations
docs: remove truncation artifacts from Gamma and curriculum content
chore: strengthen source claim and katha validation
docs: record v4 independent quality audit
```

Push to `origin/main`.

Do not force-push.

---

## Final response

Return:

- final HEAD;
- commits pushed;
- modules by honest depth status;
- kathas meeting 900–1,500-word standard;
- documented exceptions;
- source corrections by module;
- truncation artifacts removed;
- newcomer adaptations completed;
- Gamma decks passing;
- actual broken links;
- encoding warnings;
- source/claim validation result;
- human-review gates;
- publication readiness;
- working-tree status.

Do not issue unconditional GO.
