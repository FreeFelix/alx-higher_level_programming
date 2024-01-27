#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status."""

import requests

if __name__ == "__main__":
    # Send a GET request to the URL and store the response in a variable
    r = requests.get("https://alx-intranet.hbtn.io/status")

    # Print the response information
    print("Body response:")
    print("\t- type: {}".format(type(r.text)))
    print("\t- content: {}".format(r.text)))
