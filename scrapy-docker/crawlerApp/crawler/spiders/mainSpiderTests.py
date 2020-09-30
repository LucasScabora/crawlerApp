from datetime              import datetime
from crawler.items         import CrawlerappItem
from scrapy.spiders        import Rule
from scrapy.linkextractors import LinkExtractor
from scrapy_redis.spiders  import RedisCrawlSpider

# Crawler's Spider equal to mainSpider class used for unit testing
class mainSpiderTests(RedisCrawlSpider):
    name      = 'mainSpiderTests'
    redis_key = 'mainSpiderTests:start_urls'

    # Follow all the links in page
    rules = (Rule(LinkExtractor(), callback='parse_page', follow=True), )

    # Allow all domains
    def __init__(self, *args, **kwargs):
        self.allowed_domains = []
        super(mainSpiderTests, self).__init__(*args, **kwargs)

    # Parses each web page found, return both URL and timestamp
    def parse_page(self, response):
        return CrawlerappItem(link = response.url, date = datetime.now())