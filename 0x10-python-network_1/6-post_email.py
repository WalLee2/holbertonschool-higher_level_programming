#!/usr/bin/python3
"""
Sends a POST request to the passed URL passing email as a parameter
"""
import requests
import sys

if __name__ == "__main__":
    r = requests.post(sys.argv[1], data={'email': sys.argv[2]})
    print(r.text)
