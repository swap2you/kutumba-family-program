# KUTUMBA Source Integrity and Curriculum Completion — Stabilization Prompt v5

Repository root:

`C:\Development\Workspace\DevotionalRepo\kutumba-family-program`

Repository:

`swap2you/kutumba-family-program`

Current expected main baseline:

`fe84ed0b374917c849e1774b3a7e3173037c5b3e`

Resolve the actual current HEAD before working. The repository must remain PUBLIC.

## Mission

Preserve and lock the repository architecture, source provenance, public source map, source-tier policy, reader, and rights boundaries that are already good. Correct the remaining manifest, catalog, reporting, Unicode, validator, curriculum-depth, media, Gamma, newcomer, and source-traceability defects without rebuilding the repository from scratch.

This is a controlled documentation and curriculum-quality pass. Do not build an application, API, database, authentication system, or custom website.

Do not claim doctrinal, worship, safeguarding, rights, citation, pedagogy, or publication approval without named human sign-off.

Do not bulk-download or commit third-party books, purports, PDFs, audio, video, transcripts, or artwork.

---

## Phase 0 — Preserve baseline and create a lock register

Run:

```powershell
git status --short
git branch --show-current
git rev-parse HEAD
git log --oneline --decorate -25
git remote -v
gh repo view swap2you/kutumba-family-program --json visibility,isPrivate,url
```

Create an annotated safety tag at the resolved HEAD if it does not already exist:

```powershell
git tag -a kutumba-source-architecture-baseline-v1.0.0 -m "KUTUMBA accepted architecture and source-map baseline"
git push origin kutumba-source-architecture-baseline-v1.0.0
```

Create:

- `00-foundation/LOCKED-BASELINE-REGISTER.yaml`
- `build-evidence/V5-STABILIZATION-BASELINE.md`

The lock register must distinguish **structural acceptance** from **human doctrinal approval**.

Lock against uncontrolled bulk regeneration:

1. repository folder architecture;
2. 14 immutable source originals and their hashes;
3. canonical operating-model documents;
4. public source-map original and canonical extraction;
5. source authority hierarchy;
6. conservative rights posture;
7. two-group child model;
8. rendered Markdown reader architecture;
9. C1-W2 as the gold-pilot draft, still human-review-required;
10. honest Workstream 9 and KUTUMBA Setu gaps.

A locked file may still receive a reviewed correction. Every correction must record reason, source, reviewer status, and before/after evidence.

---

## Phase 1 — Reconcile every source-map URL and lock the important resource document

The authoritative resource document is:

`C:\Users\swap2\Downloads\Personal\0. KUTUMBA SANGA\Public Source Map for Prabhupada and Related Sanatana Content.docx`

Repository source IDs:

- `KUT-SRC-0013` — DOCX
- `KUT-SRC-0014` — PDF companion

Confirm both hashes and paths.

Create:

`scripts/sources/reconcile_source_map_urls.py`

It must:

1. extract and normalize every URL from the authoritative DOCX and canonical Markdown;
2. compare that exact URL set with `MASTER-SOURCE-CATALOG.yaml`;
3. account for every URL as:
   - catalogued;
   - normalized redirect/alias;
   - intentionally excluded with reason;
4. fail when a source-map URL is silently missing;
5. fail when a catalog entry has no source-map provenance and no approved added-source record;
6. remove tracking parameters while preserving meaningful query parameters;
7. produce `build-evidence/SOURCE-MAP-URL-RECONCILIATION.md` and CSV evidence.

Create a user-friendly derived directory:

`09-digital-repository-publishing/PUBLIC-SOURCE-DIRECTORY.md`

Requirements:

- preserve the canonical extraction unchanged as provenance;
- list every source as a clickable Markdown link;
- group by authority tier and content type;
- show canonical/mirror/discovery/supplementary status;
- show verified/restricted/queued status;
- show default rights posture;
- link to the canonical source-map document and machine-readable catalog;
- do not reproduce third-party content.

---

## Phase 2 — Fix manifest, inventory, tree, and report metadata

Correct `00-source-materials/SOURCE-MANIFEST.yaml`:

- `current_document_count` must be 14, not 12;
- `generated` must reflect the actual regeneration time;
- entries must equal the files on disk;
- source IDs must be unique;
- hashes must match;
- KUT-SRC-0013/0014 must have complete source-group and rights metadata.

Correct `SOURCE-INVENTORY.md`:

- regenerate timestamp;
- 14/14 count;
- canonical-path status;
- source group for the DOCX/PDF pair.

Regenerate:

- `build-evidence/REPOSITORY-TREE.txt`
- `build-evidence/SOURCE-MAP-INGESTION-REPORT.md`
- `build-evidence/FINAL-SOURCE-ENRICHMENT-REPORT.md`

The repository tree must include all new source-map, catalog, education, media, prompt-library, and audit files. Do not leave the old pre-enrichment tree as current evidence.

Add validation that top-level manifest counts equal actual entry counts and on-disk counts.

---

## Phase 3 — Make one canonical source catalog and synchronize all derived catalogs

