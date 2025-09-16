from fastapi import APIRouter, Depends, HTTPException
from typing import List
from api.routes.schemas import AlumnoCreate, AlumnoResponse
from services.alumno_service import AlumnoService
from core.dependencies import get_alumno_service

router = APIRouter(prefix="/alumnos", tags=["alumnos"])

@router.post("/", response_model=AlumnoResponse)
async def create_alumno(
    alumno: AlumnoCreate,
    service: AlumnoService = Depends(get_alumno_service)
):
    return await service.create_alumno(alumno)

@router.get("/{alumno_id}", response_model=AlumnoResponse)
async def get_alumno(
    alumno_id: int,
    service: AlumnoService = Depends(get_alumno_service)
):
    alumno = await service.get_alumno_by_id(alumno_id)
    if not alumno:
        raise HTTPException(status_code=404, detail="Alumno not found")
    return alumno

@router.get("/", response_model=List[AlumnoResponse])
async def get_all_alumnos(
    service: AlumnoService = Depends(get_alumno_service)
):
    return await service.get_all_alumnos()