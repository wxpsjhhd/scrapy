import requests

url='https://www.google.com/search?q=中国'
html=requests.get(url).content.decode('utf-8')
print(html)
