from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/")
def the_form():
    return '''<form method="POST" action="/process">
    <input type="text" name="firstName">
    <input type="text" name="lastName">
    <input type="submit" value="submit">
    </form>'''

@app.route("/process", methods=['POST'])
def process():
    fname = request.form["firstName"]
    lname = request.form["lastName"]
    return jsonify({
        "firstName" : fname,
        "lastName"  : lname
    })