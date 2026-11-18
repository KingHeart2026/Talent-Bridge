from pydantic import BaseModel, Field

class CandidateProfileCreate(BaseModel):
    headline: str | None = None
    years_experience: int = Field(
        default=0,
        ge=0,
        le=60
    )

    location: str | None = None

class CandidateProfileResponse(BaseModel):
    id : int
    user_id: int
    headine: str | None
    years_experience: int
    location: str | None
    cv_path: str | None
    model_config = {
        "from_attributes": True
    }