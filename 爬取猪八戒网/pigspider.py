#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021-09-11 16:00
# @Author  : msdc
# @FileName: pigspider.py
# @Email: wxp.0103@qq.com
import requests
from bs4 import BeautifulSoup

start_url = 'https://tianjin.zbj.com/search/f/?kw=python'


def pigspider():
    html = requests.get(start_url).content.decode('utf-8')
    # print(html)
    soup=BeautifulSoup(html,'html.parser')
    selector1=soup.find_all('div',class_='search-service-version-new')[0]
    i =0
    for each in selector1:
        print(each)
        
        print('---------------')
    print(i)
def main():
    pigspider()


if __name__ == '__main__':
    main()
