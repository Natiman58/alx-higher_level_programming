#!/usr/bin/python3
"""
    A python request that takes in a letter and sends a
    a POST request to 'http://0.0.0.0:5000/search_user'
    with letter is sent in the variable 'q'
"""


if __name__ == "__main__":
    import requests
    import sys

    url = 'http://0.0.0.0:5000/search_user'
    if len(sys.argv) > 1:
        letter = sys.argv[1]
    else:
        letter = ""

    r = requests.post(url, data={'q': letter})

    try:
        dict_t = r.json()
        if dict_t == {}:
            print('No result')
        else:
            print("[{}] {}".format(dict_t.get('id'), dict_t.get('name')))
    except ValueError:
        print("Not a valid JSON")
