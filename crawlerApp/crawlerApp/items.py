# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CrawlerappItem(scrapy.Item):
    # Receives a link and its aquisition date
    link = scrapy.Field()
    date = scrapy.Field()