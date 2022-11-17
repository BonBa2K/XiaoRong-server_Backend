from typing import List
from fastapi import APIRouter, Depends, status, Response, HTTPException
from .. import schemas, database, models, oauth2
from sqlalchemy.orm import Session
from ..repository import googletoken

router = APIRouter(prefix="/googletoken",tags=['googletoken'])
get_db=database.get_db

@router.post('/', status_code=status.HTTP_201_CREATED) 
def create_googletoken(request:schemas.Googletokens,db :Session = Depends(get_db)): #,current_user: schemas.User = Depends(oauth2.get_current_user)
    return googletoken.create_googletoken(request,db)

@router.get('/', response_model=List[schemas.Googletokens])
def all_googletoken(db: Session = Depends(get_db)): # , current_user: schemas.User = Depends(oauth2.get_current_user)
    return googletoken.get_all_googletoken(db)

@router.get('/{id}',status_code=200,response_model=schemas.Googletokens)
def one_googletoken(id,response: Response,db: Session =Depends(get_db)): #,current_user: schemas.User = Depends(oauth2.get_current_user)
    return googletoken.get_one_googletoken(id,response,db)
