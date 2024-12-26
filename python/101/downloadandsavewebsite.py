import requests

url = "https://www.google.com"
response = requests.get(url, allow_redirects=True)

if response.ok:
    fh = open("myfile.html", "wb")
    fh.write(response.content)
    fh.close()