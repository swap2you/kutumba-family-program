#!/usr/bin/env python3
"""Create KUTUMBA repository foundation: folders, READMEs, root files."""

from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(r"C:\Development\Workspace\DevotionalRepo\kutumba-family-program")

FOLDERS = [
    ("00-source-materials", "Immutable and indexed source documents", "Repository Curator", "active"),
    ("00-foundation", "Master operating model and cross-cutting foundation", "Program Director", "active"),
    ("01-governance", "Governance, charter, temple relationship", "Governance Lead", "active"),
    ("02-curriculum-architecture", "Three-year curriculum architecture", "Curriculum Architect", "active"),
    ("03-first-six-months", "First six-month detailed curriculum", "Curriculum Lead", "active"),
    ("04-children-youth", "Children and youth formation", "Children Formation Lead", "active"),
    ("05-parent-formation", "Parent formation and family care", "Parent Formation Lead", "active"),
    ("06-prasadam-operations", "Prasāda, hospitality, weekly operations", "Operations Lead", "active"),
    ("07-kirtana-worship-bhakti-labs", "Kīrtana, worship, prayers, bhakti labs", "Worship Lead", "active"),
    ("08-festivals-yatras-calendar", "Festivals, yātrās, outdoor activities, calendar", "Calendar Lead", "active"),
    ("09-digital-repository-publishing", "Repository, drive, website, digital library", "Digital Lead", "SOURCE NOT YET SUPPLIED"),
    ("10-kutumba-setu", "KUTUMBA Setu bridge materials", "Setu Lead", "DRAFT REQUIRED"),
    ("11-weekly-program-library", "Weekly program library and lesson packs", "Curriculum Lead", "active"),
    ("12-family-facing-library", "Family-facing derivatives", "Communications Lead", "active"),
    ("13-facilitator-library", "Facilitator guides and preparation", "Facilitation Lead", "active"),
    ("14-research-source-register", "Research register and legacy crosswalks", "Research Lead", "active"),
    ("15-templates", "Document and lesson templates", "Documentation Lead", "active"),
    ("16-prompt-library", "Internal reusable Cursor prompts", "Documentation Lead", "active"),
    ("17-reviews-and-audits", "Independent reviews and audits", "Review Coordinator", "active"),
    ("18-published-exports", "Controlled publication exports", "Publishing Lead", "active"),
    ("build-evidence", "Build, validation, and audit evidence", "Repository Curator", "active"),
    ("scripts", "Validation and maintenance scripts", "Repository Curator", "active"),
    ("99-archive", "Obsolete drafts preserved for reference", "Repository Curator", "archive"),
]

README_TEMPLATE = """# {name}

## Purpose

{purpose}

## Canonical content

Operating documents, curriculum materials, and controlled derivatives for this KUTUMBA workstream.

## Expected files

- Canonical Markdown working copies linked to source IDs in `00-source-materials/SOURCE-MANIFEST.yaml`
- Workstream-specific README and gap records where sources are not yet supplied
- Review status metadata where applicable

## Review owner

{owner}

## Publication status

{status}

## What does not belong here

- Bulk copyrighted PDF libraries or third-party training packs
- Private family records or completed personal forms
- Application code, databases, or deployment artifacts
- Unreviewed worship procedures presented as approved
"""


def write_file(path: Path, content: str):
    if not path.exists():
        path.write_text(content, encoding="utf-8")


