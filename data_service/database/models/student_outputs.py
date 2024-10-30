from sqlalchemy.orm import (
    mapped_column,
    Mapped
)
from sqlalchemy.ext.asyncio import AsyncAttrs

from .base import Base


class AbstractModel(AsyncAttrs, Base):
    __tablename__ = "student_outputs"

    id: Mapped[int] = mapped_column(
        autoincrement=True,
        primary_key=True
    )


class StudentOutputsModel(AbstractModel):
    full_name: Mapped[str] = mapped_column()
    speciality: Mapped[str] = mapped_column()
