from flask import Flask,jsonify
app = Flask(__name__)
HOST = "0.0.0.0"
PORT = 5000
@app.route("/")
def hello_world():
    """A dummy docstring."""
    return jsonify({
        "data":"Hello World"
    })
