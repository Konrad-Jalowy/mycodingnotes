# Python making requests
Here i have notes on making requests in Python.

## Install requests library
Paste this code (make sure you have venv)
```sh
pip install requests
```

## Very simple request:
Code:
```python
import requests

url = "https://opentdb.com/api.php?difficulty=easy&type=boolean&amount=5"

if __name__ == "__main__":
     response = requests.get(url)
     print(response)
```