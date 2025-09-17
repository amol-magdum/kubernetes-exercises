# Create an application that generates a random string on startup, 
# stores this string into memory, and outputs it every 5 seconds with a timestamp
# e.g 2020-03-30T12:15:17.705Z: 8523ecb1-c716-4cb6-a044-b9e83bb98e43

import time
from datetime import datetime
from uuid import uuid4

if __name__ == "__main__":
    while True:
        timestamp = datetime.now().isoformat() + 'Z'
        random = f"{timestamp}: {uuid4()}"
        print(random)
        time.sleep(5)


