from sqlalchemy.orm import Session
from datetime import datetime

import models
import schemas


def get_student(db: Session, uid: int):
    return db.query(models.Student).filter(models.Student.uid == uid).first()


def get_incheck(db: Session, incheck: datetime):
    return db.query(models.Informatie).filter(models.Informatie.incheck == incheck).first()


def create_incheck(db: Session, informatie: schemas.InformatieCreate):
    db_informatie = models.Informatie(**informatie.dict())
    db.add(db_informatie)
    db.commit()
    db.refresh(db_informatie)
    return "Informatie successfully created!"