"""Configuration management."""
import os
from dataclasses import dataclass


@dataclass
class Config:
    debug: bool = False
    port: int = 8080
    database_url: str = ""
    redis_url: str = ""
    log_level: str = "INFO"

    @classmethod
    def from_env(cls):
        return cls(
            debug=os.getenv("DEBUG", "false").lower() == "true",
            port=int(os.getenv("PORT", "8080")),
            database_url=os.getenv("DATABASE_URL", ""),
            redis_url=os.getenv("REDIS_URL", ""),
            log_level=os.getenv("LOG_LEVEL", "INFO"),
        )
