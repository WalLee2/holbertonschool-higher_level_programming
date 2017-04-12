#!/usr/bin/python3
"""
Send a post request to http://0.0.0.0:5000/search_user
and determining if it is proper JSON
"""
import requests
import sys


if __name__ == "__main__":
        if len(sys.argv[1]) != 2 or not sys.argv[1].isalpha():
                print("No result")
        url = 'http://0.0.0.0:5000/search_user'
        q = {"q": sys.argv[1]}
        r = requests.post(url, data=q)
        try:
            print("[{}] {}".format(r.json().get('id'), r.jsonj()('name')))
        except Exception:
            print("Not a valid JSON")
