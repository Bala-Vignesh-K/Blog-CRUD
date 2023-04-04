from fastapi import APIRouter, Depends, status, Response, HTTPException
from .. import schemas, database, models
from typing import List
from sqlalchemy.orm import Session
from .. import hashing
from ..repo import user


router = APIRouter(
    tags = ['Users'],
    prefix = "/user"
)

get_db = database.get_db



@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return user.create_user(request, db)



@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowUser)
def get_user(id:int, db: Session = Depends(get_db)):
    return user.get_user(id, db)



