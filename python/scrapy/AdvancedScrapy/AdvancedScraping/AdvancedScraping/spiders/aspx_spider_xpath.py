import scrapy


class SpidyQuotesViewStateSpider(scrapy.Spider):
    name = "spidyquotes-viewstate"
    start_urls = ["http://quotes.toscrape.com/search.aspx",]
    download_delay = 1.5

    def parse(self, response):
        for author in response.xpath('//select[@id="author"]/option/@value').extract():
            yield scrapy.FormRequest(
                    "http://quotes.toscrape.com/filter.aspx",
                    formdata = {
                        'author': author,
                        '__VIEWSTATE': response.xpath('//input[@id="__VIEWSTATE"]/@value').extract_first()
                    },
                    callback=self.parse_tags
            )

    def parse_tags(self, response):
        for tag in response.xpath('//select[@id="tag"]/option/@value').extract():
            yield scrapy.FormRequest(
                    'http://quotes.toscrape.com/filter.aspx',
                    formdata = {
                        'author': response.xpath(
                                    '//select[@id="author"]/option[@selected]/@value'
                                    ).extract_first(),
                        'tag': tag,
                        '__VIEWSTATE': response.xpath('//input[@id="__VIEWSTATE"]/@value').extract_first()
                    },
                    callback=self.parse_result
            )

    def parse_result(self, response):
        for quote in response.css("div.quote"):
            yield {
                    'quote': quote.css('span.content ::text').extract_first(),
                    'author': quote.css('span.author ::text').extract_first(),
                    'tag': quote.css('span.tag ::text').extract_first(),
                    }

