"""
INPUT:
Customer Forms

COLLECTION:
customers

USED BY:
customer_service.py
"""

from pydantic import BaseModel
from typing import List


class CustomerCreate(BaseModel):
    name: str
    email: str
    phone: str
    gender: str
    city: str
    state: str
    preferred_channel: str
    tags: List[str] = []


class CustomerUpdate(BaseModel):
    name: str
    email: str
    phone: str
    gender: str
    city: str
    state: str
    preferred_channel: str
    tags: List[str] = []