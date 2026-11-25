from sqlalchemy import (Integer, String, ForeignKey, DateTime, Text)
from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func
from app.database import Base

class ApplicationEvent(Base):
    __tablename__ = "application_events"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )

    application_id: Mapped[int] = mapped_column(
        ForeignKey("applications.id"),
        nullable=False,
        index=True
    )

    changed_by_user_id: Mapped[int | None] = mapped_column(
        ForeignKey("users.id"),
        nullable=True
    )

    old_status: Mapped[str | None] = mapped_column(
        String(30),
        nullable=True
    )

    new_status: Mapped[str] = mapped_column(
        String(30),
        nullable=False
    )

    note: Mapped[str | None] = mapped_column(
        Text,
        nullable=True
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False
    )