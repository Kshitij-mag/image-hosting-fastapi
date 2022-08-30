from sqlalchemy import Column, ForeignKey, Integer, String, BLOB, Boolean
from sqlalchemy.orm import relationship
from .database import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    password = Column(String)
    email = Column(String)
    disabled = Column(Boolean, default=False)

    images = relationship("Image", back_populates="uploader")


class Image(Base):
    __tablename__ = 'images'

    id = Column(String, primary_key=True)
    image = Column(BLOB)
    views = Column(Integer, default=0)
    likes = Column(Integer, default=0)
    user_id = Column(Integer, ForeignKey('users.id'))

    uploader = relationship("User", back_populates="images")
