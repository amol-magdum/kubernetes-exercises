# Create an application that generates a random string on startup, 
# stores this string into memory, and outputs it every 5 seconds with a timestamp
# e.g 2020-03-30T12:15:17.705Z: 8523ecb1-c716-4cb6-a044-b9e83bb98e43

import time
from datetime import datetime
from uuid import uuid4
import os
import requests

PINGPONG_URL = os.environ.get("PINGPONG_URL", "http://pingpong:8089/pingpong")

def get_pingpong_count():
    try:
        resp = requests.get(PINGPONG_URL)
        if resp.status_code == 200:
            # Expect response like "pong N\n"
            return int(resp.text.strip().split()[1])
    except Exception:
        pass
    return 0

if __name__ == "__main__":
    random_str = str(uuid4())
    while True:
        timestamp = datetime.now().isoformat() + 'Z'
        counter = get_pingpong_count()
        line = f"{timestamp}: {random_str} | pingpong_count: {counter}\n"
        print(line.strip())
        time.sleep(5)


