# -*- coding: utf-8 -*-
"""
OpenClaw GenPark TalkToReview Marketer Client
Zero-dependency Aspect-Based Sentiment Analysis (ABSA) decomposition,
Benford's Law & Poisson burst review fraud detector, and HEAR reputation recovery copy composer.
"""

import math
from typing import Dict, List, Any, Optional

class OpenClawGenParkTalkToReviewMarketer:
    """
    Decomposes customer reviews into aspect sentiments, audits fraud and unnatural burst spikes,
    and drafts empathic reputation recovery responses.
    """

    DEFAULT_ASPECTS = ["shipping", "quality", "service", "pricing", "usability"]

    SENTIMENT_LEXICON = {
        "positive": ["excellent", "great", "fast", "love", "amazing", "reliable", "perfect", "clean", "easy", "impressed", "worth"],
        "negative": ["terrible", "broken", "slow", "poor", "hate", "scam", "defect", "expensive", "confusing", "horrible", "delay"]
    }

    def decompose_aspect_based_sentiment(
        self,
        review_text: str,
        aspects: Optional[List[str]] = None
    ) -> Dict[str, Any]:
        """
        Decomposes review text into multi-attribute Aspect-Based Sentiment Analysis (ABSA) polarities.
        Polarity scale: [-1.0, 1.0]
        """
        if not review_text:
            raise ValueError("Review text cannot be empty.")

        target_aspects = aspects or self.DEFAULT_ASPECTS
        sentences = [s.strip().lower() for s in review_text.replace("!", ".").replace("?", ".").split(".") if s.strip()]

        aspect_results = {}
        for asp in target_aspects:
            relevant_sentences = [s for s in sentences if asp in s]
            if not relevant_sentences:
                aspect_results[asp] = {"mentioned": False, "polarity": 0.0, "status": "NEUTRAL"}
                continue

            pos_hits = sum(sum(1 for w in self.SENTIMENT_LEXICON["positive"] if w in s) for s in relevant_sentences)
            neg_hits = sum(sum(1 for w in self.SENTIMENT_LEXICON["negative"] if w in s) for s in relevant_sentences)

            total_hits = pos_hits + neg_hits
            polarity = round((pos_hits - neg_hits) / max(1, total_hits), 2) if total_hits > 0 else 0.0
            status = "POSITIVE" if polarity >= 0.25 else ("NEGATIVE" if polarity <= -0.25 else "NEUTRAL")

            aspect_results[asp] = {
                "mentioned": True,
                "polarity": polarity,
                "status": status,
                "sentence_matches": len(relevant_sentences)
            }

        overall_pos = sum(sum(1 for w in self.SENTIMENT_LEXICON["positive"] if w in s) for s in sentences)
        overall_neg = sum(sum(1 for w in self.SENTIMENT_LEXICON["negative"] if w in s) for s in sentences)
        overall_polarity = round((overall_pos - overall_neg) / max(1, overall_pos + overall_neg), 2)

        return {
            "review_length_chars": len(review_text),
            "sentence_count": len(sentences),
            "overall_polarity": overall_polarity,
            "overall_sentiment": "POSITIVE" if overall_polarity >= 0.2 else ("NEGATIVE" if overall_polarity <= -0.2 else "MIXED"),
            "aspects": aspect_results
        }

    def audit_review_fraud_anomalies(
        self,
        reviews: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        """
        Audits review batches for authenticity fraud: checks Benford's Law distribution
        on review length digits and Poisson burst frequency anomalies.
        """
        if not reviews:
            raise ValueError("Reviews list cannot be empty.")

        n = len(reviews)
        lengths = [len(r.get("text", "")) for r in reviews if len(r.get("text", "")) > 0]
        first_digits = [int(str(l)[0]) for l in lengths if l > 0]

        # Benford's Law theoretical probabilities P(d) = log10(1 + 1/d)
        benford_expected = {d: math.log10(1.0 + 1.0 / d) for d in range(1, 10)}
        
        # Observed digit distribution
        observed_counts = {d: 0 for d in range(1, 10)}
        for d in first_digits:
            if 1 <= d <= 9:
                observed_counts[d] += 1

        total_obs = max(1, len(first_digits))
        chi_square = 0.0
        for d in range(1, 10):
            obs = observed_counts[d]
            exp = benford_expected[d] * total_obs
            chi_square += ((obs - exp) ** 2) / max(1e-9, exp)

        # Poisson burst check: timestamp clustering
        timestamps = sorted([r.get("timestamp_epoch", 0) for r in reviews if "timestamp_epoch" in r])
        burst_detected = False
        if len(timestamps) >= 5:
            # Check if 5+ reviews occurred in < 1 hour (3600 sec)
            for i in range(len(timestamps) - 4):
                if timestamps[i + 4] - timestamps[i] < 3600:
                    burst_detected = True
                    break

        fraud_risk_score = round(min(100.0, chi_square * 3.5 + (40.0 if burst_detected else 0.0)), 1)

        return {
            "total_reviews_audited": n,
            "benford_chi_square_metric": round(chi_square, 2),
            "poisson_burst_detected": burst_detected,
            "fraud_risk_score": fraud_risk_score,
            "authenticity_rating": "AUTHENTIC_ORGANIC" if fraud_risk_score < 35.0 else ("SUSPICIOUS_ANOMALY" if fraud_risk_score < 70.0 else "HIGH_FRAUD_BURST")
        }

    def compose_reputation_recovery_response(
        self,
        review: Dict[str, Any],
        brand_tone: str = "empathic_professional"
    ) -> Dict[str, Any]:
        """
        Composes reputation recovery responses using the HEAR framework (Hear, Empathize, Apologize, Resolve).
        """
        star_rating = review.get("rating", 1)
        author = review.get("author", "Valued Customer")
        issue = review.get("primary_complaint", "your recent experience")

        if star_rating <= 2:
            opening = f"Dear {author}, thank you for bringing this to our attention. We are deeply sorry that {issue} did not meet our high standards."
            empathy = "We completely understand your frustration and take full accountability for this shortfall."
            resolution = "Our senior support team has flagged your account and would like to offer a direct refund or immediate priority replacement. Please contact executive-support@alphapark.io with reference code #REP-RECOVERY."
        elif star_rating == 3:
            opening = f"Hi {author}, thank you for your honest feedback regarding {issue}."
            empathy = "We appreciate you highlighting areas where we can improve."
            resolution = "We've passed your feedback directly to our product engineering team and would love to offer you a complimentary service credit on your next cycle."
        else:
            opening = f"Hi {author}, thank you so much for the stellar feedback!"
            empathy = "We are thrilled to hear you had a great experience."
            resolution = "We look forward to serving you again soon!"

        full_reply = f"{opening} {empathy} {resolution}"

        return {
            "star_rating": star_rating,
            "author": author,
            "brand_tone": brand_tone,
            "framework": "HEAR (Hear, Empathize, Apologize, Resolve)",
            "response_text": full_reply,
            "recommended_escalation": "DIRECT_REFUND_OR_REPLACEMENT" if star_rating <= 2 else "STANDARD_FOLLOWUP"
        }
