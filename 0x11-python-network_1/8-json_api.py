#!/usr/bin/python3
"""Sends a POST request to http://0.0.0.0:5000/search_user with a given letter.
Usage: ./8-json_api.py <letter>
  - The letter is sent as the value of the variable `q`.
  - If no letter is provided, sends `q=""`.
"""
import sys
import requests


def post_request(url: str, letter: str) -> str:
    # Create a dictionary with the letter value
    payload = {"q": letter}

    # Send a POST request to the given URL with the letter value
    r = requests.post(url, data=payload)

    try:
        # Get the JSON response
        response = r.json()

        # Check if the response is empty
        if response == {}:
            return "No result"
        else:
            # Return the id and name from the response
            return "[{}] {}".format(response.get("id"), response.get("name"))
    except ValueError:
        return "Not a valid JSON"


if __name__ == "__main__":
    # Get the URL and letter from the command line arguments
    url = "http://0.0.0.0:5000/search_user"
    letter = "" if len(sys.argv) == 1 else sys.argv[1]

    # Call the post_request function and print the result
    print(post_request(url, letter))
