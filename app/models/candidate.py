from sqlalchemy import (String, Integer, Boolean, ForeignKey, Text)
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database import Base

class CandidateProfile(Base):
    __tablename__ = "candidate_profiles"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True
    )

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        unique=True,
        nullable=False
    )

    headline: Mapped[str | None] = mapped_column(
        String(200),
        nullable=True
    )

    years_experience: Mapped[int] = mapped_column(
        Integer,
        default=0
    )

    location: Mapped[str | None] = mapped_column(
        String(150),
        nullable=True
    )

    cv_path: Mapped[str | None] = mapped_column(
        String(500),
        nullable=True
    )

    user = relationship(
        "User",
        back_populates="candidate_profile"
    )
