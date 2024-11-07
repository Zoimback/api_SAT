# app/models/item.py
from pydantic import BaseModel

class Item(BaseModel):
    """
    Simple documentacion
    """
    name: str
    description: str = None
    price: float
    tax: float = None
