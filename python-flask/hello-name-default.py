from flask import Flask

app = Flask(__name__)


@app.route('/', defaults={'name': "Stranger"})
@app.route("/<name>")
def index(name):
    return f"<h1>Hello {name}</h1>"
