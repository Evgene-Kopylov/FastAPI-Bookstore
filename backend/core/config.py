
import os
from dotenv import load_dotenv
from pydantic import BaseSettings

from pathlib import Path
env_path = Path('../.env')
load_dotenv(dotenv_path=env_path)

class Settings(BaseSettings):
    project_name:str = "bookstore api"
    project_version: str = "0.0.1"

    postgres_user : str = os.getenv("POSTGRES_USER")
    postgres_password: str = os.getenv("POSTGRES_PASSWORD")
    postgres_server : str = os.getenv("POSTGRES_SERVER","localhost")
    postgres_port : str = os.getenv("POSTGRES_PORT",5432) # default postgres port is 5432
    postgres_db : str = os.getenv("POSTGRES_DB","test_db")
    database_url = f"postgresql://{postgres_user}:{postgres_password}@{postgres_server}:{postgres_port}/{postgres_db}"

settings = Settings()