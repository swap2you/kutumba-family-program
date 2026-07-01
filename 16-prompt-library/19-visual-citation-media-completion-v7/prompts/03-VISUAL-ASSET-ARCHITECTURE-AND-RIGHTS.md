# Prompt 03 — Visual Asset Architecture and Rights

## Objective

Replace the current placeholder-only visual system with a governed, reusable visual asset system. Preserve Mermaid as one useful format, but stop treating a Mermaid viewer pair as proof that a substantive visual asset exists.

## Current limitation

The repository currently contains:

- Mermaid source/viewer files;
- visual plans;
- image placeholders in Gamma;
- almost no rendered PNG/SVG curriculum assets;
- no substantial visual library.

The old `validate_visual_assets.py` checks only `.mmd` plus `.md` viewer pairs. Rename its responsibility or replace it.

## Repository architecture

Create:

```text
14-research-source-register/visual-asset-library/
├── README.md
├── VISUAL-ASSET-CATALOG.yaml
├── VISUAL-RIGHTS-POLICY.md
├── VISUAL-DESIGN-SYSTEM.md
├── ALT-TEXT-STANDARD.md
├── SOURCE-ATTRIBUTION-STANDARD.md
├── ASSET-NAMING-STANDARD.md
├── permissions/
│   ├── README.md
│   └── PERMISSION-REQUEST-REGISTER.yaml
└── templates/
    ├── diagram-spec.yaml
    ├── visual-source-register.yaml
    ├── image-rights-register.yaml
    └── alt-text.md
```

For each module use:

```text
visuals/
├── README.md
├── VISUAL-PLAN.md
├── VISUAL-ASSET-MANIFEST.yaml
├── VISUAL-SOURCE-REGISTER.yaml
├── image-rights-register.yaml
├── ALT-TEXT.md
├── source/
│   ├── *.mmd
│   ├── *.svg
│   └── diagram-specs/
└── rendered/
    ├── *.svg
    └── *.png
```

Do not duplicate files needlessly. SVG is canonical for diagrams; PNG is a derivative only when Gamma, Word or ordinary preview requires it.

## Asset classes

Use controlled classes:

- `concept-diagram`
- `process-flow`
- `storyboard`
- `scripture-reference-card`
- `analogy-diagram`
- `timeline`
- `comparison-chart`
- `family-practice-card`
- `activity-printable`
- `map`
- `licensed-devotional-art-reference`
- `photograph-reference`

## Rights classes

- `kutumba-original`
- `public-domain-verified`
- `cc-licensed-verified`
- `permission-granted`
- `link-reference-only`
- `permission-required`
- `rights-unclear-do-not-use`

Public availability is not permission.

Do not download or commit:

- BBT paintings;
- Krishna.com paintings/photos;
- Prabhupāda photographs;
- third-party coloring books;
- screenshots of copyrighted books;
- YouTube thumbnails;

unless explicit permission or a verified license is recorded.

For rights-controlled art, store:

- source page URL;
- owner/publisher;
- candidate use;
- permission status;
- contact/permission record;
- no local binary until approved.

## Visual quality requirements

Every actual visual must have:

- asset ID;
- module/topic;
- audience;
- teaching purpose;
- canonical facts represented;
- source anchors;
- file path;
- format;
- dimensions/viewBox;
- readable text at normal display size;
- alt text;
- rights status;
- generation method;
- human doctrinal review status;
- human design review status;
- revision history.

## Generation guidance

Allowed:

- original SVG diagrams;
- Mermaid diagrams;
- simple KUTUMBA-authored line illustrations;
- icons/shapes created in code;
- public-domain/CC assets after verified license;
- congregation-owned art with written permission.

Not allowed:

- copying a devotional painting;
- asking an image model to imitate a named devotional painter;
- creating pseudo-scriptural imagery that could misrepresent siddhānta;
- generating sacred personalities casually without doctrinal and design review.

## File-size policy

- small SVG/PNG assets may live in Git;
- large source media belongs in governed Drive storage with a stable manifest link;
- introduce Git LFS only after a documented need and repository-maintainer approval;
- no LFS merely to hide an uncontrolled media dump.

## Deliverables

- visual library architecture;
- rights policy;
- asset templates;
- updated `.gitignore` if required;
- visual validation specification;
- `build-evidence/V7-VISUAL-ARCHITECTURE-REPORT.md`.
