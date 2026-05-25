#!/usr/bin/env python3
"""Module for basic JSON serialization and deserialization."""
import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python dictionary to a JSON file.

    Args:
        data: Python dictionary to serialize
        filename: Name of the output JSON file
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """
    Deserialize JSON data from a file to a Python dictionary.

    Args:
        filename: Name of the input JSON file

    Returns:
        Python dictionary with deserialized data
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
