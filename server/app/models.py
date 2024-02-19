from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from .database import Base

class User(Base):
    __tablename__="users"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    is_admin = Column(Boolean, default=True)

    tutorials = relationship("Tutorial", back_populates="creator")

class Topic(Base):
    __tablename__ = "topics"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String, nullable=True)
    sub_tobic = Column(String, nullable=True)

    tutorials = relationship("Tutorial", back_populates="topic")

class Tutorial(Base):
    __tablename__ = "tutorials"

    id = Column(Integer, primary_key=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    content = Column(String)
    creation_timestamp = Column(DateTime(timezone=True), server_default=func.now())
    last_modified_timestamp = Column(DateTime(timezone=True), onupdate=func.now())

    topic_id = Column(Integer, ForeignKey("topics.id"))
    topic = relationship("Topic", back_populates="tutorials")

    creator_id = Column(Integer, ForeignKey("users.id"))
    creator = relationship("User", back_populates="users")