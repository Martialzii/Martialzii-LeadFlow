from __future__ import annotations

from typing import Optional

import requests
from requests.auth import HTTPBasicAuth

from config import settings


class DarajaConfigError(RuntimeError):
    pass


def get_access_token(timeout: int = 20) -> Optional[str]:
    """Return a Daraja access token, or None if the request fails."""
    if not settings.daraja_consumer_key or not settings.daraja_consumer_secret:
        raise DarajaConfigError(
            "Missing DARAJA_CONSUMER_KEY or DARAJA_CONSUMER_SECRET in environment."
        )

    api_url = f"{settings.daraja_base_url}/oauth/v1/generate?grant_type=client_credentials"
    response = requests.get(
        api_url,
        auth=HTTPBasicAuth(settings.daraja_consumer_key, settings.daraja_consumer_secret),
        timeout=timeout,
    )
    response.raise_for_status()
    payload = response.json()
    return payload.get("access_token")


if __name__ == "__main__":
    try:
        token = get_access_token()
    except Exception as exc:
        print(f"Error generating token: {exc}")
    else:
        print(f"Access token received: {token[:10]}..." if token else "No token returned.")
