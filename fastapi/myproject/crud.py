from sqlalchemy.orm import Session
from datetime import datetime

import models
import schemas


def get_student(db: Session, uid: int):
    return db.query(models.Student).filter(models.Student.uid == uid).first()

def get_students(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Student).offset(skip).limit(limit).all()

def create_student(db: Session, student: schemas.StudentCreate):
    db_student = models.Student(**student.dict())
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return "Student successfully created!"


def get_examen(db: Session, naam: str):
    return db.query(models.Examen).filter(models.Examen.naam == naam).first()

def get_examens(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Examen).offset(skip).limit(limit).all()

def create_examen(db: Session, examen: schemas.ExamenCreate):
    db_examen = models.Examen(**examen.dict())
    db.add(db_examen)
    db.commit()
    db.refresh(db_examen)
    return "Examen successfully created!"


def get_incheck_by_time(db: Session, incheck: datetime):
    return db.query(models.Incheck).filter(models.Incheck.incheck == incheck).first()

def get_incheck(db: Session, student_id: int):
    return db.query(models.Incheck).filter(models.Incheck.student_id == student_id).first()

def create_incheck(db: Session, incheck: schemas.IncheckCreate):
    db_incheck = models.Incheck(**incheck.dict())
    db.add(db_incheck)
    db.commit()
    db.refresh(db_incheck)
    return "Incheck successfully created!"


def get_uitcheck_by_time(db: Session, uitcheck: datetime):
    return db.query(models.Uitcheck).filter(models.Uitcheck.uitcheck == uitcheck).first()

def get_uitcheck(db: Session, student_id: int):
    return db.query(models.Uitcheck).filter(models.Incheck.student_id == student_id).first()

def create_uitcheck(db: Session, uitcheck: schemas.UitcheckCreate):
    db_uitcheck = models.Uitcheck(**uitcheck.dict())
    db.add(db_uitcheck)
    db.commit()
    db.refresh(db_uitcheck)
    return "Uitcheck successfully created!"


def get_manual(db: Session, naam: str):
    return db.query(models.Manual).filter(models.Manual.naam == naam).first()

def get_manuals(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Manual).offset(skip).limit(limit).all()

def create_manual(db: Session, manual: schemas.ManualCreate):
    db_manual = models.Manual(**manual.dict())
    db.add(db_manual)
    db.commit()
    db.refresh(db_manual)
    return "Student successfully created!"


def delete_manual(db: Session, manual: schemas.Manual):
    db.delete(manual)
    db.commit()
    return "Student successfully deleted!"


def get_inschrijving_by_student_id(db: Session, student_id: int, skip: int = 0, limit: int = 10):
    return db.query(models.Inschrijving).filter(models.Inschrijving.student_id == student_id).offset(skip).limit(limit).all()

def get_inschrijving_by_exam_id(db: Session, examen_id: int, skip: int = 0, limit: int = 10):
    return db.query(models.Inschrijving).filter(models.Inschrijving.examen_id == examen_id).offset(skip).limit(limit).all()

def get_inschrijvingen(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Inschrijving).offset(skip).limit(limit).all()

def get_inschrijving(db: Session, student_id: int, examen_id: int):
    return db.query(models.Inschrijving).filter(models.Inschrijving.student_id == student_id and models.Inschrijving.examen_id == examen_id).first()

def create_inschrijving(db: Session, inschrijving: schemas.InschrijvingCreate):
    db_inschrijving = models.Inschrijving(**inschrijving.dict())
    db.add(db_inschrijving)
    db.commit()
    db.refresh(db_inschrijving)
    return "Inschrijving successfully created!"