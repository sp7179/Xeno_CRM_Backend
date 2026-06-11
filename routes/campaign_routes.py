from fastapi import APIRouter

from schemas.campaign_schema import (
    CampaignCreate,
    CampaignUpdate
)

from services.campaign_service import (
    get_all_campaigns,
    get_campaign_by_id,
    create_campaign,
    update_campaign,
    delete_campaign,
    launch_campaign
)

router = APIRouter(
    prefix="/api/campaigns",
    tags=["Campaigns"]
)


@router.get("")
def get_campaigns():
    return get_all_campaigns()


@router.get("/{campaign_id}")
def get_campaign(
    campaign_id: str
):
    return get_campaign_by_id(
        campaign_id
    )


@router.post("")
def add_campaign(
    request: CampaignCreate
):
    return create_campaign(
        request
    )


@router.put("/{campaign_id}")
def edit_campaign(
    campaign_id: str,
    request: CampaignUpdate
):
    return update_campaign(
        campaign_id,
        request
    )


@router.delete("/{campaign_id}")
def remove_campaign(
    campaign_id: str
):
    return delete_campaign(
        campaign_id
    )


@router.post("/{campaign_id}/launch")
def launch(
    campaign_id: str
):
    return launch_campaign(
        campaign_id
    )