from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from db.database import get_async_session
from services.alumno_service import AlumnoService

async def get_alumno_service(
    db: AsyncSession = Depends(get_async_session)
) -> AlumnoService:
    return AlumnoService(db)