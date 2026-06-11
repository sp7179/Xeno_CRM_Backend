"""
INPUT:
Product CRUD Requests

COLLECTION:
products

OUTPUT:
Product Data

USED BY:
product_routes.py
"""

from datetime import datetime

from config.database import products_collection


def get_all_products():

    products = list(
        products_collection.find(
            {},
            {"_id": 0}
        )
    )

    return {
    "success": True,
    "data": products
}


def get_product_by_id(
    product_id
):

    product = products_collection.find_one(
        {
            "product_id": product_id
        },
        {
            "_id": 0
        }
    )

    if not product:
        return {
            "success": False,
            "message": "Product not found"
        }

    return {
        "success": True,
        "product": product
    }


def create_product(data):

    existing_product = (
        products_collection.find_one(
            {
                "product_name":
                data.product_name
            }
        )
    )

    if existing_product:
        return {
            "success": False,
            "message": "Product already exists"
        }

    count = (
        products_collection
        .count_documents({})
        + 1
    )

    product_id = (
        f"PRD{str(count).zfill(3)}"
    )

    document = {
        "product_id": product_id,
        "product_name":
            data.product_name,
        "category":
            data.category,
        "description":
            data.description,
        "price":
            data.price,
        "stock_quantity":
            data.stock_quantity,
        "status":
            "Active",
        "created_at":
            datetime.utcnow(),
        "updated_at":
            datetime.utcnow()
    }

    products_collection.insert_one(
        document
    )

    return {
        "success": True,
        "message":
            "Product created",
        "product_id":
            product_id
    }


def update_product(
    product_id,
    data
):

    result = (
        products_collection.update_one(
            {
                "product_id":
                    product_id
            },
            {
                "$set": {
                    "product_name":
                        data.product_name,
                    "category":
                        data.category,
                    "description":
                        data.description,
                    "price":
                        data.price,
                    "stock_quantity":
                        data.stock_quantity,
                    "status":
                        data.status,
                    "updated_at":
                        datetime.utcnow()
                }
            }
        )
    )

    if result.modified_count == 0:
        return {
            "success": False,
            "message":
                "Product not found"
        }

    return {
        "success": True,
        "message":
            "Product updated"
    }


def delete_product(
    product_id
):

    result = (
        products_collection.delete_one(
            {
                "product_id":
                    product_id
            }
        )
    )

    if result.deleted_count == 0:
        return {
            "success": False,
            "message":
                "Product not found"
        }

    return {
        "success": True,
        "message":
            "Product deleted"
    }