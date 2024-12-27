import requests
from bs4 import BeautifulSoup

url = 'https://assets.digitalocean.com/articles/eng_python/beautiful-soup/mockturtle.html'

page = requests.get(url)

if page.ok:
    soup = BeautifulSoup(page.text, 'html.parser')
    paras = soup.find_all('p')
    for para in paras:
        print(para.get_text())