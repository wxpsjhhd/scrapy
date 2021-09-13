#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021-09-13 10:57
# @Author  : msdc
# @FileName: googlescholar.py
# @Email: wxp.0103@qq.com
# @Description: 
import requests

header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'
}

url = 'https://scholar.google.com.hk/scholar?hl=zh-CN&as_sdt=0%2C5&q=docker&btnG='
html = requests.get(url, header).content
print(html)
with open('../index.html', 'wb') as f:
    f.write(html)
