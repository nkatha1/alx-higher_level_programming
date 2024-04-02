#!/usr/bin/python3

"""
    a Python script that takes in a URL and an email address
    sends POST request to the passed URL with the email as a param
"""


if __name__ == "__main__":
    import requests
    import sys

    url = sys.argv[1]
    value = {'email': sys.argv[2]}

    r = requests.post(url, value)
    print(r.text)
