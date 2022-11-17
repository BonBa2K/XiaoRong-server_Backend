from typing import List
from fastapi import APIRouter, Depends, status, Response, HTTPException
from .. import schemas, database, models, oauth2
from sqlalchemy.orm import Session
from ..repository import googlecalendar 

router = APIRouter(prefix="/googlecalendar",tags=['googlecalendar'])
get_db=database.get_db

@router.post('/', status_code=status.HTTP_201_CREATED) 
def create_googlecalendar(request:schemas.Googlecalendar,db :Session = Depends(get_db)): #,current_user: schemas.User = Depends(oauth2.get_current_user)
    return googlecalendar.create_googlecalendar(request,db)

@router.get('/', response_model=List[schemas.Googlecalendar])
def all_googlecalendar(db: Session = Depends(get_db)): # , current_user: schemas.User = Depends(oauth2.get_current_user)
    return googlecalendar.get_all_googlecalendar(db)

@router.get('/{id}',status_code=200,response_model=schemas.Googlecalendar)
def one_googlecalendar(id,response: Response,db: Session =Depends(get_db)): #,current_user: schemas.User = Depends(oauth2.get_current_user)
    return googlecalendar.get_one_googlecalendar(id,response,db)