from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def json():
    return jsonify({"key": "val", "key2": [1,2,3]})