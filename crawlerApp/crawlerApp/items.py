# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

# Processes both the link and its aquisition date
class CrawlerappItem(scrapy.Item):
    link = scrapy.Field()
    date = scrapy.Field()