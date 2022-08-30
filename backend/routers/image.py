from fastapi import APIRouter, status, Depends, UploadFile, File, HTTPException
from fastapi.responses import Response
from .. import schemas, models
from sqlalchemy.orm import Session
from ..database import get_db
from .authenticate import get_current_active_user
from uuid import uuid4

router = APIRouter(
    tags=['image'],
    prefix="/image"
)


@router.post('/upload')
async def post_image(current_user: schemas.User = Depends(get_current_active_user),
                     image: UploadFile = File(...), db: Session = Depends(get_db)):
    contents = await image.read()
    img_id = uuid4().hex
    img = models.Image(id=img_id, user_id=current_user.id, image=contents)
    db.add(img)
    db.commit()
    db.refresh(img)
    return {"details": "image uploaded succesfully"}


@router.get('/{id}')
async def get_image(id: str, db: Session = Depends(get_db)):
    img = db.query(models.Image).filter(
        models.Image.id == id
    ).first()
    response = Response(img.image)
    return response


@router.put('/{id}')
async def update_img():
    pass


@router.delete('{id}')
async def del_img(id: str, db: Session = Depends(get_db)):
    db.query(models.Image).filter(
        models.Image.id == id
    ).delete(synchronize_session=False)

    return {"details": "fcking deleted"}
