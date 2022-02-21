from bs4 import BeautifulSoup

import requests

website = requests.get('https://sitroweb.com/').content

soup = BeautifulSoup(website, 'lxml')


for p in soup.find_all('p'):
    print(p.text)