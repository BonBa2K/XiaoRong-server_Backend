from fastapi import APIRouter, Depends,status,Response, HTTPException
from .. import schemas, database, models
from sqlalchemy.orm import Session

router = APIRouter(prefix="/turnonwifi",tags=['turnonwifi'])
get_db=database.get_db

def create_turnonwifi(request:schemas.Turnonwifi, db :Session):
    new_turnonwifi = models.Turnonwifi(isSuccess = request.isSuccess, user_id = request.user_id) 
    db.add(new_turnonwifi)
    db.commit()
    db.refresh(new_turnonwifi)
    return new_turnonwifi

def get_turnonwifi(db: Session):
    turnonwifi = db.query(models.Turnonwifi).all()
    return turnonwifi


def get_one_turnonwifi(id: int,response: Response, db: Session):
    turnonwifi = db.query(models.Turnonwifi).filter(models.Turnonwifi.id == id).first()
    if not turnonwifi:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
                            detail=f"ID {id} is not available")
    return turnonwifi