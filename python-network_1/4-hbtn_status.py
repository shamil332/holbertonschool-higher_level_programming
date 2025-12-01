#!/usr/bin/python3
"""
a Python script that fetches https://intranet.hbtn.io/status
"""
import requests

if __name__ == "__main__":
    response = requests.get("https://intranet.hbtn.io/status")
    body = response.text
    print("Body response:")
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))
