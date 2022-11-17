from typing import List
from fastapi import APIRouter, Depends, status, Response, HTTPException
from .. import schemas, database, models, oauth2
from sqlalchemy.orm import Session
from ..repository import turnonwifi

router = APIRouter(prefix="/turnonwifi",tags=['turnonwifi'])
get_db=database.get_db

@router.post('/',status_code=status.HTTP_201_CREATED)
def create(request: schemas.Turnonwifi, db :Session = Depends(get_db)): # ,current_user: schemas.User = Depends(oauth2.get_current_user
    return turnonwifi.create_turnonwifi(request, db)

@router.get('/',response_model=List[schemas.Turnonwifi])
def all_Turnonwifi(db: Session = Depends(get_db)): # ,current_user: schemas.User = Depends(oauth2.get_current_user)
    return turnonwifi.get_turnonwifi(db)

@router.get('/{id}',status_code=200,response_model=schemas.Turnonwifi)
def one_Turnonwifi(id,response: Response,db: Session =Depends(get_db)): #,current_user: schemas.User = Depends(oauth2.get_current_user)
    return turnonwifi.get_one_turnonwifi(id,response,db)
