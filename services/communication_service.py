from datetime import datetime

from config.database import (
    communications_collection
)


def get_all_communications():

    communications = list(
        communications_collection.find(
            {},
            {"_id": 0}
        )
    )

    return {
        "success": True,
        "communications": communications
    }


def get_communication_by_id(
    communication_id
):

    communication = (
        communications_collection.find_one(
            {
                "communication_id":
                communication_id
            },
            {
                "_id": 0
            }
        )
    )

    if not communication:
        return {
            "success": False,
            "message":
            "Communication not found"
        }

    return {
        "success": True,
        "communication":
        communication
    }


def create_communication(
    data
):

    count = (
        communications_collection
        .count_documents({})
        + 1
    )

    communication_id = (
        f"COM{str(count).zfill(3)}"
    )

    document = {
        "communication_id":
            communication_id,

        "campaign_id":
            data.campaign_id,

        "customer_id":
            data.customer_id,

        "channel":
            data.channel,

        "message":
            data.message,

        "delivery_status":
            data.delivery_status,

        "sent_at":
            datetime.utcnow(),

        "created_at":
            datetime.utcnow()
    }

    communications_collection.insert_one(
        document
    )

    return {
        "success": True,
        "message":
            "Communication logged",
        "communication_id":
            communication_id
    }