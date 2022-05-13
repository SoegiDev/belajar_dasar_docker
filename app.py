""" MODULE STRING """
import os
from flask import Flask,jsonify
app = Flask(__name__)
HOST = "0.0.0.0"
PORT = 5000
@app.route("/")
def hello_world():
    """A multi-line
    docstring.
    """
    env = os.environ.get('FLASK_ENV')
    return jsonify({
        "data": f"Hello World {env} TESTING VOLUMES TAMBAHAN"
    })
if __name__ == "__main__":
    app.run(host=HOST,port=PORT)
