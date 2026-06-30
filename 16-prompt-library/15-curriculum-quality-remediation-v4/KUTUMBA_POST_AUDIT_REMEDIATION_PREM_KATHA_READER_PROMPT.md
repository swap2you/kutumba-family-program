# KUTUMBA Post-Audit Remediation, Prem-kī-Kathā, Reader, and Deepening Prompt

Repository root:

`C:\Development\Workspace\DevotionalRepo\kutumba-family-program`

Repository:

`swap2you/kutumba-family-program`

Current audited baseline:

- Public repository by intentional decision
- Current post-independent-audit HEAD begins at `f46910a`
- C1-W2 is the only gold-standard module
- C1-W1, C1-W3 through C3-W6 are baseline scaffolds
- Human doctrinal, worship, safeguarding, rights, citation, and pedagogy gates remain open

This is a documentation and curriculum project. Do not build an application, API, database, authentication system, or unrelated website platform.

Work autonomously through all phases below. Do not stop for routine confirmations. Do not claim approval that has not been supplied by a named human reviewer.

---

## Phase 0 — Preserve and verify the current baseline

Run:

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

`build-evidence/POST-AUDIT-REMEDIATION-BASELINE.md`

Record:

- exact HEAD
- public visibility
- dirty files
- existing validation result
- all warnings
- current module statuses
- independent-audit findings
- the exact files changed in each later phase

Do not discard local work.

---

## Phase 1 — Correct the repository’s current factual defects

### 1.1 Broken link

Fix the C1-W2 README link to:

`17-reviews-and-audits/C1-W2-GOLD-STANDARD-PILOT-AUDIT.md`

The current module-relative link is one directory level short. Verify the corrected relative path from the module folder.

Search the entire repository for the same incorrect relative-link pattern and fix all occurrences.

### 1.2 Stale status language

Update C1-W2 README:

- Automated semantic validation: PASS at current validated baseline
- Human review: still required
- Do not say validation is pending after it has run
- Do not hard-code a self-referential current commit SHA

Update all status reports that still describe the 17 baseline modules as enhancement-complete.

### 1.3 Current validation warnings

Resolve or correctly classify:

- 12 source-original hash verification warnings
- broken Markdown link warning
- any warning caused by UTF-8 BOM handling
- any stale generated HEAD value

Do not suppress warnings merely to reach zero.

For binary hashes, use a reliable binary-safe SHA-256 implementation. Verify every original against `SOURCE-MANIFEST.yaml`.

### 1.4 Source precision defects in C1-W2

Correct the C1-W2 source matrix:

- Bhagavad-gītā 13.3 does not mean “field description begins.”
- BG 13.3 introduces Kṛṣṇa as the knower in all bodies and distinguishes the individual knower from the supreme knower.
- Keep the field/individual-knower introduction tied to the correct BG 13.1–2 treatment in the selected edition.

Correct the driver-and-vehicle analogy attribution:

- The current lecture index does not substantiate the claim that the driver/vehicle analogy is a verified Śrīla Prabhupāda analogy.
- Either add an exact verified Śrīla Prabhupāda source or relabel it as a KUTUMBA pedagogical analogy.
- Never attribute an analogy to Śrīla Prabhupāda merely because it is commonly used.

Create a source-correction record:

`17-reviews-and-audits/C1-W2-SOURCE-CORRECTION-RECORD.md`

---

## Phase 2 — Build a comfortable Markdown reader

The repository already contains `.vscode/settings.json`, but users are still opening raw Markdown.

### 2.1 Update workspace settings

Use this controlled configuration:

```json
{
  "workbench.editorAssociations": {
    "*.md": "vscode.markdown.preview.editor"
  },
  "markdown.validate.enabled": true,
  "markdown.updateLinksOnFileMove.enabled": "prompt",
  "markdown.preview.scrollPreviewWithEditor": true,
  "markdown.preview.scrollEditorWithPreview": true,
  "markdown.styles": [
    ".vscode/kutumba-markdown.css"
  ]
}
```

Do not weaken Markdown preview security.

### 2.2 Add readable preview styling

Create:

`.vscode/kutumba-markdown.css`

Requirements:

