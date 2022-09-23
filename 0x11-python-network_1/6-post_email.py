#!/usr/bin/python3
"""
    A python script that takes a URL and an email address
    and sends POST request with email as a parameter using 'requests' module
    finally displays the body of the response
"""


if __name__ == "__main__":
    import requests
    import sys

    url = sys.argv[1]

    data = {'email': sys.argv[2]}

    r = requests.post(url, data)
    print(r.text)
