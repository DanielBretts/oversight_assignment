from fastapi import FastAPI
from server.routers.map_router import router as map_router

app = FastAPI()

app.include_router(map_router)
