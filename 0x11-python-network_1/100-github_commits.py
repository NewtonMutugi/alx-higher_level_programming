#!/usr/bin/python3
"""
    script that takes 2 arguments in order to solve the challenge.
"""
import requests
import sys


if __name__ == "__main__":
    url = 'https://api.github.com/repos/{}/{}/commits'.format(
        sys.argv[2], sys.argv[1])
    r = requests.get(url)
    try:
        json = r.json()
        for i in range(10):
            print("{}: {}".format(
                json[i].get('sha'),
                json[i].get('commit').get('author').get('name')))
    except ValueError:
        print("Not a valid JSON")
