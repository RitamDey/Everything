import scrapy


class LogInSpider(scrapy.Spider):
    name = "login"
    start_urls = ["https://www.reddit.com/login",]

    def parse(self, response):
        yield scrapy.FormRequest(
                "https://www.reddit.com",
                form_data={
                    "username": "unknown_guest17",
                    "password": "Gingerbread235"
                },
                callback=self.after_login
        )

    def after_login(self, response):
        user_name = "//span[@class='user']/a/text()"
        user_link = "//span[@class='user']/a/@href"

        yield {
                "username": response.xpath(user_name).extract(),
                "userlink": response.xpath(user_link).extract()
        }

