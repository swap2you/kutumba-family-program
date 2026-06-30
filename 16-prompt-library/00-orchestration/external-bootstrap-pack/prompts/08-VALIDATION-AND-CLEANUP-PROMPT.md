# Prompt 08 — Validation, Cleanup, and Repository Quality

## Objective

Prove that the repository is coherent, safe, navigable, source-grounded, and free of avoidable clutter.

## Required validation

Create or run checks for:

- repository root nesting
- unexpected nested `.git` folders
- broken internal Markdown links
- invalid YAML and JSON
- duplicate permanent IDs
- missing required metadata
- missing required lesson sections
- missing source links
- unverified citation markers
- possible secrets
- prohibited private-data patterns
- unsupported approval terms
- temporary Office files
- generated caches
- empty folders
- duplicate large binaries
- files exceeding the repository binary policy
- unindexed originals
- indexed files without rights status
- canonical documents without source hashes
- first-six-month lesson count and completeness
- Git status

## Required scripts

Create simple maintainable scripts under `scripts/` for:

- source manifest validation
- lesson schema validation
- internal link checking
- duplicate ID checking
- secret and private-data heuristic scanning
- repository tree generation
- status summary generation

Do not build a complex software platform. Use the simplest available language already supported locally.

## Cleanup

Remove or archive:

- duplicate prompt drafts
- obsolete extraction copies
- temporary conversion files
- caches
- empty placeholder folders without purpose
- random root files
- unused scaffolding

Never delete immutable sources or evidence.

## Reports

Create:

- `build-evidence/VALIDATION-REPORT.md`
- `build-evidence/CLEANUP-REPORT.md`
- `build-evidence/REPOSITORY-TREE.txt`
- `build-evidence/CONTENT-COVERAGE-REPORT.md`
- `build-evidence/PRIVACY-AND-RIGHTS-SCAN.md`

## Gate

A validation command must return nonzero on critical failures.

Do not mark the build complete while any of these remain:

- nested repository
- missing current source document
- untracked private data
- secret
- corrupted source manifest
- lost first-six-month lesson content
- false approval statement
- bulk copyrighted library committed
- broken root navigation
