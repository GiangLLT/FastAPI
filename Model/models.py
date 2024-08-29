from pydantic import BaseModel
from typing import Optional

# class Item(BaseModel):
#     id  : int
#     name: str
#     description: Optional[str] = None
#     price: float
#     tax: Optional[float] = None
    
class Item(BaseModel):
    id: int
    name: str | None = None
    description: str | None = None
    price: float | None = None
    tax: float | None = None

