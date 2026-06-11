"""
INPUT:
Product Forms

COLLECTION:
products

USED BY:
product_service.py
"""

from pydantic import BaseModel


class ProductCreate(BaseModel):
    product_name: str
    category: str
    description: str
    price: float
    stock_quantity: int


class ProductUpdate(BaseModel):
    product_name: str
    category: str
    description: str
    price: float
    stock_quantity: int
    status: str