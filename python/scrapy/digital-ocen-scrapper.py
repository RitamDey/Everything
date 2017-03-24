"""
   Scrapy example and tutorial by DigitalOcean
   Link: https://www.digitalocean.com/community/tutorials/how-to-crawl-a-web-page-with-scrapy-and-python-3
   In this project we are crawling a site that sells products made of LEGO
"""
import scrapy


class BrickSetSpider(scrapy.Spider):
    name = 'bricketset_spider'  # Spider's name
    start_urls = ['http://brickset.com/sets/year-2016', ]  # The url to start from

    # Default method that gets called to parse the page
    def parse(self, response):

        # The main block that holds the other informations
        # Selecting it via its CSS class named as `set`
        SET_SELECTOR = '.set'

        # Selecting returns a list like SelectorList object
        for brickset in response.css(SET_SELECTOR):

            # The CSS selectors

            # Selects <h1> elements and then looks for <a> element. If found then gets the text inside it
            NAME_SELECTOR = 'h1 a::text'
            # Selects <img> elements and then gets its src attribute via the pseudo-element ::attr()
            IMAGE_SELECTOR = 'img ::attr(src)'

            # The XPath selectors
            """"
            In the PIECES_SELECTOR, the xpath first looks for a <dl> element.
            If found then it looks for <dt> element.
            If that element is found, then it checks if the text inside of <dt> is equals to Pieces or not.
            If its equals to Pieces, then it goes on and gets the <dd> element,
            From where it selects the <a> element and gets the text inside the <a>
            """
            PIECES_SELECTOR = './/dl[dt/text() = "Pieces"]/dd/a/text()'
            """"
            In the MINIFIGS_SELECTOR, the xpath first looks for a <dl> element.
            If found then it looks for <dt> element.
            If that element is found, then it checks if the text inside of <dt> is equals to Minifigs or not.
            If its equals to Minifigs, then it goes on and gets the second <dd> element (as the first is for Pieces),
            From where it selects the <a> element and gets the text inside the <a>
            """
            MINIFIGS_SELECTOR = './/dl[dt/text() = "Minifigs"]/dd[2]/a/text()'

            yield {
                    'name': brickset.css(NAME_SELECTOR).extract_first(),
                    'pieces': brickset.xpath(PIECES_SELECTOR).extract_first(),
                    'minifigs': brickset.xpath(MINIFIGS_SELECTOR).extract_first(),
                    'image': brickset.css(IMAGE_SELECTOR).extract_first(),
            }

            # Using CSS, it selects every element that has the `next` css class
            # Once it gets them, then it gets all the <a> elements
            # After that it gets the href attribute of the <a> using the pseudo-element ::attr()
            NEXT_PAGE_SELECTOR = '.next a ::attr(href)'
            next_page = response.css(NEXT_PAGE_SELECTOR).extract_first()
            # If a valid page link is found
            # Then issue a new scrapy request passing the parse method as the default callback
            if next_page:
                yield scrapy.Request(
                        response.urljoin(next_page),
                        callback = self.parse
                )
