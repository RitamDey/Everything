from scrapy.downloadermiddlewares.redirect import RedirectMiddleware
from scrapy.http import Request
import re


class AgeRestrictMiddleware(RedirectMiddleware):
    def _redirect(self, redirected, request, spider, reason):
        if not re.findall(r"agecheck/(.*)", redirected.url):
            return super()._redirect(redirected, request, spider, reason)
        
        return Request(url=request.url,
                       cookies={'mature_content': '1'},
                       meta={'dont_cache': '1'},
                       callback=spider.parse_item
        )
