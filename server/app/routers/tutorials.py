from typing import Annotated
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, Path
from starlette import status

from ..models import models, schemas
from .. import crud
from ..db.database import SessionLocal, engine, get_db

router = APIRouter()

@router.get("/tutorials", response_model=list[schemas.Tutorial])
def read_tutorials(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    tutorials = crud.get_tutorials(db, skip=skip, limit=limit)
    return tutorials