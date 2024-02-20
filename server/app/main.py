from fastapi import FastAPI
from sqlalchemy.orm import Session

from .routers import auth, tutorials, topics
from .config import PROJECT_NAME
from .models import models
from .db.database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=PROJECT_NAME
)

app.include_router(auth.router)
app.include_router(topics.router)
app.include_router(tutorials.router)