import time

import scrapy
from BingSpider.items import BingspiderItem

class BingImgSpider(scrapy.Spider):

    name = 'BingImgSpider'
    allowed_domains = ['bing.ioliu.cn']
    start_urls = ['https://bing.ioliu.cn/?p=' + str(_) for _ in range(50, 100)]

    def parse(self, response):
        selectors = response.css(".container .item");
        # print(selectors)
        for selector in selectors:
            time.sleep(1)
            item = BingspiderItem()
            imgurl = selector.css("img::attr(src)").extract_first()
            imgtitle = selector.css(".description h3::text").extract_first()
            item['img_title'] = imgtitle
            item['img_url'] = imgurl
            yield item
        # imgurls = response.css(".container img::attr(src)").extract()
        # imgtitles = response.css(".container .description h3::text").extract()
        # print(imgtitles)
        # item['img_title'] = imgtitles
        # item['img_url'] = imgurls
        # yield item
        pass
