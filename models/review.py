#!/usr/bin/python3
"""module with BaseModel class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """class with review instance"""
    place_id = ""
    user_id = ""
    text = ""
