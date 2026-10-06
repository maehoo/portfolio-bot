import os
import sys
from dotenv import load_dotenv

load_dotenv()
value = os.environ.get("DISCORD_WEBHOOK_URL")

if value:
    print(value[:30])
else:
    sys.exit("DISCORD_WEBHOOK_URL이 없습니다.")

