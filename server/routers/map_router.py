from fastapi import APIRouter
from starlette.responses import FileResponse

router = APIRouter()


# drone_service = DronesService(collection_drones)

@router.get("/")
async def get_map():
    return FileResponse("map.html")
