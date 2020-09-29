#!/bin/bash

# Destroy previous containers
docker-compose down

# Build crawler container
docker-compose build --no-cache

# Starts containers
docker-compose up -d --force-recreate