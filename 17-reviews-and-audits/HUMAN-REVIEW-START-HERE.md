# Human Review Start Here

Readable front door for human review. This page summarizes where to review; the controlling gate data remains in [PILOT-READINESS-GATE-REGISTER.yaml](PILOT-READINESS-GATE-REGISTER.yaml).

## Current review state

- Phase: `internal-development-paused`.
- Internal pilot: NO GO.
- Family-facing distribution: NO GO.
- Public publication: NO GO.
- No human reviewer names, decisions, or approvals are populated by this page.
- Automation may prepare evidence, but it cannot approve doctrine, worship, safeguarding, rights, pedagogy, visual design, Gamma, pilot launch, distribution, or publication.

## Unconditional pilot blockers

These gates block internal pilot while open:

- `GATE-SAFE-001` safeguarding policy and children-track launch readiness.
- `GATE-CPO-002` child protection operations and live-session staffing controls.
- `GATE-WOR-003` worship, kirtana, prayer, and bhakti-lab practices.
- `GATE-DOC-004` doctrinal claims and theology teaching suitability.
- `GATE-CIT-005` citation sufficiency and point-of-use source support.
- `GATE-PED-006` pedagogy, age suitability, timing, and family usability.
- `GATE-PD-011` program director launch authorization.
- `GATE-TMP-012` local temple relationship and delivery alignment.
- `GATE-OPS-013` pilot operations, cohort rules, facilitator readiness, and incident handling.

## Feature-dependent gates

These gates remain open and disabled for the founding-pilot scope unless their feature is enabled:

- `GATE-VIS-007` visual design, accessibility, readability, and source fit.
- `GATE-MED-008` media curation, playback suitability, and link status.
- `GATE-GAM-010` Gamma exported deck artifacts and post-render QA.

## Distribution and publication rights gate

`GATE-RGT-009` is distribution/publication-only. It is still open. It blocks family-facing or public release and applies unconditionally to any third-party content actually distributed or played.

## Review packet links

| Review area | Packet |
|---|---|
| Safeguarding | [review-packets/safeguarding-review-packet.md](review-packets/safeguarding-review-packet.md) |
| Worship | [review-packets/worship-review-packet.md](review-packets/worship-review-packet.md) |
| Doctrine/citation | [review-packets/doctrine-and-citation-review-packet.md](review-packets/doctrine-and-citation-review-packet.md) |
| Visual/pedagogy/accessibility | [review-packets/visual-pedagogy-accessibility-review-packet.md](review-packets/visual-pedagogy-accessibility-review-packet.md) |
| Rights/media | [review-packets/rights-and-media-review-packet.md](review-packets/rights-and-media-review-packet.md) |

## How a gate may change from open

A gate may change only when a qualified human reviewer decision is recorded in the repository with evidence. Do not infer closure from automated validation, file existence, or draft completeness.

## Required evidence

Each gate decision needs:

- reviewer name;
- reviewer role;
- date;
- decision;
- evidence path;
- conditions;
- re-review trigger.

## What automation cannot approve

Automation cannot approve human-review gates, launch an internal pilot, approve family-facing distribution, approve public publication, or substitute for local safeguarding, worship, doctrinal, pedagogical, media, rights, Gamma, program director, temple relationship, or pilot operations review.
