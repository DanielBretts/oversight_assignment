from fastapi import APIRouter
from pydantic import BaseModel
from starlette.responses import FileResponse

router = APIRouter()


@router.get("/")
async def get_map():
    return FileResponse("map.html")


class Coordinates(BaseModel):
    lat: float
    lng: float

@router.post("/coordinates/")
async def receive_coordinates(coordinates: Coordinates):
    print('kaki')
    return {"received": coordinates}
