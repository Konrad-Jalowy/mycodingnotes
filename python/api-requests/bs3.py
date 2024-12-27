import requests
from bs4 import BeautifulSoup

url = 'https://assets.digitalocean.com/articles/eng_python/beautiful-soup/mockturtle.html'

page = requests.get(url)

if page.ok:
    soup = BeautifulSoup(page.text, 'html.parser')
    paras = soup.find_all('p')
    for para in paras:
        print(para.get("href"))
        print(para.get("id"))
        print(para.get("class"))
        print(para.has_attr("href"))
        print(para.parent.name)