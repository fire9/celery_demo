#!/usr/local/bin/env python
"""
this is a celery demo_two.

pip install requests
"""

import requests
import time


def demo_one(urls):
    start = time.time()
    for url in urls:
        res = requests.get(url)
        print "Http Status Code: %s" % res.status_code
    print "It's took ", time.time() - start, "Seconds."


if __name__ == "__main__":
    demo_one(["https://www.google.com", "https://twitter.com", "https://www.facebook.com"])
