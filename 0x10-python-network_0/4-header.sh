#!/bin/bash
# A script that sends GET request with a header variable
curl -sX GET -H "X-School-User-Id: 98" "$1"
