from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.user import User
from app.schemas.service import (ServiceCreate, ServiceUpdate, ServiceResponse)
from app.schemas.service import (ServiceApplicationCreate, ServiceApplicationResponse)
from app.services import service_service
from app.models.service import ServiceApplication
from app.dependencies import get_current_user


router = APIRouter(
    prefix="/services",
    tags=["Services"]
)


@router.post("/", response_model=ServiceResponse, status_code=status.HTTP_201_CREATED)
def create_service(service_data: ServiceCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    if current_user.role != "candidate":
        raise HTTPException(
            status_code=403,
            detail="Only candidates can post services"
        )

    return service_service.create_service(db,service_data, current_user.id)


@router.get("/", response_model=list[ServiceResponse])
def get_services(db: Session = Depends(get_db)):
    return service_service.get_all_services(db)


@router.get("/{service_id}", response_model=ServiceResponse)
def get_service(service_id: int, db: Session = Depends(get_db)):
    service = service_service.get_service_by_id(db, service_id)

    if not service:
        raise HTTPException(
            status_code=404,
            detail="Service not found"
        )

    return service


@router.put("/{service_id}", response_model=ServiceResponse)
def update_service(service_id: int, service_data: ServiceUpdate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    service = service_service.get_service_by_id(db, service_id)

    if not service:
        raise HTTPException(status_code=404, detail="Service not found")

    if service.owner_id != current_user.id:
        raise HTTPException(
            status_code=403,
            detail="You cannot update another user's service"
        )

    return service_service.update_service(db, service, service_data)


@router.delete("/{service_id}")
def delete_service(service_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    service = service_service.get_service_by_id(db, service_id)

    if not service:
        raise HTTPException(status_code=404, detail="Service not found")

    if service.owner_id != current_user.id:
        raise HTTPException(
            status_code=403,
            detail="You cannot delete another user's service"
        )

    service_service.delete_service(db, service)

    return {"message": "Service deleted successfully"}


@router.post("/{service_id}/apply", response_model=ServiceApplicationResponse, status_code=status.HTTP_201_CREATED)
def apply_for_service(service_id: int, application_data: ServiceApplicationCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    if current_user.role != "candidate":
        raise HTTPException(
            status_code=403,
            detail="Only candidates can apply"
        )

    service = service_service.get_service_by_id(db, service_id)

    if not service or service.status != "active":
        raise HTTPException(status_code=404, detail="Service not found")

    if service.owner_id == current_user.id:
        raise HTTPException(status_code=400, detail="You cannot apply for your own service")

    existing = db.query(service_service.ServiceApplication).filter_by(
        service_id=service_id,
        candidate_id=current_user.id
    ).first()

    if existing:
        raise HTTPException(status_code=400, detail="You have already applied for this service")

    return service_service.apply_for_service(
        db,
        service_id,
        current_user.id,
        application_data.message
    )
