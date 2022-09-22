#!/bin/bash
# A script that takes a URL and displays all HTTP methods the server will accept
curl -si "$1" | grep Allow: | cut -d' ' -f 2-
