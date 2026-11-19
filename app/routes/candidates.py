from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.candidate import CandidateProfile
from app.models.user import UserRole
from app.schemas.candidate import (CandidateProfileCreate, CandidateProfileResponse)
from app.dependencies.auth import get_current_user

router = APIRouter(
    prefix="/candidates",
    tags=["Candidates"]
)


@router.get("/me", response_model=CandidateProfileResponse)
def get_candidate_profile(db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    
    if current_user.role != UserRole.candidate:
        raise HTTPException(
            status_code=403,
            detail="Only candidates can access this profile"
        )

    profile = db.query(CandidateProfile).filter(CandidateProfile.user_id == current_user.id).first()

    if not profile:
        raise HTTPException(
            status_code=404,
            detail="Candidate profile not found"
        )

    return profile


@router.put("/me", response_model=CandidateProfileResponse)
def update_candidate_profile(profile_data: CandidateProfileCreate, db: Session = Depends(get_db), current_user=Depends(get_current_user)):

    if current_user.role != UserRole.candidate:
        raise HTTPException(
            status_code=403,
            detail="Only candidates can update this profile"
        )

    profile = db.query(CandidateProfile).filter(CandidateProfile.user_id == current_user.id).first()

    if not profile:
        profile = CandidateProfile(user_id=current_user.id)

    db.add(profile)
    profile.headline = profile_data.headline
    profile.years_experience = profile_data.years_experience
    profile.location = profile_data.location
    db.commit()
    db.refresh(profile)

    return profile