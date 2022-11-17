from typing import List
from fastapi import APIRouter, Depends, status, HTTPException
from .. import schemas, database, models, oauth2
from sqlalchemy.orm import Session
from ..repository import userdata

router = APIRouter(
    prefix = "/userdata",
    tags = ['Userdatas']
)
get_db = database.get_db

@router.get("/", response_model = List[schemas.Userdata])
def all(db: Session = Depends(get_db)):
    return userdata.get_all(db)

@router.post("/", status_code=status.HTTP_201_CREATED)
def create(request: schemas.Userdata, db: Session = Depends(get_db)):
    return userdata.create(request, db)

@router.get("/{user_email}", status_code=200, response_model = schemas.Userdata)
def show(user_email, db: Session = Depends(get_db)):
    return userdata.show(user_email, db)

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def destroy_test( id, db: Session = Depends(get_db)):
    return userdata.destory_test(id, db)

@router.put("/email", status_code=status.HTTP_202_ACCEPTED)
def updateEmail( request: schemas.UpdateEmail, db: Session = Depends(get_db)):
    return userdata.updateEmail(request, db)

@router.put("/name", status_code=status.HTTP_202_ACCEPTED)
def updateName( request: schemas.UpdateName, db: Session = Depends(get_db)):
    return userdata.updateName(request, db)