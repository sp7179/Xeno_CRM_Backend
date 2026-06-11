"""
INPUT:
Frontend Login/Register

CALLS:
auth_service.py

ROUTES:
POST /api/auth/register
POST /api/auth/login
GET /api/auth/me

OUTPUT:
JWT + User Details
"""

from fastapi import (
    APIRouter,
    Header
)

from schemas.auth_schema import (
    RegisterRequest,
    LoginRequest
)

from services.auth_service import (
    register_user,
    login_user,
    get_current_user
)

router = APIRouter(
    prefix="/api/auth",
    tags=["Authentication"]
)


@router.post("/register")
def register(
    request: RegisterRequest
):
    return register_user(
        request
    )


@router.post("/login")
def login(
    request: LoginRequest
):
    return login_user(
        request
    )


@router.get("/me")
def me(
    authorization: str = Header(None)
):

    if not authorization:
        return {
            "success": False,
            "message": "Token required"
        }

    token = authorization.replace(
        "Bearer ",
        ""
    )

    return get_current_user(
        token
    )