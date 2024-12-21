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