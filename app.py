"""A dummy docstring."""
from flask import Flask,jsonify
import os
app = Flask(__name__)
HOST = "0.0.0.0"
PORT = 5000
@app.route("/")
def hello_world():
    env = os.environ.get('FLASK_ENV')
    """A dummy docstring."""
    return jsonify({
        "data": f"Hello World {env}"
    })
