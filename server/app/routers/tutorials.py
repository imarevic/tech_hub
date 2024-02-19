from typing import Annotated
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, Path
from starlette import status

from .. import crud, models, schemas
from ..database import SessionLocal, engine

router = APIRouter()

# dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/test")
def test():
    return "Hello World"

@router.get("/tutorials", response_model=list[schemas.Tutorial])
def read_tutorials(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    #tutorials = crud.get_tutorials(db, skip=skip, limit=limit)
    tutorials = "my tutorials"
    return tutorials