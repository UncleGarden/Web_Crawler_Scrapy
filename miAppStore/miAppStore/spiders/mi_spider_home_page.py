#!/usr/bin/python
# -*- coding:utf-8 -*-

from scrapy.linkextractors import LinkExtractor
from scrapy.selector import HtmlXPathSelector
from scrapy.spiders import CrawlSpider, Rule

from scrapy.spiders import Spider
from scrapy.selector import Selector
from miappstore.items import MiappstoreItem

class MiappstoreSpider(Spider):
    name = "miappstore_home"
    allowed_domains = ["app.mi.com"]
    start_urls = ["http://app.mi.com/topList"]

    def parse(self, response):

        sites = Selector(response).xpath('//h5')
        items = []

        for site in sites:
            item = MiappstoreItem()

            title = site.xpath("a/text()").extract()
            link = site.xpath("a/@href").extract()

            item["title"] = [t.encode('utf-8') for t in title]
            item["link"] = [l.encode('utf-8') for l in link]

            items.append(item)

        return items

'''
from scrapy.item import Item, Field

class MiappstoreItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = Field()
    link = Field()


class MySpider(CrawlSpider):
    name = "miappstore"
    allowed_domains = ["app.mi.com"]
    start_urls = ["http://app.mi.com/topList"]

    rules = (
        Rule(LinkExtractor(allow=(), restrict_xpaths=('//a[@class="next"]',)), callback="parse_items", follow= True),
    )

    def parse_items(self, response):
        hxs = HtmlXPathSelector(response)
        titles = hxs.xpath('//h5')

        items = []
        for titles in titles:
            item = MiappstoreItem()

            title = titles.xpath("a/text()").extract()
            link = titles.xpath("a/@href").extract()

            item["title"] = [t.encode('utf-8') for t in title]
            item["link"] = [l.encode('utf-8') for l in link]

            items.append(item)
        return(items)
'''