# Concept Map

Rendered viewer for [`concept-map.mmd`](concept-map.mmd). Open this file in Markdown preview to see the diagram.

```mermaid
flowchart TB
    subgraph CHANGES["What changes (deha / body)"]
        A1[Childhood body]
        A2[Youth body]
        A3[Old age body]
        A4[Appearance / cells / strength]
    end

    subgraph CONTINUES["What continues (dehī / self)"]
        B1[Conscious awareness]
        B2[Capacity to serve Kṛṣṇa]
        B3[Constitutional servant identity]
    end

    subgraph FIELD["BG 13 teaser — field & knower"]
        C1[kṣetra = body as field]
        C2[kṣetrajña = knower]
        C3["Full detail → C1-W3"]
    end

    A1 --> A2 --> A3
    B1 -.->|"same subject"| A1
    B1 -.->|"same subject"| A2
    B1 -.->|"same subject"| A3
    C1 --- A4
    C2 --- B1
    C3 -.->|"deferred"| D1[Subtle body / transmigration]

    style D1 stroke-dasharray: 5 5
```

_Source file: `concept-map.mmd` — edit the `.mmd` file for diagram changes._
