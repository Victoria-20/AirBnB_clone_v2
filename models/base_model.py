#!/usr/bin/python3
"""
The base model where all other models will inherit from
"""
from datetime import datetime
import uuid


class BaseModel:
    """A class from where all other models will inherit from
    """
    def __init__(self,  *args, **kwargs):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()


    def __str__(self):
        """Returns a human readable string"""
        return "{[:s]} {(:s)} {}".\
                format(type(self.__name__), self.id, self.__dic__)


    def save(self):
        """updates the public instance attribute updated_at with the current datetime"""
        updated_at = datetime.now()


        
    def to_dic(self):
        """ returns a dictionary containing all keys/values of __dict__ 
        of the instance"""
        new_dic = self.__dic__.copy()
        new_dic['__class__'] = type(self.__name__)
        new_dic['created_at'] = new_dic['created_at'].isoformat()
        new_dic['updated_at'] = new_dic['updated_at'].isoformat()

        return new_dic
