from pydantic import BaseModel


class CampaignCreate(BaseModel):
    campaign_name: str
    segment_id: str
    channel: str
    message: str


class CampaignUpdate(BaseModel):
    campaign_name: str
    segment_id: str
    channel: str
    message: str
    campaign_status: str