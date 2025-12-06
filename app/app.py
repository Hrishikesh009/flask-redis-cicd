from flask import Flask, jsonify
import redis

app = Flask(__name__)

r = redis.Redis(host="redis_db", port=6379, decode_responses=True)

@app.route("/")
def home():
    r.incr("visits")
    return jsonify({
        "message": "Hello Hrishi! Your CI/CD Flask App + Redis",
        "visits": r.get("visits")
    })

@app.route("/status")
def status():
    return jsonify({"status": "running", "container": "flask_app"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
