#!/usr/bin/python3
"""Sends a request to a given URL and displays the response body.
Usage: ./7-error_code.py <URL>
  - Handles HTTP errors.
"""
import sys
import requests


def get_response_body(url: str) -> str:
    # Send a GET request to the given URL
    r = requests.get(url)

    # Check if the status code is greater than or equal to 400
    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        # Display the response body
        print(r.text)


if __name__ == "__main__":
    # Get the URL from the command line arguments
    url = sys.argv[1]

    # Call the get_response_body function
    get_response_body(url)
