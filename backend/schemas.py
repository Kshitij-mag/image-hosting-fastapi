from pydantic import BaseModel
from typing import Union


class Image(BaseModel):
    image: bytes


class User(BaseModel):
    id: int
    username: str
    email: str
    disabled: Union[bool, None] = None

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Union[str, None] = None


class UserInDB(User):
    password: str
