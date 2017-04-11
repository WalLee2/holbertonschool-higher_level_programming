#!/usr/bin/python3
"""
Takes in a URL and displays the value of the variable X-Request-Id
"""
import requests
import sys

r = requests.get(sys.argv[1])

for key, values in r.headers.items():
    if key == "X-Request-Id":
        print(values)
