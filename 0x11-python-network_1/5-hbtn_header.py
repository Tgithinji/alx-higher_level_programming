#!/usr/bin/python3
"""
Displays the value of the variable X-Request_Id
"""
import requests
import sys


if __name__ == "__main__":
    response = requests.get(sys.argv[1])
    x_request = response.headers.get('X-Request_Id')
    print(x_request)
