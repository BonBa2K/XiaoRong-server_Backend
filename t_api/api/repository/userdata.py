from sqlalchemy.orm import Session
from .. import models, schemas
from fastapi import HTTPException, status

def get_all(db: Session):
    datas = db.query(models.Userdata).all()
    return datas

def create(request: schemas.Userdata, db: Session):
    new_data = models.Userdata(status = request.status, music_account = request.music_account, device = request.device, 
                                user_name = request.user_name, user_email = request.user_email)
    db.add(new_data)
    db.commit()
    db.refresh(new_data)
    return new_data

def show(user_email: str, db: Session):
    userdata = db.query(models.Userdata).filter(models.Userdata.user_email == user_email).first()
    if not userdata:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
                            detail=f"Email {user_email} is not available")
    return userdata

def destory_test(id: int, db: Session):
    userdata = db.query(models.Userdata).filter(models.Userdata.id == id)
    if not userdata.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Userdata with id {id} not found")
    userdata.delete(synchronize_session=False)
    db.commit()
    return 'done'

def updateEmail(request: schemas.UpdateEmail, db: Session):
    userdata = db.query(models.Userdata).filter(models.Userdata.user_email == str(request.user_email))
    if not userdata.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Userdata with email {request.user_email} not found")
    userdata.update({'user_email':request.new_email})
    db.commit()
    return 'done'

def updateName(request: schemas.UpdateName, db: Session):
    userdata = db.query(models.Userdata).filter(models.Userdata.user_email == str(request.user_email))
    if not userdata.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Userdata with email {request.user_email} not found")
    userdata.update({'user_name':request.user_name})
    db.commit()
    return 'done'