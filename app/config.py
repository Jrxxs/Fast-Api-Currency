import os
import pathlib
from dataclasses import dataclass
from dotenv import load_dotenv


BASE_DIR = pathlib.Path(__file__).parent.resolve()

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path=dotenv_path)

dataclass
class DBSettings:
    DB_USER: str = os.getenv("POSTGRES_USER")
    DB_PASS: str = os.getenv("POSTGRES_PASSWORD")
    DB_HOST: str = os.getenv("DB_HOST")
    DB_PORT: int = os.getenv("DB_PORT")
    DB_NAME: str = os.getenv("POSTGRES_DB")

    @property
    def DATABASE_URL_asyncpg(self):
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

db_settings = DBSettings()
