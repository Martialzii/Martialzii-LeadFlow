import requests
from requests.auth import HTTPBasicAuth

# Your Daraja App Credentials
CONSUMER_KEY = "YOUR_CONSUMER_KEY"
CONSUMER_SECRET = "YOUR_CONSUMER_SECRET"

def get_access_token():
    api_url = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
    try:
        response = requests.get(api_url, auth=HTTPBasicAuth(CONSUMER_KEY, CONSUMER_SECRET))
        json_response = response.json()
        return json_response['access_token']
    except Exception as e:
        print(f"❌ Error generating token: {e}")
        return None

if __name__ == "__main__":
    token = get_access_token()
    if token:
        print(f"✅ Success! Access Token: {token[:10]}...")