"""
INPUT:
Customer CRUD Requests

COLLECTION:
customers

OUTPUT:
Customer Data

USED BY:
customer_routes.py
"""

from datetime import datetime

from config.database import customers_collection


def get_all_customers():

    customers = list(
        customers_collection.find(
            {},
            {"_id": 0}
        )
    )

    return {
        "success": True,
        "customers": customers
    }


def get_customer_by_id(customer_id):

    customer = customers_collection.find_one(
        {
            "customer_id": customer_id
        },
        {
            "_id": 0
        }
    )

    if not customer:
        return {
            "success": False,
            "message": "Customer not found"
        }

    return {
        "success": True,
        "customer": customer
    }


def create_customer(data):

    existing_customer = customers_collection.find_one(
        {
            "email": data.email
        }
    )

    if existing_customer:
        return {
            "success": False,
            "message": "Customer email already exists"
        }

    count = (
        customers_collection.count_documents({})
        + 1
    )

    customer_id = (
        f"CUST{str(count).zfill(3)}"
    )

    document = {
        "customer_id": customer_id,
        "name": data.name,
        "email": data.email,
        "phone": data.phone,
        "gender": data.gender,
        "city": data.city,
        "state": data.state,
        "signup_date": datetime.utcnow(),
        "total_orders": 0,
        "total_spend": 0,
        "last_order_date": None,
        "customer_status": "Active",
        "preferred_channel": data.preferred_channel,
        "tags": data.tags,
        "created_at": datetime.utcnow(),
        "updated_at": datetime.utcnow()
    }

    customers_collection.insert_one(
        document
    )

    return {
        "success": True,
        "message": "Customer created",
        "customer_id": customer_id
    }

def update_customer(
    customer_id,
    data
):

    result = customers_collection.update_one(
        {
            "customer_id": customer_id
        },
        {
            "$set": {
                "name": data.name,
                "email": data.email,
                "phone": data.phone,
                "gender": data.gender,
                "city": data.city,
                "state": data.state,
                "preferred_channel": data.preferred_channel,
                "tags": data.tags,
                "updated_at": datetime.utcnow()
            }
        }
    )

    if result.modified_count == 0:
        return {
            "success": False,
            "message": "Customer not found"
        }

    return {
        "success": True,
        "message": "Customer updated"
    }


def delete_customer(
    customer_id
):

    result = customers_collection.delete_one(
        {
            "customer_id": customer_id
        }
    )

    if result.deleted_count == 0:
        return {
            "success": False,
            "message": "Customer not found"
        }

    return {
        "success": True,
        "message": "Customer deleted"
    }