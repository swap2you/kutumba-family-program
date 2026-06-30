# Prompt 04 — Week-Pack Information Architecture and Reader Experience

## Objective

Keep the successful existing module folders, but add a consistent deep-research and production layer without making the folder unreadable.

## Preserve existing top-level files

Keep the current delivery files at the module root.

Add these subfolders to every module:

```text
research/
visuals/
gamma/
project/
reviews/
audio-video/
```

## Required enhanced module structure

```text
module-folder/
├── README.md
├── complete-week.md
├── overview.md
├── learning-outcomes.md
├── prem-ki-katha.md
├── parent-lesson.md
├── children/
│   ├── lala-lali-lesson.md
│   ├── kisora-kisori-lesson.md
│   └── shared-family-transition.md
├── analogy-and-application.md
├── questions.md
├── bhakti-lab.md
├── family-home-practice.md
├── facilitator-guide.md
├── materials.md
├── assessment.md
├── newcomer-adaptation.md
├── risks-and-sensitive-points.md
├── worksheet.md
├── sankalpa.md
├── slide-outline.md
├── sources.yaml
├── review-status.yaml
├── research/
│   ├── RESEARCH-DOSSIER.md
│   ├── SOURCE-MATRIX.md
│   ├── CLAIM-REGISTER.yaml
│   ├── VERSE-AND-REFERENCE-STUDY.md
│   ├── PRABHUPADA-LECTURE-INDEX.md
│   ├── APPROVED-TEACHER-MEDIA-INDEX.md
│   ├── MISCONCEPTIONS-AND-BOUNDARIES.md
│   ├── CONTEMPORARY-APPLICATIONS.md
│   ├── FAQ.md
│   └── BIBLIOGRAPHY.md
├── visuals/
│   ├── VISUAL-PLAN.md
│   ├── concept-map.mmd
│   ├── process-flow.mmd
│   ├── image-rights-register.yaml
│   └── assets/
├── gamma/
│   ├── GAMMA-MASTER-DECK-BRIEF.md
│   ├── GAMMA-PARENT-DECK-PROMPT.md
│   ├── GAMMA-LALA-LALI-DECK-PROMPT.md
│   ├── GAMMA-KISORA-KISORI-DECK-PROMPT.md
│   └── SPEAKER-NOTES.md
├── project/
│   ├── MODULE-PROJECT-BRIEF.md
│   ├── CYCLE-CONTRIBUTION.md
│   └── PRESENTATION-RUBRIC.md
├── reviews/
│   ├── DOCTRINAL-REVIEW.md
│   ├── CITATION-AUDIT.md
│   ├── SAFEGUARDING-REVIEW.md
│   ├── RIGHTS-REVIEW.md
│   └── PEDAGOGY-REVIEW.md
└── audio-video/
    └── MEDIA-INDEX.yaml
```

## Reader experience

The README is the front door. It must contain:

- two-minute summary;
- “teach this tonight” link;
- deep-research link;
- parent link;
- Lāla–Lālī link;
- Kiśora–Kiśorī link;
- visuals link;
- Gamma link;
- project link;
- review status;
- source status;
- what remains unapproved.

## Markdown reading configuration

Create `.vscode/settings.json` with safe repository-level settings:

```json
{
  "workbench.editorAssociations": {
    "*.md": "vscode.markdown.preview.editor"
  },
  "markdown.validate.enabled": true,
  "markdown.updateLinksOnFileMove.enabled": "prompt"
}
```

Preserve strict Markdown preview security.

Do not require a plugin for basic reading. Cursor/VS Code supports Markdown preview and Mermaid diagrams natively.

## Content principles

- Prefer headings, callouts, diagrams, and short tables.
- Avoid converting every paragraph into a table.
- No giant unbroken text blocks.
- No decorative complexity.
- Use transliteration consistently.
- Put technical provenance in frontmatter or source files, not in the main teaching flow.
