# General imports
import os
import hashlib
import sqlite3 as sl

from urllib.parse import urlparse


# Exception when managing the database
class dbException(Exception):
    def __init__(self, expression, message):
        self.expression = expression
        self.message    = message


# Define database manipulations
class dbManager:
    
    # Initializes database
    def __init__(self, name = 'database_urls.db'):
        # Validates database name
        if len(name) < 1:
            raise dbException('Database Name', 'Name is too short. Minimum of 1 character!')

        # Creates URL table if the database file does not exists
        will_create_table = not (os.path.isfile(name))
        
        self.flagConnOpen = False
        try:
            self.conn         = sl.connect(name)
            self.flagConnOpen = True

            if will_create_table:
                self.createSchema()

        except Exception as ex:
            raise dbException('Error creating database', ex)


    # Create the URL table
    def createSchema(self):
        self.conn.execute("""
            CREATE TABLE URLs (
                id            INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                url           TEXT,
                acquired_date DATE,
                url_hash      TEXT
            );""")

        # Creates a index to validate similar URLs
        self.conn.execute("""CREATE INDEX SIMILAR_URLs ON URLs(url_hash);""")

    # Close database connection
    def close(self):
        if( self.flagConnOpen ):
            self.conn.close()
            self.flagConnOpen = False

    # List tuples in URL table
    def listURLs(self):
        if( self.flagConnOpen ):
            try:
                cur = self.conn.cursor()

                # Fetches and print all rows of URL table
                cur.execute("SELECT acquired_date, url FROM URLs")
                print('The URL table have the following URL links:')
                for row in cur.fetchall():
                    print(row)

            except Exception as ex:
                raise dbException('Error listing URLs', ex)
        else:
            print('Unable to print URLs because database is closed')


    # Saves a new URL, returning its id
    def appendURL(self, url, acquired_date):
        if( self.flagConnOpen ):
            try:
                cursor = self.conn.cursor()
                cursor.execute("""INSERT INTO URLs (url, acquired_date, url_hash) 
                                  VALUES ('{}', '{}', '{}')""".format(url, 
                                  	acquired_date, self.hashURL(url)))
                self.conn.commit()

                # Returns the URL's id
                last_id = int(cursor.lastrowid)
                cursor.close()
                return last_id

            except Exception as ex:
                raise dbException('Error saving URL', ex)
        else:
        	# Fail on insertion
            return -1


    # Validates duplicated URLs
    def isDublicatedURL(self, url):
        if( self.flagConnOpen ):
            # Hashes the URL
            hash_url = self.hashURL(url)

            # Searches for duplicated URLs based on the hash value
            cursor = self.conn.cursor()
            cursor.execute("""SELECT id, url FROM URLs WHERE url_hash = '{}'""".format(hash_url))
            for row in cursor.fetchall():
                if (row[1] == url):
                    return True

            # Not duplicated
            return False


    # General URL manipulations
    # Returns escaped URL (for storing in the database)
    def escapeURL(self, url):
        return url.replace("'","''")

    # Validates URL. Returns True if the URL is valid, otherwise returns False
    def isValidURL(self, url):
        parsed_url = urlparse(url)
        if bool(parsed_url.scheme): 
            return True
        else:
            return False

    # Get MD5 from URL string
    def hashURL(self, url):
        return hashlib.md5(url.encode('utf-8')).hexdigest()