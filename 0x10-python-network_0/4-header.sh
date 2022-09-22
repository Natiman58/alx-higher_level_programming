#!/bin/bash
# A script that sends GET request with a header variable
curl -s "$1" GET -H "X-School-User-Id: 98"
