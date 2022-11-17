from fastapi import APIRouter, Depends,status,Response, HTTPException
from .. import schemas, database, models
from sqlalchemy.orm import Session



router = APIRouter(prefix="/connectwifi",tags=['connectwifi'])
get_db=database.get_db

def create_connectwifi(request:schemas.Connectwifi, db :Session):
    new_connectwifi = models.Connectwifi(SSID = request.SSID, 
                                            password = request.password, 
                                            isConnected = request.isConnected, 
                                            user_id = request.user_id) 
    db.add(new_connectwifi)
    db.commit()
    db.refresh(new_connectwifi)
    return new_connectwifi

def get_connectwifi(db: Session):
    connectwifi = db.query(models.Connectwifi).all()
    return connectwifi

def get_one_connectwifi(id: int,response: Response, db: Session):
    connectwifi = db.query(models.Connectwifi).filter(models.Connectwifi.id == id).first()
    if not connectwifi:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
                            detail=f"ID {id} is not available")
    return connectwifi