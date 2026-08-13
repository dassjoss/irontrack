from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.router import api_router

app = FastAPI(
    title="IronTrack API",
    version="0.1.0",
    description="Backend de alto rendimiento para el seguimiento de entrenamiento físico y rutinas.",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Configuración de CORS para desarrollo local y redes de Tailscale
origins = [
    "http://localhost:3000",
    "http://localhost:8000",
    "http://127.0.0.1:8000",
    "*"  # En producción, restringir a dominios específicos o *.ts.net
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir router v1
app.include_router(api_router, prefix="/api/v1")


@app.get("/", summary="Bienvenida")
async def root():
    return {
        "app": "IronTrack API",
        "version": "0.1.0",
        "docs": "/docs",
        "tailscale_ready": True
    }
