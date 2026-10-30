# -*- coding: utf-8 -*-
import json
from client import OpenClawGenParkTalkToReviewMarketer

marketer = OpenClawGenParkTalkToReviewMarketer()

# 1. Aspect-Based Sentiment Analysis (ABSA)
review = "The product quality is amazing and super reliable! However, shipping was a terrible delay and customer service was unhelpful."
absa = marketer.decompose_aspect_based_sentiment(review)
print(f"ABSA Sentiment: Overall={absa['overall_sentiment']} (Polarity: {absa['overall_polarity']})")
for aspect, data in absa["aspects"].items():
    if data["mentioned"]:
        print(f"  [{aspect.upper()}]: Polarity={data['polarity']} -> {data['status']}")

# 2. Fraud & Anomaly Audit (Benford's Law + Poisson Burst)
review_batch = [
    {"text": "Great tool " * 12, "timestamp_epoch": 1730000000},
    {"text": "Super fast " * 18, "timestamp_epoch": 1730000200},
    {"text": "Loved it " * 25, "timestamp_epoch": 1730000400},
    {"text": "Amazing experience " * 30, "timestamp_epoch": 1730000600},
    {"text": "Best purchase ever " * 40, "timestamp_epoch": 1730000800} # artificial burst
]
fraud = marketer.audit_review_fraud_anomalies(review_batch)
print()
print(f"Fraud Audit: Risk={fraud['fraud_risk_score']}/100 ({fraud['authenticity_rating']}) | BurstDetected={fraud['poisson_burst_detected']}")

# 3. Reputation Recovery Response (HEAR Framework)
negative_review = {
    "rating": 1,
    "author": "Marcus Sterling",
    "primary_complaint": "the unexpected shipping delay and damaged packaging"
}
recovery = marketer.compose_reputation_recovery_response(negative_review)
print()
print(f"Reputation Recovery Response ({recovery['framework']}):")
print(f"  {recovery['response_text']}")
