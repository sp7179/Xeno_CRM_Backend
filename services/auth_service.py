"""
INPUT:
Frontend Login/Register

COLLECTION:
users

OUTPUT:
JWT + User Data

USED BY:
Login Page
All Future Services

ROUTES:
POST /api/auth/register
POST /api/auth/login
GET /api/auth/me
"""

from datetime import datetime

from config.database import users_collection

from utils.password_handler import (
    hash_password,
    verify_password
)

from utils.jwt_handler import (
    create_access_token,
    verify_access_token
)


def register_user(data):

    existing_user = users_collection.find_one(
        {"email": data.email}
    )

    if existing_user:
        return {
            "success": False,
            "message": "Email already exists"
        }

    user_count = users_collection.count_documents({}) + 1

    user_id = f"USR{str(user_count).zfill(3)}"

    user_doc = {
        "user_id": user_id,
        "name": data.name,
        "email": data.email,
        "password_hash": hash_password(
            data.password
        ),
        "role": data.role,
        "is_active": True,
        "last_login": None,
        "created_at": datetime.utcnow(),
        "updated_at": datetime.utcnow()
    }

    users_collection.insert_one(
        user_doc
    )

    return {
        "success": True,
        "message": "User created successfully",
        "user_id": user_id
    }


def login_user(data):

    user = users_collection.find_one(
        {"email": data.email}
    )

    if not user:
        return {
            "success": False,
            "message": "Invalid credentials"
        }

    if not user["is_active"]:
        return {
            "success": False,
            "message": "User disabled"
        }

    if not verify_password(
        data.password,
        user["password_hash"]
    ):
        return {
            "success": False,
            "message": "Invalid credentials"
        }

    token = create_access_token(
        {
            "user_id": user["user_id"],
            "email": user["email"],
            "role": user["role"]
        }
    )

    users_collection.update_one(
        {"user_id": user["user_id"]},
        {
            "$set": {
                "last_login": datetime.utcnow(),
                "updated_at": datetime.utcnow()
            }
        }
    )

    return {
        "success": True,
        "access_token": token,
        "token_type": "bearer",
        "user": {
            "user_id": user["user_id"],
            "name": user["name"],
            "email": user["email"],
            "role": user["role"]
        }
    }


def get_current_user(token: str):

    payload = verify_access_token(
        token
    )

    if not payload:
        return {
            "success": False,
            "message": "Invalid token"
        }

    user = users_collection.find_one(
        {
            "user_id": payload["user_id"]
        }
    )

    if not user:
        return {
            "success": False,
            "message": "User not found"
        }

    if not user["is_active"]:
        return {
            "success": False,
            "message": "User disabled"
        }

    return {
        "success": True,
        "user": {
            "user_id": user["user_id"],
            "name": user["name"],
            "email": user["email"],
            "role": user["role"]
        }
    }