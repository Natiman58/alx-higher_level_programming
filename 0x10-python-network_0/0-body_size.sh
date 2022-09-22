#!/bin/bash
curl -Is "$1" | grep 'Content-Length' | awk '{print $2}'