- maximum readable content width approximately 1050–1150 px
- centered page
- 18 px base text
- 1.6–1.75 line height
- clear h1/h2/h3 hierarchy
- readable tables with cell padding
- visually distinct blockquotes and cautions
- good contrast in light and dark themes
- print-friendly formatting
- no external font dependency
- no JavaScript

### 2.3 Create a reader front door

Create:

`KUTUMBA-READER-HOME.md`

It must link to:

- current status
- roadmap
- master operating model
- governance
- three-year curriculum architecture
- Cycle 1, 2, and 3 landing pages
- each of the 18 module READMEs
- family library
- facilitator library
- source register
- visual gallery index
- media index
- reviews and approvals
- “what is complete / what is scaffold / what is awaiting review”

Create cycle reader pages:

- `11-weekly-program-library/first-six-months/CYCLE-1-READER.md`
- `11-weekly-program-library/first-six-months/CYCLE-2-READER.md`
- `11-weekly-program-library/first-six-months/CYCLE-3-READER.md`

Each must contain:

- cycle purpose
- module sequence
- two-minute summary per module
- direct links to parent, Lāla–Lālī, Kiśora–Kiśorī, Prem-kī-Kathā, visuals, Gamma, project, and review status
- current depth status

### 2.4 Mermaid rendering

The built-in Markdown preview renders Mermaid inside fenced `mermaid` blocks. It does not reliably render standalone `.mmd` files as a finished diagram.

For every `.mmd` visual:

- retain the `.mmd` source
- create a matching `.md` viewer containing the source in a fenced `mermaid` block
- link the rendered viewer from the module README and visual plan

Examples:

- `visuals/concept-map.md`
- `visuals/process-flow.md`

Where Mermaid CLI is locally available, optionally generate SVG. Do not require it for reading.

### 2.5 Reader instructions

Create:

`docs/READING-KUTUMBA-DOCUMENTS.md`

Include:

- close old raw Markdown tabs
- `Ctrl+Shift+P` → `Developer: Reload Window`
- reopen the file
- `Ctrl+Shift+V` for rendered preview
- `Ctrl+K`, then `V` for side-by-side preview
- `Ctrl+Shift+O` for headings in one file
- `Ctrl+T` for headings across the workspace
- right-click tab → `Reopen Editor With...` → `Markdown Preview`
- how to return to text mode
- how to open the public GitHub-rendered version

Do not install a third-party Markdown-preview extension as a mandatory dependency.

---

## Phase 3 — Correct the Prem-kī-Kathā model

The current files named `prem-ki-katha.md` are generally one-paragraph modern hooks. They are not full Prem-kī-Kathā.

### 3.1 Preserve and rename the current hooks

For every module:

- move the existing short modern scenario into `opening-hook.md`
- preserve its provenance
- do not delete it
- remove the label “Prem-kī-Kathā” from a modern problem statement

### 3.2 Define the new standard

Create:

`15-templates/PREM-KI-KATHA-STANDARD.md`

A valid Prem-kī-Kathā must be:

- an actual source-grounded devotional narrative
- selected from Śrīla Prabhupāda’s books, Kṛṣṇa-līlā, Caitanya-līlā, Bhāgavatam narratives, recognized Gauḍīya history, or verified Śrīla Prabhupāda-līlā
- connected naturally to the module principle
- devotional and heart-engaging
- understandable to adults and children together
- free of invented quotations attributed to sacred personalities
- free of unsupported dramatic details
- clear about which sentences are source narrative, paraphrase, or facilitator transition

Required length:

- 12–15 minutes narrated
- normally 900–1,500 words depending on interaction
- plus 3–5 minutes of simple family interaction

Required structure:

1. Katha title
2. Module connection
3. Primary source references and links
4. Setting and devotional mood
5. Main personalities
6. Source-grounded narrative
7. Turning point
8. Central teaching
9. Heart reflection
10. Two Lāla–Lālī interaction cues
11. Two Kiśora–Kiśorī reflection cues
12. Parent bridge
13. Transition to the philosophy lesson
14. Narration cautions
15. Visual/storyboard plan
16. Rights and quotation status
17. Human doctrinal review status

### 3.3 Katha source control

Create per module:

`katha/KATHA-SOURCE-REGISTER.yaml`

Required fields:

