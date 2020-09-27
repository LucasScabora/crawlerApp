# Technical Test
As a Software Analyst, I want to collect web links (URL’s) from a given initial web link (URL)

## Requirements
- [X] The app needs to receive an URL;
- [X] The app needs to find all links inside this given URL;
- [X] The app needs to save these links found in the database (SQL or No-SQL)
- [X] The app needs to list these links saved in the database.
- [X] After collecting all links from the initial URL. Collect from the newly found links. I mean, the system gets the first link saved, and start the process (get all links and keep on the database). Follow does it to the second, third and successively until the last link saved and tracked.

## Extra
- [X] Your code needs to be integrated with git on your GitHub personal profile;
- [X] Your code needs to contain unit testing;
- [ ] Your code needs to be served on the IBM Cloud;
- [ ] Your code needs to run with containers, with in IBM Cloud;


## Commentaries for the scrapy-single Solution (finished)
This version (folder **scrapy-single**) is a standalone version that executes in your local machine. 

To run the unit test for URL and database manipulation:
> *python3 -m unittest -v crawlerAppUnitTest.py*

And to execute the crawler, using the IBM website as a starting point:
> scrapy crawl mainSpider -a starting_url=https://www.ibm.com/

Commentaries:
- Currently using *DEPTH_LIMIT = 1*, which can be changed in *settings.py* file.
- Using sqlite3 to store the URLs, with an indexed column with the URL hash values (MD5) to validate duplicity
- Changed the URL processing order to BFO using: https://docs.scrapy.org/en/latest/faq.html
- Required libs (installed with *pip*):
|     lib | version |
| ------- | ------- |
| scrapy  | 2.3.0   |
| sqlite3 | 2.6.0   |


## Commentaries for the scrapy-cluster Solution (in progress)
The enhanced version (folder **scrapy-cluster**) to run with containers (docker) based on the following tutorial:
```
https://scrapy-cluster.readthedocs.io/en/latest/
```