The current repository has inconsistent tier counts and verification status:

- `PUBLIC-SOURCE-CATALOG-REPORT.md` reports approximately A=35, C=20;
- independent audit reports A=42, C=13;
- MASTER catalog contains current verification results;
- split catalogs may still show `catalogued-pending-verification`.

Make `MASTER-SOURCE-CATALOG.yaml` the single canonical dataset.

Generate all split catalogs from the final in-memory master **after** verification data is applied.

Create:

`scripts/sources/validate_catalog_consistency.py`

It must verify:

- total entries = 79 unless a formally approved added-source record changes the count;
- every split entry exactly matches the corresponding master entry;
- no duplicate source IDs;
- no duplicate normalized URLs;
- tier counts agree in every report;
- status, last_verified, verification_method, rights posture, and aliases agree;
- every queue entry resolves to a master source ID;
- every master source has exactly one catalog bucket.

Fix catalog field accuracy:

- Spanish VedaBase entry must use language `es`, not hard-coded `en`;
- PDF URLs must include content type `pdf`;
- YouTube entries must include `video-channel` or `video`;
- audio archives must include `audio`;
- ebook portals must include `ebook-catalog`;
- `authentication_required` must not be blindly hard-coded when unknown;
- owners and affiliations must be evidence-based or marked `needs-verification`;
- `primary_or_secondary` must not label the supplementary tier merely as generic secondary without its supplementary classification.

Regenerate:

- all tier-split YAML files;
- `PUBLIC-SOURCE-CATALOG-REPORT.md`;
- `SOURCE-LINK-AND-RIGHTS-AUDIT.md`;
- `SOURCE-VERIFICATION-QUEUE.yaml`;
- `SOURCE-ALIAS-AND-MIRROR-MAP.yaml`.

---

## Phase 4 — Resolve the verification queue honestly

Recheck all 24 queued URLs with:

- respectful rate limiting;
- browser-compatible user agent;
- HEAD followed by limited GET where appropriate;
- redirect recording;
- timeout and DNS classification;
- manual-browser-required classification for bot-blocked sources.

Do not bypass access controls.

Classify each URL as:

- verified-available;
- verified-redirected;
- access-restricted-but-known;
- manual-browser-verification-required;
- temporarily-unreachable;
- retired-or-dead;
- replacement-source-required.

A 403/405 from an automated request must not be called dead.

Create a replacement-source recommendation for genuinely dead URLs.

---

## Phase 5 — Correct validators and eliminate misleading PASS output

### Module counting

Fix validators that print `21 modules` by counting all entries in the folder. They must count only directories matching:

`^c[1-3]-w[1-6]-`

Expected module count: exactly 18.

Fix at least:

- `validate_week_schema.py`
- `validate_prem_ki_katha.py`
- any dashboard/status generator with the same defect.

### Unicode links

Fix the PowerShell internal-link validator:

- explicit UTF-8 reads;
- Unicode Normalization Form C;
- literal-path resolution;
- zero mojibake warnings;
- actual broken links must still fail.

### Claims

`detect_unverified_claims.py` must not print warnings and still return PASS.

For C1-W1 through C1-W6:

- bind every `scripture-text` claim to valid source keys;
- fail when source keys are empty;
- ensure keys resolve to source registry entries;
- label automated result `structurally traceable — human doctrinal review required`.

### External links

`check_external_links.py` must return a meaningful categorized result. Its return code must be respected by `run_curriculum_validation.py`.

### Dangerous generation scripts

Audit one-off generators such as:

- `deepen_c1_gold_standard.py`
- `deepen_cycle2_gold_standard.py`
- `deepen_cycle3_modules.py`
- `batch_enhance_weeks.py`
- prior status-sync scripts.

Remove truncation logic and false status promotion. If a script is no longer safe or reproducible, move it to `99-archive/unsafe-or-one-time-generators/` with a warning and prevent routine execution.

No script may overwrite human-reviewed curriculum content by default.

---

## Phase 6 — Complete the source-to-module research layer

The 18 `SOURCE-EXPANSION-BRIEF.md` files currently range from useful pilot planning to generic placeholders such as broad chapter names, `no reviewed lecture entry yet`, or `none mapped yet`.

Deepen every module brief.

For each module require:

1. exact controlling book references with stable links;
2. exact Śrīla Prabhupāda lecture/conversation/letter/walk candidates;
3. date, place, title and relevant segment/timestamp when available;
4. exact kathā source ranges;
5. official education-method candidates;
6. child-resource candidates;
7. media candidates;
8. supplementary sources, only when directly relevant;
9. excluded sources with reason;
10. rights posture;
11. doctrinal, citation, pedagogy and rights review status;
12. a source-to-claim mapping table.

Do not use vague entries such as:

- `CC Ādi`
- `SB holy name themes`
- `lecture candidates`
- `see media index`

Replace them with exact references or an honest research ticket.

Update `SOURCE-TO-MODULE-MAP.yaml` from the completed briefs.

---

## Phase 7 — Complete the curriculum content gaps in cycle order

Do not regenerate all files blindly.

