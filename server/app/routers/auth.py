from typing import Annotated
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, Path
from starlette import status

from ..models import models, schemas
from .. import crud
from ..db.database import SessionLocal, engine, get_db

router = APIRouter()
