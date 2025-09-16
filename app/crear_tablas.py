import asyncio
from db.database import engine
from db.models import Base

async def crear_tablas():
    async with engine.begin() as conn:
        # Crear todas las tablas de forma async
        await conn.run_sync(Base.metadata.create_all)
    
    print("✅ Tablas creadas exitosamente")

# Ejecutar
if __name__ == "__main__":
    asyncio.run(crear_tablas())