from typing import List
from fastapi import APIRouter, Depends, status, HTTPException
from .. import schemas, database, models, oauth2
from sqlalchemy.orm import Session
from ..repository import devicedata

router = APIRouter(prefix = "/devicedata",tags = ['Devicedatas'])
get_db = database.get_db

@router.get("/", response_model = List[schemas.Devicedata])
def all(db: Session = Depends(get_db)):
    return devicedata.get_all(db)

@router.post("/", status_code=status.HTTP_201_CREATED)
def create(request: schemas.CreateDevicedata, db: Session = Depends(get_db)):
    return devicedata.create(request, db)

@router.get("/{dev_id}", status_code=200, response_model = schemas.Devicedata)
def show(dev_id, db: Session = Depends(get_db)):
    return devicedata.show(dev_id, db)

@router.delete("/{dev_id}", status_code=status.HTTP_204_NO_CONTENT)
def destroy( dev_id, db: Session = Depends(get_db)):
    return devicedata.destory(dev_id, db)
"""
@router.put("/device", status_code=status.HTTP_202_ACCEPTED)
def updateDevice( request: schemas.Devicedata, db: Session = Depends(get_db)):
    return devicedata.updateDevice(request, db)
"""
@router.put("/region", status_code=status.HTTP_202_ACCEPTED)
def updateRegion( request: schemas.UpdateRegion, db: Session = Depends(get_db)):
    return devicedata.updateRegion(request, db)

@router.put("/timezone", status_code=status.HTTP_202_ACCEPTED)
def updateTimezone( request: schemas.UpdateTimezone, db: Session = Depends(get_db)):
    return devicedata.updateTimezone(request, db)