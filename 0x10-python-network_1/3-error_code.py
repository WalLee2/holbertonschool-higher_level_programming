#!/usr/bin/python3
"""
Send a request to the URL and display the response decoded in utf-8
"""
import urllib.request
import sys

try:
    with urllib.request.urlopen(sys.argv[1]) as my_req:
        print(my_req.read().decode('utf-8'))

except urllib.error.HTTPError as error:
    print("Error code: {}".format(error.code))
