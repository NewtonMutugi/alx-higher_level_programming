#!/usr/bin/python3
"""Module that returns an object represented by a JSON string"""
import json


def from_json_string(my_str):
    """Returns an object represented by a JSON string
    Args:
        my_str (str): JSON string to convert
    Returns:
        Object represented by JSON string
    """
    return json.loads(my_str)
