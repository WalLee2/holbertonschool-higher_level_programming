#!/usr/bin/python3
"""
Display the value of the X-Request-Id variable in the header of the response
"""
import urllib
import sys
from urllib.request import urlopen

if __name__ == '__main__':
    with urlopen(sys.argv[1]) as my_url:
        url_info = my_url.info()
        for key, value in url_info.items():
            if key == "X-Request-Id":
                print(value)
