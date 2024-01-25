from sqlalchemy.orm import Session
from datetime import datetime

import models
import schemas


def get_student(db: Session, uid: int):
    return db.query(models.Student).filter(models.Student.uid == uid).first()


def get_incheck(db: Session, incheck: datetime):
    return db.query(models.Informatie).filter(models.Informatie.incheck == incheck).first()


def get_informatie(db: Session, student_id: int):
    return db.query(models.Informatie).filter(models.Informatie.student_id == student_id).first()


def create_incheck(db: Session, informatie: schemas.InformatieCreate):
    db_informatie = models.Informatie(**informatie.dict())
    db.add(db_informatie)
    db.commit()
    db.refresh(db_informatie)
    return "Informatie successfully created!"


def create_student(db: Session, student: schemas.StudentCreate):
    db_student = models.Student(**student.dict())
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return "Student successfully created!"


def update_informatie(db: Session, informatie: schemas.InformatieCreate):
    db_informatie = db.query(models.Informatie).filter(models.Informatie.uitcheck == informatie.uitcheck).first()
    db_informatie.incheck = informatie.incheck
    db.commit()
    db.refresh(db_informatie)
    return "Informatie successfully updated!"
