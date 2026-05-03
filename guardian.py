import psutil
import time

def monitor_system():
    print("🛡️ Martialzii System-Guardian is active...")
    while True:
        disk_usage = psutil.disk_usage('C:').percent
        cpu_usage = psutil.cpu_percent(interval=1)
        
        # Alert if disk usage drifts from your 2% target
        if disk_usage > 10:
            print(f"⚠️ ALERT: Disk usage at {disk_usage}%! Check background processes.")
            
        if cpu_usage > 50:
            print(f"⚠️ ALERT: CPU spike detected: {cpu_usage}%")
            
        time.sleep(60) # Check every minute to keep resource usage low

if __name__ == "__main__":
    monitor_system()