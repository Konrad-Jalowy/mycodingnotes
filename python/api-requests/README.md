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

## response.ok, response.status_code
Self explanatory:
```python
import requests

url = "https://opentdb.com/api.php?difficulty=easy&type=boolean&amount=5"

if __name__ == "__main__":
     response = requests.get(url)
     if response.ok:
        print("response ok!")
     else:
        print("response not ok")
     print("Status code: ", response.status_code)
```

## response.json(), results, pprint for better debuging experience
Self explanatory
```python
import requests
import pprint

url = "https://opentdb.com/api.php?difficulty=easy&type=boolean&amount=5"

if __name__ == "__main__":
     response = requests.get(url)
     if response.ok:
        data = response.json()
        results = data["results"]
        pprint.pp(results)
     else:
        print("response not ok", response.status_code)
```