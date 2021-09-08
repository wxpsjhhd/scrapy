import requests

url='https://www.idefun.com'

for i in range(5):
    html=requests.get(url).content.decode('utf-8')
print(html)
