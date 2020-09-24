# Define your item pipelines here

import os
import hashlib
import sqlite3 as sl

from urllib.parse import urlparse
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem

class CrawlerappPipeline:	
    # Opens a database connection (to do)
    def open_spider(self, spider):
        # Flag to determine if a table need to be created
        will_create_table = False

        # Checks if a database file does not exists
        if ( os.path.isfile('database_urls.db') == False ):
            will_create_table = True

        # Connects to the database (or create a new one)
        try:
            # Creates the connection
            self.conn = sl.connect('database_urls.db')

            # If a new database is created, also creates the Table
            if (will_create_table == True):
                self.conn.execute("""
                    CREATE TABLE URLs (
                        id            INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                        url           TEXT,
                        acquired_date DATE,
                        url_hash      TEXT
                    );""")

                # Also, creates a index to validate similar URLs
                self.conn.execute("""CREATE INDEX SIMILAR_URLs ON URLs(url_hash);""")
        except Error as ex:
            print('Error creating database: ' + ex)
            print('\nThe crawler will proceed without storing the URLs')
       
    # List results and closes a database connection
    def close_spider(self, spider):
        # List all URLs stored in the database
        try:
            cur = self.conn.cursor()

            # Fetches all the rows
            cur.execute("SELECT acquired_date, url FROM URLs")
            rows = cur.fetchall()

            # Iterates over the rows printing them
            print('The URL table have the following URL links:')
            for row in rows:
                print(row)

            # Finally, closes the connection
            self.conn.close()
        except Exception as ex:
            print('Error in the database, URLs might be compromised: ' + ex)

    # Process each URL found
    def process_item(self, item, spider):
        # Cleans the url (escapes single quotes)
        clean_url = item['link'].replace("'","''")

        # Validates the URL if it has a scheme
        parsed_url = urlparse(clean_url)
        if bool(parsed_url.scheme): 
            # Hashes URL to validate duplicated elements (Uses MD5 but can be others)
            hash_url = hashlib.md5(clean_url.encode('utf-8')).hexdigest()

            # Searches for duplicated URLs based on the hash values
            cur = self.conn.cursor()
            cur.execute("""SELECT id, url FROM URLs WHERE url_hash = '{}'""".format(hash_url))
            rows = cur.fetchall()
            for row in rows:
                if (row[1] == clean_url):
                    print('[ERROR] Dupplicated URL. In database it is id = ' + str(row[0]))
                    raise DropItem("""Invalid URL in '{}'""".format(item))

            # Saves (or at least tries to save) the URL into the database
            try:
                self.conn.execute("""INSERT INTO URLs (url, acquired_date, url_hash) 
                                     VALUES ('{}', '{}', '{}')""".format(item['link'], item['date'], hash_url))
                self.conn.commit()
            except Error as ex:
                print('Error saving URL to database: ' + ex)
            finally:
                return item
        else:
            raise DropItem("""Invalid URL in '{}'""".format(item))