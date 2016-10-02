# -*- coding: utf-8 -*-
from scrapy.exceptions import DontCloseSpider
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy import signals
from bc.items import BcItem
from scrapy.loader import ItemLoader
from scrapy.http import Request
import datetime
from urllib.parse import urljoin
import socket
import scrapy

from scrapy.loader.processors import MapCompose, Join


class BCSpider(CrawlSpider):
    name = 'bc'
    rules = (
       Rule(LinkExtractor(), follow=True),
    )

    def __init__(self, *args, **kwargs):
        super(BCSpider, self).__init__(*args, **kwargs)
        self._follow_links = True

    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        spider = super(BCSpider, cls).from_crawler(crawler, *args, **kwargs)
        spider._set_crawler(crawler)
        #spider.crawler.signals.connect(spider.spider_idle, signal=signals.spider_idle)
        return spider

    def spider_idle(self):
        self.log("Spider idle signal caught.")
        raise DontCloseSpider

    def parse(self, response):
        # Get the next index URLs and yield Requests
        self.logger.info('Parse function called on %s', response.url)
        next_selector = response.xpath('//*[contains(@class,"next")]//@href')
        for url in next_selector.extract():
            yield Request(urljoin(response.url, url))

        # Get item URLs and yield Requests
        self.logger.info('item selector called on %s', response.url)
        item_selector = response.xpath('//*[@itemprop="url"]/@href')
        for url in item_selector.extract():
            yield Request(urljoin(response.url, url),
                          callback=self.parse_item)

    def parse_item(self, response):
        """ This function parses a property page.

        @url http://web:9312/properties/property_000000.html
        @returns items 1
        @scrapes title price description address image_urls
        @scrapes url project spider server date
        """
        self.logger.info('Parse_item function called on %s', response.url)

        # Create the loader using the response
        l = ItemLoader(item=BcItem(), response=response)

        # Load fields using XPath expressions
        l.add_xpath('title', '//*[@itemprop="name"][1]/text()')
        l.add_xpath('price', './/*[@itemprop="price"][1]/text()')
        l.add_xpath('description', '//*[@itemprop="description"][1]/text()')
        l.add_xpath('address', '//*[@itemtype="http://schema.org/Place"][1]/text()')
        l.add_xpath('image_urls', '//*[@itemprop="image"][1]/@src')

        # Housekeeping fields
        l.add_value('url', response.url)
        l.add_value('project', self.settings.get('BOT_NAME'))
        l.add_value('spider', self.name)
        l.add_value('server', socket.gethostname())
        l.add_value('date', datetime.datetime.now())

        return l.load_item()

    # def spider_opened(self, spider):
    #     self.logger.info('OPEN')
    #     file = open('%s_products.xml' % spider.name, 'w+b')
    #     self.files[spider] = file
    #     self.exporter = XmlItemExporter(file)
    #     self.exporter.start_exporting()

    # def spider_closed(self, spider):
    #     self.logger.info('CLOSE')
    #     self.exporter.finish_exporting()
    #     file = self.files.pop(spider)
    #     file.close()
