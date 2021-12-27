#!/usr/bin/python3
""" Defines BaseModel that defines all common attributes/methods for other classes"""

from uuid import uuid4
from datetime import datetime

from models import storage


class BaseModel:
    """ class BaseModel """

    def __init__(self, *args, **kwargs):
        """
            Initialize a new BaseModel instance
            Parameters
            ----------
                width : int
                    width of the rectangle
                height : int
                    height of the rectangle
        """
        if not kwargs:
            self.id = str(uuid4())
            self.created_at = self.updated_at = datetime.now()
            storage.new(self)
        else:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key in ("created_at", "updated_at"):
                        setattr(self, key, datetime.fromisoformat(value))
                    else:
                        setattr(self, key, value)

    def __str__(self):
        """
            String representation of the instance of BaseModel

            Returns
            -------
                str
                    the BaseModel instance string representation
        """
        return "[{}] ({}) {}".format(type(self).__name__, self.id,
                                     self.__dict__)

    def save(self):
        """
            updates the public instance attribute updated_at
            with the current datetime
        """

        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
            get dictionary representation of a BaseModel
            instance
            
            Returns
            -------
                dict
                    dictionary representation of a BaseModel
        """
        result = {}

        for key, value in self.__dict__.items():
            if isinstance(value, datetime):
                result[key] = value.isoformat()
            else:
                result[key] = value

        result['__class__'] = self.__class__.__name__

        return result
            
