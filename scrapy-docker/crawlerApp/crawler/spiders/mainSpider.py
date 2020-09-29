from datetime              import datetime
from crawler.items         import CrawlerappItem
from scrapy.spiders        import Rule
from scrapy.linkextractors import LinkExtractor
from scrapy_redis.spiders  import RedisCrawlSpider

# Main Crawler's Spider Class
class mainSpider(RedisCrawlSpider):
    name      = 'mainSpider'
    redis_key = 'mainSpider:start_urls'

    # Follow all the links in page
    rules = (Rule(LinkExtractor(), callback='parse_page', follow=True), )

    # Allow all domains
    def __init__(self, *args, **kwargs):
        self.allowed_domains = []
        super(mainSpider, self).__init__(*args, **kwargs)

    # Parses each web page found, return both URL and timestamp
    def parse_page(self, response):
        return CrawlerappItem(link = response.url, date = datetime.now())