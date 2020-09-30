# Scrapy settings for example project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'crawlerApp'

SPIDER_MODULES = ['crawler.spiders']
NEWSPIDER_MODULE = 'crawler.spiders'

# For debugging
LOG_LEVEL   = 'DEBUG'

# General configuration for scrapy-redis lib
USER_AGENT            = "scrapy-redis"
DUPEFILTER_CLASS      = "scrapy_redis.dupefilter.RFPDupeFilter"
SCHEDULER             = "scrapy_redis.scheduler.Scheduler"

# If True: Don't cleanup redis queues, allows to pause/resume crawls
SCHEDULER_PERSIST = False

# BFO order of navigating URLs
SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.FifoQueue"

# The item pipeline serializes and stores the items in this redis key
REDIS_ITEMS_KEY = '%(spider)s:items'

# Pipelines
ITEM_PIPELINES = {
    'crawler.pipelines.CrawlerappPipeline': 300,
    'scrapy_redis.pipelines.RedisPipeline': 400,
}

# Introduce an artifical delay to make use of parallelism
DOWNLOAD_DELAY = 1

# Obey robots.txt rules
ROBOTSTXT_OBEY = True