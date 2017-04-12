#!/usr/bin/python3
"""
Send a post request to http://0.0.0.0:5000/search_user
and determining if it is proper JSON
"""
import requests
import sys


if __name__ == "__main__":
        if len(sys.argv) != 2 or not sys.argv[1].isalpha():
                print("No result")
        else:
                url = 'http://0.0.0.0:5000/search_user'
                r = requests.post(url, data={'q': sys.argv[1]})
                js = r.json()
                try:
                        print("[{}] {}".format(js.get('id'), js.get('name')))
                except Exception:
                        print("Not a valid JSON")
