from typing import Annotated
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, Path
from starlette import status

from ..models import models, schemas
from .. import crud
from ..db.database import SessionLocal, engine, get_db

router = APIRouter()


@router.get("/topics", response_model=list[schemas.Topic])
def read_tutorials(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    topics = crud.get_topics(db, skip=skip, limit=limit)
    return topics

@router.post("/topics", response_model=schemas.Topic, status_code=status.HTTP_201_CREATED)
def create_topic(topic : schemas.TopicCreate, db: Session = Depends(get_db)):
    return crud.create_topic(db=db, topic=topic)