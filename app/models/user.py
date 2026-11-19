from sqlalchemy import String, Integer, Boolean, Enum
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import relationship
from app.database import Base

import enum

class UserRole(str, enum.Enum):
    candidate = "candidate"
    employer = "employer"
    admin = "admin"

class User(Base):
    __tablename__ = "uers"

    id: Mapped[int] = mapped_column(
        Integer,
        Primary_key=True,
        index=True
    )

    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    hashed_password: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    role: Mapped[UserRole] = mapped_column(
        Enum(UserRole),
        default=UserRole.candidate,
        nullable=False
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False
    )

    company = relationship(
        "Company",
        back_populates="owner",
        uselist=False
    )

    candidate_profile = relationship(
        "CandidateProfile",
        back_populates="user",
        uselist=False
    )