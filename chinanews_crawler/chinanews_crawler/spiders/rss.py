# _*_coding: utf-8 _*_
from chinanews_crawler.items import ChinanewsCrawlerItem
import scrapy
from bs4 import  BeautifulSoup
from scrapy.http import response
from scrapy.http.request import Request

class RssSpider(scrapy.Spider):
    name = 'rss'
    allowed_domains = ['web']
    start_urls = ['https://www.chinanews.com/rss/rss_2.html']

    def parse(self, response):
        rss_page=BeautifulSoup(response.body,'html.parser')
        rss_links=set(item['href'] for item in rss_page.find_all('a'))
        for link in rss_links:
            yield Request(url=link,callback=self.parse_feed)
    def parse_feed(self,response):
        rss=BeautifulSoup(response.body,'html.parser')
        for item in rss.find_all('item'):
            feed_item=ChinanewsCrawlerItem()
            feed_item['title']=item.title
            feed_item['link']=item.link
            feed_item['desc']=item.description
            feed_item['pub_date']=item.pubdate
            yield feed_item
        
