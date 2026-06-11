from pydantic import BaseModel


class AnalyticsResponse(BaseModel):
    success: bool