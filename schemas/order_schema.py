from pydantic import BaseModel


class OrderCreate(BaseModel):
    customer_id: str
    amount: float
    items_count: int
    category: str
    payment_method: str


class OrderUpdate(BaseModel):
    amount: float
    items_count: int
    category: str
    payment_method: str
    order_status: str