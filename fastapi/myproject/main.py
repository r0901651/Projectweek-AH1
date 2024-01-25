from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI, HTTPException, status
import crud
import models
import schemas
from database import SessionLocal, engine
import os


if not os.path.exists('.\sqlitedb'):
    os.makedirs('.\sqlitedb')

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/student/{uid}", response_model=schemas.Student)
def read_student(uid: int, db: Session = Depends(get_db)):
    student = crud.get_student(db, uid=uid)
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return student


@app.get("/informatie/{student_id}", response_model=schemas.Informatie)
def read_informatie(student_id: int, db: Session = Depends(get_db)):
    informatie = crud.get_informatie(db, student_id=student_id)
    if informatie is None:
        raise HTTPException(status_code=404, detail="Informatie not found")
    return informatie


@app.post("/student/")
def create_student(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    new_student = crud.get_student(db, uid=student.uid)
    if new_student is not None:
        raise HTTPException(status_code=400, detail="Student already excists")
    return crud.create_student(db=db, student=student)


@app.post("/informatie/")
def create_informatie(informatie: schemas.InformatieCreate, db: Session = Depends(get_db)):
    incheck = crud.get_incheck(db, incheck=informatie.incheck)
    if incheck is not None:
        raise HTTPException(status_code=400, detail="Incheck already placed")
    return crud.create_incheck(db=db, informatie=informatie)


@app.patch("/informatie/{student_id}")
def update_informatie(student_id: int, informatie: schemas.InformatieCreate, db: Session = Depends(get_db)):
    db_informatie = crud.get_informatie(db, student_id=student_id)
    if db_informatie is None:
        raise HTTPException(status_code=404, detail="Informatie not found")
    return crud.update_informatie(db=db, informatie=informatie)

