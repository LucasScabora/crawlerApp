#!/bin/bash

# Starts the Crawler used in Unit Test
scrapy crawl mainSpiderTests -s DEPTH_LIMIT=1 > crawlerUnitTest.log 2>&1 &

# Run unit testing
python3 -m unittest -v crawlerUnitTest.py