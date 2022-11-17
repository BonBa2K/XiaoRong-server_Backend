import re
from fastapi import APIRouter, Depends, status, Response, HTTPException
from .. import schemas, database, models
from sqlalchemy.orm import Session

router = APIRouter(prefix="/searchresult",tags=['searchresult'])
get_db=database.get_db

def create_searchresult(request:schemas.Searchresult, db :Session):
    new_result = models.Searchresult(searchResultURL = request.searchResultURL, 
                                        searchKeyWord = request.searchKeyWord, 
                                        time = request.time, 
                                        user_id = request.user_id)
    db.add(new_result)
    db.commit()
    db.refresh(new_result)
    return new_result

def get_searchresult(db: Session):
    result = db.query(models.Searchresult).all()
    return result

def get_one_searchresult(id: int,response: Response, db: Session):
    result = db.query(models.Searchresult).filter(models.Searchresult.id == id).first()
    if not result:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
                            detail=f"ID {id} is not available")
    return result