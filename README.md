
# Technical Test
As a Software Analyst, I want to collect web links (URL’s) from a given initial web link (URL)

## Commentaries for the scrapy-single Solution (finished)
This version (folder **scrapy-single**) is a standalone version that executes in your local machine (for learning)

To run the unit test for URL and database manipulation:
> python3 -m unittest -v [crawlerAppUnitTest.py](scrapy-single/crawlerAppUnitTest.py)

And to execute the crawler, using the IBM website as a starting point:
> scrapy crawl mainSpider -a starting_url=https://www.ibm.com/

Commentaries:
- Currently using *DEPTH_LIMIT = 1*, which can be changed in [settings.py](scrapy-single/crawlerApp/settings.py) file
- Stores URLs in sqlite3, using an indexed column with the URL hash values (MD5) to validate duplicity
- Required libs (installed with *pip*):

|     lib | version |
| ------- | ------- |
| scrapy  | 2.3.0   |
| sqlite3 | 2.6.0   |


## Commentaries for the scrapy-docker Solution (finished)
The enhanced version (folder **scrapy-docker**) to run with containers (docker) based on the following component:
```
https://pypi.org/project/scrapy-redis/
```

1) Mount your docker instances (with unit test):
> bash [buildContainers.sh](scrapy-docker/buildContainers.sh)

2) Feed or List URLs into Redis (use **-h** for tips):
> python3 [manageCrawler.py](scrapy-docker/manageCrawler.py)

- Check for crawler logs with: 
> sudo docker logs scrapydocker_crawler_1 --follow