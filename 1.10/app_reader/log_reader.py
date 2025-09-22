from flask import Flask, Response
import os

app = Flask(__name__)
LOG_FILE = os.environ.get("LOG_FILE", "/data/log.txt")

@app.route("/logs", methods=["GET"])
def get_logs():
    if not os.path.exists(LOG_FILE):
        return Response("Log file not found.", status=404)
    with open(LOG_FILE, "r") as f:
        content = f.read()
    return Response(content, mimetype="text/plain")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)