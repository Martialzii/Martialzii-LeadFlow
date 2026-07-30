from __future__ import annotations

import re


KENYAN_PHONE_PATTERN = re.compile(r"(?<!\d)(?:\+?254|0)7\d{8}(?!\d)")
EMAIL_PATTERN = re.compile(r"[\w\.-]+@[\w\.-]+\.\w+")


def redact_sensitive_data(text: str) -> str:
    """Redact common lead PII before logging or showing diagnostic output."""
    redacted = KENYAN_PHONE_PATTERN.sub("[REDACTED_PHONE]", text)
    return EMAIL_PATTERN.sub("[REDACTED_EMAIL]", redacted)


if __name__ == "__main__":
    sample = "New Lead: Cyrus, Phone: 254712345678, Email: test@example.com"
    print(redact_sensitive_data(sample))
