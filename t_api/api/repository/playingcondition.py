from fastapi import APIRouter, Depends, status, Response, HTTPException
from .. import schemas, database, models
from sqlalchemy.orm import Session

router = APIRouter(prefix="/playingcondition",tags=['playingcondition'])
get_db=database.get_db

def create_playingcondition(request:schemas.Playingcondition, db :Session):
    new_condition = models.Playingcondition(isPlaying = request.isPlaying, isPause = request.isPause, 
                                    isStop = request.isStop, user_id = request.user_id) 
    db.add(new_condition)
    db.commit()
    db.refresh(new_condition)
    return new_condition

def get_playingcondition(db: Session):
    condition = db.query(models.Playingcondition).all()
    return condition


def get_one_playingcondition(id: int,response: Response, db: Session):
    googletoken = db.query(models.Playingcondition).filter(models.Playingcondition.id == id).first()
    if not googletoken:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
                            detail=f"ID {id} is not available")
    return googletoken