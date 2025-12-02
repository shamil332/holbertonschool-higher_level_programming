#!/usr/bin/python3
"""
a basic Python script to fetch posts from JSONPlaceholder using requests.get().
"""
import requests
import csv

url = "https://jsonplaceholder.typicode.com/posts"
def fetch_and_print_posts():
    res = requests.get(url)
    print(f"Status code: {res.status_code}")
    if res.status_code == 200:
        res_json = res.json()
        for v in res_json:
            print(v['title'])

def fetch_and_save_posts():
    res = requests.get(url)
    if res.status_code == 200:
        res_json = res.json()
        posts = [
            {"id": p["id"], "title": p["title"], "body": p["body"]}
            for p in res_json
        ]
        fieldnames = ["id", "title", "body"]
        with open("posts.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(posts)
