#!/bin/bash
# Thsi script takes in a url, sends a request and displays the body size of the response
curl -sI "$1" |grep -i "Content-Length:" | awk '{print $2}'
