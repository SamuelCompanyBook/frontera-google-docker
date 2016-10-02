# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class BcPipeline(object):
    def process_item(self, item, spider):
        spider.log('Well, here is an Item: %s.' % item)
        return item

class JsonWriterPipeline(object):
    def __init__(self):
        self.file = open('items.jl', 'wb')

    def process_item(self, item, spider):
        spider.logger.info('>>>>>>>>>>>>>>Pipeline Dump: %s.' % item)
        a = item.get('title')
        self.file.write(a[0].encode('utf-8') if a else "".encode('utf-8'))
        return item
