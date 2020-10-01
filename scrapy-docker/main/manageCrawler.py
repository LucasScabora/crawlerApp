import redis
import json
import argparse

from urllib.parse import urlparse

# Delimiter for exporting URLs
delimiter = ','

# ====================================
# Util function to Validates URL
def isInvalidURL(url):
    parsed_url = urlparse(url)
    if bool(parsed_url.scheme): 
        return False
    else:
        return True
# ====================================


# Prepare parameters
parser = argparse.ArgumentParser(description='Process iterations with Redis.')
parser.add_argument('--feed', metavar='<URL>', type=str, help='Feed crawler with <URL>')
parser.add_argument('--list', action='store_true', help='List URLs crawled')

# Parse Parameters
args, leftovers = parser.parse_known_args()

# Connects to Redis
db_r = redis.Redis(host='localhost', port=6379, db=0)

# Starts processing arguments
if args.feed is not None:
    # 1) Feed parser (priority)
    if isInvalidURL(args.feed):
        print("[ERROR] Invalid URL provided: {}".format(args.feed))	
    else:
        try:
            db_r.lpush('mainSpider:start_urls', args.feed)
            print("""Feeded crawler with: {}""".format(args.feed))
        except redis.exceptions.ConnectionError as r_con_error:
            print("[ERROR] Unable to feed Redis: {}".format(r_con_error))
elif args.list is not None:
    # 2) List crawled URLs, starting by the header
    try:
        db_r.ping()
        print("""{} {} url""".format('date'.rjust(19, ' '), delimiter))
        for url in db_r.lrange('mainSpider:items', 0, -1):
            url_fields = json.loads(url)
            print("""{} {} {}""".format(url_fields['date'], delimiter, url_fields['link']) )
    except redis.exceptions.ConnectionError as r_con_error:
        print("[ERROR] Unable to list crawler results: {}".format(r_con_error))	