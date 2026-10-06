import os
import sys
import requests
from dotenv import load_dotenv

def send_discord(webhook_url, message):
    response = requests.post(webhook_url, json = {"content" : message} , timeout = 10)
    print(response.status_code)

def main():
    load_dotenv()
    value = os.environ.get("DISCORD_WEBHOOK_URL")

    if value:
        print(value[:30])
    else:
        sys.exit("DISCORD_WEBHOOK_URL이 없습니다.")

    send_discord(value, "main으로 보낸 메시지")


if __name__ == "__main__":
    main()
