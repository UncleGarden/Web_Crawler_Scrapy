import scrapy

class LeetcodeSpider(scrapy.Spider):
    name = 'leetcode'
    start_urls = ['https://leetcode.com/problemset/algorithms']

    def parse(self, response):
        for href in response.css('.row tr td a::attr(href)'):
            full_url = response.urljoin(href.extract())
            yield scrapy.Request(full_url, callback=self.parse_question)

    def parse_question(self, response):
        yield {
            'Link': response.url,
            'Title': response.css('h3::text').extract()[0],
            'Total Accepted:': response.css('.total-ac strong::text').extract()[0], # make sense, some of the tests need login
            #'body': response.css('.question .post-text').extract()[0],
            #'tags': response.css('.question .post-tag::text').extract(),

        }
