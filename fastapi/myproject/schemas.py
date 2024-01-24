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
    start: time = time(14, 30)
    incheck: time = None
    minimale_tijd: time = None
    uitcheck: time = None


class InformatieCreate(InformatieBase):
    pass


class Informatie(InformatieBase):
    id: int

    class Config:
        orm_mode = True
