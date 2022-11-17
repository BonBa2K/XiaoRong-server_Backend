from typing import List
from fastapi import APIRouter, Depends, status, Response, HTTPException
from .. import schemas, database, models, oauth2
from sqlalchemy.orm import Session
from ..repository import log

router = APIRouter(prefix="/log",tags=['log'])
get_db=database.get_db

@router.post('/',status_code=status.HTTP_201_CREATED)
def create(request: schemas.Log,db :Session = Depends(get_db)): # ,current_user: schemas.User = Depends(oauth2.get_current_user
    return log.create_log(request,db)

@router.get('/',response_model=List[schemas.Log])
def all_log(db: Session = Depends(get_db)): # ,current_user: schemas.User = Depends(oauth2.get_current_user)
    return log.get_log(db)

@router.get('/{id}',status_code=200,response_model=schemas.Log)
def one_log(id,response: Response,db: Session =Depends(get_db)): #,current_user: schemas.User = Depends(oauth2.get_current_user)
    return log.get_one_log(id,response,db)
