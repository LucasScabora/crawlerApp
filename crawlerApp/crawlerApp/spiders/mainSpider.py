import scrapy

from datetime              import datetime
from crawlerApp.items      import CrawlerappItem
from scrapy.spiders        import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

# Main Spider Class
class mainSpider(CrawlSpider):
    name = 'mainSpider'

    # Sets default arguments
    def __init__(self, starting_url=None, *args, **kwargs):
        super(mainSpider, self).__init__(*args, **kwargs)
        self.starting_url   = starting_url
        self.link_extractor = LinkExtractor()


    # Defines starting point (input parameter: -a starting_url=<YOUR URL>)
    def start_requests(self):
        # If a starting URL was not informed, uses IBM's webpage
        if self.starting_url is None:
            yield scrapy.Request('https://www.ibm.com/', self.parse)
        else: 
            yield scrapy.Request(self.starting_url, self.parse)

    
    # Parses each web page found
    def parse(self, response):
        # Acquires the fields (current link and date)
        currlink = response.url
        currdate = datetime.now()

        # Mount and return the item
        yield CrawlerappItem(link = currlink, date = currdate)

        # Go to next URL
        for link in self.link_extractor.extract_links(response):
            if link is not None:
                yield response.follow(link, self.parse)