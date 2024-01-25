from pydantic import BaseModel
from datetime import time, datetime, timedelta


class StudentBase(BaseModel):
    uid: int
    naam: str


class StudentCreate(StudentBase):
    pass


class Student(StudentBase):
    id: int


class IncheckBase(BaseModel):
    incheck: datetime = None
    student_id: int


class IncheckCreate(IncheckBase):
    pass


class Incheck(IncheckBase):
    id: int

    class Config:
        orm_mode = True


class UitcheckBase(BaseModel):
    uitcheck: datetime = None
    student_id: int


class UitcheckCreate(UitcheckBase):
    pass


class Uitcheck(UitcheckBase):
    id: int

    class Config:
        orm_mode = True
