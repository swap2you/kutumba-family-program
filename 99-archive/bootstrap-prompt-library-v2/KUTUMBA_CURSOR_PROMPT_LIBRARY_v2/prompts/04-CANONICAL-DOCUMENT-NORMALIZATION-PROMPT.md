# Prompt 04 — Canonical Document Normalization

## Objective

Create faithful, searchable canonical Markdown versions of every current KUTUMBA operating document while preserving the original documents unchanged.

## Source handling

For every current KUTUMBA DOCX, PDF, slide deck, or spreadsheet:

1. Preserve the original in `00-source-materials/01-current-kutumba-originals/`.
2. Extract content into a temporary working area.
3. Create a canonical Markdown document in the correct workstream folder.
4. Preserve all substantive:
   - headings
   - document-control fields
   - tables
   - numbered rules
   - role definitions
   - cautions
   - forms
   - checklists
   - appendices
   - detailed weekly content
   - risk notes
   - review status
5. Do not reduce the source to a summary.
6. Record any extraction ambiguity.
7. Link the canonical file to its source ID and source hash.
8. Create a parity report.

## Known core documents

At minimum, locate and normalize:

- KUTUMBA Master Operating Model
- KUTUMBA Governance, Charter and Temple Relationship Framework
- KUTUMBA First Six-Month Detailed Curriculum
- KUTUMBA Children and Youth Formation Operating Model

Also normalize every other completed workstream document found in the current KUTUMBA source folder.

## Required outputs

- `00-foundation/MASTER-OPERATING-MODEL.md`
- `01-governance/GOVERNANCE-CHARTER-AND-TEMPLE-RELATIONSHIP.md`
- `03-first-six-months/FIRST-SIX-MONTH-DETAILED-CURRICULUM.md`
- `04-children-youth/CHILDREN-YOUTH-FORMATION-OPERATING-MODEL.md`
- corresponding documents for all other supplied workstreams
- `build-evidence/DOCUMENT-PARITY-REPORT.md`
- one extraction report per source document

## First-six-month protection

The supplied curriculum contains 18 active sessions. Preserve every detailed lesson.

Each active week must retain, where supplied:

- code and title
- purpose
- outcomes
- primary sources
- key verse
- Prem-kī-Kathā
- parent lesson
- age-banded child lesson
- analogy and practical example
- discovery, understanding, and application questions
- bhakti laboratory
- family home practice
- worksheet
- slide outline
- teacher preparation
- required materials
- assessment
- newcomer adaptation
- risks and sensitive points

Split the monolithic curriculum into individual week files only after preserving the complete monolithic canonical document.

## DOCX formatting evidence

Create a document style guide derived from the best supplied KUTUMBA documents.

Do not claim visual parity without rendering and inspecting generated documents.

If DOCX regeneration is not reliable, retain originals as official visual baselines and use Markdown as the canonical working source. Mark automated DOCX regeneration as a later controlled capability.
