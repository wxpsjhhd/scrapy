import requests

url='https://www.tiktok.com/'
html=requests.get(url).content.decode('utf-8')
print(html)
