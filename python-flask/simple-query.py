from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/<int:id>")
def index(id):
    return jsonify({"id": id, "name": "Jane Doe"})

@app.route("/query")
def query():
    page = request.args.get("page")
    name = request.args.get("name")
    return f"Page: {page} Name: {name}"