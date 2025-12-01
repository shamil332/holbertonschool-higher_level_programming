#!/usr/bin/python3
"""
a Python script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""
import sys
import requests

if __name__ == "__main__":
    profile = sys.argv[1]
    token = sys.argv[2]
    url = "https://api.github.com/user"
    res = requests.get(url, auth=(profile, token))

    if res.status_code == 200:
        res = res.json()
        print(res.get('id'))
    else:
        print("None")
