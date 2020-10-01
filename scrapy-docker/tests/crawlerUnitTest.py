import unittest
import redis
import json
import time

from urllib.parse import urlparse

# Tests every URL manipulation
class crawlerAppUnitTest(unittest.TestCase):

    # Tests feeding a URL
    def test_feedUrl(self):
        # Feeds with IBM URL
        db_r = redis.Redis(host='localhost', port=6379, db=0)
        db_r.lpush('mainSpiderTests:start_urls', 'https://www.ibm.com/')

        # Wait for 20 seconds (for the URL be processed)
        time.sleep(20)

        # Check if the input has been processed
        self.assertEqual(len(db_r.lrange('mainSpiderTests:start_urls', 0, -1)), 0)

        # Check some returned URLs
        url_list = db_r.lrange('mainSpiderTests:items', 0, -1)
        self.assertIsNotNone( url_list )
        self.assertTrue( len(url_list) > 0 )
        for url in url_list:
            url_fields = json.loads(url)
            parsed_url = urlparse(url_fields['link'])
            self.assertTrue(bool(parsed_url.scheme))


    # Validates duplicated URLs
    def test_validateDuplicatedUrl(self):
        # Feeds with the same IBM URL
        db_r = redis.Redis(host='localhost', port=6379, db=0)
        db_r.lpush('mainSpiderTests:start_urls', 'https://www.ibm.com/')

        # Wait for 20 seconds (for the URL be processed)
        time.sleep(20)
        
        # Validates repeated URLs in the response
        url_list = db_r.lrange('mainSpiderTests:items', 0, -1)
        self.assertIsNotNone( url_list )
        self.assertTrue( len(url_list) > 0 )

        # Set for validating duplicates
        url_seen = set()
        for url in url_list:
            url_fields = json.loads(url)
            self.assertNotIn(url_fields['link'], url_seen)
            url_seen.add(url_fields['link'])



# Performs a unit test
if __name__ == '__main__':
    unittest.main()