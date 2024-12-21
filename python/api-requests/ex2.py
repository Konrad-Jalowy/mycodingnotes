import requests

url = "https://opentdb.com/api.php?difficulty=easy&type=boolean&amount=5"

if __name__ == "__main__":
     response = requests.get(url)
     if response.ok:
        print("response ok!")
     else:
        print("response not ok")
     print("Status code: ", response.status_code)