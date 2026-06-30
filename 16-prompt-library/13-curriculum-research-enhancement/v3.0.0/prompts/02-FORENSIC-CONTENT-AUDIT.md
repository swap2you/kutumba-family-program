# Prompt 02 — Forensic Content Audit

## Objective

Determine what is genuinely complete, partially complete, empty, duplicated, overlong, unsupported, or misleading across the 18 first-six-month module folders.

## Scope

Audit:

`11-weekly-program-library/first-six-months/`

Do not trust `weekly_derivative_pack: complete` without checking content.

## Required checks per module

Check every expected file and classify:

- complete;
- thin;
- empty shell;
- duplicated;
- unsupported claim;
- missing source;
- missing application;
- missing child differentiation;
- missing materials;
- missing assessment;
- missing newcomer adaptation;
- missing visual;
- missing presentation brief;
- rights uncertainty;
- human review required.

An empty Markdown heading, empty table, placeholder sentence, or link-only file does not count as content.

## Known patterns to detect

Detect files that contain only structures such as:

```markdown
| **Analogy** | **Practical family example** |
| --- | --- |
```

or:

```markdown
| **Materials A** | **Materials B** |
| --- | --- |
```

or:

```markdown
| **KUTUMBA Setu application** |
| --- |
```

Also detect:

- `Key verse` headings with no study content;
- `Competency check` headings with no criteria;
- source YAML containing only the original KUTUMBA DOCX;
- missing direct source links;
- age labels still using 4–6, 7–9, 10–13;
- `complete` status despite empty components.

## Reports

Create:

- `build-evidence/FIRST-SIX-MONTH-CONTENT-AUDIT.md`
- `build-evidence/EMPTY-AND-THIN-SECTIONS.csv`
- `build-evidence/WEEK-QUALITY-DASHBOARD.md`

The dashboard must have one row per module and one column per required content domain.

## Initial status correction

Where a module has empty mandatory components, change:

`weekly_derivative_pack: complete`

to:

`weekly_derivative_pack: enhancement-required`

Do not change:

`canonical_detailed_source: complete`

when the source monolith remains intact.

## Gate

Do not begin bulk enhancement until the audit proves the exact baseline.
