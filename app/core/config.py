from pydantic_settings import BaseSettings
from hashlib import sha256
from functools import lru_cache


class Settings(BaseSettings):
    SECRET_KEY_RAW: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    DATABASE_URL: str

    @property
    def SECRET_KEY(self) -> str:
        return sha256(self.SECRET_KEY_RAW.encode()).hexdigest()

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


@lru_cache()
def get_settings():
    return Settings()

settings = get_settings()
