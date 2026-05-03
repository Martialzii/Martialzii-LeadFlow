import datetime

# Mock database of pending payments from LeadFlow
pending_payments = [
    {"client": "Client_A", "amount": 500, "status": "Pending", "timestamp": "2026-05-03 11:00:00"},
]

def send_reminder(client_name):
    print(f"🔔 SENT: Automated follow-up sent to {client_name} regarding their M-Pesa request.")

def check_payment_status():
    current_time = datetime.datetime.now()
    for payment in pending_payments:
        # Match the timestamp format exactly
        payment_time = datetime.datetime.strptime(payment["timestamp"], "%Y-%m-%d %H:%M:%S")
        
        # If payment is older than 2 hours (7200 seconds)
        time_diff = (current_time - payment_time).total_seconds()
        if time_diff > 7200 and payment["status"] == "Pending":
            send_reminder(payment["client"])
        else:
            print(f"⏳ Status: {payment['client']} is still within the 2-hour window.")

# Run the sentinel
if __name__ == "__main__":
    check_payment_status()