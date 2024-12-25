from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def the_form():
    if request.method == 'GET':
        return '''<form method="POST" action="/">
                    <input type="text" name="firstName">
                    <input type="text" name="lastName">
                    <input type="submit" value="submit">
                </form>'''
    fname = request.form["firstName"]
    lname = request.form["lastName"]
    return jsonify({
        "firstName": fname,
        "lastName": lname
    })
