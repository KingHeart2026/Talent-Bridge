
from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.sql import func
from app.database import Base

class Service(Base):
    __tablename__ = "services"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(150), nullable=False)
    description = Column(Text, nullable=False)
    category = Column(String(100), nullable=False)
    location = Column(String(150), nullable=False)
    price = Column(String(100), nullable=True)
    status = Column(String(30), default="active", nullable=False)
    owner_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )
    created_at = Column(DateTime(timezone=True), server_default=func.now())


from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    DateTime,
    UniqueConstraint
)


class ServiceApplication(Base):
    __tablename__ = "service_applications"

    __table_args__ = (
        UniqueConstraint(
            "service_id",
            "candidate_id",
            name="unique_service_application"
        ),
    )

    id = Column(Integer, primary_key=True, index=True)

    service_id = Column(
        Integer,
        ForeignKey("services.id"),
        nullable=False
    )

    candidate_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    message = Column(String(1000), nullable=True)

    status = Column(
        String(30),
        default="pending",
        nullable=False
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )
