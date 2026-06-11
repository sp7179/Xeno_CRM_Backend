from pydantic import BaseModel


class SegmentBuilderRequest(BaseModel):
    query: str


class MessageGeneratorRequest(BaseModel):
    campaign_goal: str
    audience: str
    channel: str


class CampaignAdvisorRequest(BaseModel):
    campaign_name: str
    objective: str


class BusinessInsightsRequest(BaseModel):
    question: str


class QuickCampaignRequest(BaseModel):
    business_goal: str