from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
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





@app.post("/informatie/")
def create_informatie(informatie: schemas.InformatieCreate, db: Session = Depends(get_db)):
    incheck = crud.get_incheck(db, incheck=informatie.incheck)
    if incheck < informatie.start or incheck :
        raise HTTPException(status_code=400, detail="Incheck already placed")
    return crud.create_incheck(db=db, informatie=informatie)

