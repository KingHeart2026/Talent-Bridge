from sqlalchemy import (
    Integer,
    String,
    ForeignKey,
    UniqueConstraint
)
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
            UniqueConstraint(
                "cadidate_id",
                "skill_id"
            ),
        )

        id: Mapped[int] = mapped_column(
            Integer,
            primary_key=True
        )

        candidate_id: Mapped[int] = mapped_column(
            ForeignKey("candidate_profiles.id"),
            nullable=False
        )

        Skill_id: Mapped[int] = mapped_column(
            ForeignKey("skill.id"),
            nullble=False
        )