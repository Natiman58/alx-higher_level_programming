#!/usr/bin/python3
"""
    A python script that sends a POST request to URL for an email
"""
if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    import sys

    url = sys.argv[1]
    param = {"email": sys.argv[2]}
    query_string = urllib.parse.urlencode(param)
    data = query_string.encode("ascii")

    with urllib.request.urlopen(url, data) as response:
        response_text = response.read().decode("utf-8")
        print(response_text)
