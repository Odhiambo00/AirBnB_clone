#!/usr/bin/python3

"""Defines BaseModel class"""

from datetime import datetime
from uuid import uuid4
import models


class BaseModel:
    """
    Represents the parent class that subsequent HBnB project classes will
    inherit from
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes the BaseModel class
        Args:
            *args (any type): Unused
            **kwargs (dict): Attributes key/value pairs
        """

        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if kwargs:
            for k, v in kwargs.items():
                if k == '__class__':
                    continue
                elif k == 'created_at' or k == 'updated_at':
                    setattr(self, k, datetime.strptime(v,
                            '%Y-%m-%dT%H:%M:%S.%f'))
                else:
                    setattr(self, k, v)
        else:
            models.storage.new(self)

    def __str__(self):
        """Returns the string representation of the BaseModel class"""

        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates `updated_at` with the current datetime"""

        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary of BaseModel class instances
        The dictionary includes key,value pair __class__ representing the class
        name of the object
        """

        base_dict = self.__dict__.copy()
        base_dict['created_at'] = self.created_at.isoformat()
        base_dict['updated_at'] = self.updated_at.isoformat()
        base_dict['__class__'] = self.__class__.__name__
        return base_dict
