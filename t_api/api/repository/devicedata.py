from sqlalchemy.orm import Session
from .. import models, schemas
from fastapi import HTTPException, status

def get_all(db: Session):
    datas = db.query(models.Devicedata).all()
    return datas

def create(request: schemas.CreateDevicedata, db: Session):
    new_data = models.Devicedata(user_token = request.user_token, status = 'NULL', dev_id = request.dev_id, dev_name = request.dev_name, language = request.language, 
        system_volume = request.system_volume, media_volume = request.media_volume, region = request.region, time_zone = request.time_zone, user_account = request.user_account )
    db.add(new_data)
    db.commit()
    db.refresh(new_data)
    return new_data.status

def show(dev_id: str, db: Session):
    devicedata = db.query(models.Devicedata).filter(models.Devicedata.dev_id == dev_id).first()
    if not devicedata:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
                            detail=f"dev_id {dev_id} is not available")
    return devicedata

def destory( dev_id: str, db: Session):
    devicedata = db.query(models.Devicedata).filter(models.Devicedata.dev_id == dev_id)
    if not devicedata.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Devicedata with dev_id {dev_id} not found")
    devicedata.delete(synchronize_session=False)
    db.commit()
    return 'done'
"""
def updateDevice(request: schemas.Devicedata, db: Session):
    devicedata = db.query(models.Devicedata).filter(models.Devicedata.device_name == str(request.device_name))
    if not devicedata.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Devicedata with name {request.device_name} not found")
    devicedata.update(request.dict())
    db.commit()
    return 'updated'
"""
def updateRegion(request: schemas.UpdateRegion, db: Session):
    devicedata = db.query(models.Devicedata).filter(models.Devicedata.dev_id == str(request.dev_id))
    if not devicedata.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Devicedata with dev_id {request.dev_id} not found")
    devicedata.update(request.dict())
    db.commit()
    return 'done'

def updateTimezone(request: schemas.UpdateTimezone, db: Session):
    devicedata = db.query(models.Devicedata).filter(models.Devicedata.dev_id == str(request.dev_id))
    if not devicedata.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Devicedata with dev_id {request.dev_id} not found")
    devicedata.update(request.dict())
    db.commit()
    return 'done'