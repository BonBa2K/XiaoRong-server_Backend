from typing import List
from fastapi import APIRouter, Depends, status, Response, HTTPException
from .. import schemas, database, models, oauth2
from sqlalchemy.orm import Session
from ..repository import turnoffwifi

router = APIRouter(prefix="/turnoffwifi",tags=['turnoffwifi'])
get_db=database.get_db

@router.post('/',status_code=status.HTTP_201_CREATED)
def create(request: schemas.Turnoffwifi, db :Session = Depends(get_db)): # ,current_user: schemas.User = Depends(oauth2.get_current_user
    return turnoffwifi.create_turnoffwifi(request, db)

@router.get('/',response_model=List[schemas.Turnoffwifi])
def all_turnoffwifi(db: Session = Depends(get_db)): # ,current_user: schemas.User = Depends(oauth2.get_current_user)
    return turnoffwifi.get_turnoffwifi(db)

@router.get('/{id}',status_code=200,response_model=schemas.Turnoffwifi)
def one_turnoffwifi(id,response: Response,db: Session =Depends(get_db)): #,current_user: schemas.User = Depends(oauth2.get_current_user)
    return turnoffwifi.get_one_turnoffwifi(id,response,db)
