from sqlalchemy.orm import Session
from . import models, schemas

def get_user(id: int, db_session: Session):
    return db_session.query(models.User).filter(models.User.id == id).first()

def create_user(user: schemas.User, db: Session):
    db_user = models.User(name=user.name, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(id: int, user: schemas.User, db: Session):
    db_user = get_user(id,db)
    db_user.name = user.name
    db_user.email = user.email
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(id: int, db: Session):
    db_user = get_user(id,db)
    if db_user is None:
        return None
    db.delete(db_user)
    db.commit()
    return db_user
