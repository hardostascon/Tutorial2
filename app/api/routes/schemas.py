from pydantic import BaseModel, EmailStr
from datetime import date
from typing import Optional

class AlumnoBase(BaseModel): 
    nombre_alumno: str
    apellido_alumno: str
    email_alumno: EmailStr
    fecha_nacimiento:date
    activo: bool = True
   
class AlumnoCreate(AlumnoBase):
    pass 

class AlumnoUpdate(BaseModel):
    nombre_alumno: Optional[str] = None
    apellido_alumno: Optional[str] = None
    email_alumno: Optional[EmailStr] = None
    fecha_nacimiento: Optional[date] = None
    activo: Optional[bool] = None

class AlumnoResponse(AlumnoBase):
    id_alumno: int
    
    class Config:
        from_attributes = True

class MaestroBase(BaseModel):
    nombre_maestro: str
    apellido_maestro: str
    email_maestro: EmailStr
    especialidad: int
    activo: bool = True   
    
class MaestroCreate(MaestroBase):
    pass

class MaestroResponse(MaestroBase):
    id_maestro: int
    
    class Config:
        from_attributes = True
    
class EspecialidadBase(BaseModel): 
    nombre_especialidad: str
    descripcion: str
    activo: bool = True  
    
class EspecialidadCreate(EspecialidadBase):
    pass

class EspecialidadResponse(EspecialidadBase):
    id_especialidad: int
    
    class Config:
        from_attributes = True    
 
class CursoBase(BaseModel): 
    nombre_curso: str  
    descripcion: str
    activo: bool = True
    
class CursoCreate(CursoBase):
    pass

class CursoResponse(CursoBase):
    id_curso: int
    
    class Config:
        from_attributes = True   
    
class CursoMaestroBase(BaseModel): 
    curso_id: int
    maestro_id: int
    activo: bool = True    

class CalificacionBase(BaseModel): 
    alumno_id: int
    curso_maestro_id: int
    fecha_calificacion: str  
    calificacion: int
    activo: bool = True    
    
class CalificacionCreate(CalificacionBase):
    pass

class CalificacionResponse(CalificacionBase):
    id_calificacion: int
    
    class Config:
        from_attributes = True  