# Define your item pipelines here

from itemadapter          import ItemAdapter
from scrapy.exceptions    import DropItem
from scrapy.exceptions    import DropItem

from crawlerApp.dbManager import dbManager


class CrawlerappPipeline:	
    # Starts the spider of the crawler
    def open_spider(self, spider):
        self.db = dbManager('database_urls.db')
       

    # Finishes the spider of the crawler
    def close_spider(self, spider):
        self.db.listURLs()
        self.db.close()


    # Process each URL found
    def process_item(self, item, spider):
        # Escape quotes in the URL
        escaped_url = self.db.escapeURL(item['link'])

        if (self.db.isValidURL(escaped_url)) & (not self.db.isDublicatedURL(escaped_url)): 
            self.db.appendURL(escaped_url, item['date'])
            return item
        else:
            raise DropItem("""Invalid or duplicated URL in '{}'""".format(item))