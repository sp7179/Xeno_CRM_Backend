from datetime import datetime

from config.database import (
    orders_collection,
    customers_collection
)


def get_all_orders():

    orders = list(
        orders_collection.find(
            {},
            {"_id": 0}
        )
    )

    return {
    "success": True,
    "data": orders
}


def get_order_by_id(order_id):

    order = orders_collection.find_one(
        {
            "order_id": order_id
        },
        {
            "_id": 0
        }
    )

    if not order:
        return {
            "success": False,
            "message": "Order not found"
        }

        return {
    "success": True,
    "data": orders
}


def create_order(data):

    customer = customers_collection.find_one(
        {
            "customer_id":
            data.customer_id
        }
    )

    if not customer:
        return {
            "success": False,
            "message": "Customer not found"
        }

    count = (
        orders_collection.count_documents({})
        + 1
    )

    order_id = (
        f"ORD{str(count).zfill(3)}"
    )

    document = {
        "order_id": order_id,
        "customer_id":
            data.customer_id,
        "amount":
            data.amount,
        "items_count":
            data.items_count,
        "category":
            data.category,
        "payment_method":
            data.payment_method,
        "order_date":
            datetime.utcnow(),
        "order_status":
            "Delivered",
        "created_at":
            datetime.utcnow(),
        "updated_at":
            datetime.utcnow()
    }

    orders_collection.insert_one(
        document
    )

    customers_collection.update_one(
        {
            "customer_id":
            data.customer_id
        },
        {
            "$inc": {
                "total_orders": 1,
                "total_spend":
                data.amount
            },
            "$set": {
                "last_order_date":
                datetime.utcnow()
            }
        }
    )

    return {
        "success": True,
        "message": "Order created",
        "order_id": order_id
    }


def update_order(
    order_id,
    data
):

    result = orders_collection.update_one(
        {
            "order_id":
            order_id
        },
        {
            "$set": {
                "amount":
                    data.amount,
                "items_count":
                    data.items_count,
                "category":
                    data.category,
                "payment_method":
                    data.payment_method,
                "order_status":
                    data.order_status,
                "updated_at":
                    datetime.utcnow()
            }
        }
    )

    if result.modified_count == 0:
        return {
            "success": False,
            "message": "Order not found"
        }

    return {
        "success": True,
        "message": "Order updated"
    }


def delete_order(
    order_id
):

    result = orders_collection.delete_one(
        {
            "order_id":
            order_id
        }
    )

    if result.deleted_count == 0:
        return {
            "success": False,
            "message": "Order not found"
        }

    return {
        "success": True,
        "message": "Order deleted"
    }