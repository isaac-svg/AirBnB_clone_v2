#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column,  String
import models
from models.city import City
import shlex


class State(BaseModel, Base):
    """Defintion for the State class
    Attributes:
        name: input name
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade='all, delete, delete-orphan', backref="state")

    @property
    def cities(self):
        var = models.storage.all()
        city_list = []
        result = []
        for key in var:
            city = key.replace('.', ' ')
            city = shlex.split(city)
            if (city[0] == 'City'):
                city_list.append(var[key])
        for element in city_list:
            if (element.state_id == self.id):
                result.append(element)
        return (result)
