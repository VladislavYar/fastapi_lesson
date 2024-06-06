from pydantic import BaseModel, AnyHttpUrl
from pydantic_settings import BaseSettings, SettingsConfigDict

from pathlib import Path


BASE_DIR = Path(__file__).parent

SQLITE_DB_PATH = BASE_DIR / "db.sqlite3"


class PermissionServiceSettings(BaseModel):
    url: AnyHttpUrl = "http://localhost:8000/permissions/check/"


class CorsSettings(BaseModel):
    allow_origins: list[str] = [
        "http://localhost",
        "http://localhost:8000",
        "http://127.0.0.1",
        "http://127.0.0.1:8000",
    ]
    allow_credentials: bool = True
    allow_methods: list[str] = ["*"]
    allow_headers: list[str] = ["*"]


class DbSettings(BaseModel):
    url: str = f"sqlite+aiosqlite:///{SQLITE_DB_PATH}"
    echo: bool = True


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_prefix="APP_",
        env_nested_delimiter="__",
    )
    host: str = "localhost"
    port: int = 8000
    reload: bool = True
    cors: CorsSettings = CorsSettings()
    db: DbSettings = DbSettings()
    permission: PermissionServiceSettings = PermissionServiceSettings()


settings = Settings()
