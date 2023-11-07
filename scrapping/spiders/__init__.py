# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
import scrapy
from scrapping.items import MyItem

class MySpider(scrapy.Spider):
    name = 'myspider'
    start_urls = ['https://www.olx.co.id/mobil-bekas_c198']

    def parse(self, response):
        item_boxes = response.xpath('//li[contains(@class, "_3V_Ww")]')
        for item_box in item_boxes:
            item = MyItem()
            item['item_title'] = item_box.xpath('.//div[@class="_2Gr10"]/text()').get().strip()
            item['item_subtitle'] = item_box.xpath('.//div[@class="_21gnE"]/text()').get().strip()
            item['item_price'] = item_box.xpath('.//span[@class="_1zgtX"]/text()').get().strip()
            yield item