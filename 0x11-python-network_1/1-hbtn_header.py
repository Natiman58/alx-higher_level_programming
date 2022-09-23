#!/usr/bin/python3
"""
    A python script that displays 'X-Request-Id' from the url header
"""
if __name__ == "__main__":
    from urllib.request import urlopen
    import sys

    url = sys.argv[1]

    with urlopen(url) as response:
        req_id = response.headers.get('X-Request-Id')
        print(req_id)
