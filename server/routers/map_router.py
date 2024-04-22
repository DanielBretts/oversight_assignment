import os

from fastapi import APIRouter
from pydantic import BaseModel
from starlette.responses import FileResponse
from data.data_fetcher import get_images_by_location
from data.db_connection import create_connection, list_tables, execute_query
from data.models.coordinate import CoordinatesBoundary, CoordinatesEntity

router = APIRouter()

path_to_db = os.getcwd()+"/data/coordinates"


@router.get("/")
async def get_map():
    return FileResponse("map.html")


def store_point_locally(conn,coordinates: CoordinatesEntity):
    ce = CoordinatesEntity(id=coordinates['id'],lat=coordinates['computed_geometry']['coordinates'][1],
                                             lng=coordinates['computed_geometry']['coordinates'][0])


    query = f"INSERT INTO points (id, latitude, longitude) \
        VALUES ('{ce.id}', '{ce.lat}', '{ce.lng}');"

    if conn:
        # Execute the query and fetch the results
        results = execute_query(conn, query)
        conn.commit()
        if results:
            for row in results:
                print(row)

    else:
        print("Error! cannot create the database connection.")


# @router.post("/coordinates/")
# async def receive_coordinates(coordinates: CoordinatesBoundary):
#     bbox_radius = 0.5
#     bbox = {
#         "min_lng": round(coordinates.lng - bbox_radius, 3),
#         "min_lat": round(coordinates.lat - bbox_radius, 3),
#         "max_lng": round(coordinates.lng + bbox_radius, 3),
#         "max_lat": round(coordinates.lat + bbox_radius, 3),
#     }
#     print(bbox)
#
#     response = await get_images_by_location(bbox)
#     if response:
#         conn = create_connection(path_to_db)
#         data = response['data']
#         for coordinate in data:
#             print(coordinate)
#             store_point_locally(conn,coordinate)
#         # Close the connection
#         conn.close()
#         return {"received": data}
#     return {"error": "error"}
@router.post("/coordinates/")
async def receive_coordinates(coordinates: CoordinatesBoundary):
    bbox_radius = 0.5
    bbox = {
        "min_lng": round(coordinates.lng - bbox_radius, 3),
        "min_lat": round(coordinates.lat - bbox_radius, 3),
        "max_lng": round(coordinates.lng + bbox_radius, 3),
        "max_lat": round(coordinates.lat + bbox_radius, 3),
    }
    print(bbox)

    response = await get_images_by_location(bbox)
    if response:
        try:
            conn = create_connection(path_to_db)
            data = response['data']
            for coordinate in data:
                print(coordinate)
                store_point_locally(conn, coordinate)
            # Close the connection
            conn.close()
            return {"received": data}
        except Exception as e:
            return {"error": str(e)}
    return {"error": "No response from get_images_by_location"}
