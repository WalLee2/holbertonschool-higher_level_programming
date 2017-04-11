#!/usr/bin/python3
"""
Takes in a URL and displays the value of the variable X-Request-Id
"""
import requests
import sys

if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    value = r.headers.get('X-Request-Id')
    print(value)
