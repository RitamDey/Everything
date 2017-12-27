from scrapy.utils.python import unique as unique_list
from scrapy.utils.response import get_base_url
from scrapy.linkextractors import LinkExtractor
from scrapy.link import Link


class Extractor(LinkExtractor):
    def extract_links(self, response):
        base_url = get_base_url(response)

        if self.restrict_xpaths:
            links = [link
                    for xpath in self.restrict_xpaths
                    for link in response.xpath(xpath)]
        else:
            links = [response.selector,]

        all_links = [Link(response.url),]

        for link in links:
            new_link = self._extract_links(link, response.url, response.encoding, base_url)
            all_links.extend(self._process_links(new_link))

        return unique_list(all_links)

