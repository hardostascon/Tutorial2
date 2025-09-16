from pydantic_settings import BaseSettings
#class Settings(BaseSettings):
   # user = 'postgres'
   # password = '123456'
   # host = 'localhost'
   # port = '5432'
    #database = 'instituto'
    #DATABASE_URL: str = f"postgresql+asyncpg://{user}:{password}@{host}:{port}/{database}"
    #API_V1_STR: str = "/api/v1"
    #
    
    
class Settings(BaseSettings):
    user: str = 'postgres'
    password: str = '123456'
    host: str = 'localhost'
    port: str = '5432'
    database: str = 'instituto'
    DATABASE_URL: str = f"postgresql+asyncpg://{user}:{password}@{host}:{port}/{database}"
    API_V1_STR: str = "/api/v1"

settings = Settings()
