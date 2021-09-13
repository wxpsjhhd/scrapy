#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021-09-11 14:53
# @Author  : msdc
# @FileName: dyttspider.py
# @Email: wxp.0103@qq.com
import requests
from bs4 import BeautifulSoup

url = 'https://dytt89.com/'
page = requests.get(url).content.decode('gbk')
# print(page)
soup = BeautifulSoup(page, 'html.parser')
index_list = soup.find_all('div', class_='co_area2')
# print(index_list)
items_list = list()

for each in index_list:
    item_list = list()
    item_dict1 = dict()
    item_dict1['title'] = each.span.text
    item_dict1['more'] = each.em.a['href']
    items = each.find_all('li')
    for item in items:
        item_dict = dict()
        item_dict['item_title'] = item.a['title']
        item_dict['item_link'] = item.a['href']
        item_list.append(item_dict)
    item_dict1['content'] = item_list
    items_list.append(item_dict1)
# print(items_list)
for c in items_list:
    print(c['title'])
    if c['more'].find('https://'):
        c['more'] = 'https://dytt89.com' + c['more']
    else:
        pass
    print('详情：',c['more'])
    print('----------------------')
    for d in c['content']:
        print(d['item_title'])

        if d['item_link'].find('https://'):
            d['item_link']='https://dytt89.com'+d['item_link']
        else:
            pass
        print(d['item_link'])
    print('**********************')
