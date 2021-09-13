#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021-09-11 14:25
# @Author  : msdc
# @FileName: doubanspider.py
# @Email: wxp.0103@qq.com
import requests
from bs4 import BeautifulSoup

url_list = list()
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'
}


def getUrl():
    start_num = 0
    for i in range(10):
        # 获取每页链接
        start_url = f'https://movie.douban.com/top250?start={start_num}&filter='
        start_num += 25
        url_list.append(start_url)


def spider():
    # 单独爬取
    # for url in url_list:
    print(url_list[0])
    page = requests.get(url_list[0], headers).content
    print(page)


def main():
    # getUrl()
    # spider()
    # print(url_list[0])
    html = requests.get('https://movie.douban.com/top250', headers).text
    print(html)


if __name__ == '__main__':
    main()
