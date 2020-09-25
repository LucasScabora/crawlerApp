import os
import unittest

from crawlerApp.dbManager import dbManager
from datetime             import datetime

# Database test name
db_name = 'database_unit_test.db'

# Tests every URL manipulation
class TestURLManipulations(unittest.TestCase):


    # Validates valid and invalid URLs
    def test_validUrl(self):
        # Removes test database
        if os.path.exists(db_name):
            os.remove(db_name)

        # Performs the tests
        db = dbManager(db_name)
        self.assertTrue(db.isValidURL('https://www.ibm.com/'))
        self.assertFalse(db.isValidURL('invalid'))
        self.assertFalse(db.isValidURL(''))
        self.assertFalse(db.isValidURL(None))
        self.assertTrue(db.isValidURL('http://www.google.com/'))
        db.close()

        # Finishes by removing test database
        os.remove(db_name)



    # Validates escaping urls
    def test_escapeUrl(self):
        # Removes test database
        if os.path.exists(db_name):
            os.remove(db_name)

        # Performs the tests
        db = dbManager(db_name)
        self.assertEqual(db.escapeURL("https://www.ibm.com/"), "https://www.ibm.com/")
        self.assertNotEqual(db.escapeURL("https://www.ibm'.com/"), "https://www.ibm.com/")
        self.assertEqual(db.escapeURL("https://www.ibm'.com/"), "https://www.ibm''.com/")
        self.assertEqual(db.escapeURL("https://www.ibm''''.com/"), "https://www.ibm''''''''.com/")
        db.close()

        # Finishes by removing test database
        os.remove(db_name)



    # Validates URL MD5 hash
    def test_hashUrl(self):
        # Removes test database
        if os.path.exists(db_name):
            os.remove(db_name)

        # Performs the tests
        db = dbManager(db_name)
        self.assertEqual(db.hashURL('https://www.ibm.com/'), '1bab3f16e219f6242b86db0c18e33cfd')
        self.assertEqual(db.hashURL('https://www.ibm.com/'), db.hashURL('https://www.ibm.com/'))
        self.assertNotEqual(db.hashURL('https://www.ibm.com/'), db.hashURL('https://www.google.com/'))
        db.close()

        # Finishes by removing test database
        os.remove(db_name)



    # Validates duplicated URLs
    def test_duplicatedUrl(self):
        # Removes test database
        if os.path.exists(db_name):
            os.remove(db_name)

        # Starts the tests by adding 2 URLs
        db = dbManager(db_name)
        success = db.appendURL('https://www.ibm.com/', datetime.now())
        self.assertTrue(success > 0)
        success = db.appendURL('https://www.google.com/', datetime.now())
        self.assertTrue(success > 0)
        
        # Validates duplicated
        self.assertTrue(db.isDublicatedURL('https://www.ibm.com/'))
        self.assertTrue(db.isDublicatedURL('https://www.google.com/'))
        self.assertFalse(db.isDublicatedURL('https://www.python.org/'))

        # Inserts third URL and validates it
        success = db.appendURL('https://www.python.org/', datetime.now())
        self.assertTrue(success > 0)
        self.assertTrue(db.isDublicatedURL('https://www.python.org/'))

        # Tests insert on closed database
        db.close()
        success = db.appendURL('https://www.ibm.com/', datetime.now())
        self.assertFalse(success > 0)

        # Finishes by removing test database
        os.remove(db_name)



# Performs a unit test
if __name__ == '__main__':
    unittest.main()