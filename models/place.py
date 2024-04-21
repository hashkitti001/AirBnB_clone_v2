#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel,Base
import models
from sqlalchemy import Column, String, Integer, Float


class Place(BaseModel,Base):
    """ A place to stay """
    if models.storage_type == "db":
       __tablename__ = 'places'
       city_id =  Column(String(60), nullable="False"),
       user_id =  Column(String(60), nullable="False"),
       name =  Column(String(128), nullable="False"),
       description =  Column(String(1024), nullable="False"),
       number_rooms =  Column(Integer, nullable="False", default=0),
       max_guest = Column(Integer, nullable=False)
       latitude = Column(Float, nullable=False)
       longitude = Column(Float, nullable=False)
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []
