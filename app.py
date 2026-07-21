from flask import Flask
import socket

app = Flask(__name__)

@app.route("/")
def home():
    hostname = socket.gethostname()
    return f"""
    <h1>Welcome to DevOps CI/CD Project!</h1>
    <h2>Served by Pod:</h2>
    <h3>{hostname}</h3>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)