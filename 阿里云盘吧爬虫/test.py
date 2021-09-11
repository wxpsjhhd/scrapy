import requests

url='https://www.youtube.com/'
html=requests.get(url).content.decode('utf-8')
print(html)
