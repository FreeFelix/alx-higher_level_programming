#!/usr/bin/python3
"""Displays the X-Request-Id header variable of a request to a given URL.
Usage: ./1-hbtn_header.py <URL>
"""

import sys
import urllib.request

if __name__ == "__main__":
    # Get the URL from the command line arguments
    url = sys.argv[1]

    # Create a request object for the URL
    request = urllib.request.Request(url)

    # Send the request and store the response in a variable
    with urllib.request.urlopen(request) as response:
        # Extract the X-Request-Id header from the response
        x_request_id = dict(response.headers).get("X-Request-Id")

        # Print the X-Request-Id header value
        print(x_request_id)
