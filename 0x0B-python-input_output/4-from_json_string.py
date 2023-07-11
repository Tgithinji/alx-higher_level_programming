#!/usr/bin/python3
"""
This module defines from_json_string function
"""
import json


def from_json_string(my_str):
    """
    Returns a Python data structure
    """
    return json.loads(my_str)
