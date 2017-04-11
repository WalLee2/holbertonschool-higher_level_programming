#!/usr/bin/python3
"""
Script that fetches a URL
"""
import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as my_req:
        open_page1 = my_req.read()
        print("Body response:")
        print("\t- type: {}".format(type(open_page1)))
        print("\t- content: {}".format(open_page1))
        print("\t- utf8 content: {}".format(open_page1.decode('utf-8')))
