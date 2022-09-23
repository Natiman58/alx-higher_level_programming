#!/usr/bin/python3
"""
    A python script that takes your git hub credentials(username, pwd)
    and uses the GitHub API to display your id
    uses  Basic Authentication with personal access token
    to access info
"""

if __name__ == "__main__":
    import requests
    import sys
    from requests.auth import HTTPBasicAuth

    username = sys.argv[1]
    password = sys.argv[2]
    url = "https://api.github.com/user"
    authr = HTTPBasicAuth(username, password)

    r = requests.get(url, auth=authr)
    if r.status_code >= 400:
        print('None')
    else:
        print(r.json().get('id'))
