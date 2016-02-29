#!/usr/bin/python
# -*- coding:utf-8 -*-
'''
import scrapy
from scrapy.selector import Selector

class MiAppStoreSpider(scrapy.Spider):
    name = 'mi-app-store'
    start_urls = ['http://app.mi.com/topList']

    def parse(self, response):
        href = Selector(response).xpath('//div[@class="pages"]/a[@class="next"]')
        print href
        while href:
            full_url = response.urljoin(Selector(response).xpath('//div[@class="pages"]/a[@class="next"]/@href').extract()[0])
            yield scrapy.Request(full_url, callback=self.parse_app)

    def parse_app(self, response):
        yield {
            'Link': response
            #'App': Selector(response).xpath('//div[@class="applist-wrap"]/ul[@class="applist"]/li/h5/a').extract()[0],
            #'Title': response.css('h3::text').extract()[0],
            #'Total Accepted:': response.css('.total-ac strong::text').extract()[0], # make sense, some of the tests need login
            #'body': response.css('.question .post-text').extract()[0],
            #'tags': response.css('.question .post-tag::text').extract(),

        }
'''

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import HtmlXPathSelector
from items import MiAppStoreItem

class MySpider(CrawlSpider):
    name = "mi-app-store"
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
            item = MiAppStoreItem()

            title = titles.xpath("a/text()").extract()
            link = titles.xpath("a/@href").extract()

            item["title"] = [t.encode('utf-8') for t in title]
            item["link"] = [l.encode('utf-8') for l in link]

            items.append(item)
        return(items)
