from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from app.database import get_db
from app.models.company import Company
from app.models.user import UserRole
from app.dependencies.auth import require_role

router = APIRouter(
    prefix="/admin",
    tags=["Administration"]
)


class CompanyVerification(BaseModel):
    is_verified: bool


@router.patch("/companies/{company_id}")
def verify_company(company_id: int, verification: CompanyVerification, db: Session = Depends(get_db), admin=Depends(require_role(UserRole.admin))):

    company = db.query(Company).filter(Company.id == company_id).first()

    if not company:
        raise HTTPException(status_code=404, detail="Company not found")

    company.is_verified = verification.is_verified
    db.commit()
    db.refresh(company)

    return {
        "message": "Company verification updated",
        "company_id": company.id,
        "is_verified": company.is_verified
    }