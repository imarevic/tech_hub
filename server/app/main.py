from fastapi import FastAPI
from sqlalchemy.orm import Session

from .routers import auth, tutorials
from .config import PROJECT_NAME

app = FastAPI(
    title=PROJECT_NAME
)

app.include_router(auth.router)
app.include_router(tutorials.router)