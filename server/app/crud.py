from sqlalchemy.orm import Session

from .models import models, schemas

# user queries
def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

# tutorial queries
def get_tutorials(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Tutorial).offset(skip).limit(limit).all()

def get_tutorial_by_id(db: Session, tutorial_id: int):
    return db.query(models.Tutorial).filter(models.Tutorial.id == tutorial_id).first()

def get_tutorial_by_name(db: Session, tutorial_name: int):
    return db.query(models.Tutorial).filter(models.Tutorial.name == tutorial_name).first()

def create_user_tutorial(db: Session, tutorial: schemas.TutorialCreate, user_id: int):
    db_tutorial = models.Tutorial(**tutorial.dict(), owner_id=user_id)
    db.add(db_tutorial)
    db.commit()
    db.refresh(db_tutorial)
    return db_tutorial

# topic queries
def get_topics(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Topic).offset(skip).limit(limit).all()

def get_topic_by_id(db: Session, topic_id: int):
    return db.query(models.Topic).filter(models.Topic.id == topic_id).first()

def get_topic_by_name(db: Session, topic_name: int):
    return db.query(models.Topic).filter(models.Topic.name == topic_name).first()

def create_topic(db: Session, topic: schemas.TopicCreate):
    db_topic = models.Topic(**topic.dict())
    db.add(db_topic)
    db.commit()
    db.refresh(db_topic)
    return db_topic