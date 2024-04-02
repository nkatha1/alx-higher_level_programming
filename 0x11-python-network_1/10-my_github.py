#!/usr/bin/python3

"""
    Python script that takes in a letter and sends a POST request
    to http://0.0.0.0:5000/search_user with the letter as a param
"""


if __name__ == "__main__":
    from requests.auth import HTTPBasicAuth
    import requests
    import sys

    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    r = requests.get("https://api.github.com/user", auth=auth)
    print(r.json().get("id"))