- module ID
- katha title
- primary book
- chapter/reference
- stable source links
- exact verses used
- direct quotations
- paraphrased portions
- facilitator-created transitions
- omitted complex details
- audience cautions
- doctrinal reviewer
- rights status
- approval status

Create:

`14-research-source-register/PREM-KI-KATHA-SOURCE-MAP.md`

Map all 18 modules to candidate kathas.

Do not force the same type of story into every week.

### 3.4 C1-W2 katha pilot

Replace the C1-W2 Prem-kī-Kathā with one authentic narrative selected after source review.

Preferred candidate families:

- Sanātana Gosvāmī asks Śrī Caitanya Mahāprabhu, “Who am I?” and receives the constitutional-identity teaching
- Arjuna’s grief before Kṛṣṇa’s compassionate body–soul instruction
- Jaḍa Bharata and King Rahūgaṇa, using only the part suitable for this foundational module

Select one principal katha. Do not combine three stories into one overloaded narration.

The katha must:

- create devotional feeling, not only intellectual curiosity
- lead naturally to BG 2.13
- preserve the distinction between C1-W2 and C1-W3
- avoid frightening death imagery for young children
- avoid invented dialogue
- include a visual storyboard and narration guide

### 3.5 Prem-kī-Kathā quality gate

Create:

`scripts/curriculum/validate_prem_ki_katha.py`

Fail when:

- file is under the substantive threshold
- no primary source
- no stable source link
- no katha source register
- no module connection
- no child interaction cues
- no parent bridge
- no transition to lesson
- invented quotation markers are unresolved
- the file is only a modern scenario
- review status falsely says approved

Add the validator to `run_curriculum_validation.py`.

C1-W2 must pass before applying the model to other modules.

---

## Phase 4 — Build a real media and lecture library

The current media library is mostly Gamma prompts plus a small Prabhupāda lecture index.

### 4.1 Approved-speaker governance

Keep the approved-speaker registry empty until exact identities and authorized source channels are provided.

Do not infer “Bhajji Maharaj” or any partially named teacher.

Add a controlled pending-entry template requiring:

- full initiated/public name
- exact official channel or user-owned source folder
- relation to KUTUMBA
- approved topics
- prohibited topics
- rights status
- reviewer
- approval date

### 4.2 Media library structure

Create:

```text
14-research-source-register/media-library/
├── README.md
├── PRABHUPADA-LECTURE-CATALOG.yaml
├── APPROVED-TEACHER-CATALOG.yaml
├── KATHA-AUDIO-CATALOG.yaml
├── BHAJANA-AND-KIRTANA-CATALOG.yaml
├── VIDEO-CATALOG.yaml
├── MEDIA-RIGHTS-REGISTER.yaml
└── TOPIC-TO-MEDIA-MAP.md
```

Do not download or commit copyrighted audio/video by default.

Store:

- metadata
- stable link
- exact timestamp
- topic
- teaching purpose
- audience
- duration
- source authority tier
- rights status
- human review status

### 4.3 Module integration

Each module’s `audio-video/MEDIA-INDEX.yaml` must link to:

- relevant verified Śrīla Prabhupāda lectures
- relevant katha audio, if approved
- relevant bhajana/kīrtana, if approved
- rendered Gamma deck status
- external media rights status

Do not mark a module’s media layer complete merely because Gamma prompt files exist.

---

## Phase 5 — Correct the quality dashboard and semantic validators

### 5.1 Dashboard defects

The present dashboard incorrectly labels every module as:

- 3 blanks
- legacy-3-band

even after the two-group addendum and enhancement work.

Fix `audit_empty_sections.py`:

- active age model must be determined from active Lāla–Lālī and Kiśora–Kiśorī files
- preserved legacy `children/lesson.md` must not cause the active model to be reported as legacy
- report legacy source separately
- identify exact blank/thin files, not only a count
- distinguish gold, deepened, baseline-scaffold, and source-only
- report actual word/line/content metrics
- report substantive source count
- report substantive claim count
- report substantive Gamma card count
- report Prem-kī-Kathā status
- report media depth

Regenerate:

- `build-evidence/WEEK-QUALITY-DASHBOARD.md`
- `build-evidence/EMPTY-AND-THIN-SECTIONS.csv`
- `build-evidence/FIRST-SIX-MONTH-CONTENT-AUDIT.md`

### 5.2 Implement missing validators

