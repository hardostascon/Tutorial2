

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from db.models import Alumno
from api.routes.schemas import AlumnoCreate, AlumnoResponse
from typing import List, Optional

class AlumnoService: 
    def __init__(self, db):
        self.db = db
    
    async def create_alumno(self, user_data):
        db_alumno = Alumno(
            nombre_alumno=user_data.nombre_alumno,
            apellido_alumno=user_data.apellido_alumno,
            email_alumno=user_data.email_alumno,
            fecha_nacimiento=user_data.fecha_nacimiento
        )
        self.db.add(db_alumno)
        await self.db.commit()
        await self.db.refresh(db_alumno)
        return AlumnoResponse.from_orm(db_alumno)
      
    async def get_alumno_by_id(self, alumno_id: int) -> Optional[AlumnoResponse]:
        result = await self.db.execute(
            select(Alumno).where(Alumno.id_alumno == alumno_id)
        )
        alumno = result.scalar_one_or_none()
        
        if alumno:
            return AlumnoResponse.from_orm(alumno)
        return None
    
    async def get_all_alumnos(self) -> List[AlumnoResponse]:
        result = await self.db.execute(
            select(Alumno).where(Alumno.activo == True)
        )
        alumnos = result.scalars().all()
        
        return [AlumnoResponse.from_orm(alumno) for alumno in alumnos]        