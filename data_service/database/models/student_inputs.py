from sqlalchemy.orm import (
    mapped_column,
    Mapped
)
from sqlalchemy.ext.asyncio import AsyncAttrs

from .base import Base


class AbstractModel(AsyncAttrs, Base):
    __tablename__ = "student_inputs"

    id: Mapped[int] = mapped_column(
        autoincrement=True,
        primary_key=True
    )


class StudentInputsModel(AbstractModel):
    full_name: Mapped[str] = mapped_column()
    gender: Mapped[int] = mapped_column()
    age: Mapped[int] = mapped_column()
    sport: Mapped[int] = mapped_column()
    is_foreign: Mapped[int] = mapped_column()
    education: Mapped[str] = mapped_column()
    gpa: Mapped[float] = mapped_column()
    study_form: Mapped[str] = mapped_column()
    total_points: Mapped[int] = mapped_column()
    bonus_total_points: Mapped[int] = mapped_column()
    is_enrolled: Mapped[int] = mapped_column()
    drawing_exam: Mapped[int] = mapped_column()
    math_exam: Mapped[int] = mapped_column()
    russian_exam: Mapped[int] = mapped_column()
    social_exam: Mapped[int] = mapped_column()
    physic_exam: Mapped[int] = mapped_column()
    history_exam: Mapped[int] = mapped_column()
    composition_architecture_exam: Mapped[int] = mapped_column()
    composition_design_exam: Mapped[int] = mapped_column()
    informatics_exam: Mapped[int] = mapped_column()
    chemistry_exam: Mapped[int] = mapped_column()
    composition_exam: Mapped[int] = mapped_column()
