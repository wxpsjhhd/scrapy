# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import json
# link='http://www.chinanews.com/rss/scroll-news.xml'

pages = requests.get('http://www.chinanews.com/rss/rss_2.html').content.decode('gb2312')
soup = BeautifulSoup(pages, 'html.parser')
links = set(item['href'] for item in soup.find_all('a'))

for link in links:
    response = requests.get(link).content.decode('utf-8')
    rss = BeautifulSoup(response, "html.parser")

    items = []

    for item in rss.find_all('item'):
        feed_item = {
            'title': item.title.text,
            'link': item.link.text,
            'desc': item.description.text,
            'pub_date': item.pubdate.text
        }
        items.append(feed_item)
    # print(items)
    print(json.loads(json.dumps(items, indent=4)))
    with open('result.json', 'wt') as f:
        f.write(json.dumps(items, indent=4))
