from fastapi import APIRouter

from schemas.order_schema import (
    OrderCreate,
    OrderUpdate
)

from services.order_service import (
    get_all_orders,
    get_order_by_id,
    create_order,
    update_order,
    delete_order
)

router = APIRouter(
    prefix="/api/orders",
    tags=["Orders"]
)


@router.get("")
def get_orders():
    return get_all_orders()


@router.get("/{order_id}")
def get_order(
    order_id: str
):
    return get_order_by_id(
        order_id
    )


@router.post("")
def add_order(
    request: OrderCreate
):
    return create_order(
        request
    )


@router.put("/{order_id}")
def edit_order(
    order_id: str,
    request: OrderUpdate
):
    return update_order(
        order_id,
        request
    )


@router.delete("/{order_id}")
def remove_order(
    order_id: str
):
    return delete_order(
        order_id
    )