#!/bin/bash
# This script takes a url, sends a POST request to the url and displays the body of the response
curl -sX POST "$1" -d "email=test@gmail.com&subject=I will always be here for PLD"
