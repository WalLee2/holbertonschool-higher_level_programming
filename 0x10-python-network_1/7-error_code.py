#!/usr/bin/python3
"""
Takes in a URL and displays the body of the response
"""
import sys
import requests


if __name__ == "__main__":
    try:
        r = requests.get(sys.argv[1])
        print(r.text)
    except requests.exceptions.HTTPError:
        print("Error code: {}".format(r.status_code))
