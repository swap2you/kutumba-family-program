# Prompt 10 — Independent V7 Review

## Objective

Perform a fresh read-only independent review after all V7 production commits. Do not trust generated summaries.

## Resolve baseline

Record:

```powershell
git status --short
git rev-parse HEAD
git log --oneline --decorate -20
git diff --check
```

## Independent checks

### Repository and evidence

- actual current HEAD reflected accurately;
- clean working tree;
- no nested repository;
- historical reports preserved;
- current status and roadmap aligned.

### Sources and citations

- source originals 14/14;
- authoritative URL count and total catalog entry count separately reported;
- known SB 1.2.17–1.2.19 errors absent from current canonical files;
- C3-W2 Mathurā/Gokula fact consistent across all current files;
- Cycle 1 point-of-use citations consistent with claim registers.

### Visuals

Inspect every Cycle 1 manifest and actual asset.

Verify:

- assets exist;
- rendered previews are meaningful;
- no placeholder-only pass;
- text readable;
- no factual drift;
- alt text present;
- rights status valid;
- Gamma asset links resolve.

Deep-inspect the theology expansion diagrams. Do not approve doctrine; report whether source mapping and review boundaries are honest.

### Media

Sample every priority module.

Verify records have exact links, relevance and rights status. Confirm no media files were bulk-downloaded.

### Gamma

Deep-read all three C1-W2 decks and one deck from every other Cycle 1 module. Confirm render-ready content, card-specific notes and exact asset references.

### Kathā

Recalculate standard and short-form narrative metrics for C1-W1 through C1-W6. Confirm C1-W2 status is honest.

### Rights

Search tracked files for:

- unauthorized BBT art;
- downloaded Prabhupāda photos;
- copied book pages;
- YouTube thumbnails;
- full purports;
- third-party PDFs;
- unclear licenses.

### Human gates

Confirm all named human gates remain open unless signed records actually exist.

## Independent report

Create:

`17-reviews-and-audits/V7-INDEPENDENT-VISUAL-CITATION-MEDIA-AUDIT.md`

Give separate verdicts:

- repository;
- source integrity;
- citation consistency;
- visual architecture;
- Cycle 1 visual completeness;
- theology visual source discipline;
- media curation;
- Gamma render readiness;
- kathā timing;
- rights;
- internal pilot readiness;
- public publication readiness.

## Final verdict rules

Allowed:

- `GO WITH CONDITIONS for named human review`
- `GO WITH CONDITIONS for internal pilot preparation`
- `NO GO`

Not allowed:

- unconditional public publication GO;
- doctrinal approval by automation;
- visual approval based only on file count.

## Final Git completion

After the independent report is committed:

```powershell
git status --short
git log -1 --oneline
git push origin main
git status --short
```

Working tree must be clean.
