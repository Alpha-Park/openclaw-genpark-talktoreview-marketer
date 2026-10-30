# -*- coding: utf-8 -*-
"""
OpenClaw GenPark TalkToReview Marketer FastMCP Server
"""

import json
from typing import Dict, List, Any, Optional
from mcp.server.fastmcp import FastMCP
from client import OpenClawGenParkTalkToReviewMarketer

mcp = FastMCP("openclaw-genpark-talktoreview-marketer")
marketer = OpenClawGenParkTalkToReviewMarketer()

@mcp.tool()
def decompose_aspect_based_sentiment(
    review_text: str,
    aspects_json: Optional[str] = None
) -> str:
    """
    Decomposes review text into multi-attribute Aspect-Based Sentiment Analysis (ABSA) polarities.
    """
    aspects = json.loads(aspects_json) if aspects_json else None
    res = marketer.decompose_aspect_based_sentiment(review_text, aspects)
    return json.dumps(res, indent=2)

@mcp.tool()
def audit_review_fraud_anomalies(reviews_json: str) -> str:
    """
    Audits review batches for authenticity fraud: checks Benford's Law and Poisson burst anomalies.
    """
    reviews = json.loads(reviews_json)
    res = marketer.audit_review_fraud_anomalies(reviews)
    return json.dumps(res, indent=2)

@mcp.tool()
def compose_reputation_recovery_response(
    review_json: str,
    brand_tone: str = "empathic_professional"
) -> str:
    """
    Composes reputation recovery responses using the HEAR framework.
    """
    review = json.loads(review_json)
    res = marketer.compose_reputation_recovery_response(review, brand_tone)
    return json.dumps(res, indent=2)

def main():
    print("Testing TalkToReview Marketer:")
    print(decompose_aspect_based_sentiment("The quality is amazing, but shipping was a terrible delay."))

if __name__ == "__main__":
    main()
