from functools import lru_cache

from dotenv import find_dotenv
from pydantic import BaseSettings, PostgresDsn, validator


class __DBSettings(BaseSettings):
    """DB connection settings"""

    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str
    POSTGRES_PORT: str
    POSTGRES_DB: str
    SQLALCHEMY_DATABASE_URI: PostgresDsn | None = None

    @validator("SQLALCHEMY_DATABASE_URI")
    def assemble_db_con(cls, current_value: str | None, values: dict[str, str]) -> str:
        return (
            current_value
            if current_value
            else str(
                PostgresDsn.build(
                    scheme="postgresql+asyncpg",
                    user=values.get("POSTGRES_USER"),
                    password=values.get("POSTGRES_PASSWORD"),
                    host=values.get("POSTGRES_HOST"),
                    port=values.get("POSTGRES_PORT"),
                    path="/" + values.get("POSTGRES_DB", ""),
                )
            )
        )


class Settings(__DBSettings):
    """All app settings"""

    PROJECT_NAME: str = "Interview Backend"
    DESCRIPTION: str = "Test task for Interview"
    VERSION: str = "0.1.0"
    DEBUG: bool
    API_PREFIX: str = "/api"

    HOST: str = "0.0.0.0"
    PORT: int = 5000

    @validator("DEBUG")
    def assemble_secure(cls, development: bool | None, values: dict[str, str]) -> bool:
        if development is not None:
            values["GUNICORN_RELOAD"] = str(development)
            return development

        raise ValueError("DEBUG must be set")

    class Config:
        env_file = find_dotenv(raise_error_if_not_found=False)
        env_file_encoding = "utf-8"
        case_sensitive = True


@lru_cache
def get_settings() -> Settings:
    """Cached Settings factory, prevents unnecessary reading of the env file"""

    return Settings()
