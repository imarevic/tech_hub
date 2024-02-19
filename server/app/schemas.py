from pydantic import BaseModel
from datetime import datetime

class TopicBase(BaseModel):
    name: str
    description: str | None = None
    sub_topic: str | None = None

class TopicCreate(TopicBase):
    pass

class Topic(TopicBase):
    id: int
    tutorials: int

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool
    is_admin: bool

    class Config:
        orm_mode = True

class TutorialBase(BaseModel):
    name: str
    description: str
    content: str
    creation_timestamp: datetime
    last_modified_timestamp: datetime

class TutorialCreate(TutorialBase):
    pass

class Tutorial(TutorialBase):
    id: int
    topic: int
    creator: int

    class Config:
        orm_mode = True
