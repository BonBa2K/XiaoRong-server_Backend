from typing import List
from fastapi import APIRouter, Depends, status, Response, HTTPException
from .. import schemas, database, models, oauth2
from sqlalchemy.orm import Session
from ..repository import connectwifi

router = APIRouter(prefix="/connectwifi",tags=['connectwifi'])
get_db=database.get_db

@router.post('/',status_code=status.HTTP_201_CREATED)
def create(request: schemas.Connectwifi, db :Session = Depends(get_db)): # ,current_user: schemas.User = Depends(oauth2.get_current_user
    return connectwifi.create_connectwifi(request, db)

@router.get('/',response_model=List[schemas.Connectwifi])
def all_Connectwifi(db: Session = Depends(get_db)): # ,current_user: schemas.User = Depends(oauth2.get_current_user)
    return connectwifi.get_connectwifi(db)
    
@router.get('/{id}',status_code=200,response_model=schemas.Connectwifi)
def one_Connectwifi(id,response: Response,db: Session =Depends(get_db)): #,current_user: schemas.User = Depends(oauth2.get_current_user)
    return connectwifi.get_one_connectwifi(id,response,db)
