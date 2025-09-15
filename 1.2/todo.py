import os
from flask import Flask

app = Flask(__name__)

@app.get("/")
def ok():
    return "OK\n"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", "9080"))
    print(f"Server started in port {port}", flush=True)
    app.run(host="0.0.0.0", port=port)
    