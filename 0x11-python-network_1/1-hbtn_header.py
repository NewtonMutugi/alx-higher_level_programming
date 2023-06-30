#!/usr/bin/env python3
"""script that takes in a URL, sends a request to the URL and displays the
value of the X-Request-Id variable found in the header of the response"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    with requests.get(url) as response:
        print(response.headers.get("X-Request-Id"))
