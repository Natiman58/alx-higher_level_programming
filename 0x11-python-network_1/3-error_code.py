#!/usr/bin/python3
"""
    Sends a request to a URL and
    displays the body response in decoded format of utf-8
    handles errors according to the 'RFC 2616' status code
"""

if __name__ == "__main__":
    import urllib.request
    import urllib.error
    import sys

    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            response_text = response.read().decode("utf-8", 'strict')
            print(response_text)
    except urllib.error.HTTPError as Error:
        print('Error code: {}'.format(Error.code))
