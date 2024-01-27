#!/usr/bin/python3
"""Uses the GitHub API to display a GitHub ID based on given credentials.
"""
import sys
import requests
from requests.auth import HTTPBasicAuth


def get_github_id(username: str, password: str) -> str:
    # Create an HTTPBasicAuth object with the given credentials
    auth = HTTPBasicAuth(username, password)

    # Send a GET request to the GitHub API to get the user information
    r = requests.get("https://api.github.com/user", auth=auth)

    # Return the user ID from the response
    return r.json().get("id")


if __name__ == "__main__":
    # Get the username and password from the command line arguments
    username = sys.argv[1]
    password = sys.argv[2]

    # Call the get_github_id function and print the result
    print(get_github_id(username, password))
