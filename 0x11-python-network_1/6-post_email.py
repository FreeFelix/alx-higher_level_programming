#!/usr/bin/python3
"""Sends a POST request to a given URL with a given email.
Usage: ./6-post_email.py <URL> <email>
  - Displays the body of the response.
"""
import sys
import requests


def post_email(url: str, email: str) -> str:
    # Create a dictionary with the email value
    value = {"email": email}

    # Send a POST request to the given URL with the email value
    r = requests.post(url, data=value)

    # Return the body of the response
    return r.text


if __name__ == "__main__":
    # Get the URL and email address from the command line arguments
    url = sys.argv[1]
    email = sys.argv[2]

    # Call the post_email function and print the result
    print(post_email(url, email))
