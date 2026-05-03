import re

def redact_sensitive_data(text):
    # Redacts Kenyan Phone Numbers (e.g., 2547...)
    phone_pattern = r'(\+?254|0)(7\d{8})'
    redacted_text = re.sub(phone_pattern, r'\1XXXXXXX', text)
    
    # Redacts Email Addresses
    email_pattern = r'[\w\.-]+@[\w\.-]+\.\w+'
    redacted_text = re.sub(email_pattern, "[REDACTED_EMAIL]", redacted_text)
    
    return redacted_text

# Example test
if __name__ == "__main__":
    test_lead = "New Lead: Cyrus, Phone: 254712345678, Email: test@example.com"
    print(f"🔒 Secure Output: {redact_sensitive_data(test_lead)}")