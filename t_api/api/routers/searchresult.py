from typing import List
from fastapi import APIRouter, Depends, status, Response, HTTPException
from .. import schemas, database, models, oauth2
from sqlalchemy.orm import Session
from ..repository import searchresult

router = APIRouter(prefix="/searchresult",tags=['searchresult']) 
get_db=database.get_db

@router.post('/',status_code=status.HTTP_201_CREATED)
def create(request: schemas.Searchresult,db :Session = Depends(get_db)): # ,current_user: schemas.User = Depends(oauth2.get_current_user
    return searchresult.create_searchresult(request,db)

@router.get('/',response_model=List[schemas.Searchresult])
def all_searchresult(db: Session = Depends(get_db)): # ,current_user: schemas.User = Depends(oauth2.get_current_user)
    return searchresult.get_searchresult(db)

@router.get('/{id}',status_code=200,response_model=schemas.Searchresult)
def one_searchresult(id,response: Response,db: Session =Depends(get_db)): #,current_user: schemas.User = Depends(oauth2.get_current_user)
    return searchresult.get_one_searchresult(id,response,db)
