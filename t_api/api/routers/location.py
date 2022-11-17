from typing import List
from fastapi import APIRouter, Depends, status, Response, HTTPException
from .. import schemas,database, models, oauth2
from sqlalchemy.orm import Session
from ..repository import location

router = APIRouter(prefix="/location",tags=['location'])
get_db=database.get_db


@router.post('/',status_code=status.HTTP_201_CREATED)
def create(request: schemas.Location,db :Session = Depends(get_db)): # ,current_user: schemas.User = Depends(oauth2.get_current_user
    return location.create_location(request,db)

@router.get('/',response_model=List[schemas.Location])
def all_location(db: Session = Depends(get_db)): # ,current_user: schemas.User = Depends(oauth2.get_current_user)
    return location.get_location(db)

@router.get('/{id}',status_code=200,response_model=schemas.Location)
def one_location(id,response: Response,db: Session =Depends(get_db)): #,current_user: schemas.User = Depends(oauth2.get_current_user)
    return location.get_one_location(id,response,db)