### 7.1 Prem-kī-Kathā

Use the approved standard:

- normally 900–1,500 substantive words;
- documented exception for integration/showcase modules;
- exact source register;
- no invented dialogue;
- devotional narrative, not only a modern hook;
- Lāla–Lālī interaction;
- Kiśora–Kiśorī reflection;
- parent bridge;
- lesson transition;
- visual/storyboard plan;
- human doctrinal review required.

Complete in this order:

1. C1-W1, C1-W3, C1-W4, C1-W5;
2. C1-W6 as a documented integration exception;
3. C2-W1 through C2-W5;
4. C2-W6 as integration exception if justified;
5. C3-W1 through C3-W5;
6. C3-W6 as showcase/integration exception if justified.

C1-W2 remains the gold-pilot draft and must not be bulk-overwritten.

### 7.2 Newcomer adaptations

Complete module-specific newcomer adaptations for all 17 non-pilot modules:

- minimum concept;
- terms to define;
- terms to defer;
- reduced source load;
- parent participation option;
- Lāla–Lālī placement;
- Kiśora–Kiśorī placement;
- laboratory adaptation;
- home-practice minimum;
- sensitive-topic caution;
- host-family action;
- KUTUMBA Setu bridge;
- follow-up path.

### 7.3 Gamma

Validate all three decks per module:

- parent;
- Lāla–Lālī;
- Kiśora–Kiśorī.

Require complete card content, speaker notes, source note, visual instruction, rights status, age suitability and no clipped text.

### 7.4 Media

The current media library is a governed architecture with only a small number of reviewed candidates. Do not call it fully populated.

For each module add reviewed metadata-first candidates where they can be verified. Otherwise retain `no-reviewed-entry-yet`.

Do not download media.

### 7.5 Education resource application

The education-resource map currently applies to only a subset of modules. Review all 18 and either:

- map an appropriate official pedagogy/activity resource; or
- record `no-relevant-official-resource-selected` with reason.

KUTUMBA adaptations remain original and source-attributed.

---

## Phase 8 — Preserve open structural gaps honestly

Do not mark Workstream 9 complete merely because the public source map is complete.

Maintain:

- Public source map and directory: complete as a governed source component;
- Full Workstream 9 Digital Repository Operating Manual: source still required;
- KUTUMBA Setu: not approved.

Create or update a detailed production brief for each gap, but do not claim final approval.

---

## Phase 9 — Independent review and accepted-baseline update

Create:

- `build-evidence/V5-SOURCE-INTEGRITY-REPORT.md`
- `build-evidence/V5-CATALOG-CONSISTENCY-REPORT.md`
- `build-evidence/V5-MODULE-SOURCE-DEPTH-REPORT.md`
- `build-evidence/V5-CURRICULUM-COMPLETION-REPORT.md`
- `build-evidence/V5-VALIDATION-REPORT.md`
- `17-reviews-and-audits/V5-INDEPENDENT-QUALITY-AUDIT.md`

The independent audit must sample every module and deeply review at least one complete module from each cycle plus all corrected high-risk modules.

Update `LOCKED-BASELINE-REGISTER.yaml` only for areas that now meet the defined acceptance criteria.

Human review gates remain OPEN until signed.

---

## Phase 10 — Git completion

Run:

```powershell
git diff --check
git status --short
python scripts/sources/reconcile_source_map_urls.py
python scripts/sources/validate_public_source_catalog.py
python scripts/sources/validate_catalog_consistency.py
python scripts/curriculum/run_curriculum_validation.py
powershell -File scripts/Validate-KutumbaRepository.ps1
```

Required automated state:

- 14 source originals and manifest count agree;
- all source-map URLs reconciled;
- one synchronized 79-entry catalog;
- tier counts agree everywhere;
- split catalogs match master;
- zero actual broken internal links;
- zero mojibake warnings;
- exactly 18 modules reported;
- no unresolved scripture claims with empty source keys;
- no truncation artifacts;
- honest curriculum depth statuses;
- no unauthorized third-party content;
- clean working tree after commit.

Use logical commits. Do not force-push.

Suggested commits:

```text
chore: lock accepted KUTUMBA architecture baseline
fix: reconcile source manifest inventory and repository evidence
fix: synchronize public source catalogs and tier counts
fix: correct Unicode links module counts and validation verdicts
docs: deepen source expansion briefs for all first-six-month modules
docs: complete source-grounded kathas and newcomer adaptations
docs: strengthen Gamma media and education mappings
chore: archive unsafe one-time generation scripts
docs: record v5 independent quality audit
```

Push to `origin/main`.

## Final response

Report:

- final HEAD;
- safety tag;
- areas locked;
- source original count;
- source-map URL reconciliation count;
- catalog entries and tier counts;
- queue outcomes;
- module source-depth status;
- kathā status;
- newcomer status;
- Gamma status;
- media status;
- education mapping status;
- validator results;
- remaining human gates;
- Workstream 9 and Setu status;
- publication readiness;
- commits pushed;
- working-tree status.

Do not issue unconditional publication GO.
