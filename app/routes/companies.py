from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.company import Company
from app.models.user import UserRole
from app.schemas.company import (CompanyCreate, CompanyResponse)
from app.dependencies.auth import get_current_user

router = APIRouter(
    prefix="/companies",
    tags=["Companies"]
)

@router.post("/me", response_model=CompanyResponse, status_code=201)
def create_company(company_data: CompanyCreate, db: Session = Depends(get_db), current_user=Depends(get_current_user)):

    if current_user.role != UserRole.employer:
        raise HTTPException(
            status_code=403,
            detail="Only employers can create companies"
        )

    existing_company = db.query(Company).filter(Company.owner_id == current_user.id).first()

    if existing_company:
        raise HTTPException(
            status_code=409,
            detail="You already have a company"
        )

    company = Company(
        owner_id=current_user.id,
        name=company_data.name,
        website=str(company_data.website)
        if company_data.website else None,
        description=company_data.description
    )

    db.add(company)
    db.commit()
    db.refresh(company)

    return company


@router.get("/me", response_model=CompanyResponse)
def get_my_company(db: Session = Depends(get_db), current_user=Depends(get_current_user)):

    if current_user.role != UserRole.employer:
        raise HTTPException(
            status_code=403,
            detail="Only employers can view company profiles"
        )

    company = db.query(Company).filter(Company.owner_id == current_user.id).first()

    if not company:
        raise HTTPException(
            status_code=404,
            detail="Company not found"
        )

    return company