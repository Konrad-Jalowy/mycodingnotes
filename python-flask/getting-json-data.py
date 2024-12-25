from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/", methods=['POST'])
def process():
    data = request.get_json()
    fname = data["firstName"]
    lname = data["lastName"]
    return jsonify({
        "firstName" : fname,
        "lastName"  : lname
    })