from datetime import datetime
from fastapi import HTTPException, status
from ..models import Image


def search_image(url, user_id, db):
    search = db.query(Image).filter(Image.user_id == user_id).all()
    for x in search:
        if url == x.url:
            return True
    return False


def get_image(id, db):
    image = db.query(Image).filter(Image.id == id).first()

    if not image:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"image {id} not found")

    return image


def post_image(request, db):
    if search_image(request.url, request.user_id, db):
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE,
                            detail=f"image already belongs to user {request.user_id}")

    image = Image(
        date=datetime.utcnow(),
        url=request.url,
        user_id=request.user_id
    )
    db.add(image)
    db.commit()
    db.refresh(image)


def update_views(id, db):
    image = db.query(Image).filter(Image.id == id).first()
    image.views = image.views + 1
    db.commit()
