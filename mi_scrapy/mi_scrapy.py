import scrapy
from scrapy.selector import Selector

class LeetcodeSpider(scrapy.Spider):
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
