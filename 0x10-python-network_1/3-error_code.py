#!/usr/bin/python3
"""
Send a request to the URL and display the response decoded in utf-8
"""
import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as my_req:
            my_req = (my_req.read()).decode('utf-8'))
            print(my_req)
    except urllib.error.HTTPError as error:
        print("Error code: {}".format(error.code))
