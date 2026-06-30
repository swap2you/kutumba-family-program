# Prompt 03 — Repository Foundation and Navigation

## Objective

Create a clean documentation-first repository that is easy to understand without Cursor.

## Root rule

The repository root is the folder currently open. Never create another repository folder inside it.

## Required root files

Create or normalize:

- `README.md`
- `CURRENT-STATUS.md`
- `ROADMAP.md`
- `GOVERNANCE.md`
- `CONTRIBUTING.md`
- `CHANGELOG.md`
- `SECURITY-PRIVACY.md`
- `RIGHTS-AND-USE.md`
- `AGENTS.md`
- `.gitignore`
- `.gitattributes`
- `.editorconfig`

## Target structure

Create only meaningful folders:

```text
00-source-materials/
00-foundation/
01-governance/
02-curriculum-architecture/
03-first-six-months/
04-children-youth/
05-parent-formation/
06-prasadam-operations/
07-kirtana-worship-bhakti-labs/
08-festivals-yatras-calendar/
09-digital-repository-publishing/
10-kutumba-setu/
11-weekly-program-library/
12-family-facing-library/
13-facilitator-library/
14-research-source-register/
15-templates/
16-prompt-library/
17-reviews-and-audits/
18-published-exports/
build-evidence/
scripts/
```

Do not use empty decorative nesting. Every folder must have a `README.md` explaining:

- purpose
- canonical content
- expected files
- review owner
- publication status
- what does not belong there

## Navigation

The root README must provide:

- KUTUMBA identity and boundaries
- source-of-truth model
- repository map
- current status
- how to locate weekly material
- how to add a source
- how to propose a correction
- how to run validation
- privacy warning
- copyright warning
- status vocabulary
- link to roadmap and build report

## Repository operating controls

Add Cursor rules and `AGENTS.md` that prohibit:

- application development
- duplicate repo roots
- unsupported doctrinal writing
- invented citations
- unreviewed worship procedures
- private family data
- bulk copyrighted source copying
- false approval labels
- silent loss of source detail

## No clutter rule

Move obsolete setup drafts, duplicate prompt files, temporary extraction files, and generated debris into a dated `99-archive` folder only when preservation is useful. Do not leave files such as:

- `final-final-v2`
- duplicate README files
- random exports at root
- temporary conversion files
- unused scaffolding
- empty folders
- generated caches

Record every cleanup decision in `build-evidence/CLEANUP-REPORT.md`.
