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