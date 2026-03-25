"""Application configuration helpers."""

from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
ENV_PATH = BASE_DIR / ".env"


def load_env(env_path: Path = ENV_PATH) -> None:
    """Load simple KEY=VALUE pairs from a .env file if present."""
    if not env_path.exists():
        return

    for raw_line in env_path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))


@dataclass
class Settings:
    openai_api_key: str
    model_name: str = "gpt-4o-mini"
    temperature: float = 0.7
    max_history: int = 10
    app_name: str = "AI Chatbot"


def get_settings() -> Settings:
    """Return application settings from environment variables."""
    load_env()
    return Settings(
        openai_api_key=os.getenv("OPENAI_API_KEY", ""),
        model_name=os.getenv("MODEL_NAME", "gpt-4o-mini"),
        temperature=float(os.getenv("TEMPERATURE", "0.7")),
        max_history=int(os.getenv("MAX_HISTORY", "10")),
        app_name=os.getenv("APP_NAME", "AI Chatbot"),
    )

