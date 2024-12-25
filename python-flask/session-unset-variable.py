from flask import Flask, request, redirect, url_for,session

app = Flask(__name__)

app.config['SECRET_KEY'] = "blablabla"

@app.route("/")
def home():
    name = "Stranger"
    if 'name' in session:
        name = session["name"]
    return f"<h1>Hello {name}"

@app.route("/forgetname")
def forgetname():
    session.pop('name', None)
    return redirect(url_for('home'))

@app.route("/form", methods=['GET', 'POST'])
def the_form():
    if request.method == 'GET':
        return '''<form method="POST" action="/form">
                    <input type="text" name="firstName">
                    <input type="submit" value="submit">
                </form>'''
    name = request.form["firstName"]
    session["name"] = name
    return redirect(url_for('home'))