The curriculum orchestrator currently runs only a subset of the promised validators.

Implement and execute:

- `validate_source_registry.py`
- `validate_claim_register.py`
- `check_external_links.py`
- `validate_visual_assets.py`
- `validate_gamma_briefs.py`
- `detect_unverified_claims.py`
- `measure_live_session_load.py`
- `build_week_quality_dashboard.py`
- `build_cycle_coverage_report.py`
- `generate_curriculum_status.py`
- `validate_prem_ki_katha.py`
- `validate_media_indexes.py`

Add all applicable validators to:

`scripts/curriculum/run_curriculum_validation.py`

### 5.3 Validation honesty

Do not declare all gates PASS when:

- repository validator still has warnings
- external links were not checked
- source hashes were skipped
- review-status files remain pending
- a module is only baseline-scaffold
- the media layer is empty
- Prem-kī-Kathā is only a hook

Use separate verdicts:

- structural validation
- semantic validation
- source validation
- rights validation
- human-review status
- publication readiness

---

## Phase 6 — Deepen the 17 baseline modules

Do not perform another shallow batch fill.

Use this order:

1. Finish Cycle 1
2. Audit Cycle 1
3. Finish Cycle 2
4. Audit Cycle 2
5. Finish Cycle 3
6. Audit Cycle 3

Within each module, reach the approved C1-W2 standard or document a justified module-specific minimum.

Required minimum:

- full research dossier
- 8–15 meaningful primary sources as appropriate
- verified source matrix
- 8–12 traceable claims as appropriate
- verified Śrīla Prabhupāda lecture index
- substantive misconceptions and boundaries
- 5–9 anonymized contemporary cases where appropriate
- full Lāla–Lālī timed lesson
- full Kiśora–Kiśorī timed lesson
- themed family transition
- full materials
- full assessment
- newcomer adaptation
- real Prem-kī-Kathā
- visual plan
- rendered Mermaid wrapper pages
- full Gamma card content
- media index
- substantive reviewer worksheets
- cycle project contribution
- semantic validation pass

Do not use arbitrary counts when they do not fit the module. Record the reason.

Correct the known batch defects:

- duplicated legacy age blocks inside Lāla–Lālī files
- generic family-transition files
- copy-pasted death imagery cautions in unrelated modules
- thin Kiśora–Kiśorī lessons
- hollow claim registers
- empty lecture indexes
- 6–8 line Gamma outlines
- generic review stubs

Only change:

`weekly_derivative_pack: baseline-scaffold`

to:

`weekly_derivative_pack: enhancement-complete`

after all module gates pass.

---

## Phase 7 — Reports and commits

Maintain:

- `CURRENT-STATUS.md`
- `build-evidence/POST-AUDIT-REMEDIATION-LEDGER.md`
- `build-evidence/WEEK-QUALITY-DASHBOARD.md`
- `build-evidence/PREM-KI-KATHA-STATUS.md`
- `build-evidence/MEDIA-LIBRARY-STATUS.md`
- `build-evidence/READER-IMPLEMENTATION-REPORT.md`
- `build-evidence/VALIDATION-COVERAGE-REPORT.md`
- `build-evidence/FINAL-POST-AUDIT-REPORT.md`

Commit logically:

```text
fix: correct curriculum source mappings and broken links
docs: add KUTUMBA rendered reading experience
docs: establish authentic Prem-kī-Kathā standard
docs: complete C1-W2 Prem-kī-Kathā pilot
docs: add controlled media-library architecture
chore: strengthen semantic curriculum validation
docs: deepen cycle 1 modules
docs: deepen cycle 2 modules
docs: deepen cycle 3 modules
docs: record final post-audit curriculum report
```

Run all validation before every phase commit.

Push to `origin/main`.

Do not force-push.

---

## Final response

Report:

- current HEAD
- commits pushed
- broken links fixed
- binary hashes verified
- reader setup
- Mermaid viewer count
- Prem-kī-Kathā pilot verdict
- authentic katha count
- media entries by source tier
- approved-speaker status
- module depth status
- dashboard accuracy
- validators implemented
- validation verdicts by category
- warnings
- human-review gates
- working-tree status
- exact next human actions

Do not issue unconditional publication GO while human doctrinal, worship, safeguarding, rights, citation, or pedagogy approvals remain open.
