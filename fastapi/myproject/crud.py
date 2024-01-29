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


def get_examen(db: Session, id: int):
    return db.query(models.Examen).filter(models.Examen.id == id).first()

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
