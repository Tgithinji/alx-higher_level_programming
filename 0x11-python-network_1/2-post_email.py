#!/usr/bin/python3
"""
This script takes a url an an email
sends a POST request to the url with email as parameter
displays the body of the response
"""
import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    values = {'email': sys.argv[2]}

    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    with urllib.request.urlopen(url, data=data) as response:
        content = response.read()
        content_utf = content.decode('utf-8')
        print(content_utf)
