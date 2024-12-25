from flask import Flask, request, redirect, url_for,session, render_template
app = Flask(__name__)

app.config['SECRET_KEY'] = "blablabla"

@app.route("/")
def home():
    name = "stranger"
    if 'name' in session:
        name = session["name"]
    return render_template('home.html', name=name)

@app.route("/forgetname")
def forgetname():
    session.pop('name', None)
    return redirect(url_for('home'))

@app.route("/form", methods=['GET', 'POST'])
def the_form():
    if request.method == 'GET':
        return render_template('form.html')
    name = request.form["firstName"]
    session["name"] = name
    return redirect(url_for('home'))