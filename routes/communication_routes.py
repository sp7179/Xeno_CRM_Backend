from fastapi import APIRouter

from schemas.communication_schema import (
    CommunicationCreate
)

from services.communication_service import (
    get_all_communications,
    get_communication_by_id,
    create_communication
)

router = APIRouter(
    prefix="/api/communications",
    tags=["Communications"]
)


@router.get("")
def get_communications():
    return get_all_communications()


@router.get("/{communication_id}")
def get_communication(
    communication_id: str
):
    return get_communication_by_id(
        communication_id
    )


@router.post("")
def add_communication(
    request: CommunicationCreate
):
    return create_communication(
        request
    )