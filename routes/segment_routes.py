from fastapi import APIRouter

from schemas.segment_schema import (
    SegmentCreate,
    SegmentUpdate
)

from services.segment_service import (
    get_all_segments,
    get_segment_by_id,
    create_segment,
    update_segment,
    delete_segment
)

router = APIRouter(
    prefix="/api/segments",
    tags=["Segments"]
)


@router.get("")
def get_segments():
    return get_all_segments()


@router.get("/{segment_id}")
def get_segment(
    segment_id: str
):
    return get_segment_by_id(
        segment_id
    )


@router.post("")
def add_segment(
    request: SegmentCreate
):
    return create_segment(
        request
    )


@router.put("/{segment_id}")
def edit_segment(
    segment_id: str,
    request: SegmentUpdate
):
    return update_segment(
        segment_id,
        request
    )


@router.delete("/{segment_id}")
def remove_segment(
    segment_id: str
):
    return delete_segment(
        segment_id
    )