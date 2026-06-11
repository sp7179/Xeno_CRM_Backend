from pydantic import BaseModel, EmailStr, field_validator
import re

class RegisterRequest(BaseModel):
    name: str
    email: EmailStr
    password: str
    role: str

    @field_validator("password")
    @classmethod
    def validate_password(cls, value):

        if len(value) < 12 or len(value) > 16:
            raise ValueError(
                "Password must be 12-16 characters"
            )

        if not re.search(r"[A-Z]", value):
            raise ValueError(
                "Password must contain an uppercase letter"
            )

        if not re.search(r"\d", value):
            raise ValueError(
                "Password must contain a number"
            )
        if not re.search(r"[a-z]", value):
            raise ValueError(
                "Password must contain a lowercase letter"
            )

        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", value):
            raise ValueError(
                "Password must contain a special character"
            )

        return value

class LoginRequest(BaseModel):
    email: EmailStr
    password: str