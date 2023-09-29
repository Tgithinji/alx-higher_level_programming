#!/usr/bin/python3
"""
Post request to the passed URL with email as parameter
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    values = {'email': sys.argv[2]}

    response = requests.post(url, data=values)
    content = response.content.decode('utf-8')
    print(content)
