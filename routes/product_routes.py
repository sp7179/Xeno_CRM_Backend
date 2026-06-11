"""
INPUT:
Product Requests

CALLS:
product_service.py

COLLECTION:
products
"""

from fastapi import APIRouter

from schemas.product_schema import (
    ProductCreate,
    ProductUpdate
)

from services.product_service import (
    get_all_products,
    get_product_by_id,
    create_product,
    update_product,
    delete_product
)

router = APIRouter(
    prefix="/api/products",
    tags=["Products"]
)


@router.get("")
def get_products():
    return get_all_products()


@router.get("/{product_id}")
def get_product(
    product_id: str
):
    return get_product_by_id(
        product_id
    )


@router.post("")
def add_product(
    request: ProductCreate
):
    return create_product(
        request
    )


@router.put("/{product_id}")
def edit_product(
    product_id: str,
    request: ProductUpdate
):
    return update_product(
        product_id,
        request
    )


@router.delete("/{product_id}")
def remove_product(
    product_id: str
):
    return delete_product(
        product_id
    )