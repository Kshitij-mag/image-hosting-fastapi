from fastapi import APIRouter, status, Depends
from typing import List
from ..repository import user_funx
from .. import schemas
from sqlalchemy.orm import Session
from ..database import get_db

router = APIRouter(
    tags=['user'],
    prefix="/user"
)


@router.get('/all', status_code=status.HTTP_226_IM_USED,
            response_model=List[schemas.User])
async def get_all_users(db: Session = Depends(get_db)):
    return user_funx.get_user_data(db)


@router.get('/{id}', status_code=status.HTTP_226_IM_USED,
            response_model=schemas.User)
async def get_all_users(id: int, db: Session = Depends(get_db)):
    return user_funx.get_user_data(db, id)


@router.post('/signup')
async def signup(request: schemas.UserInDB, db: Session = Depends(get_db)):
    user_funx.create_user(request, db)
    return f"user {request.username} created successfully"
