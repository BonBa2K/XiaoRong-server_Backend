from fastapi import APIRouter, Depends,status, Response, HTTPException #
from .. import schemas,database,models
from sqlalchemy.orm import Session


router = APIRouter(prefix="/bluetooth",tags=['bluetooth'])
get_db = database.get_db

def create_bluetooth(request:schemas.Bluetooth,db: Session):
    new_bluetooth = models.Bluetooth(bluetoothDeviceName=request.bluetoothDeviceName, user_id=request.user_id) #
    db.add(new_bluetooth)
    db.commit()
    db.refresh(new_bluetooth)
    return new_bluetooth

def update_bluetooth(id:int, request, db :Session):
    new_bluetooth = db.query(models.Bluetooth).filter(models.Bluetooth.id == id)
    if not new_bluetooth.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blutooth with the id {id} is not available")
    new_bluetooth.update({'bluetoothDeviceName':request.bluetoothDeviceName})
    db.commit()
    # db.refresh(new_bluetooth)
    return 'updated'

def destroy_bluetooth(id:int ,db: Session):
    bluetooth = db.query(models.Bluetooth).filter(models.Bluetooth.id == id)
    if not bluetooth.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Bluetooth with id {id} not found")
    bluetooth.delete(synchronize_session=False)
    db.commit()
