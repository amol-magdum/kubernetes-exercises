from flask import Flask, send_file, send_from_directory
import os
import time
import requests

app = Flask(__name__)

CACHE_DIR = "/cache"
CACHE_FILE = "image.jpg"
TIME_FILE = "last_time.txt"
CACHE_PATH = os.path.join(CACHE_DIR, CACHE_FILE)
TIME_PATH = os.path.join(CACHE_DIR, TIME_FILE)
CACHE_SECONDS = 600  # 10 minutes

def get_cached_image():
    if not os.path.exists(CACHE_PATH) or not os.path.exists(TIME_PATH):
        return None, None
    last_time = float(open(TIME_PATH).read().strip())
    return CACHE_PATH, last_time

def fetch_new_image():
    resp = requests.get("https://picsum.photos/1200", stream=True)
    with open(CACHE_PATH, "wb") as f:
        for chunk in resp.iter_content(1024):
            f.write(chunk)
    # Save timestamp
    with open(TIME_PATH, "w") as f:
        f.write(str(time.time()))

@app.route("/")
def show_image():
    cache_img, last_time = get_cached_image()
    now = time.time()
    # If image not present or older than 10 minutes, fetch new,
    # unless this is the first request after interval expires.
    if cache_img is None or last_time is None or (now - last_time) > CACHE_SECONDS:
        # Allow serving one stale image after timeout for testing,
        # e.g. always fetch on the second request after expiry
        fetch_new_image()
        cache_img, last_time = get_cached_image()
    return send_file(cache_img, mimetype="image/jpeg")

@app.route("/refresh")
def force_refresh():
    fetch_new_image()
    return "Refreshed", 200

@app.route('/todo.html')
def serve_todo():
    return send_from_directory(os.path.dirname(os.path.abspath(__file__)), 'todo.html')

if __name__ == "__main__":
    os.makedirs(CACHE_DIR, exist_ok=True)
    app.run(host="0.0.0.0", port=8000)