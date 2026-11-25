from sqlalchemy import (Integer, String, ForeignKey, UniqueConstraint)
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base

class Skill(Base):
    __tablename__ = "skills"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )

    name: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        nullable=False
    )

class CandidateSkill(Base):
    __tablename__ = "candidate_skills"

    __table_args__ = (
        UniqueConstraint("candidate_id", "skill_id"),
    )

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )

    candidate_id: Mapped[int] = mapped_column(
        ForeignKey("candidate_profiles.id"),
        nullable=False
    )

    skill_id: Mapped[int] = mapped_column(
        ForeignKey("skills.id"),
        nullable=False
    )


class JobSkill(Base):
    __tablename__ = "job_skills"

    __table_args__ = (
        UniqueConstraint(
            "job_id",
            "skill_id",
            name="unique_job_skill"
        ),
    )

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )

    job_id: Mapped[int] = mapped_column(
        ForeignKey("jobs.id"),
        nullable=False,
        index=True
    )

    skill_id: Mapped[int] = mapped_column(
        ForeignKey("skills.id"),
        nullable=False,
        index=True
    )