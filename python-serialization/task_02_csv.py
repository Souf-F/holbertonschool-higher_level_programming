#!/usr/bin/env python3
"""Module for converting CSV data to JSON format."""
import csv
import json


def convert_csv_to_json(csv_file):
    """
    Convert CSV file to JSON format.

    Args:
        csv_file: Name of the CSV file to convert

    Returns:
        True if conversion was successful, False otherwise
    """
    try:
        data = []
        with open(csv_file, 'r', encoding='utf-8') as f:
            csv_reader = csv.DictReader(f)
            for row in csv_reader:
                data.append(row)

        with open('data.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)

        return True
    except Exception:
        return False
