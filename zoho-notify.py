import time
import os
import subprocess
import requests
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID     = os.getenv("ZOHO_CLIENT_ID")
CLIENT_SECRET = os.getenv("ZOHO_CLIENT_SECRET")
REFRESH_TOKEN = os.getenv("ZOHO_REFRESH_TOKEN")
ACCOUNT_ID    = "1302322000000008002"

access_token = None
token_expiry = 0

def get_access_token():
    global access_token, token_expiry
    if time.time() < token_expiry - 60:
        return access_token
    r = requests.post("https://accounts.zoho.com/oauth/v2/token", data={
        "grant_type":    "refresh_token",
        "client_id":     CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "refresh_token": REFRESH_TOKEN,
    })
    data = r.json()
    access_token = data["access_token"]
    token_expiry = time.time() + data.get("expires_in", 3600)
    return access_token

def get_unread(token):
    r = requests.get(
        f"https://mail.zoho.com/api/accounts/{ACCOUNT_ID}/messages/view",
        headers={"Authorization": f"Zoho-oauthtoken {token}"},
        params={"status": "unread", "limit": 5}
    )
    return r.json().get("data", [])

def notify(subject, sender):
    subprocess.run(['notify-send', f'{sender}', subject])

def main():
    print("Starting Zoho mail notifier...")
    seen = set()

    for msg in get_unread(get_access_token()):
        seen.add(msg["messageId"])

    print(f"Watching inbox...")

    while True:
        try:
            messages = get_unread(get_access_token())
            for msg in messages:
                mid = msg["messageId"]
                if mid not in seen:
                    seen.add(mid)
                    notify(msg.get("subject", "No subject"), msg.get("fromAddress", "Unknown"))
        except Exception as e:
            print(f"Error: {e}")
        time.sleep(2)

if __name__ == "__main__":
    main()
