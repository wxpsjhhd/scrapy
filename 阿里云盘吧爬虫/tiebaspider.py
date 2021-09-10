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
    'Date': 'Fri, 10 Sep 2021 06:36:15 GMT',
    'Server': 'Apache',
    'Set-Cookie': '''tb_as_data=7e6aeca662aeaf630fa6abd9b58530b52b34bc1cf14b10ffad54ce05cc729f03802389d7a2745029c6f5eaab95c1959d8003273e5c9c62c5f2ac61d6066238f288d5edd50b97dd528c2d00bc4db6d841820fb88c9aed9bafcf3239a075897d8ae043c84acdbeaf638ee89c0daafac34c;path=/;Domain=tieba.baidu.com''',
    'Set-Cookie': 'TIEBA_USERTYPE=524dbb48cd64a69b527aac90; expires=Thu, 31-Dec-2020 15:59:59 GMT; path=/; domain=tieba.baidu.com',
    'Set-Cookie': 'TIEBAUID=5a13ed666dbd98b8a3da1132; expires=Thu, 31-Dec-2020 15:59:59 GMT; path=/; domain=tieba.baidu.com',
    'Tracecode': 21752249950281355018091014,
    'Tracecode': 21752249950306832138091014,
    'Transfer-Encoding': 'chunked',
    'Vary': 'Accept-Encoding',
    'X-Tb-Frs': 'pcfrsui',
    'X-Xss-Protection': '1; mode=block',
    'X_bd_st_subid': 'tb_pc_frs'
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
