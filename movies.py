from dataclasses import dataclass
from typing import Optional


@dataclass
class Movies:
    id: int
    title: str = None
    year: int = None
    director: str = None
    genre: str = None
    rating: float = None
    id: Optional[int] = None
