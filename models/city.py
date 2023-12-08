#!/usr/bin/python3

from models.base_model import BaseModel


class City(BaseModel):
    """City class that inherits from BaseModel
    with Public class attributes
    """
    state_id: str = ""
    name: str = ""
