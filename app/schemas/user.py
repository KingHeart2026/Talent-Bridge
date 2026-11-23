from pydantic import BaseModel, EmailStr, Field
from app.models.user import UserRole
from typing import Literal

class UserRegister(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    email: EmailStr
    password: str = Field(min_length=7, max_length=128)
    role: UserRole

class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    role: Literal["candidate", "employer"]
    is_active: bool
    model_config = {
        "from_attributes": True
    }
