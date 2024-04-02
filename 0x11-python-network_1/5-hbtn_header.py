#!/usr/bin/python3

"""
    a Python script that takes in a URL, sends a request to the URL
    displays the value of the variable X-Request-Id in the res header
"""


if __name__ == "__main__":
    import sys
    import requests

    url = sys.argv[1]
    r = requests.get(url)

    print(r.headers.get("X-Request-Id"))
