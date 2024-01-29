from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from fastapi import Depends, FastAPI, HTTPException, status, Query
from fastapi.middleware.cors import CORSMiddleware
import crud
import models
import schemas
from typing import List
from database import SessionLocal, engine
import os


if not os.path.exists('.\sqlitedb'):
    os.makedirs('.\sqlitedb')

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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


@app.get("/student/", response_model=List[schemas.Student])
def read_students(skip: int = Query(0, description="Number of items to skip"), limit: int = Query(10, description="Number of items to return"), db: Session = Depends(get_db)):
    students = crud.get_students(db, skip=skip, limit=limit)
    return students


@app.post("/student/")
def create_student(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    new_student = crud.get_student(db, uid=student.uid)
    if new_student is not None:
        raise HTTPException(status_code=400, detail="Student already exists")
    return crud.create_student(db=db, student=student)


@app.get("/examen/{id}", response_model=schemas.Examen)
def read_examen(id: int, db: Session = Depends(get_db)):
    examen = crud.get_examen_by_id(db, id=id)
    if examen is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return examen


@app.get("/examen/", response_model=List[schemas.Examen])
def read_examens(skip: int = Query(0, description="Number of items to skip"), limit: int = Query(10, description="Number of items to return"), db: Session = Depends(get_db)):
    examens = crud.get_examens(db, skip=skip, limit=limit)
    return examens


@app.post("/examen/")
def create_examen(examen: schemas.ExamenCreate, db: Session = Depends(get_db)):
    new_examen = crud.get_examen_by_name(db, naam=examen.naam)
    if new_examen is not None:
        raise HTTPException(status_code=400, detail="Examen already exists")
    return crud.create_examen(db=db, examen=examen)


@app.get("/incheck/{student_id}", response_model=schemas.Incheck)
def read_incheck(student_id: int, db: Session = Depends(get_db)):
    incheck = crud.get_incheck(db, student_id=student_id)
    if incheck is None:
        raise HTTPException(status_code=404, detail="Incheck not found")
    return incheck


@app.post("/incheck/")
def create_incheck(incheck: schemas.IncheckCreate, db: Session = Depends(get_db)):
    new_incheck = crud.get_incheck_by_time(db, incheck=incheck.incheck)
    if new_incheck is not None:
        raise HTTPException(status_code=400, detail="Incheck already placed")
    return crud.create_incheck(db=db, incheck=incheck)


@app.get("/uitcheck/{student_id}", response_model=schemas.Uitcheck)
def read_uitcheck(student_id: int, db: Session = Depends(get_db)):
    uitcheck = crud.get_uitcheck(db, student_id=student_id)
    if uitcheck is None:
        raise HTTPException(status_code=404, detail="Uitcheck not found")
    return uitcheck


@app.post("/uitcheck/")
def create_uitcheck(uitcheck: schemas.UitcheckCreate, db: Session = Depends(get_db)):
    new_uitcheck = crud.get_uitcheck_by_time(db, uitcheck=uitcheck.uitcheck)
    if new_uitcheck is not None:
        raise HTTPException(status_code=400, detail="Uitcheck already placed")
    return crud.create_uitcheck(db=db, uitcheck=uitcheck)


@app.get("/manual/{naam}", response_model=schemas.Manual)
def read_manual(naam: str, db: Session = Depends(get_db)):
    manual = crud.get_manual(db, naam=naam)
    if manual is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return manual


@app.post("/manual/")
def create_manual(manual: schemas.UitcheckCreate, db: Session = Depends(get_db)):
    new_manual = crud.get_manual(db, naam=manual.naam)
    if new_manual is not None:
        raise HTTPException(status_code=400, detail="Student already placed")
    return crud.create_manual(db=db, manual=manual)


@app.delete("/manual/{naam}")
def delete_manual(naam: str, db: Session = Depends(get_db)):
    manual = crud.get_manual(db, naam=naam)
    if not manual:
        raise HTTPException(status_code=404, detail="Student not found")
    return crud.delete_manual(db=db, manual=manual)


@app.get("/inschrijving/{student_id}", response_model=List[schemas.Inschrijving])
def read_inschrijving_by_student_id(student_id: int, skip: int = Query(0, description="Number of items to skip"), limit: int = Query(10, description="Number of items to return"), db: Session = Depends(get_db)):
    inschrijving = crud.get_inschrijving_by_student_id(db, student_id=student_id, skip=skip, limit=limit)
    if inschrijving is None:
        raise HTTPException(status_code=404, detail="Inschrijving not found")
    return inschrijving


@app.get("/inschrijving/{examen_id}", response_model=List[schemas.Inschrijving])
def read_inschrijving_by_exam_id(examen_id: int, skip: int = Query(0, description="Number of items to skip"), limit: int = Query(10, description="Number of items to return"), db: Session = Depends(get_db)):
    inschrijving = crud.get_inschrijving_by_exam_id(db, examen_id=examen_id, skip=skip, limit=limit)
    if inschrijving is None:
        raise HTTPException(status_code=404, detail="Inschrijving not found")
    return inschrijving


@app.get("/inschrijving/", response_model=List[schemas.Inschrijving])
def read_inschrijvingen(skip: int = Query(0, description="Number of items to skip"), limit: int = Query(10, description="Number of items to return"), db: Session = Depends(get_db)):
    inschrijvingen = crud.get_inschrijvingen(db, skip=skip, limit=limit)
    if inschrijvingen is None:
        raise HTTPException(status_code=404, detail="Inschrijving not found")
    return inschrijvingen

@app.post("/inschrijving/")
def create_inschrijving(inschrijving: schemas.InschrijvingCreate, db: Session = Depends(get_db)):
    new_inschrijving = crud.get_inschrijving_by_student_id(db, student_id=inschrijving.student_id)
    if new_inschrijving is not None:
        raise HTTPException(status_code=400, detail="Inschrijving already placed")
    return crud.create_inschrijving(db=db, inschrijving=inschrijving)