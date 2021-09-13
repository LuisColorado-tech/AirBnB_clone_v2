#!/usr/bin/python3
"""this module defines engine DBStorage"""
from sqlalchemy import (create_engine)
from os import getenv
from sqlalchemy.orm import sessionmaker, Session
from models.base_model import Base, BaseModel
from models.amenity import Amenity
from models.city import City
from models.state import State
from models.user import User
from models.place import Place
from models.review import Review
from sqlalchemy.orm import scoped_session


class DBStorage:
    """DBStorage class"""
    __engine = None
    __session = None

    def __init__(self):
        """initialization of class DBStorage"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(getenv("HBNB_MYSQL_USER"),
                                              getenv("HBNB_MYSQL_PWD"),
                                              getenv("HBNB_MYSQL_HOST"),
                                              getenv("HBNB_MYSQL_DB")),
                                      pool_pre_ping=True)

        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """method that return all objecs"""
        new_dict = {}
        if cls is not None:
            for key in self.__session.query(cls):
                new_dict[key.__class__.__name__ + "." + key.id] = key
            return new_dict

        else:
            for key in (self.__session.query(User)):
                new_dict[key.__class__.__name__ + "." + key.id] = key
            for key in(self.__session.query(State)):
                new_dict[key.__class__.__name__ + "." + key.id] = key
            for key in (self.__session.query(City)):
                new_dict[key.__class__.__name__ + "." + key.id] = key
            for key in (self.__session.query(Place)):
                new_dict[key.__class__.__name__ + "." + key.id] = key
            for key in (self.__session.query(Review)):
                new_dict[key.__class__.__name__ + "." + key.id] = key
            return new_dict

    def new(self, obj):
        """method new that add a new object"""
        self.__session.add(obj)

    def save(self):
        """method save that commit changes"""
        self.__session.commit()

    def delete(self, obj=None):
        """method delete that delete the databade"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """method reload that reload the session"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
        
    def close(self):
        """removing the session"""
        self.__session.close()
