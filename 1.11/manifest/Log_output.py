# Create an application that generates a random string on startup, 
# stores this string into memory, and outputs it every 5 seconds with a timestamp
# e.g 2020-03-30T12:15:17.705Z: 8523ecb1-c716-4cb6-a044-b9e83bb98e43


import time
from datetime import datetime
from uuid import uuid4
import os

COUNTER_FILE = os.environ.get("COUNTER_FILE", "/data/counter.txt")
LOG_FILE = os.environ.get("LOG_FILE", "/data/log.txt")

def read_counter():
    try:
        with open(COUNTER_FILE, "r") as f:
            return int(f.read().strip())
    except Exception:
        return 0

if __name__ == "__main__":
    random_str = str(uuid4())
    while True:
        timestamp = datetime.now().isoformat() + 'Z'
        counter = read_counter()
        line = f"{timestamp}: {random_str} | pingpong_count: {counter}\n"
        print(line.strip())
        # Optionally, also write to a log file
        if LOG_FILE:
            os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
            with open(LOG_FILE, "a") as f:
                f.write(line)
        time.sleep(5)


