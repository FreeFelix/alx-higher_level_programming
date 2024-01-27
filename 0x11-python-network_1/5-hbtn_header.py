#!/usr/bin/python3
"""Displays the X-Request-Id header variable of a request to a given URL.
"""
import sys
import requests


def get_request_id(url: str) -> str:
    r = requests.get(url)
    return r.headers.get("X-Request-Id")


if __name__ == "__main__":
    url = sys.argv[1]
    print(get_request_id(url))
