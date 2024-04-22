from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from server.routers.map_router import router as map_router

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # This allows requests from any origin. Adjust as needed.
    allow_credentials=True,
    allow_methods=["POST"],
    allow_headers=["*"],
)

app.include_router(map_router)
