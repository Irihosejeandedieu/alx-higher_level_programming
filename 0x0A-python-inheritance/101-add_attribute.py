#!/usr/bin/python3

"""
python3 add attribute.py
"""
def add_attribute(obj, name, value):
    """we are going to add attribute by using this function."""

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute") #this error will be raised it is not possible to add it.
    setattr(obj, name, value)

