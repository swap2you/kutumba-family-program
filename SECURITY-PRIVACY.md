# Security and Privacy

## Repository visibility (governing decision)

KUTUMBA is a **public documentation and curriculum-development repository** on GitHub during the development and review period. This is intentional.

Public access applies **only** to:

- general program content
- source-controlled operating models
- curriculum materials and architecture
- templates and production prompts
- non-sensitive reference metadata (indexes without bulk third-party files)

## Prohibited content in Git

Regardless of visibility, the following must **never** be committed:

| Category | Examples |
|---|---|
| Credentials | passwords, API keys, tokens, service-account files |
| Private participant data | family contact records, attendance, mentor notes |
| Completed forms | applications, surveys with personal answers |
| Child records | identifiers, safeguarding case detail |
| Health data | medical or allergy response records tied to individuals |
| Incident records | safeguarding incidents, disciplinary case files |
| Confidential care records | pastoral or family-care notes |

Automated validation runs heuristic checks for common secret patterns and prohibited record types. **Automated heuristic checks passed does not replace human review.**

## Public curriculum is permitted

Governance charters, operating models, curriculum architecture, detailed lesson sources, templates, and reference indexes (metadata only) may remain public when they contain no private participant data.

## Local path provenance

Reference indexes use `source_root_id` and portable relative paths. Machine-specific absolute paths belong in the gitignored file `config/local-source-roots.yaml` (see `config/local-source-roots.example.yaml`).

## Legacy and third-party material

Legacy Bhaktivriksha, Granth, and Jayapataka BV collections are **indexed only** — not bulk-copied. See [RIGHTS-AND-USE.md](RIGHTS-AND-USE.md).

## Reporting

Report privacy concerns to the Repository Curator through the project governance channel.
