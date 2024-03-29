from pydantic import BaseModel
from datetime import time, datetime, timedelta


class StudentBase(BaseModel):
    uid: int
    naam: str
    r_nummer: str

class StudentCreate(StudentBase):
    pass


class Student(StudentBase):
    id: int

    class Config:
        orm_mode = True


class ExamenBase(BaseModel):
    naam: str
    startuur: str
    einduur: str


class ExamenCreate(ExamenBase):
    pass


class Examen(ExamenBase):
    id: int

    class Config:
        orm_mode = True


class IncheckBase(BaseModel):
    incheck: str
    student_id: int
    examen_id: int


class IncheckCreate(IncheckBase):
    pass


class Incheck(IncheckBase):
    id: int

    class Config:
        orm_mode = True


class UitcheckBase(BaseModel):
    uitcheck: str
    student_id: int
    examen_id: int


class UitcheckCreate(UitcheckBase):
    pass


class Uitcheck(UitcheckBase):
    id: int

    class Config:
        orm_mode = True


class ManualBase(BaseModel):
    naam: str
    r_nummer: str


class ManualCreate(ManualBase):
    pass


class Manual(ManualBase):
    id: int

    class Config:
        orm_mode = True


class InschrijvingBase(BaseModel):
    student_id: int
    examen_id: int

class InschrijvingCreate(InschrijvingBase):
    pass

class Inschrijving(InschrijvingBase):
    id: int

    class Config:
        orm_mode = True
