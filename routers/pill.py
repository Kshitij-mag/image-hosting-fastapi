from fastapi import APIRouter, status, Depends
from repository import pill_funx
import schemas
from sqlalchemy.orm import Session
from database import get_db

router = APIRouter(
    tags=['user'],
    prefix="/user"
)


@router.post('')
def addPill(request: schemas.)