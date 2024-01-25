from pydantic import BaseModel
from datetime import time, datetime, timedelta


class StudentBase(BaseModel):
    uid: int
    naam: str


class StudentCreate(StudentBase):
    pass


class Student(StudentBase):
    id: int


class InformatieBase(BaseModel):
    incheck: datetime = None
    uitcheck: datetime = None
    student_id: int


class InformatieCreate(InformatieBase):
    pass


class Informatie(InformatieBase):
    id: int

    class Config:
        orm_mode = True
