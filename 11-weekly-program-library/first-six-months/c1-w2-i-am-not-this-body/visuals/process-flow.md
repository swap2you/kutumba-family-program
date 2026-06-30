# Process Flow

Rendered viewer for [`process-flow.mmd`](process-flow.mmd). Open this file in Markdown preview to see the diagram.

```mermaid
flowchart LR
    START([Family photo question]) --> STAGES

    subgraph STAGES["BG 2.13 — Life stages"]
        S1[Baby / kaumāra]
        S2[Youth / yauvana]
        S3[Older / jarā]
        S1 --> S2 --> S3
    end

    STAGES --> DEHI["Same dehī observes all stages"]
    DEHI --> SOBER[Sober — not bewildered]

    subgraph GARMENT["BG 2.22 — Garment analogy"]
        G1[Old garment]
        G2[New garment]
        G1 -->|soul changes| G2
    end

    SOBER --> GARMENT
    GARMENT --> CARE

    subgraph CARE["Body care for service"]
        C1[Sleep / food / medicine]
        C2[Cleanliness / movement]
        C3[Chant & hear]
        C1 --> SVC[Kṛṣṇa's service]
        C2 --> SVC
        C3 --> SVC
    end

    CARE --> IDENTITY["CC Madhya 20.108 — eternal servant"]
    IDENTITY --> PAUSE([Daily identity pause])
```

_Source file: `process-flow.mmd` — edit the `.mmd` file for diagram changes._
