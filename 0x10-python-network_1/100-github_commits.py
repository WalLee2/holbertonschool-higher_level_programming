#!/usr/bin/python3
import sys
import requests


if __name__ == '__main__':
    repo = sys.argv[2]
    owner = sys.argv[1]
    url = 'https://api.github.com/repos/{}/{}/commits'.format(repo, owner)
    req = requests.get(url).json()
    count = 0
    for i in req:
        r = dict(i)
        if count < 10:
            print("{}: {}".format(r.get("sha"), r.get("commit").get("author").get("name")))
            count += 1
