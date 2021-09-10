#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021-09-05 8:30
# @Author  : msdc
# @FileName: test.py
# @Email: wxp.0103@qq.com
import json

items_template = ''

with open('data.json', 'r') as f1:
    contennt = json.loads(f1.read())
for each in contennt:
    # print(each)
    TITLE = each['title']
    AUTHOR = each['author']
    LINK = each['link']
    DESC = ''
    for desc in each['desc']:
        DESC += desc + '\n'
    # print(DESC)
    item_template = f'''<div id='item'>
<a href="{LINK}"><h4 id="tit">{TITLE}</h4></a>
<p id="author">用户：{AUTHOR}</p>
<p id="desc">{DESC}</p>
</div>'''
    items_template += item_template + '\n'
# print(items_template)
with open('template.html', 'r',encoding='utf-8') as f2:
    file = f2.read()
#     file=(f2.read()).format(items_template=items_template)
# print(file)
post = file.find('<ul>')
if post != -1:
    html = file[:post + len('<ul>')] + items_template + file[post + len('<ul>'):]
    print(html)
    with open('index.html','w',encoding='utf-8') as f3:
        f3.write(html)
