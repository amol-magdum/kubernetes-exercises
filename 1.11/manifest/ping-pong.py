# Develop a second application that simply responds with "pong 0" to a GET request and increases a counter (the 0) so that you can see how many requests have been sent. 
# The counter should be in memory so it may reset at some point.
#  Create a new deployment for it and have it share ingress with "Log output" application. Route requests directed '/pingpong' to it.


import os
from flask import Flask

app = Flask(__name__)
COUNTER_FILE = os.environ.get("COUNTER_FILE", "/data/counter.txt")

def read_counter():
    try:
        with open(COUNTER_FILE, "r") as f:
            return int(f.read().strip())
    except Exception:
        return 0

def write_counter(value):
    os.makedirs(os.path.dirname(COUNTER_FILE), exist_ok=True)
    with open(COUNTER_FILE, "w") as f:
        f.write(str(value))

@app.route('/pingpong', methods=['GET'])
def pingpong():
    counter = read_counter() + 1
    write_counter(counter)
    return f"pong {counter}\n"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8089))
    app.run(host='0.0.0.0', port=port)
            