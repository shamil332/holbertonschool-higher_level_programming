#!/usr/bin/python3
"""
this script lists 10 commits from the repo
"rails" by the user "rails".
"""
import sys
import requests

if __name__ == "__main__":
	repo = sys.argv[1]
	user = sys.argv[2]
	url = f"https://api.github.com/repos/{owner}/{repo}/commits"
	params = {"per_page": 10}
	r = requests.get(url, params=params)
	commits = r.json()
	for commit in commits:
		sha = commit.get("sha")
		auth = commit.get("commit", {}).get("author", {}).get("name")
		print(f"{sha}: {author}")
