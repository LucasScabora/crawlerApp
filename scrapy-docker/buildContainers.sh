#!/bin/bash

# Destroy previous containers
docker-compose down

# Build crawler container
docker-compose build --no-cache

# Starts containers
docker-compose up -d --force-recreate

# Perform unit testing for crawling
docker exec -it scrapydocker_crawler_1 bash performUnitTest.sh