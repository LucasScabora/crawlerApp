FROM python:3.8
MAINTAINER Lucas Scabora <csb.lucas@gmail.com>

# Configure OS
RUN apt-get update && apt-get -y install \
  build-essential \
  python3-dev     \
  libsqlite3-dev  \
  && rm -rf /var/lib/apt/lists/*
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# Install requirements
COPY crawlerApp/requirements.txt /usr/src/app/
RUN pip3 install --no-cache-dir -r requirements.txt

# Move crawler code to container
COPY crawlerApp /usr/src/app

# Move unit test to container
COPY tests /usr/src/app

# Starts default crawler
ENTRYPOINT ["scrapy"]
CMD ["crawl", "mainSpider"]