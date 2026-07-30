from __future__ import annotations

import datetime as dt
from typing import Iterable


PENDING_PAYMENTS = [
    {
        "client": "Client_A",
        "amount": 500,
        "status": "Pending",
        "timestamp": "2026-05-03 11:00:00",
    },
]


def send_reminder(client_name: str) -> None:
    print(f"Reminder queued for {client_name} regarding their M-Pesa request.")


def check_payment_status(
    payments: Iterable[dict] = PENDING_PAYMENTS,
    now: dt.datetime | None = None,
    reminder_after_seconds: int = 7200,
) -> None:
    current_time = now or dt.datetime.now()

    for payment in payments:
        payment_time = dt.datetime.strptime(payment["timestamp"], "%Y-%m-%d %H:%M:%S")
        time_diff = (current_time - payment_time).total_seconds()

        if time_diff > reminder_after_seconds and payment["status"] == "Pending":
            send_reminder(payment["client"])
        else:
            print(f"Status: {payment['client']} is still within the reminder window.")


if __name__ == "__main__":
    check_payment_status()
