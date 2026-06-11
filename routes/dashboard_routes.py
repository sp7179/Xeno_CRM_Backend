from fastapi import APIRouter

from services.dashboard_service import (
    get_dashboard_overview
)

router = APIRouter(
    prefix="/api/dashboard",
    tags=["Dashboard"]
)


@router.get("/overview")
def dashboard_overview():

    return get_dashboard_overview()