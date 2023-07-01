#!/usr/bin/python3
"""
    script that takes your GitHub credentials (username and password) and uses
    the GitHub API to display your id
"""
import requests
import sys


if __name__ == "__main__":
    url = 'https://api.github.com/user'
    username = sys.argv[1]
    password = sys.argv[2]
    r = requests.get(url, auth=(username, password))
    try:
        json = r.json()
        print(json.get('id'))
    except ValueError:
        print("Not a valid JSON")
