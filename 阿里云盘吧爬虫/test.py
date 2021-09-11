import requests

url='http://www.idefun.com'
html=requests.get(url).content.decode('utf-8')
print(html)
