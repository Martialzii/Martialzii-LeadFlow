from __future__ import annotations

import os
from dataclasses import dataclass

from dotenv import load_dotenv


load_dotenv()


@dataclass(frozen=True)
class Settings:
    gemini_api_key: str = os.getenv("GEMINI_API_KEY", "")
    daraja_consumer_key: str = os.getenv("DARAJA_CONSUMER_KEY", "")
    daraja_consumer_secret: str = os.getenv("DARAJA_CONSUMER_SECRET", "")
    daraja_env: str = os.getenv("DARAJA_ENV", "sandbox")
    evaluation_fee: int = int(os.getenv("LEADFLOW_EVALUATION_FEE", "500"))

    @property
    def daraja_base_url(self) -> str:
        if self.daraja_env.lower() == "production":
            return "https://api.safaricom.co.ke"
        return "https://sandbox.safaricom.co.ke"


settings = Settings()
