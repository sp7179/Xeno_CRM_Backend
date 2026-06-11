"""
INPUT:
Customer Requests

CALLS:
customer_service.py

COLLECTION:
customers
"""

from fastapi import APIRouter

from schemas.customer_schema import (
    CustomerCreate,
    CustomerUpdate
)

from services.customer_service import (
    get_all_customers,
    get_customer_by_id,
    create_customer,
    update_customer,
    delete_customer
)

router = APIRouter(
    prefix="/api/customers",
    tags=["Customers"]
)


@router.get("")
def get_customers():
    return get_all_customers()


@router.get("/{customer_id}")
def get_customer(
    customer_id: str
):
    return get_customer_by_id(
        customer_id
    )


@router.post("")
def add_customer(
    request: CustomerCreate
):
    return create_customer(
        request
    )


@router.put("/{customer_id}")
def edit_customer(
    customer_id: str,
    request: CustomerUpdate
):
    return update_customer(
        customer_id,
        request
    )


@router.delete("/{customer_id}")
def remove_customer(
    customer_id: str
):
    return delete_customer(
        customer_id
    )