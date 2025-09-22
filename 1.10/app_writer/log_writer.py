import time
from datetime import datetime
from uuid import uuid4
import os

LOG_FILE = os.environ.get("LOG_FILE", "/data/log.txt")

if __name__ == "__main__":
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
    random_str = str(uuid4())
    while True:
        timestamp = datetime.now().isoformat() + 'Z'
        line = f"{timestamp}: {random_str}\n"
        with open(LOG_FILE, "a") as f:
            f.write(line)
        time.sleep(5)