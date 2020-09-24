import scrapy

from datetime              import datetime
from crawlerApp.items      import CrawlerappItem
from scrapy.spiders        import CrawlSpider
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
        # Default starting URL: IBM's webpage
        if self.starting_url is None:
            yield scrapy.Request('https://www.ibm.com/', self.parse)
        else: 
            yield scrapy.Request(self.starting_url, self.parse)

    
    # Parses each web page found
    def parse(self, response):
        # Mounts the item and return it
        currlink = response.url
        currdate = datetime.now()
        yield CrawlerappItem(link = currlink, date = currdate)

        # Goes to next URLs
        for link in self.link_extractor.extract_links(response):
            yield response.follow(link, self.parse)