# openclaw-genpark-talktoreview-marketer

![Tests](https://img.shields.io/badge/tests-passing-brightgreen)
![License](https://img.shields.io/badge/license-MIT-blue)
![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![Dependencies](https://img.shields.io/badge/dependencies-zero-success)
![Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen)

OpenClaw GenPark TalkToReview Marketer is a zero-dependency customer sentiment intelligence and brand reputation engine implementing Aspect-Based Sentiment Analysis (ABSA), Benford's Law and Poisson burst review fraud anomaly detection, and automated HEAR framework reputation recovery copywriting.

```mermaid
flowchart TD
    A[Customer Review Text] --> B[Sentence-Level ABSA Tokenizer]
    B --> C[Aspect Polarities: Shipping, Quality, Usability]
    D[Review Batch Stream] --> E[Benford's Law & Poisson Burst Engine]
    E --> F[Authenticity & Fraud Anomaly Score]
    G[1-Star / Negative Review] --> H[HEAR Framework Generator]
    H --> I[Empathic Recovery & Priority Support Escalation]
```

## Features
- **Aspect-Based Sentiment (ABSA)**: Evaluates granular sentiment polarities across distinct dimensions (shipping, product quality, service, usability).
- **Fraud Anomaly Auditor**: Flags fabricated review campaigns using Benford's Law digit deviations and Poisson temporal clustering bursts.
- **HEAR Recovery Framework**: Generates empathic, brand-aligned responses to de-escalate churn and recover customer trust.

## Quickstart

```python
from client import OpenClawGenParkTalkToReviewMarketer

marketer = OpenClawGenParkTalkToReviewMarketer()
res = marketer.decompose_aspect_based_sentiment("Quality is top notch but shipping took forever.")
print("Quality:", res["aspects"]["quality"]["status"])
```

## License
MIT
