from fastapi import APIRouter

from services.analytics_service import (
    get_overview_analytics,
    get_campaign_analytics
)

router = APIRouter(
    prefix="/api/analytics",
    tags=["Analytics"]
)


@router.get("/overview")
def analytics_overview():

    return get_overview_analytics()


@router.get("/campaigns")
def analytics_campaigns():

    return get_campaign_analytics()