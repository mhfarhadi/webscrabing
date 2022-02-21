import requests

website = requests.get('https://sitroweb.com/web_security/')

print(website.text)