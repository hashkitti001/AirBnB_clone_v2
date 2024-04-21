#!/usr/bin/python3
from sqlalchemy import create_engine
from os import getenv
from sqlalchemy.ext.declarative import declarative_base
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

classes = {
    "Amenity": Amenity, 
    "City": City,
    "Place": Place, 
    "Review": Review, 
    "State": State, 
    "User": User 
    }
Base = declarative_base()


class DBStorage:
    """
    Manages storage of entities in the MySQL database
    """
    __engine = None
    __session = None

    def __init__(self):
        """Establishes a connection to the database server"""
        hbnb_user = getenv("HBNB_MYSQL_USER")
        hbnb_passwd = getenv("HBNB_MYSQL_PWD")
        hbnb_host = getenv("HBNB_MYSQL_HOST", "localhost")
        hbnb_db = getenv("HBNB_MYSQL_DB")
        hbnb_env = getenv("HBNB_ENV")
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(hbnb_user,
                                              hbnb_passwd,
                                              hbnb_host,
                                              hbnb_db), pool_pre_ping=True)
        if hbnb_env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Queries based on the current database selection"""
        new_dict = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.name + '.' + obj.id
                    new_dict[key] = obj
                return new_dict
    def new(self, obj):
        """Adds an object to the current database session"""
        self.__session.add(obj)
    def save(self):
        """Commits the changes made in the database session"""
        self.__session.commit()
    def delete(self, obj=None):
        """Deletes an item from the current database session"""
        if obj is not None:
            self.__session.delete(obj)
    def reload(self):
        """Creates all tables in the database"""
        from sqlalchemy.orm import sessionmaker, scoped_session
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(Session)
x = DBStorage()
x.all()