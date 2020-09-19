import time

import scrapy
from BingSpider.items import BingspiderItem

class BingImgSpider(scrapy.Spider):

    name = 'BingImgSpider'
    allowed_domains = ['bing.ioliu.cn']
    # start_urls = ['https://bing.ioliu.cn/?p=' + str(_) for _ in range(50, 100)]

    start_urls = ['https://bing.ioliu.cn']

    def parse(self, response):
        selectors = response.css(".container .item");
        
        # for selector in selectors:
        #     time.sleep(1)
        #     item = BingspiderItem()
        #     imgurl = selector.css("img::attr(src)").extract_first()
        #     imgtitle = selector.css(".description h3::text").extract_first()
        #     item['img_title'] = imgtitle
        #     item['img_url'] = imgurl
        #     yield item
        
        item = BingspiderItem()
        imgurl = selectors.css("img::attr(src)").extract_first()
        imgtitle = selectors.css(".description h3::text").extract_first()
        item['img_title'] = imgtitle
        pre_url = imgurl.split('?')
        item['img_url'] = imgurl.split('?')[0].replace('640x480', '1920x1080')
        yield item

        pass
