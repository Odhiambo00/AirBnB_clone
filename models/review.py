#!/usr/bin/python3

"""Defines class Review"""

from models.base_model import BaseModel


class Review(BaseModel):
    """class Review that inherits from class BaseModel"""

    place_id = ''
    user_id = ''
    text = ''
