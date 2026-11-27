from sqlalchemy.orm import Session
from app.models.job import Job
from app.schemas.job import JobCreate, JobUpdate

def create_job(db: Session, data: JobCreate, user_id: int):
    job = Job(
        **data.model_dump(),
        owner_id=user_id
    )

    db.add(job)
    db.commit()
    db.refresh(job)

    return job


def get_all_jobs(db: Session):
    return db.query(Job).filter(Job.status == "active").all()


def get_job(db: Session, job_id: int):
    return db.query(Job).filter(Job.id == job_id).first()


def update_job(db: Session, job: Job, data: JobUpdate):
    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(job, key, value)

    db.commit()
    db.refresh(job)

    return job


def delete_job(db: Session, job: Job):
    db.delete(job)
    db.commit()
