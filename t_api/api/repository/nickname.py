from sqlalchemy.sql.expression import false, null, true
from fastapi import APIRouter, Depends, status, Response, HTTPException
from .. import schemas, database, models
from sqlalchemy.orm import Session

router = APIRouter(prefix="/nickname",tags=['nickname'])
get_db=database.get_db

def create_nickname(request:schemas.Nickname, db :Session):
    new_nickname = models.Nickname(speakerNickname = request.speakerNickname, 
                                    isSuccess = request.isSuccess,
                                    user_id = request.user_id) 
    db.add(new_nickname)
    db.commit()
    db.refresh(new_nickname)
    return new_nickname

def get_nickname(db: Session):
    nickname = db.query(models.Nickname).all()
    return nickname

def update_nickname(speakerNickname:str, request, db :Session):
    new_nickname = db.query(models.Nickname).filter(models.Nickname.speakerNickname == speakerNickname)
    issuccess = db.query(models.Nickname).filter(models.Nickname.isSuccess)
    if not new_nickname.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blutooth with the id {id} is not available")
    new_nickname.update({'speakerNickname':request.speakerNickname})
    issuccess.update = ({'isSuccess':true})
    db.commit()
    # return issuccess
    return 'updated'

def get_one_nickname(id: int,response: Response, db: Session):
    nickname = db.query(models.Nickname).filter(models.Nickname.id == id).first()
    if not nickname:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
                            detail=f"ID {id} is not available")
    return nickname