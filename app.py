from flask import Flask
import socket, os

app = Flask(__name__)

@app.route("/")
def home():
    return f"""
    <h1>SWE40006 Task 4.2 - Flask in Docker</h1>
    <p>Student: Tyler Marwood 104545589 </p>
    <p>Container hostname: {socket.gethostname()}</p>
    """

@app.route("/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)   # 0.0.0.0 is required inside a container