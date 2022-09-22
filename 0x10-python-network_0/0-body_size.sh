#!/bin/bash
# A bash script that takes in a URL and sends the request to that URL
# and displays the size of the body of the response
curl -sI "$1" | grep Content-Length | cut -f2 -d' '

