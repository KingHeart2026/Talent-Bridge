from typing import Literal, Optional
from datetime import datetime
from pydantic import BaseModel, ConfigDict


class JobCreate(BaseModel):
    title: str
    description: str
    location: str
    employment_type: str
    job_type: str
    salary_min: int | None = None
    salary_max: int | None = None
    is_remote: bool = False

    opportunity_type: Literal["employment", "service"] = "employment"


class JobResponse(BaseModel):
    id: int
    company_id: int | None
    posted_by_user_id: int

    title: str
    description: str
    location: str
    job_type: str
    salary_min: int | None
    salary_max: int | None
    is_remote: bool
    opportunity_type: str
    status: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)  #this allows Pydantic to read information directly from your SQLAlchemy Job model when returning API responses.

class JobUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    location: Optional[str] = None
    job_type: Optional[str] = None
    salary: Optional[str] = None
    status: Optional[str] = None

