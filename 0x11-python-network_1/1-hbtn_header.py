#!/usr/bin/python3
"""
This script takes a URL as argument
sends a request to the url
displays the value of X-Request_Id variable found in response header
"""
import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        x_request = response.info()['X-Request-Id']
        print(x_request)
