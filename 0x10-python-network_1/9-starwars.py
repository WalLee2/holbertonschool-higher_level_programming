#!/usr/bin/python3
"""
Takes a string and sends a search request to the Star Wars API
"""
import requests
import sys

if __name__ == '__main__':
    char = sys.argv[1]
    r = requests.get('https://swapi.co/api/people/?search={}'.format(char))
    my_peeps = r.json().get("results")
    print("Number of result: {}".format(r.json().get("count")))
    for entity in my_peeps:
        print("{}".format(entity.get("name")))
