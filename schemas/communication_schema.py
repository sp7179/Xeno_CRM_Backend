from pydantic import BaseModel


class CommunicationCreate(BaseModel):
    campaign_id: str
    customer_id: str
    channel: str
    message: str
    delivery_status: str