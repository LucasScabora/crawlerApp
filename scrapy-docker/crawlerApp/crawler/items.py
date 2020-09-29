# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

# Processes both the link and its aquisition date
class CrawlerappItem(Item):
    link = Field()
    date = Field()