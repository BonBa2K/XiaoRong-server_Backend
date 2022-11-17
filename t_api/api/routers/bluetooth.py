from typing import List
from fastapi import APIRouter, Depends, status, Response, HTTPException
from .. import schemas,database, models, oauth2
from sqlalchemy.orm import Session
from ..repository import bluetooth

router = APIRouter(prefix="/bluetooth",tags=['bluetooth'])
get_db=database.get_db


@router.post('/',status_code=status.HTTP_201_CREATED) 
def create_bluetooth(request:schemas.Bluetooth,db :Session = Depends(get_db)): #,current_user: schemas.User = Depends(oauth2.get_current_user)
    return bluetooth.create_bluetooth(request,db)


@router.put('/{id}',status_code=status.HTTP_202_ACCEPTED) #, response_model=schemas.Bluetooth
def update_bluetooth(id, request:schemas.Bluetooth, db:Session = Depends(get_db)): #, current_user: schemas.User = Depends(oauth2.get_current_user)
    return bluetooth.update_bluetooth(id,request,db)


@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
def destroy_bluetooth(id,db: Session = Depends(get_db)): #,current_user: schemas.User = Depends(oauth2.get_current_user)
    return bluetooth.destroy_bluetooth(id,db)
    

