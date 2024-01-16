#!/usr/bin/python3
"""This is the review class"""
from sqlalchemy import Column, Integer, String, ForeignKey
from models.base_model import BaseModel, Base


class Review(BaseModel, Base):
    """Defintion for the  Review class
    Attributes:
        user_id: user id
        text: review description
        place_id: place id
    """
    __tablename__ = "reviews"
    text = Column(String(1024), nullable=False)
    place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
