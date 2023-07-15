#!/usr/bin/python3

"""Defines class User"""

from models.base_model import BaseModel


class User(BaseModel):
    """class User that inherits from class BaseModel"""

    email = ''
    password = ''
    first_name = ''
    last_name = ''
