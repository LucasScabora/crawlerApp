# Define your item pipelines here

import sqlite3 as sl

from itemadapter import ItemAdapter

class CrawlerappPipeline:	
    # Opens a database connection (to do)
    def open_spider(self, spider):
        self.conn = sl.connect('my_urls.db')
        with self.conn:
            self.conn.execute("""
                CREATE TABLE URLs (
                    id            INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    url           TEXT,
                    acquired_date DATE
                );""")

    # Closes a database connection (to do)
    def close_spider(self, spider):
        self.conn.close()

    def process_item(self, item, spider):
        # Validates the URL and adds date to database (to do)
        if True: 
            self.conn.execute("""INSERT INTO URLs (url) VALUES ('{}')""".format(item['link']))
            return item
        else:
            raise DropItem("""Invalid URL in '{}'""".format(item))