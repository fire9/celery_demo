#!/usr/local/bin/env python
"""
this is a celery demo.

Install redis
brew install reids

Install python package
pip install requests
pip install redis
pip install celery

# startup celery broker
celery worker -A example  -l info -c 5
"""

import requests
from celery import Celery


app = Celery('demo_two', broker="redis://localhost:6379/0")


@app.task
def fetch_url(url):
    res = requests.get(url)
    print "Http Status Code: {}".format(res.status_code)


def demo_two(urls):
    for url in urls:
        fetch_url.delay(url)


if __name__ == "__main__":
    demo_two(["https://www.google.com", "https://twitter.com", "https://facebook.com"])
