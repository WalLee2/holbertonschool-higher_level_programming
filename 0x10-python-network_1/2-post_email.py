#!/usr/bin/python3
"""
Sends a POST request to the passed URL
"""
import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    data = urllib.parse.urlencode({'email': email})
    data = data.encode('ascii')
    with urllib.request.urlopen(url, data) as my_req:
        post_req = (my_req.read()).decode('utf-8')
        print(post_req)
