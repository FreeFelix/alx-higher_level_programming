#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status."""

import urllib.request

if __name__ == "__main__":
    # Create a request object for the URL
    request = urllib.request.Request("https://alx-intranet.hbtn.io/status")

    # Send the request and store the response in a variable
    with urllib.request.urlopen(request) as response:
        # Read the response body
        body = response.read()

        # Print the response information
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode("utf-8")))

