#!/usr/bin/python3
"""
This module defines the load_from_json_file
"""
import json


def load_from_json_file(filename):
    """
    Creates an Object from JSON file
    """
    with open(filename, 'r', encoding='utf-8') as f:
        json.load(f)
