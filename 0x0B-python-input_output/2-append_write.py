#!/usr/bin/python3


def append_write(filename="", text=""):
    with open(filename, "a", encoding="utf-8") as x:
        return x.write(text)
