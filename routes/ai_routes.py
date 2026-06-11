from fastapi import APIRouter

from schemas.ai_schema import (
    SegmentBuilderRequest,
    MessageGeneratorRequest,
    CampaignAdvisorRequest,
    BusinessInsightsRequest,
    QuickCampaignRequest
)

from services.ai_service import (
    build_segment,
    generate_message,
    campaign_advisor,
    business_insights,
    quick_campaign
)

router = APIRouter(
    prefix="/api/ai",
    tags=["AI"]
)


@router.post("/segment-builder")
def segment_builder(
    request: SegmentBuilderRequest
):
    return build_segment(
        request
    )


@router.post("/message-generator")
def message_generator(
    request: MessageGeneratorRequest
):
    return generate_message(
        request
    )


@router.post("/campaign-advisor")
def advisor(
    request: CampaignAdvisorRequest
):
    return campaign_advisor(
        request
    )


@router.post("/business-insights")
def insights(
    request: BusinessInsightsRequest
):
    return business_insights(
        request
    )


@router.post("/quick-campaign")
def quick_campaign_route(
    request: QuickCampaignRequest
):
    return quick_campaign(
        request
    )