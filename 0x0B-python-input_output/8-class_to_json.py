#!/usr/bin/python3
"""
This module defines class_to_json function
"""
import json


def class_to_json(obj):
    """
    Returns the dictionary description with simple data structures
    """
    return json.dumps(obj.__dict__)
