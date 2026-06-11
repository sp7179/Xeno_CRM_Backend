from datetime import datetime

from config.database import (
    campaigns_collection,
    segments_collection
)


def get_all_campaigns():

    campaigns = list(
        campaigns_collection.find(
            {},
            {"_id": 0}
        )
    )

    return {
    "success": True,
    "data": campaigns
}


def get_campaign_by_id(
    campaign_id
):

    campaign = campaigns_collection.find_one(
        {
            "campaign_id":
            campaign_id
        },
        {
            "_id": 0
        }
    )

    if not campaign:
        return {
            "success": False,
            "message": "Campaign not found"
        }

    return {
        "success": True,
        "data": campaign
    }


def create_campaign(data):

    segment = (
        segments_collection.find_one(
            {
                "segment_id":
                data.segment_id
            }
        )
    )

    if not segment:
        return {
            "success": False,
            "message": "Segment not found"
        }

    count = (
        campaigns_collection
        .count_documents({})
        + 1
    )

    campaign_id = (
        f"CMP{str(count).zfill(3)}"
    )

    document = {
        "campaign_id":
            campaign_id,

        "campaign_name":
            data.campaign_name,

        "segment_id":
            data.segment_id,

        "channel":
            data.channel,

        "message":
            data.message,

        "campaign_status":
            "Draft",

        "audience_size":
            segment.get(
                "audience_count",
                0
            ),

        "sent_count":
            0,

        "delivered_count":
            0,

        "opened_count":
            0,

        "clicked_count":
            0,

        "conversion_count":
            0,

        "created_at":
            datetime.utcnow(),

        "updated_at":
            datetime.utcnow()
    }

    campaigns_collection.insert_one(
        document
    )

    return {
        "success": True,
        "message":
            "Campaign created",
        "campaign_id":
            campaign_id
    }


def update_campaign(
    campaign_id,
    data
):

    result = (
        campaigns_collection.update_one(
            {
                "campaign_id":
                campaign_id
            },
            {
                "$set": {
                    "campaign_name":
                        data.campaign_name,

                    "segment_id":
                        data.segment_id,

                    "channel":
                        data.channel,

                    "message":
                        data.message,

                    "campaign_status":
                        data.campaign_status,

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
                "Campaign not found"
        }

    return {
        "success": True,
        "message":
            "Campaign updated"
    }


def delete_campaign(
    campaign_id
):

    result = (
        campaigns_collection.delete_one(
            {
                "campaign_id":
                campaign_id
            }
        )
    )

    if result.deleted_count == 0:
        return {
            "success": False,
            "message":
                "Campaign not found"
        }

    return {
        "success": True,
        "message":
            "Campaign deleted"
    }


def launch_campaign(
    campaign_id
):

    result = (
        campaigns_collection.update_one(
            {
                "campaign_id":
                campaign_id
            },
            {
                "$set": {
                    "campaign_status":
                        "Launched",

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
                "Campaign not found"
        }

    return {
        "success": True,
        "message":
            "Campaign launched"
    }