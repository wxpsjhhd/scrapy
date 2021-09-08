# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from bs4 import BeautifulSoup
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem

# 过滤性管道，过滤游戏
class BlockGamePipeline:
    def process_item(self, item, spider):
        filter_key="游戏"
        if filter_key in (item['tiltle']).encode('utf-8'):
            raise DropItem
        return item

# 加工性管道 去除html标记
class CleanHTMLOioeline:
    def clean_html(text):
        html=BeautifulSoup(text)
        return html.get_text()

    def Process_item(self,item,spider):
        item['tiltle']=self.clean_html(item['title'])
        item['desc']=self.clean_html(item['desc'])

        return item

