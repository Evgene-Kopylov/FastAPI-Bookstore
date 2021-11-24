
import os
from typing import Optional
from dotenv import load_dotenv, find_dotenv
from pydantic import BaseSettings


load_dotenv(find_dotenv())

class Settings(BaseSettings):
    project_name:str = "bookstore api"
    project_version: str = "0.0.1"

    postgres_user: Optional[str] = os.getenv("POSTGRES_USER")
    postgres_password: Optional[str] = os.getenv("POSTGRES_PASSWORD")
    postgres_server: Optional[str] = os.getenv("POSTGRES_SERVER","localhost")
    postgres_port: Optional[str] = os.getenv("POSTGRES_PORT", 5432) # default postgres port is 5432
    postgres_db: Optional[str] = os.getenv("POSTGRES_DB","test_db")
    database_url: Optional[str] = f"postgresql://{postgres_user}:{postgres_password}@{postgres_server}:{postgres_port}/{postgres_db}"

settings = Settings()