def main():
    for folder, purpose, owner, status in FOLDERS:
        p = REPO_ROOT / folder
        p.mkdir(parents=True, exist_ok=True)
        readme = p / "README.md"
        if not readme.exists():
            readme.write_text(
                README_TEMPLATE.format(
                    name=folder,
                    purpose=purpose,
                    owner=owner,
                    status=status,
                ),
                encoding="utf-8",
            )

    # Root files
    write_file(REPO_ROOT / ".gitignore", """# Office lock files
~$*
*.tmp

# OS
Thumbs.db
.DS_Store
desktop.ini

# Python
__pycache__/
*.pyc
.venv/
venv/

# Build working
build-evidence/extraction-working/
*.log

# Secrets
.env
*.pem
credentials.json

# Large binaries policy — reference collections stay local
""")

    write_file(REPO_ROOT / ".gitattributes", """* text=auto
*.md text eol=lf
*.yaml text eol=lf
*.yml text eol=lf
*.json text eol=lf
*.csv text eol=lf
*.ps1 text eol=lf
*.py text eol=lf
""")

    write_file(REPO_ROOT / ".editorconfig", """root = true

[*]
charset = utf-8
end_of_line = lf
insert_final_newline = true
trim_trailing_whitespace = true

[*.md]
trim_trailing_whitespace = false
""")

    write_file(REPO_ROOT / "00-foundation" / "REVIEW-QUEUE.md", """# Review Queue

Items requiring human review before adoption or publication.

| ID | Item | Type | Owner | Status | Notes |
|---|---|---|---|---|---|
| RQ-001 | Digital Repository/Publishing workstream | missing-source | Digital Lead | open | No dedicated source document in KUTUMBA SANGA |
| RQ-002 | KUTUMBA Setu materials | missing-source | Setu Lead | open | No dedicated source document supplied |
| RQ-003 | Legacy Bhaktivriksha adoption decisions | rights-review | Research Lead | open | Index only; no bulk copy |
| RQ-004 | Granth PDF redistribution | copyright-review | Research Lead | open | Reference catalog only |
| RQ-005 | Worship procedures in canonical docs | worship-review | Worship Lead | open | Verify temple alignment |
| RQ-006 | Children/youth safeguarding content | safety-review | Children Formation Lead | open | Per operating model |
""")

    write_file(REPO_ROOT / "README.md", """# KUTUMBA — Families Growing in Krishna Consciousness

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

Original download folders under `C:\\Users\\swap2\\Downloads\\Personal\\0. KUTUMBA SANGA` remain untouched.

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
""")

    for name, body in {
        "ROADMAP.md": "# KUTUMBA Repository Roadmap\n\n1. Complete first-six-month weekly library split\n2. Produce missing workstream documents (digital publishing, Setu)\n3. Three-year detailed lesson production backlog execution\n4. Independent repository audit (Prompt 10)\n5. Controlled DOCX regeneration capability\n",
        "GOVERNANCE.md": "# KUTUMBA Repository Governance\n\nThis repository follows the KUTUMBA Governance Charter. Canonical governance document: `01-governance/GOVERNANCE-CHARTER-AND-TEMPLE-RELATIONSHIP.md`.\n\nChanges to worship procedures, children safeguarding content, or temple relationship boundaries require designated reviewer approval before merge.\n",
        "CONTRIBUTING.md": "# Contributing\n\n1. Never invent doctrinal content or citations.\n2. Link canonical changes to source IDs and hashes.\n3. Run validation before commit.\n4. Add review-queue entries for worship, safety, rights, or doctrinal gates.\n5. Do not bulk-copy copyrighted reference material.\n",
        "CHANGELOG.md": "# Changelog\n\n## 2026-06-29\n\n- Initial repository build from KUTUMBA SANGA source documents\n- Source ingestion, canonical normalization, workstream assembly\n",
        "SECURITY-PRIVACY.md": "# Security and Privacy\n\n- Repository is private on GitHub.\n- No private family records, completed forms, or secrets in Git.\n- Reference registers may contain local filesystem paths for provenance; do not expose publicly.\n- Report concerns to the Repository Curator.\n",
        "RIGHTS-AND-USE.md": "# Rights and Use\n\n- KUTUMBA-authored project documents: internal program use.\n- Legacy Bhaktivriksha, Granth, and Jayapataka Swami BV Material: reference-only, rights review required before any adoption or redistribution.\n- No bulk commit of copyrighted PDF libraries.\n",
        "AGENTS.md": """# Agent Instructions

This is a **documentation and knowledge-base** project. Agents must NOT:

- Build applications, APIs, databases, authentication, or websites
- Create nested repository roots or duplicate `kutumba-family-program` folders
- Invent doctrinal content, citations, or worship procedures
- Bulk-copy copyrighted PDF libraries
- Replace detailed operating documents with shallow summaries
- Fabricate complete documents for missing workstreams
- Commit private family data or secrets
- Apply false approval labels

Agents MUST:

- Preserve source depth and link canonical files to source IDs and SHA-256 hashes
- Update `CURRENT-STATUS.md` at phase boundaries
- Create structured gaps and review-queue entries for missing content
- Run validation before commit and push
- Treat legacy collections as reference-only unless formally reviewed and adopted
""",
    }.items():
        write_file(REPO_ROOT / name, body)

    # Archive duplicate prompt pack nesting
    archive_note = REPO_ROOT / "99-archive" / "README.md"
    write_file(archive_note, "# Archive\n\nObsolete drafts and duplicate bootstrap files preserved during repository build.\n")

    # Cursor rules
    cursor_rules = REPO_ROOT / ".cursor" / "rules" / "kutumba-documentation.mdc"
    cursor_rules.parent.mkdir(parents=True, exist_ok=True)
    write_file(cursor_rules, """---
description: KUTUMBA documentation repository constraints
globs: **/*
---

# KUTUMBA documentation-only repository

- No application development
- No nested git roots
- Preserve source document depth
- Index legacy references; do not bulk-copy copyrighted PDFs
- Update CURRENT-STATUS.md at phase boundaries
- Link canonical docs to source_id and source_hash
""")

    print("Foundation created")


if __name__ == "__main__":
    main()
