#!/usr/bin/python3
'''
    Implementation of the User class which inherits from BaseModel
'''
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv


class User(BaseModel, Base):
    '''
        Definition of the User class
    '''
    __tablename__ = 'users'

    if getenv('HBNB_TPYE_STORAGE') == 'db':
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places = relationship("Place", passive_deletes=True, backref="user")
        reviews = relationship("Review", passive_deletes=True, backref="user")
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""
