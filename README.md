# KUTUMBA — Families Growing in Krishna Consciousness

Private documentation-first knowledge base for the KUTUMBA family formation program.

## Identity and boundaries

KUTUMBA is a family-oriented Krishna consciousness formation program. This repository holds operating models, curriculum architecture, detailed lessons, governance documents, and controlled production prompts. It does **not** contain an application, API, database, or public website implementation.

## Source-of-truth model

| Layer | Location | Role |
|---|---|---|
| Originals | `00-source-materials/01-current-kutumba-originals/` | Immutable DOCX/PDF sources from project authoring |
| Manifest | `00-source-materials/SOURCE-MANIFEST.yaml` | SHA-256 provenance and metadata |
| Canonical working copies | Workstream folders (`00-foundation/` … `18-published-exports/`) | Searchable Markdown linked to source IDs |
| Legacy references | `00-source-materials/03-external-reference-index/` | Metadata indexes only — not bulk-copied |
| Git | This repository | Canonical working source after intake |

Original download folders under `C:\Users\swap2\Downloads\Personal\0. KUTUMBA SANGA` remain untouched.

## Repository map

| Folder | Content |
|---|---|
| `00-source-materials/` | Sources, manifest, legacy indexes |
| `00-foundation/` | Master operating model |
| `01-governance/` | Governance and temple relationship |
| `02-curriculum-architecture/` | Three-year architecture |
| `03-first-six-months/` | First six-month detailed curriculum |
| `04-children-youth/` | Children and youth formation |
| `05-parent-formation/` | Parent formation and family care |
| `06-prasadam-operations/` | Prasāda and weekly operations |
| `07-kirtana-worship-bhakti-labs/` | Worship and bhakti laboratories |
| `08-festivals-yatras-calendar/` | Festivals and calendar |
| `09-digital-repository-publishing/` | Digital library (gap — source not supplied) |
| `10-kutumba-setu/` | KUTUMBA Setu (gap — draft required) |
| `11-weekly-program-library/` | Weekly lesson packs |
| `14-research-source-register/` | Legacy crosswalks and research backlog |
| `16-prompt-library/` | Reusable production prompts |
| `17-reviews-and-audits/` | Independent review handoff |
| `build-evidence/` | Build and validation reports |
| `scripts/` | Validation scripts |

## Current status

See [CURRENT-STATUS.md](CURRENT-STATUS.md) and [build-evidence/FINAL-BUILD-REPORT.md](build-evidence/FINAL-BUILD-REPORT.md).

## Weekly material

Detailed weeks live under `11-weekly-program-library/`. The monolithic canonical curriculum is at `03-first-six-months/FIRST-SIX-MONTH-DETAILED-CURRICULUM.md`.

## How to add a source

1. Place the original in the controlled source location (do not alter Downloads originals).
2. Run `scripts/ingest-sources.py` or follow `16-prompt-library/00-orchestration/import-new-source-document.md`.
3. Normalize to canonical Markdown with source ID and hash frontmatter.
4. Update `SOURCE-MANIFEST.yaml` and `CURRENT-STATUS.md`.

## How to propose a correction

Open a change against the canonical Markdown file, cite the source ID, and add an entry to `00-foundation/REVIEW-QUEUE.md` if doctrinal, worship, or safety review is required.

## Validation

```powershell
powershell -File scripts/Validate-KutumbaRepository.ps1
```

## Privacy warning

Do not commit private family records, completed personal forms, or credentials. See [SECURITY-PRIVACY.md](SECURITY-PRIVACY.md).

## Copyright warning

Do not bulk-copy copyrighted PDF libraries, books, or third-party training packs. Legacy collections are indexed only. See [RIGHTS-AND-USE.md](RIGHTS-AND-USE.md).

## Status vocabulary

- `active` — canonical content present and maintained
- `SOURCE NOT YET SUPPLIED` — workstream gap; no fabricated complete document
- `DRAFT REQUIRED` — structured placeholder awaiting production
- `reference-only` — indexed external material, not canonical
- `review-required` — pending human gate

## Links

- [ROADMAP.md](ROADMAP.md)
- [GOVERNANCE.md](GOVERNANCE.md)
- [build-evidence/FINAL-BUILD-REPORT.md](build-evidence/FINAL-BUILD-REPORT.md)
