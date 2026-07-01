# KUTUMBA — Families Growing in Krishna Consciousness

Public documentation and curriculum-development repository for the KUTUMBA family formation program.

> KUTUMBA is a public documentation and curriculum-development repository. Public access applies only to general program content, source-controlled operating models, curriculum materials, templates and non-sensitive reference metadata. Private participant and operational records are prohibited from Git.

## Identity and boundaries

KUTUMBA is a family-oriented Krishna consciousness formation program. This repository holds operating models, curriculum architecture, detailed lessons, governance documents, and controlled production prompts. It does **not** contain an application, API, database, or public website implementation.

> Project owner or reviewer: start with [START-HERE.md](START-HERE.md). For comfortable browsing, use [KUTUMBA-READER-HOME.md](KUTUMBA-READER-HOME.md). For pause/resume instructions, use [PROJECT-PAUSE-HANDOFF.md](PROJECT-PAUSE-HANDOFF.md).

## Licence and rights

- Original KUTUMBA-authored content: [CC BY-NC-SA 4.0](LICENSE.md)
- Third-party, BBT, and legacy material: see [RIGHTS-AND-USE.md](RIGHTS-AND-USE.md)
- Privacy controls: [SECURITY-PRIVACY.md](SECURITY-PRIVACY.md)

## Source-of-truth model

| Layer | Location | Role |
|---|---|---|
| Originals | `00-source-materials/01-current-kutumba-originals/` | Immutable DOCX/PDF sources from project authoring |
| Manifest | `00-source-materials/SOURCE-MANIFEST.yaml` | SHA-256 provenance and metadata |
| Canonical working copies | Workstream folders (`00-foundation/` … `18-published-exports/`) | Searchable Markdown linked to source IDs |
| Legacy references | `00-source-materials/03-external-reference-index/` | Metadata indexes only — not bulk-copied |
| Local path mapping | `config/local-source-roots.yaml` (gitignored) | Machine-specific paths for reference collections |
| Git | This repository | Canonical working source after intake |

Use `config/local-source-roots.example.yaml` as a template for local source roots. Original download folders remain outside Git.

## Repository map

| Folder | Content |
|---|---|
| `00-source-materials/` | Sources, manifest, legacy indexes |
| `00-foundation/` | Master operating model |
| `01-governance/` | Governance and temple relationship |
| `02-curriculum-architecture/` | Three-year architecture and navigation maps |
| `03-first-six-months/` | First six-month detailed curriculum (monolith) |
| `04-children-youth/` | Children and youth formation |
| `05-parent-formation/` | Parent formation and family care |
| `06-prasadam-operations/` | Prasāda and weekly operations |
| `07-kirtana-worship-bhakti-labs/` | Worship and bhakti laboratories |
| `08-festivals-yatras-calendar/` | Festivals and calendar |
| `09-digital-repository-publishing/` | Public source map, source directory, and publishing indexes (operating manual not supplied) |
| `10-kutumba-setu/` | KUTUMBA Setu (gap — draft required) |
| `11-weekly-program-library/` | Weekly lesson packs |
| `12-family-facing-library/` | Family-facing publication index (planned) |
| `13-facilitator-library/` | Facilitator resource index |
| `14-research-source-register/` | Legacy crosswalks and research backlog |
| `16-prompt-library/` | Reusable production prompts |
| `17-reviews-and-audits/` | Independent and completion audits |
| `build-evidence/` | Build, validation, and completion reports |
| `scripts/` | Validation and extraction scripts |

## Current status

See [CURRENT-STATUS.md](CURRENT-STATUS.md) and [PROJECT-PAUSE-HANDOFF.md](PROJECT-PAUSE-HANDOFF.md). As of the V10A.1 safe pause, the repository is in `internal-development-paused`; internal pilot, family-facing distribution, and public publication are all `NO GO` while blocking human gates remain open. Automated validation is structural evidence only and is not doctrinal, worship, safeguarding, rights, pedagogy, design, citation, Gamma, pilot, distribution, or publication approval.

## Source directory and catalog

| Artifact | Path |
|---|---|
| Public source map | `09-digital-repository-publishing/PUBLIC-SOURCE-MAP-FOR-PRABHUPADA-AND-SANATANA-CONTENT.md` |
| Public source directory | `09-digital-repository-publishing/PUBLIC-SOURCE-DIRECTORY.md` |
| Master catalog | `14-research-source-register/public-source-catalog/MASTER-SOURCE-CATALOG.yaml` |
| Source manifest (14 originals) | `00-source-materials/SOURCE-MANIFEST.yaml` |

Workstream 9: public source-map and source-directory components are complete; the full Digital Repository Operating Manual has not been supplied.

## Weekly material

Detailed weeks live under `11-weekly-program-library/first-six-months/`. Each week includes a `complete-week.md` extracted from the monolithic canonical curriculum at `03-first-six-months/FIRST-SIX-MONTH-DETAILED-CURRICULUM.md`.

## How to add a source

1. Place the original in the controlled source location.
2. Run `scripts/ingest-sources.py` or follow `16-prompt-library/00-orchestration/import-new-source-document.md`.
3. Normalize to canonical Markdown with source ID and hash frontmatter.
4. Update `SOURCE-MANIFEST.yaml` and `CURRENT-STATUS.md`.

## How to propose a correction

Open a change against the canonical Markdown file, cite the source ID, and add an entry to `00-foundation/REVIEW-QUEUE.md` if doctrinal, worship, or safety review is required.

## Validation

```powershell
python scripts/curriculum/run_curriculum_validation.py
python scripts/curriculum/validate_v10a_truth_freeze.py
python scripts/sources/reconcile_source_map_urls.py
python scripts/sources/validate_catalog_consistency.py
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
- `planned — not yet published` — family/facilitator derivative not approved for publication
- `canonical-detailed-source-complete` — monolith week block present
- `weekly-derivative-pack-complete` — all required weekly component files present

## Links

- [ROADMAP.md](ROADMAP.md)
- [LICENSE.md](LICENSE.md)
- [GOVERNANCE.md](GOVERNANCE.md)
- [build-evidence/FINAL-BUILD-REPORT.md](build-evidence/FINAL-BUILD-REPORT.md)
