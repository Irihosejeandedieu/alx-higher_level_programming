#!/usr/bin/python3

"""
python3 add attribute.py
"""
def add_attribute(obj, name, value):
    """Let's add attribute by using this function."""

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
