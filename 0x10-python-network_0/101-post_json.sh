#!/bin/bash
# sends a json Post request to a URL passed as the first argument and displays the body of the response
curl -X POST "$1" -H "Content-Type: application/json" --data @"$2"
