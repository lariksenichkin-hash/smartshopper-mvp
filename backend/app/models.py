from pydantic import BaseModel
from typing import Optional

class Item(BaseModel):
    title: str
    price: float
    source: str
    type: str
    availability: str
    pickup: Optional[dict]
