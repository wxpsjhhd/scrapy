#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021-09-09 21:58
# @Author  : msdc
# @FileName: tiebaspider.py
# @Email: wxp.0103@qq.com
import requests
import json
from bs4 import BeautifulSoup

header = {
    'Connection': 'keep-alive',
    'Content-Encoding': 'gzip',
    'Content-Type': 'text/html; charset=UTF-8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'
}
lists = list()


def aliyunpan_sipder(page_num):
    n = 0
    for i in range(1):
        url = f'https://tieba.baidu.com/f?kw=%E9%98%BF%E9%87%8C%E4%BA%91%E7%9B%98&ie=utf-8&pn={n}'
        print(url)
        n += 50
        page = requests.get(url, header).content.decode('utf-8')
        print('------------------------------------')
        # print(page)
        selector = BeautifulSoup(page, 'html.parser')
        # info = selector.find_all('ul', id='thread_list')[0]
        content = selector.find_all('li', class_=' j_thread_list clearfix thread_item_box')
        for each in content:
            content_dict = dict()
            texts = list()
            # 标题
            title = each.find_all('a', class_='j_th_tit ')[0].get_text()
            # 作者
            try:
                author = each.find_all('span', class_='tb_icon_author ')[0].get_text()
            except Exception as ret:
                pass
            # 链接
            link = 'https://tieba.baidu.com' + each.find_all('a', class_='j_th_tit ')[0]['href']
            details = requests.get(link, header).content.decode('utf-8')
            d_selector = BeautifulSoup(details, 'html.parser')
            d_content = d_selector.find_all('div', class_='d_post_content j_d_post_content ')
            for k in d_content:
                # print(k.get_text())
                texts.append(k.get_text().replace(' ', ''))
            content_dict['title'] = title
            content_dict['author'] = author
            content_dict['link'] = link
            content_dict['desc'] = texts
            print('标题：' + title)
            print('作者：' + author)
            print('链接：' + link)
            print('内容：', content_dict)
            lists.append(content_dict)
            print('---------------------------')


def storeData():
    data = json.dumps(lists)
    with open('data.json', 'w') as f:
        f.write(data)


def writeFile():
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
    <p id="author">{AUTHOR}</p>
    <p id="desc">{DESC}</p>
    </div>'''
        items_template += item_template + '\n'
    # print(items_template)
    with open('template.html', 'r', encoding='utf-8') as f2:
        file = f2.read()
    #     file=(f2.read()).format(items_template=items_template)
    # print(file)
    post = file.find('<ul>')
    if post != -1:
        html = file[:post + len('<ul>')] + items_template + file[post + len('<ul>'):]
        with open('index.html', 'w', encoding='utf-8') as f3:
            f3.write(html)


def main():
    # page_num = int(input('请输入要爬取页面个数：'))
    page_num = 0
    aliyunpan_sipder(page_num)
    storeData()
    writeFile()


if __name__ == '__main__':
    main()
