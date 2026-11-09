from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    app_name: str = "Universal YouTube Agent API"
    environment: str = "development"
    database_url: str = "postgresql+psycopg://postgres:postgres@localhost:5432/youtube_agent"
    redis_url: str = "redis://localhost:6379/0"
    publishing_mode: str = "approval_required"
    max_monthly_spend_usd: float = Field(default=0, ge=0)
    secret_encryption_key: str | None = None


@lru_cache
def get_settings() -> Settings:
    return Settings()
