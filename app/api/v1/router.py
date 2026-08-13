from fastapi import APIRouter
from app.api.v1.endpoints import health

api_router = APIRouter()

# Registrar submódulos de la API v1
api_router.include_router(health.router, tags=["Health & System"])
