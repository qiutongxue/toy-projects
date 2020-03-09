# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BingspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # imgurl = scrapy.Field()
    # pass
    img_url = scrapy.Field()
    img_title = scrapy.Field()
    pass
