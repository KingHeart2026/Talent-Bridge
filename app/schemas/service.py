from pydantic import BaseModel, Field, ConfigDict
from typing import Optional
from datetime import datetime


class ServiceCreate(BaseModel):
    title: str = Field(min_length=3, max_length=150)
    description: str = Field(min_length=10)
    category: str = Field(min_length=2, max_length=100)
    location: str = Field(min_length=2, max_length=150)
    price: Optional[str] = None


class ServiceUpdate(BaseModel):
    title: Optional[str] = Field(default=None, min_length=3)
    description: Optional[str] = Field(default=None, min_length=10)
    category: Optional[str] = None
    location: Optional[str] = None
    price: Optional[str] = None
    status: Optional[str] = None


class ServiceResponse(BaseModel):
    id: int
    title: str
    description: str
    category: str
    location: str
    price: Optional[str]
    status: str
    owner_id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class ServiceApplicationCreate(BaseModel):
    message: Optional[str] = Field(
        default=None,
        max_length=1000
    )


class ServiceApplicationResponse(BaseModel):
    id: int
    service_id: int
    candidate_id: int
    message: Optional[str]
    status: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
