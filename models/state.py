#!/usr/bin/python3
"""State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
import models

Base = declarative_base()

class State(BaseModel, Base):
    """ Representation of state"""
    if models.storage_type == "db":
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        #places = relationship("Place", backref="cities")
    else:
        state_id = ""
        name = ""
    def __init__(self, *args, **kwargs):
        """Initializes city"""
        super().__init__(*args, **kwargs)
