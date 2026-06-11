from pydantic import BaseModel
from typing import Dict


class SegmentCreate(BaseModel):
    segment_name: str
    description: str
    filters: Dict


class SegmentUpdate(BaseModel):
    segment_name: str
    description: str
    filters: Dict
    status: str