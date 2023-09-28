#!/bin/bash
# Send a request to a url passed as argument and displays only the status code of the response
curl -sI -o /dev/null -w "%{http_code}" "$1"
