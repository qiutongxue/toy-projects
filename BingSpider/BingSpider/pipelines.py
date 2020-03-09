# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
from scrapy.pipelines.images import ImagesPipeline
import scrapy
import re
class BingspiderPipeline(ImagesPipeline):

    # def process_item(self, item, spider):
    #     return item
    # def get_media_requests(self, item, info):
    #     # 循环每一张图片地址下载，若传过来的不是集合则无需循环直接yield
    #     for image_url in item['imgurl']:
    #         yield scrapy.Request(image_url)
    def get_media_requests(self, item, info):
        # for image_url in item['img_url']:
        yield scrapy.Request(item['img_url'], meta={'name': item['img_title']})

    def file_path(self, request, response=None, info=None):
        filename = request.meta['name'] + ".jpg"
        filename = re.sub(r'[？\\*|“<>:/]', '', filename)
        return filename

        # pass
