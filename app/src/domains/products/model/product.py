from dataclasses import dataclass
from typing import Optional
from pydantic import BaseModel


@dataclass
class Product:
    id: str
    title: str
    price: float
    image: str
    brand: str
    review_score: Optional[float]


class ProductResponse(BaseModel):
    """
    Schema for single product http response
    """
    id: str
    title: str
    price: float
    image: str
    brand: str
    review_score: Optional[float]
