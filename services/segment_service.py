from datetime import datetime

from config.database import (
    segments_collection
)


def get_all_segments():

    segments = list(
        segments_collection.find(
            {},
            {"_id": 0}
        )
    )

    return {
    "success": True,
    "data": segments
}


def get_segment_by_id(
    segment_id
):

    segment = segments_collection.find_one(
        {
            "segment_id":
            segment_id
        },
        {
            "_id": 0
        }
    )

    if not segment:
        return {
            "success": False,
            "message": "Segment not found"
        }

    return {
        "success": True,
        "data": segment
    }


def create_segment(data):

    count = (
        segments_collection.count_documents({})
        + 1
    )

    segment_id = (
        f"SEG{str(count).zfill(3)}"
    )

    document = {
        "segment_id":
            segment_id,
        "segment_name":
            data.segment_name,
        "created_by":
            "Manual",
        "description":
            data.description,
        "filters":
            data.filters,
        "audience_count":
            0,
        "status":
            "Active",
        "created_at":
            datetime.utcnow(),
        "updated_at":
            datetime.utcnow()
    }

    segments_collection.insert_one(
        document
    )

    return {
        "success": True,
        "message":
            "Segment created",
        "segment_id":
            segment_id
    }


def update_segment(
    segment_id,
    data
):

    result = (
        segments_collection.update_one(
            {
                "segment_id":
                segment_id
            },
            {
                "$set": {
                    "segment_name":
                        data.segment_name,
                    "description":
                        data.description,
                    "filters":
                        data.filters,
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
            "Segment not found"
        }

    return {
        "success": True,
        "message":
        "Segment updated"
    }


def delete_segment(
    segment_id
):

    result = (
        segments_collection.delete_one(
            {
                "segment_id":
                segment_id
            }
        )
    )

    if result.deleted_count == 0:
        return {
            "success": False,
            "message":
            "Segment not found"
        }

    return {
        "success": True,
        "message":
        "Segment deleted"
    }