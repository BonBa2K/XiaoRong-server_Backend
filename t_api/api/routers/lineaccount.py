from typing import List
from fastapi import APIRouter, Depends, status, Response, HTTPException
from .. import schemas, database, models, oauth2
from sqlalchemy.orm import Session
from ..repository import lineaccount

router = APIRouter(prefix="/lineaccount",tags=['lineaccount']) 
get_db=database.get_db

@router.post('/',status_code=status.HTTP_201_CREATED)
def create(request: schemas.Lineaccount,db :Session = Depends(get_db)): # ,current_user: schemas.User = Depends(oauth2.get_current_user
    return lineaccount.create_searchresult(request,db)

@router.get('/',response_model=List[schemas.Lineaccount])
def all_searchresult(db: Session = Depends(get_db)): # ,current_user: schemas.User = Depends(oauth2.get_current_user)
    return lineaccount.get_searchresult(db)