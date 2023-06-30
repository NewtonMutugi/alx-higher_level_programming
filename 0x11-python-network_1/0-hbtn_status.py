#!/usr/bin/env python3
"""Script to fetch https://intranet.hbtn.io/status"""
import requests


if __name__ == "__main__":
    url = "https://intranet.hbtn.io/status"
    with requests.get(url) as response:
        print("Body response:")
        print("\t- type: {}".format(type(response.text)))
        print("\t- content: {}".format(response.text))
