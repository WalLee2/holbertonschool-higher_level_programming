#!/usr/bin/python3
"""
fetch https://intranet.hbtn.io/status and use requests
"""
import requests

r = requests.get('https://intranet.hbtn.io/status')
print("Body response:")
print("\t- type: {}".format(type(r.text)))
print("\t- content: {}".format(r.content.decode('utf-8')))
