import os
from fastapi import APIRouter
from starlette.responses import FileResponse
from data.data_fetcher import get_images_by_location
from data.db_connection import create_connection, execute_query
from data.models.coordinate import CoordinatesEntity, CoordinatesBoundary
from server.services.map_service import MapService

router = APIRouter()

path_to_db = os.getcwd() + "/data/coordinates"

map_service = MapService(path_to_db)


@router.get("/")
async def get_map():
    return FileResponse("map.html")


@router.post("/coordinates/")
async def receive_coordinates(coordinates: CoordinatesBoundary):
    bbox_radius = 3
    bbox = {
        "min_lng": round(coordinates.lng - bbox_radius, 3),
        "min_lat": round(coordinates.lat - bbox_radius, 3),
        "max_lng": round(coordinates.lng + bbox_radius, 3),
        "max_lat": round(coordinates.lat + bbox_radius, 3),
    }

    response = await get_images_by_location(bbox)
    if response:
        try:
            data = response["data"]
            boundaries = await map_service.store_coordinates(data)
            print(boundaries)
            return {"received": boundaries}
        except Exception as e:
            return {"error": str(e)}
        finally:
            map_service.connection.close()
    return {"error": "No response from get_images_by_location"}


@router.get("/points/")
async def get_points_from_db():
    try:
        points = await map_service.fetch_points_from_db()
        return {"points": points}
    except Exception as e:
        return {"error": str(e)}
