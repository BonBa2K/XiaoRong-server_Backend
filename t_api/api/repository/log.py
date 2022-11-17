from fastapi import APIRouter, status, Response, HTTPException
from .. import schemas, database, models
from sqlalchemy.orm import Session

router = APIRouter(prefix="/log",tags=['log'])
get_db=database.get_db

def create_log(request:schemas.Log, db :Session):
    new_log = models.Log(status = request.status, user_id = request.user_id) 
    db.add(new_log)
    db.commit()
    db.refresh(new_log)
    return new_log

def get_log(db: Session):
    log = db.query(models.Log).all()
    return log

def get_one_log(id: int,response: Response, db: Session):
    log = db.query(models.Log).filter(models.Log.id == id).first()
    if not log:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
                            detail=f"ID {id} is not available")
    return log