from sqlalchemy import (Integer, String, Text, ForeignKey, Boolean, DateTime)
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func
from app.database import Base


class Job(Base):
    __tablename__ = "jobs"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True
    )

    company_id: Mapped[int] = mapped_column(
        ForeignKey("companies.id"),
        nullable=False,
        index=True
    )

    title: Mapped[str] = mapped_column(
        String(150),
        nullable=False
    )

    description: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    location: Mapped[str] = mapped_column(
        String(150),
        nullable=False
    )

    employment_type: Mapped[str] = mapped_column(
        String(50),
        nullable=False
    )

    salary_min: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True
    )

    salary_max: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True
    )

    is_remote: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False
    )

    status: Mapped[str] = mapped_column(
        String(30),
        default="open",
        nullable=False
    )

    created_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False
    )