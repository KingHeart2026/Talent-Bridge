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

    user_id: Mapped[int] = mapped_column()