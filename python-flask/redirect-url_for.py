from flask import Flask, request, redirect, url_for

app = Flask(__name__)

@app.route("/<name>")
def home(name):
    return f"<h1>Hello {name}"

@app.route("/form", methods=['GET', 'POST'])
def the_form():
    if request.method == 'GET':
        return '''<form method="POST" action="/form">
                    <input type="text" name="firstName">
                    <input type="submit" value="submit">
                </form>'''
    name = request.form["firstName"]
    return redirect(url_for('home', name=name))
