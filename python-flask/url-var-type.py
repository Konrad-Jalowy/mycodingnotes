from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/<int:id>")
def index(id):
    return jsonify({"id": id, "name": "Jane Doe"})