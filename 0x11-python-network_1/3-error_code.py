#!/usr/bin/python3
"""
Takes a URL as argument, sends a request and displays the body of a reponse
"""
import sys
from urllib import request, error


if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with request.urlopen(url) as response:
            content = response.read().decode('utf-8')
            print(content)

    except error.HTTPError as e:
        print(f"Error code: {e.code}")
