from typing import List
from fastapi import APIRouter, Depends, status, Response, HTTPException
from .. import schemas, database, models, oauth2
from sqlalchemy.orm import Session
from ..repository import playingcondition

router = APIRouter(prefix="/playingcondition",tags=['playingcondition'])
get_db=database.get_db

@router.post('/',status_code=status.HTTP_201_CREATED)
def create(request: schemas.Playingcondition,db :Session = Depends(get_db)): # ,current_user: schemas.User = Depends(oauth2.get_current_user
    return playingcondition.create_playingcondition(request,db)

@router.get('/',response_model=List[schemas.Playingcondition])
def all_playingcondition(db: Session = Depends(get_db)): # ,current_user: schemas.User = Depends(oauth2.get_current_user)
    return playingcondition.get_playingcondition(db)

@router.get('/{id}',status_code=200,response_model=schemas.Playingcondition)
def one_playingcondition(id,response: Response,db: Session =Depends(get_db)): #,current_user: schemas.User = Depends(oauth2.get_current_user)
    return playingcondition.get_one_playingcondition(id,response,db)
