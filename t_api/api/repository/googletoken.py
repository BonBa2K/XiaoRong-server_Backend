from fastapi import APIRouter, Depends,status,Response, HTTPException
from .. import schemas, database, models
from sqlalchemy.orm import Session

router = APIRouter(prefix="/googletoken",tags=['googletoken'])
get_db=database.get_db


def create_googletoken(request:schemas.Googletokens,db: Session):
    new_googletoken = models.Googletokenc(access_token = request.access_token, 
                                            api_key = request.api_key, 
                                            client_secret = request.client_secret, 
                                            user_id = request.user_id)
    db.add(new_googletoken)
    db.commit()
    db.refresh(new_googletoken)
    return new_googletoken

def get_all_googletoken(db: Session): # , response_model=List[schemas.Googletoken]
    googletoken = db.query(models.Googletokenc).all()
    return googletoken

def get_one_googletoken(id: int,response: Response, db: Session):
    googletoken = db.query(models.Googletokenc).filter(models.Googletokenc.id == id).first()
    if not googletoken:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
                            detail=f"ID {id} is not available")
    return googletoken