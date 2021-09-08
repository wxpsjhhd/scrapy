# -*- coding: utf-8 -*-
# @File    :   quotes_spider.py
# @Time    :   2021/09/07 10:24:35
# @Author  :   Tobabm 
# @Email   :   tobabm@qq.com
# @Site    :   https://www.idefun.com/
# @Version :   
# @Desc    :   

import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'http://quotes.toscrape.com/tag/humor/',
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'author': quote.xpath('span/small/text()').get(),
                'text': quote.css('span.text::text').get(),
            }

        next_page = response.css('li.next a::attr("href")').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)