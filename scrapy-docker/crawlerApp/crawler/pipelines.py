# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html

# Simple Pipeline Code to Inform URL processed
# The URL will be saved in redis
class CrawlerappPipeline(object):	
	# Opens/Closes the spider
    def open_spider(self, spider):
        spider.log('Opening spider')
    def close_spider(self, spider):
    	spider.log('Closing spider')

    # Process each URL found
    def process_item(self, item, spider):
        spider.log('Processing and returning URL: ' + item['link'])
        return item