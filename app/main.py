from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# ユーザーを全件取得
@app.get("/users/")
def read_users(db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    return users

# ユーザーを1件取得
@app.get("/users/{user_id}")
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = crud.get_user(user_id, db)
    return user

# ユーザーの登録
@app.post("/users/")
def create_user(user: schemas.User, db: Session = Depends(get_db)):
    return crud.create_user(user=user, db=db)

# ユーザーの更新
@app.put("/users/{user_id}")
def update_user(user_id: int, user: schemas.User, db: Session = Depends(get_db)):
    db_user = crud.update_user(id=user_id, user=user, db=db)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

# ユーザーの削除
@app.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.delete_user(id=user_id, db=db)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
