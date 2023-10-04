#!/usr/bin/python3
"""
Displays the value of the variable X-Request_Id
"""
import requests
import sys


if __name__ == "__main__":
    response = requests.get(sys.argv[1])
    if 'X-Request-Id' in response.headers:
        print(response.headers['X-Request-Id'])
