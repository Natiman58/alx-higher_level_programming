#!/bin/bash
# A script that sends GET request to a URL th a header variable
curl -sX GET -H "X-School-User-Id: 98" "$1"
