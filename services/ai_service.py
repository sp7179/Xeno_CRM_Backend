"""
INPUT:
AI Requests

OUTPUT:
Gemini Responses

USED BY:
ai_routes.py
"""

from utils.gemini_client import (
    ask_gemini
)


def build_segment(data):

    prompt = f"""
    Create customer segmentation logic.

    User Query:
    {data.query}

    Return:
    Segment Name
    Filters
    Audience Description
    """

    return {
        "success": True,
        "result": ask_gemini(prompt)
    }


def generate_message(data):

    prompt = f"""
    Create a marketing message.

    Goal:
    {data.campaign_goal}

    Audience:
    {data.audience}

    Channel:
    {data.channel}

    Generate high converting content.
    """

    return {
        "success": True,
        "result": ask_gemini(prompt)
    }


def campaign_advisor(data):

    prompt = f"""
    Campaign Name:
    {data.campaign_name}

    Objective:
    {data.objective}

    Suggest:

    Best Audience
    Best Channel
    Best Timing
    Expected Outcome
    """

    return {
        "success": True,
        "result": ask_gemini(prompt)
    }


def business_insights(data):

    prompt = f"""
    Business Analytics Question:

    {data.question}

    Provide detailed business insights.
    """

    return {
        "success": True,
        "result": ask_gemini(prompt)
    }


def quick_campaign(data):

    prompt = f"""
    Business Goal:

    {data.business_goal}

    Create:

    Campaign Name
    Target Audience
    Channel
    Message
    CTA
    """

    return {
        "success": True,
        "result": ask_gemini(prompt)
    }