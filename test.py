#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021-09-05 8:30
# @Author  : msdc
# @FileName: test.py
# @Email: wxp.0103@qq.com
import requests
from bs4 import BeautifulSoup
from scrapy import Item, Field
import json

link = 'http://www.chinanews.com/rss/scroll-news.xml'
response = requests.get(link).content.decode('utf-8')
rss = BeautifulSoup(response, "html.parser")

items = []


class FeedItem(Item):
    title = Field()
    link = Field()
    desc = Field()
    pub_date = Field()


news_items = []


for item in rss.find_all('item'):
    news_item = FeedItem()
    feed_item = {
        'title': item.title.text,
        'link': item.link.text,
        'desc': item.description.text,
        'pub_date': item.pubdate.text
    }
    news_item['title'] = feed_item['title']
    news_item['link'] = feed_item['link']
    news_items.append(news_item)
    items.append(feed_item)
print(news_items)

# print(items)
# print(json.loads(json.dumps(items, indent=4)))
# with open('result1.json', 'wt') as f:
#     f.write(json.dumps(items, indent=4))
