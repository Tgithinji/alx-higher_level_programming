#!/usr/bin/python3
# This script takes in a url, sends a request and
# displays the body of the response
import sys
import requests


if __name__ == "__main__":
    response = requests.get(sys.argv[1])

    if response.status_code >= 400:
        print(f"Error code: {response.status_code}")
    else:
        print(response.text)
