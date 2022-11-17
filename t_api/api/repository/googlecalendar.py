# 
from fastapi import APIRouter, Depends, status, Response, HTTPException
from .. import schemas, database, models
from sqlalchemy.orm import Session

router = APIRouter(prefix="/googlecalendar",tags=['googlecalendar'])
get_db=database.get_db

def create_googlecalendar(request:schemas.Googlecalendar,db: Session):
    new_googlecalendar = models.Googlecalendar(ACCESS_TOKEN= request.ACCESS_TOKEN, 
                                            API_KEY = request.API_KEY, 
                                            CLIENT_SECRET = request.CLIENT_SECRET, 
                                            user_id = request.user_id)
    db.add(new_googlecalendar)
    db.commit()
    db.refresh(new_googlecalendar)
    return new_googlecalendar

def get_all_googlecalendar(db: Session): # , response_model=List[schemas.Googletoken]
    googlecalendar = db.query(models.Googlecalendar).all()
    return googlecalendar

def get_one_googlecalendar(id: int,response: Response, db: Session):
    googlecalendar = db.query(models.Googlecalendar).filter(models.Googlecalendar.id == id).first()
    if not googlecalendar:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
                            detail=f"ID {id} is not available")
    return googlecalendar