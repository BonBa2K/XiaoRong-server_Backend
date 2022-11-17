from typing import List
from fastapi import APIRouter, Depends, status, Response, HTTPException
from .. import schemas, database, models
from sqlalchemy.orm import Session

router = APIRouter(prefix="/turnoffwifi",tags=['turnoffwifi'])
get_db=database.get_db

def create_turnoffwifi(request:schemas.Turnonwifi, db :Session):
    new_turnoffwifi = models.Turnoffwifi(isSuccess = request.isSuccess, user_id = request.user_id) 
    db.add(new_turnoffwifi)
    db.commit()
    db.refresh(new_turnoffwifi)
    return new_turnoffwifi

def get_turnoffwifi(db: Session):
    turnoffwifi = db.query(models.Turnoffwifi).all()
    return turnoffwifi

def get_one_turnoffwifi(id: int,response: Response, db: Session):
    turnoffwifi = db.query(models.Turnoffwifi).filter(models.Turnoffwifi.id == id).first()
    if not turnoffwifi:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
                            detail=f"ID {id} is not available")
    return turnoffwifi