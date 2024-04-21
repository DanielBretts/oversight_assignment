from fastapi import APIRouter
from pydantic import BaseModel
from starlette.responses import FileResponse
from data.data_handler import get_images_by_location

router = APIRouter()


@router.get("/")
async def get_map():
    return FileResponse("map.html")


class Coordinates(BaseModel):
    lat: float
    lng: float


@router.post("/coordinates/")
async def receive_coordinates(coordinates: Coordinates):
    bbox_radius = 0.1  # Example: 0.01 degrees
    bbox = {
        "min_lng": round(coordinates.lng - bbox_radius, 3),
        "min_lat": round(coordinates.lat - bbox_radius, 3),
        "max_lng": round(coordinates.lng + bbox_radius,3),
        "max_lat": round(coordinates.lat + bbox_radius,3),
    }

    print(bbox)

    print(await get_images_by_location(bbox))
    return {"received": coordinates}
