from pydantic import BaseModel, HttpUrl, Field

class CompanyCreate(BaseModel):
    name: str = Field(min_length=2, max_length=150)
    website: HttpUrl | None = None
    description: str | None = None

class CompanyResponse(BaseModel):
    id: int
    name: str | None
    website: str | None
    description: str | None
    is_verified: bool
    model_config = {
        "from_attributes": True
    }