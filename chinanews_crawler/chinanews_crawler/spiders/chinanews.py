# _*_coding: utf-8 _*_
from chinanews_crawler.items import ChinanewsCrawlerItem
import scrapy
from bs4 import  BeautifulSoup

# class FeedItem(scrapy.Item):
#     title = scrapy.Field()
#     link = scrapy.Field()
#     desc = scrapy.Field()
#     pub_date = scrapy.Field()
class ChinanewsSpider(scrapy.Spider):
    name = 'chinanews'
    allowed_domains = ['chinanews.com']
    start_urls = ['http://www.chinanews.com/rss/scroll-news.xml']

    def parse(self, response):
        rss=BeautifulSoup(response.body,'html.parser')
        for item in rss.find_all('item'):
            feed_item=ChinanewsCrawlerItem()
            feed_item['title']=item.title
            feed_item['link']=item.link
            feed_item['desc']=item.description
            feed_item['pub_date']=item.pubdate
            yield feed_item
