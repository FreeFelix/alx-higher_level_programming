#!/usr/bin/python3
"""Sends a request to a given URL and displays the response body.
Usage: ./3-error_code.py <URL>
  - Handles HTTP errors.
"""

import sys
import urllib.error
import urllib.request

if __name__ == "__main__":
    # Get the URL from the command line arguments
    url = sys.argv[1]

    # Create a request object for the URL
    request = urllib.request.Request(url)

    try:
        # Send the request and store the response in a variable
        with urllib.request.urlopen(request) as response:
            # Read the response body and print it
            print(response.read().decode("ascii"))
    except urllib.error.HTTPError as e:
        # Print the error code
        print("Error code: {}".format(e.code))
