from dataclasses import dataclass
from typing import Optional


@dataclass
class Product:
    id: str
    title: str
    price: float
    image: str
    brand: str
    review_score: Optional[float]
