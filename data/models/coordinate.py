from typing import Optional

from pydantic import BaseModel


class CoordinatesBoundary(BaseModel):
    lat: float
    lng: float


class CoordinatesEntity(BaseModel):
    id: str
    lat: float
    lng: float
    image_url: str
