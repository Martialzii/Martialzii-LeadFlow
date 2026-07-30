from __future__ import annotations

import time

import psutil


def monitor_system(disk_path: str = "C:", interval_seconds: int = 60) -> None:
    print("Martialzii System Guardian is active.")

    while True:
        disk_usage = psutil.disk_usage(disk_path).percent
        cpu_usage = psutil.cpu_percent(interval=1)

        if disk_usage > 90:
            print(f"Alert: disk usage is high at {disk_usage}%.")

        if cpu_usage > 80:
            print(f"Alert: CPU usage is high at {cpu_usage}%.")

        time.sleep(interval_seconds)


if __name__ == "__main__":
    monitor_system()
