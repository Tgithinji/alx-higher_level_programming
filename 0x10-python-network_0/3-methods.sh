#!/bin/bash
# This script displays all the HTTP methods the server will accept
curl -sI "$1" | grep -i "Allow:" | awk -F ": " '{print $2}' 
