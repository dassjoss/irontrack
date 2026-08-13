from fastapi import APIRouter

router = APIRouter()


@router.get("/health", summary="Diagnóstico de salud del servicio")
async def health_check():
    """
    Verifica el estado del servicio IronTrack.
    """
    return {
        "status": "healthy",
        "service": "IronTrack API",
        "version": "0.1.0"
    }
