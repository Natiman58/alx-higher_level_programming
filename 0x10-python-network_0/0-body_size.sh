#!/bin/bash
# A bash script that takes in a URL and sends the request to that URL
# and displays the size if the body of the response
curl -Is "$1" | grep 'Content-Length' | awk '{print $2}'

