
from typing import Literal

from pydantic import BaseModel, ConfigDict


class JobCreate(BaseModel):
    title: str
    description: str
    location: str
    employment_type: str

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
    employment_type: str

    salary_min: int | None
    salary_max: int | None

    is_remote: bool
    opportunity_type: str
    status: str

    model_config = ConfigDict(from_attributes=True)  #this allows Pydantic to read information directly from your SQLAlchemy Job model when returning API responses.
