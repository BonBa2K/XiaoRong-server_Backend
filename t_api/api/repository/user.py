from fastapi import APIRouter,status
from .. import schemas,database,models
from sqlalchemy.orm import Session
from ..hashing import Hash

router = APIRouter(prefix="/user",tags=['users'])
get_db=database.get_db

def create(request: schemas.User,db :Session):
    new_user = models.User(name = request.name,email = request.email ,password = Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
    
def show(id:int,db: Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"User with the id {id} is not available")
    return user
"""
def showlocation(id:int, db: Session):
    location = db.query(models.User).filter(models.User.id == id).first()
    if not location:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with the id {id} is not available")
    return location[5] # 如何挑出 位置
"""
# def googletoken():
