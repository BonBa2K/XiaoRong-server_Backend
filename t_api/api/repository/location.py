from fastapi import APIRouter, Depends, status,Response, HTTPException
from .. import schemas,database,models
from sqlalchemy.orm import Session

router = APIRouter(prefix="/location",tags=['location'])
get_db=database.get_db


def create_location(request: schemas.Location, db :Session):
    new_location = models.Location(userArea = request.userArea, user_id = request.user_id)
    db.add(new_location)
    db.commit()
    db.refresh(new_location)
    return new_location

def get_location(db: Session):
    location = db.query(models.Location).all()
    return location


def get_one_location(id: int,response: Response, db: Session):
    location = db.query(models.Location).filter(models.Location.id == id).first()
    if not location:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
                            detail=f"ID {id} is not available")
    return location