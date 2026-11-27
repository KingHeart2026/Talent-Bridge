from sqlalchemy.orm import Session
from app.models.service import Service, ServiceApplication
from app.schemas.service import ServiceCreate, ServiceUpdate


def create_service(db: Session, service_data: ServiceCreate, user_id: int):
    new_service = Service(
        **service_data.model_dump(),
        owner_id=user_id
    )

    db.add(new_service)
    db.commit()
    db.refresh(new_service)

    return new_service


def get_all_services(db: Session):
    return db.query(Service).filter(Service.status == "active").all()


def get_service_by_id(db: Session, service_id: int):
    return db.query(Service).filter(Service.id == service_id).first()


def update_service(db: Session, service: Service,service_data: ServiceUpdate):
    update_data = service_data.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(service, key, value)

    db.commit()
    db.refresh(service)

    return service


def delete_service(db: Session, service: Service):
    db.delete(service)
    db.commit()


def apply_for_service(db: Session, service_id: int, candidate_id: int, message: str = None):
    application = ServiceApplication(service_id=service_id, candidate_id=candidate_id, message=message)

    db.add(application)
    db.commit()
    db.refresh(application)

    return application
