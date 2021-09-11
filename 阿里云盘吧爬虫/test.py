import requests

url='https://www.google.com/intl/zh-CN_cn/adsense/start/'
html=requests.get(url).content.decode('utf-8')
print(html)
