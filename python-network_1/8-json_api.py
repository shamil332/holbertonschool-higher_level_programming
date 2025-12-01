#!/usr/bin/python3
"""
a Python script that takes in a letter and
sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""
import sys
import requests

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    l = sys.argv[1] if len(sys.argv) > 1 else ""
    data = {'q': l}

    try:
        res = requests.post(url, data=data)
        res_json = res.json()
        if res_json:
            print(f"[{res_json.get('id')}] {res_json.get('name')}")
        else:
            print("No result")

    except ValueError:
        print("Not a valid JSON")
