#!/usr/bin/python3
"""Sends a POST request to a given URL with a given email.
"""

import sys
import urllib.parse
import urllib.request

if __name__ == "__main__":
    # Get the URL and email from the command line arguments
    url = sys.argv[1]
    email = sys.argv[2]

    # Encode the email as a dictionary value
    value = {"email": email}

    # Encode the dictionary as a URL-encoded string
    data = urllib.parse.urlencode(value).encode("ascii")

    # Create a request object for the URL with the encoded data
    request = urllib.request.Request(url, data)

    # Send the request and print the response
    with urllib.request.urlopen(request) as response:
        print(response.read().decode("utf-8"))
