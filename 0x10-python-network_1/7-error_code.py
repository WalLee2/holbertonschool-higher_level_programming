#!/usr/bin/python3
"""
Takes in a URL and displays the body of the response
"""
import sys
import requests


if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    if r.status_code == requests.codes.ok
        print(r.text)
    else:
        print("Error code: {}".format(r.status_code))
