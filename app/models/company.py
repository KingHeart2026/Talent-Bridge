from sqlalchemy import (String, Integer, Boolean, ForeignKey, Text)
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database import Base

class Company(Base):
    __tablename__ = "companies"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True
    )

    owner_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),               #the foreign key ensures that the company references to an existing user.
        unique=True,
        nullable=False
    )

    name: Mapped[str] = mapped_column(
        String(150),
        nullable=True
    )

    description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True
    )

    is_verified: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        naullable=False
    )

    owner = relationship(
        "User",
        back_populates="company"
    )