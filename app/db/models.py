# models.py - CORREGIDO

from sqlalchemy import Boolean, Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship 
from .database import Base  # ← Cambiar import relativo

class Alumno(Base):
    __tablename__ = "alumno"
    
    id_alumno = Column(Integer, primary_key=True, index=True)
    nombre_alumno = Column(String, nullable=False)
    apellido_alumno = Column(String, nullable=False)
    email_alumno = Column(String, unique=True, nullable=False)
    fecha_nacimiento = Column(Date, nullable=False)
    activo = Column(Boolean, default=True)
    
    # ✅ CORRECTA: Alumno tiene muchas calificaciones
    calificaciones = relationship("Calificacion", back_populates="alumno")
    
    # ❌ INCORRECTA: ¿Por qué Alumno tiene maestros?
    # maestros = relationship("Maestro", back_populates="especialidad_rel")  # ← ELIMINAR


class Especialidad(Base):
    __tablename__ = "especialidad"
    
    id_especialidad = Column(Integer, primary_key=True, index=True)
    nombre_especialidad = Column(String, unique=True, nullable=False)
    descripcion = Column(String)
    activo = Column(Boolean, default=True)
    
    # ✅ CORRECTA: Una especialidad tiene muchos maestros
    maestros = relationship("Maestro", back_populates="especialidad_rel")


class Maestro(Base):
    __tablename__ = "maestro"
    
    id_maestro = Column(Integer, primary_key=True, index=True)
    nombre_maestro = Column(String, nullable=False)
    apellido_maestro = Column(String, nullable=False)
    email_maestro = Column(String, unique=True, nullable=False)
    especialidad = Column(Integer, ForeignKey("especialidad.id_especialidad"))
    activo = Column(Boolean, default=True)
    
    # ✅ CORRECTAS: 
    especialidad_rel = relationship("Especialidad", back_populates="maestros")
    cursos_maestro = relationship("CursoMaestro", back_populates="maestro")


class Curso(Base):
    __tablename__ = "curso"
    
    id_curso = Column(Integer, primary_key=True, index=True)
    nombre_curso = Column(String, unique=True, nullable=False)
    descripcion = Column(String)
    activo = Column(Boolean, default=True)
    
    # ✅ CORRECTA: Un curso puede tener muchos maestros (a través de curso_maestro)
    cursos_maestro = relationship("CursoMaestro", back_populates="curso")


class CursoMaestro(Base):  # ← Cambiar nombre de clase (sin guión bajo)
    __tablename__ = "curso_maestro"
    
    id_curso_maestro = Column(Integer, primary_key=True, index=True)
    curso_id = Column(Integer, ForeignKey("curso.id_curso"))
    maestro_id = Column(Integer, ForeignKey("maestro.id_maestro"))
    activo = Column(Boolean, default=True)
    
    # ✅ CORRECTAS:
    curso = relationship("Curso", back_populates="cursos_maestro")
    maestro = relationship("Maestro", back_populates="cursos_maestro")
    calificaciones = relationship("Calificacion", back_populates="curso_maestro")


class Calificacion(Base):
    __tablename__ = "calificacion"
    
    id_calificacion = Column(Integer, primary_key=True, index=True)
    alumno_id = Column(Integer, ForeignKey("alumno.id_alumno"))
    curso_maestro_id = Column(Integer, ForeignKey("curso_maestro.id_curso_maestro"))
    fecha_calificacion = Column(Date, nullable=False)
    calificacion = Column(Integer, nullable=False)
    activo = Column(Boolean, default=True)
    
    # ✅ CORRECTAS:
    alumno = relationship("Alumno", back_populates="calificaciones")
    curso_maestro = relationship("CursoMaestro", back_populates="calificaciones")