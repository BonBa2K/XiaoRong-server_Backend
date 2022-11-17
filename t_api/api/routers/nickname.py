from typing import List
from fastapi import APIRouter, Depends, status, Response, HTTPException
from .. import schemas, database, models, oauth2
from sqlalchemy.orm import Session
from ..repository import nickname

router = APIRouter(prefix="/nickname",tags=['nickname'])
get_db=database.get_db

@router.post('/',status_code=status.HTTP_201_CREATED)
def create(request: schemas.Nickname, db :Session = Depends(get_db)): # ,current_user: schemas.User = Depends(oauth2.get_current_user
    return nickname.create_nickname(request,db)


@router.put('/{id}',status_code=status.HTTP_202_ACCEPTED) #, response_model=schemas.Bluetooth
def update_nickname(speakerNickname, request:schemas.Nickname, db:Session = Depends(get_db)): #, current_user: schemas.User = Depends(oauth2.get_current_user)
    return nickname.update_nickname(speakerNickname, request, db)

@router.get('/',response_model=List[schemas.Nickname])
def all_nickname(db: Session = Depends(get_db)): # ,current_user: schemas.User = Depends(oauth2.get_current_user)
    return nickname.get_nickname(db)

@router.get('/{id}',status_code=200,response_model=schemas.Nickname)
def one_nickname(id,response: Response,db: Session =Depends(get_db)): #,current_user: schemas.User = Depends(oauth2.get_current_user)
    return nickname.get_one_nickname(id,response,db)