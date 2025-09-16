from fastapi import FastAPI
from api.routes import alumnos
from core.config import settings


app = FastAPI(title="Instituto API")

app.include_router(alumnos.router, prefix=settings.API_V1_STR)

@app.get("/")
async def root():
    return {"message": "Instituto API"}