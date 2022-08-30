from fastapi import HTTPException, status
from ..models import User
from ..routers import authenticate


def get_user_data(db, id=None):
    if not id:
        user = db.query(User).all()
    else:
        user = db.query(User).filter(User.id == id).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='user not available'
        )

    return user


def create_user(reqeust, db):
    user = User(username=reqeust.username, email=reqeust.email,
                password=authenticate.get_password_hash(reqeust.password))

    db.add(user)
    db.commit()
    db.refresh(user)
