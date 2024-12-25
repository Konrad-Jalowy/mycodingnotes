# Python-Flask
Here flask notes if i ever forget something.

## Running app
File must be named app.py (or you set FLASK_APP variable with some other filename that is entry point)
Kinda like that 
```sh
export FLASK_APP=application.py
```
or
```sh
set FLASK_APP=app.py
```
You dont have to do that if you have entry point called app.py.

When you want to start your app you run command
```sh
flask run
```

## Simplest app
Just skeleton:
```python
from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>Hello</h1>"
```

## Hello name
```python
from flask import Flask

app = Flask(__name__)


@app.route("/<name>")
def index(name):
    return f"<h1>Hello {name}</h1>"
```

## Hello name with default value
```python
from flask import Flask

app = Flask(__name__)


@app.route('/', defaults={'name': "Stranger"})
@app.route("/<name>")
def index(name):
    return f"<h1>Hello {name}</h1>"
```

## flask jsonify
```python
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def json():
    return jsonify({"key": "val", "key2": [1,2,3]})
```
## url var type
you can specify type
```python
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/<int:id>")
def index(id):
    return jsonify({"id": id, "name": "Jane Doe"})
```

## query string in URL
simple example
```python
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
```

## simple working with forms
```python
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
```

## getting json data (from postman for example)
```python
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
```