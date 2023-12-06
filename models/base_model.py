#!/usr/bin/python3

from uuid import uuid4
from datetime import datetime


class BaseModel:
    """BaseModel class for creating and managing instances.
    """
    def __init__(self, *args, **kwargs):
        """Initialize a new instance of BaseModel.

        Args:
            - *args: arguments
            - **kwargs: a dictionary of key-values arguments
        """
        if kwargs:
            for key, value in kwargs.items():
                time_format = "%Y-%m-%dT%H:%M:%S.%f"
                if key != '__class__':
                    if key in ["created_at", "updated_at"]:
                        value = datetime.strptime(value, time_format)
                        setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """Return a string representation of the instance."""
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def save(self):
        """Update the updated_at attribute and save the instance."""
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of __dict__ of the instance.
        A key __class__ must be added to this dictionary with the class name of the object.
        created_at and updated_at must be converted to string object in ISO format.
        """
        result = self.__dict__.copy()
        result['__class__'] = self.__class__.__name__

        for key, value in result.items():
            if isinstance(value, datetime):
                result[key] = value.isoformat()

        return result