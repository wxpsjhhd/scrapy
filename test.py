import requests

url='https://www.idefun.com'

headers = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
    
}

for i in range(5):
    html=requests.get(url,headers=headers).content.decode('utf-8')
print(html)
